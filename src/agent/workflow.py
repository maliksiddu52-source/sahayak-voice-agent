"""
Main Agent Workflow.
Handles the loop: Listen -> Think -> Act -> Speak.
"""
import json
from src.agent.brain import Brain
from src.agent.state import AgentState
from src.tools.api import search_schemes, check_eligibility, get_scheme_details

# For Gemini, we pass the actual functions, not the JSON Schema.
TOOLS = [search_schemes, check_eligibility, get_scheme_details]

SYSTEM_PROMPT = """
You are 'Sahayak', an AI assistant that helps Indian citizens find and apply for government schemes.
You communicate in the user's preferred language (Default: Telugu). 
You must act as a distinct agent with a personality: helpful, polite, and knowledgeable about Indian welfare.

CORE RULES:
1. VOICE-FIRST: Your responses will be spoken. Keep them concise, clear, and natural. Avoid long lists.
2. AGENTIC BEHAVIOR: Do not just chat. Plan your actions. If you need information (age, income), ask for it.
3. LANGUAGE: If the user speaks Telugu, reply in Telugu (Telugu Script). Do not use English characters for Telugu words. If English, reply in English.
4. TOOLS: Use the provided tools to find real information. Do not hallucinate schemes.
   IMPORTANT: The database is in English. You MUST translate user queries (e.g., 'Rythu') to English (e.g., 'Farmer') when calling `search_schemes`.
5. FAILURE HANDLING: If a tool fails or you don't understand, ask clarifying questions politely.
"""

class Agent:
    def __init__(self):
        self.brain = Brain()
        self.state = AgentState()
        self.state.add_message("system", SYSTEM_PROMPT)
    
    def process_input(self, user_text: str):
        """
        Process user input and return the agent's response text.
        Handles the ReAct loop internally.
        """
        print(f"\n[User]: {user_text}")
        self.state.add_message("user", user_text)
        
        # Reason and Act Loop
        # We allow up to 3 turns of tool usage before forcing a final answer
        for _ in range(5): 
            response_msg = self.brain.think(self.state.get_history(), tools=TOOLS)
            
            if response_msg.tool_calls:
                self.state.add_message("assistant", response_msg.content or "Let me check that for you.") 
                
                # Execute tools
                for tool_call in response_msg.tool_calls:
                    function_name = tool_call.function.name
                    # Arguments are currently a JSON string because of our Brain adapter
                    arguments = json.loads(tool_call.function.arguments)
                    print(f"[Agent Action]: Calling {function_name} with {arguments}")
                    
                    tool_result = None
                    if function_name == "search_schemes":
                        tool_result = search_schemes(arguments['query'])
                    elif function_name == "check_eligibility":
                        tool_result = check_eligibility(**arguments)
                    elif function_name == "get_scheme_details":
                        tool_result = get_scheme_details(**arguments)
                    
                    # Feed result back to brain
                    self.state.history.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": function_name,
                        "content": json.dumps(tool_result)
                    })
            else:
                # Final answer
                final_text = response_msg.content
                self.state.add_message("assistant", final_text)
                return final_text
                
        return "I am taking too long to think properly. Please ask again."
