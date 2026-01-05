"""
Maya Umani - Main Response Handler
Life Coach - Mindfulness & Values Alignment
"""

import os
from openai import OpenAI
from typing import List, Dict, Optional

class MayaUmani:
    def __init__(self, system_prompt: str):
        """Initialize Maya with system prompt"""
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
        """Get natural, human-like response from Maya"""
        self.add_message("user", user_message)
        
        messages = [
            {"role": "system", "content": self.system_prompt}
        ] + self.conversation_history
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=300
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
        """Detect user emotional state from message"""
        message_lower = user_message.lower()
        
        if any(word in message_lower for word in ["overwhelm", "too much", "everything", "can't handle"]):
            return "stressed"
        elif any(word in message_lower for word in ["doubt", "unsure", "capable", "enough"]):
            return "doubtful"
        elif any(word in message_lower for word in ["motivation", "drive", "enjoy", "excited"]):
            return "unmotivated" if "no" in message_lower or "lost" in message_lower else "motivated"
        elif any(word in message_lower for word in ["sleep", "stress", "anxious", "panic"]):
            return "stressed"
        
        return None