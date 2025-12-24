"""
Brain of the Agent (LLM Interface).
Uses Google GenAI SDK (google-genai).
"""
import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class Brain:
    def __init__(self):
        # Configure Gemini
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("Warning: GEMINI_API_KEY not found in environment variables.")
        
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-2.5-flash" 

    def think(self, history: list, tools: list = None):
        """
        Send messages to Gemini and get response.
        Adapts the OpenAI-style history to Gemini's format.
        """
        try:
            # Convert History to Gemini Format
            # OpenAI: [{"role": "user", "content": "hi"}, ...]
            # Gemini SDK handles 'user' and 'model'. System prompt is separate config.
            
            contents = []
            system_instruction = None

            for msg in history:
                role = msg['role']
                content_text = msg.get('content')
                
                if role == 'system':
                    system_instruction = content_text
                    continue
                
                if role == 'assistant':
                    role = 'model'
                    
                if role == 'tool':
                    # For tool outputs in manual loop, we simulate them as user context 
                    # or part of the flow. The new SDK has chat sessions but for
                    # stateless 'think' we do it manually.
                    role = 'user' 
                    content_text = f"Tool Output ({msg.get('name')}): {content_text}"

                if content_text:
                    contents.append(types.Content(
                        role=role,
                        parts=[types.Part.from_text(text=content_text)]
                    ))
            
            # Configure Tool Config if tools are present
            tool_config = None
            if tools:
                # The SDK usually takes a list of functions directly in 'tools' argument
                pass

            # Generate Content
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=contents,
                config=types.GenerateContentConfig(
                    tools=tools,
                    system_instruction=system_instruction
                )
            )
            
            return self._adapt_response(response)

        except Exception as e:
            print(f"Error in Brain.think: {e}")
            from collections import namedtuple
            Message = namedtuple('Message', ['content', 'tool_calls', 'role'])
            return Message(content="Sorry, I am having trouble thinking right now.", tool_calls=None, role="assistant")

    def _adapt_response(self, response):
        """
        Convert Gemini response to a simple object similar to OpenAI's structure
        so workflow.py doesn't need massive changes.
        """
        from collections import namedtuple
        
        # Define a simple ToolCall object
        ToolCall = namedtuple('ToolCall', ['id', 'function'])
        Function = namedtuple('Function', ['name', 'arguments'])
        Message = namedtuple('Message', ['content', 'tool_calls', 'role'])

        try:
            # Check if we have candidates
            if not response.candidates:
                return Message(content="I didn't get a response.", tool_calls=None, role="assistant")

            candidate = response.candidates[0]
            # content_parts = candidate.content.parts
            
            text_content = ""
            tool_calls = []
            
            for part in candidate.content.parts:
                if part.text:
                    text_content += part.text
                
                if part.function_call:
                    fc = part.function_call
                    # Arguments in Gemini are already a dict (or object)
                    args_json = json.dumps(fc.args)
                    
                    tool_calls.append(ToolCall(
                        id="call_" + fc.name, # Dummy ID
                        function=Function(name=fc.name, arguments=args_json)
                    ))
            
            if not text_content and not tool_calls:
                text_content = "Thinking..."

            return Message(content=text_content, tool_calls=tool_calls if tool_calls else None, role="assistant")
            
        except Exception as e:
            print(f"Error adapting response: {e}")
            return Message(content="Error processing response.", tool_calls=None, role="assistant")
