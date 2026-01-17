"""
Maya Umani - Main Response Handler - SYNCED
Life Coach - Returns EXACT responses with reflection variety + creative for novel questions
Synced with condensed prompt structure and safety protocols
"""

import os
import random
from openai import OpenAI
from typing import List, Dict, Optional
from difflib import SequenceMatcher

class MayaUmani:
    def __init__(self, system_prompt: str, scenario_responses: dict):
        """Initialize Maya with system prompt and scenario database"""
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
    
    def get_crisis_response(self, user_message: str, is_confirmed: bool = False) -> str:
        """Get appropriate crisis response - Stage 1 or Stage 2"""
        if is_confirmed:
            return """This is a state of emergency. I can't be the support you need — you need immediate professional care.

📞 National Crisis Hotline: 09815747623
📞 Call 911 or Emergency Services immediately
📞 Go to nearest emergency room

Tell someone you trust TODAY. You deserve real professional help, not a chatbot. Will you make that call now?"""
        else:
            return """I want to pause here because what you're sharing sounds really serious. I'm not a medical professional, and you deserve real support.

Please reach out right now:
📞 National Crisis Hotline: 09815747623
📞 Call 911 or Emergency Services
📞 Crisis Text Line: Text HOME to 741741

Will you reach out to one of these right now?

Does what you're experiencing mean you've had thoughts about harming yourself?"""
    
    def find_matching_scenario(self, user_message: str) -> Optional[str]:
        """Find matching scenario from database based on user input"""
        user_lower = user_message.lower().strip().strip('"')
        
        scenarios = self.scenario_responses.get("maya", {})
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
        """Get response from database with variety for Maya"""
        scenarios = self.scenario_responses.get("maya", {})
        scenario = scenarios.get(scenario_key, {})
        maya_responses = scenario.get("maya")
        
        # If it's a list (multiple variations), pick one randomly
        if isinstance(maya_responses, list):
            return random.choice(maya_responses)
        # If it's a string (single response), return it
        else:
            return maya_responses
    
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
        
        # CRITICAL: Check for safety crisis FIRST
        if self.check_safety_crisis(user_message):
            self.add_message("user", user_message)
            
            # If this is a follow-up to an already-detected crisis
            if self.crisis_detected:
                response = self.get_crisis_response(user_message, is_confirmed=True)
            else:
                response = self.get_crisis_response(user_message, is_confirmed=False)
                self.crisis_detected = True
            
            self.add_message("assistant", response)
            self.session_started = True
            return response
        
        # Try to find matching scenario
        scenario_key = self.find_matching_scenario(user_message)
        
        if scenario_key:
            # Return response from database (with variety for Maya)
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
        self.crisis_detected = False