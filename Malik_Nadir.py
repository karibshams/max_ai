"""
Malik Nadir - Main Response Handler - SYNCED
Performance Coach - Returns EXACT responses + creative for novel questions
Synced with condensed prompt structure, sequential questioning, and safety protocols
"""

import os
from openai import OpenAI
from typing import List, Dict, Optional
from difflib import SequenceMatcher

class MalikNadir:
    def __init__(self, system_prompt: str, scenario_responses: dict):
        """Initialize Malik with system prompt and scenario database"""
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o-mini"
        self.system_prompt = system_prompt
        self.scenario_responses = scenario_responses
        self.conversation_history = []
        self.session_started = False
        self.crisis_detected = False
    
    def add_message(self, role: str, content: str):
        """Add message to conversation history"""
        self.conversation_history.append({
            "role": role,
            "content": content
        })
    
    def check_safety_crisis(self, user_message: str) -> bool:
        """Check if user message contains self-harm/suicide indicators"""
        crisis_keywords = [
            "hurt myself",
            "take my life",
            "end it",
            "don't want to live",
            "can't go on",
            "ending it",
            "suicide",
            "self harm",
            "cut myself",
            "overdose",
            "kill myself",
            "want to die",
            "better off dead"
        ]
        
        message_lower = user_message.lower()
        return any(keyword in message_lower for keyword in crisis_keywords)
    
    def get_crisis_response(self, user_message: str, is_confirmed: bool = False, stage: int = 1, user_name: str = "there") -> dict:
        """Get appropriate crisis response - Returns dict with message and metadata for backend"""
        if stage == 1:
            from conversation_database import get_crisis_message
            response = get_crisis_message("malik", 1, user_name)
            return {
                "message": response,
                "stage": 1,
                "block_chat": False,
                "await_response": True,
                "next_stage": 2
            }
        elif stage == 2:

            from conversation_database import get_crisis_message
            response = get_crisis_message("malik", 2)
            return {
                "message": response,
                "stage": 2,
                "block_chat": False,
                "await_response": True,
                "next_stage": 3
            }
        elif stage == 3:
            from conversation_database import get_crisis_stage_3_response, should_block_chat
            user_wants_help = not should_block_chat(user_message)
            response = get_crisis_stage_3_response("malik", user_wants_help)
            return {
                "message": response,
                "stage": 3,
                "block_chat": not user_wants_help,
                "await_response": False,
                "next_stage": None
            }
        
        return {"message": "", "stage": 0, "block_chat": False}
    
    def find_matching_scenario(self, user_message: str) -> Optional[str]:
        """Find matching scenario from database based on user input"""
        user_lower = user_message.lower().strip().strip('"')
        
        scenarios = self.scenario_responses.get("malik", {})
        best_match = None
        best_ratio = 0
        
        for scenario_key, scenario_data in scenarios.items():
            user_input = scenario_data.get("user", "").lower()
            ratio = SequenceMatcher(None, user_lower, user_input).ratio()
            if ratio > 0.7:
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_match = scenario_key
        
        return best_match if best_ratio > 0.7 else None
    
    def get_exact_response(self, scenario_key: str) -> Optional[str]:
        """Get EXACT response from database"""
        scenarios = self.scenario_responses.get("malik", {})
        scenario = scenarios.get(scenario_key, {})
        return scenario.get("malik")
    
    def get_creative_response(self, user_message: str) -> str:
        """Get creative response from OpenAI for novel questions"""
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
        
        return assistant_message
    
    def get_response(self, user_message: str, crisis_stage: int = 1, user_name: str = "there") -> dict:
        """Get response - handles both normal and crisis scenarios"""
        if self.check_safety_crisis(user_message):
            self.add_message("user", user_message)
            response = self.get_crisis_response(user_message, stage=crisis_stage, user_name=user_name)
            self.add_message("assistant", response["message"])
            self.crisis_detected = True
            self.session_started = True
            return response
        scenario_key = self.find_matching_scenario(user_message)
        
        if scenario_key:
            exact_response = self.get_exact_response(scenario_key)
            if exact_response:
                self.add_message("user", user_message)
                self.add_message("assistant", exact_response)
                self.session_started = True
                return {"message": exact_response, "is_crisis": False}
        response = self.get_creative_response(user_message)
        self.session_started = True
        return {"message": response, "is_crisis": False}
    
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
        self.crisis_detected = False