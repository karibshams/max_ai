"""
Malik Nadir - Main Response Handler
Performance Coach - Returns EXACT responses from database + creative for novel questions
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
    
    def add_message(self, role: str, content: str):
        """Add message to conversation history"""
        self.conversation_history.append({
            "role": role,
            "content": content
        })
    
    def find_matching_scenario(self, user_message: str) -> Optional[str]:
        """Find matching scenario from database based on user input"""
        user_lower = user_message.lower().strip().strip('"')
        
        scenarios = self.scenario_responses.get("malik", {})
        best_match = None
        best_ratio = 0
        
        for scenario_key, scenario_data in scenarios.items():
            user_input = scenario_data.get("user", "").lower()
            ratio = SequenceMatcher(None, user_lower, user_input).ratio()
            
            # Check for exact or very similar matches
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
    
    def get_response(self, user_message: str) -> str:
        """Get response - EXACT from database or creative for novel questions"""
        
        # Try to find matching scenario
        scenario_key = self.find_matching_scenario(user_message)
        
        if scenario_key:
            # Return EXACT response from database
            exact_response = self.get_exact_response(scenario_key)
            if exact_response:
                self.add_message("user", user_message)
                self.add_message("assistant", exact_response)
                self.session_started = True
                return exact_response
        
        # If no match, get creative response from OpenAI
        response = self.get_creative_response(user_message)
        self.session_started = True
        return response
    
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