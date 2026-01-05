"""
Malik Nadir - Main Response Handler
Performance Coach - Stress Management & Resilience
"""

import os
from openai import OpenAI
from typing import List, Dict, Optional

class MalikNadir:
    def __init__(self, system_prompt: str):
        """Initialize Malik with system prompt"""
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o-mini"
        self.system_prompt = system_prompt
        self.conversation_history = []
        self.session_started = False
    
    def add_message(self, role: str, content: str):
        """Add message to conversation history"""
        self.conversation_history.append({
            "role": role,
            "content": content
        })
    
    def is_first_message(self) -> bool:
        """Check if this is the first user message"""
        return len(self.conversation_history) == 0
    
    def get_response(self, user_message: str) -> str:
        """Get natural, human-like response from Malik"""
        self.add_message("user", user_message)
        
        messages = [
            {"role": "system", "content": self.system_prompt}
        ] + self.conversation_history
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.5,
            max_tokens=200
        )
        
        assistant_message = response.choices[0].message.content
        self.add_message("assistant", assistant_message)
        self.session_started = True
        
        return assistant_message
    
    def get_conversation_history(self) -> List[Dict]:
        """Return full conversation history"""
        return self.conversation_history
    
    def get_conversation_length(self) -> int:
        """Get number of exchanges"""
        return len(self.conversation_history)
    
    def reset_conversation(self):
        """Clear conversation history for new session"""
        self.conversation_history = []
        self.session_started = False
    
    def detect_user_state(self, user_message: str) -> Optional[str]:
        """Detect user performance state from message"""
        message_lower = user_message.lower()
        
        if any(word in message_lower for word in ["overwhelm", "too much", "pressure", "can't focus"]):
            return "stressed"
        elif any(word in message_lower for word in ["doubt", "capable", "good enough"]):
            return "doubtful"
        elif any(word in message_lower for word in ["motivation", "drive", "energy", "tired"]):
            return "fatigued" if any(w in message_lower for w in ["tired", "fatigue", "drained"]) else "motivated"
        elif any(word in message_lower for word in ["sleep", "recover", "rest", "worn out"]):
            return "stressed"
        
        return None