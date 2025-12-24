"""
Agent State Management.
Tracks conversation history and context.
"""
from typing import List, Dict, Any
from dataclasses import dataclass, field
import json

@dataclass
class AgentState:
    history: List[Dict[str, str]] = field(default_factory=list)
    user_profile: Dict[str, Any] = field(default_factory=dict)
    current_plan: str = ""
    
    def add_message(self, role: str, content: str):
        self.history.append({"role": role, "content": content})
        
    def get_history(self):
        return self.history
    
    def update_profile(self, key: str, value: Any):
        self.user_profile[key] = value
        
    def clear_history(self):
        self.history = []
        self.user_profile = {}

    def to_json(self):
        return json.dumps({
            "history": self.history,
            "user_profile": self.user_profile
        }, indent=2)
