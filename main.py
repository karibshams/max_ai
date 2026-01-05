"""
Main Test Interface - Live Chat with Maya & Malik
Complete test platform with all conversation data
"""

import os
from dotenv import load_dotenv
from Maya_Umani import MayaUmani
from Malik_Nadir import MalikNadir
from Maya_Umani_prompt import MAYA_SYSTEM_PROMPT
from Malik_Nadir_prompt import MALIK_SYSTEM_PROMPT
from conversation_database import (
    CONVERSATION_STARTERS, 
    SCENARIO_RESPONSES,
    get_starter,
    get_scenario_response
)

load_dotenv()

class ChatInterface:
    def __init__(self):
        """Initialize chat interface with both coaches"""
        self.maya = MayaUmani(MAYA_SYSTEM_PROMPT)
        self.malik = MalikNadir(MALIK_SYSTEM_PROMPT)
        self.current_coach = None
        self.coach_name = None
        self.coach_type = None
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("AI COACHING PLATFORM - Live Chat")
        print("="*60)
        print("1. Chat with Maya Umani (Life Coach - Mindfulness)")
        print("2. Chat with Malik Nadir (Performance Coach - Resilience)")
        print("3. View Conversation Starters")
        print("4. View Example Scenarios")
        print("5. Exit")
        print("="*60)
    
    def select_coach(self) -> bool:
        """Let user select which coach to chat with"""
        self.display_menu()
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == "1":
            self.current_coach = self.maya
            self.coach_name = "Maya Umani"
            self.coach_type = "maya"
            print(f"\n✓ Connected with {self.coach_name}")
            return True
        elif choice == "2":
            self.current_coach = self.malik
            self.coach_name = "Malik Nadir"
            self.coach_type = "malik"
            print(f"\n✓ Connected with {self.coach_name}")
            return True
        elif choice == "3":
            self.show_starters()
            return self.select_coach()
        elif choice == "4":
            self.show_scenarios()
            return self.select_coach()
        elif choice == "5":
            print("Thank you for using AI Coaching Platform!")
            return False
        else:
            print("Invalid choice. Try again.")
            return self.select_coach()
    
    def show_starters(self):
        """Display conversation starters"""
        print("\n" + "="*60)
        print("CONVERSATION STARTERS")
        print("="*60)
        
        for coach_name in ["maya", "malik"]:
            print(f"\n{coach_name.upper()}:")
            for category, starters in CONVERSATION_STARTERS[coach_name].items():
                print(f"\n  {category.replace('_', ' ').upper()}:")
                for i, starter in enumerate(starters[:2], 1):
                    print(f"    {i}. {starter}")
    
    def show_scenarios(self):
        """Display scenario examples"""
        print("\n" + "="*60)
        print("EXAMPLE SCENARIOS")
        print("="*60)
        
        scenarios = {
            "feeling_overwhelmed": "Feeling Overwhelmed",
            "self_doubt": "Self-Doubt",
            "loss_of_motivation": "Loss of Motivation",
            "fear_wrong_decision": "Fear of Wrong Decision",
            "stress_sleep": "Stress & Sleep Issues",
            "relationship_conflict": "Relationship Conflict",
            "procrastination": "Procrastination",
            "boundaries": "Struggling with Boundaries",
            "career_doubt": "Career/Purpose Doubt",
            "setback_loss": "Setback or Loss"
        }
        
        for coach_name in ["maya", "malik"]:
            print(f"\n{coach_name.upper()}:")
            for scenario_key, scenario_name in list(scenarios.items())[:3]:
                scenario = get_scenario_response(coach_name, scenario_key)
                if scenario:
                    print(f"\n  {scenario_name}:")
                    print(f"    User: {scenario.get('user', 'N/A')}")
                    print(f"    Coach: {scenario.get('response', 'N/A')}")
    
    def start_chat(self):
        """Start live chat session"""
        if not self.select_coach():
            return
        
        print("\n" + "="*60)
        print(f"CHAT SESSION WITH {self.coach_name.upper()}")
        print("="*60)
        print("Commands:")
        print("  'back' - Select different coach")
        print("  'history' - View conversation")
        print("  'clear' - Clear conversation")
        print("  'exit' - End session")
        print("="*60 + "\n")
        
        while True:
            try:
                user_input = input(f"You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == "exit":
                    print("Session ended.")
                    break
                
                if user_input.lower() == "back":
                    print("\n(Returning to coach selection...)")
                    self.start_chat()
                    break
                
                if user_input.lower() == "history":
                    self.show_history()
                    continue
                
                if user_input.lower() == "clear":
                    self.current_coach.reset_conversation()
                    print("Conversation cleared.\n")
                    continue
                
                print(f"\n{self.coach_name}: ", end="", flush=True)
                response = self.current_coach.get_response(user_input)
                print(response + "\n")
            
            except KeyboardInterrupt:
                print("\n\nSession interrupted.")
                break
            except Exception as e:
                print(f"Error: {str(e)}")
                continue
    
    def show_history(self):
        """Display conversation history"""
        history = self.current_coach.get_conversation_history()
        
        if not history:
            print("\nNo conversation yet.\n")
            return
        
        print("\n" + "-"*60)
        print("CONVERSATION HISTORY")
        print("-"*60)
        for msg in history:
            role = "YOU" if msg["role"] == "user" else self.coach_name.upper()
            content = msg["content"]
            print(f"\n{role}:\n{content}")
        print("\n" + "-"*60 + "\n")

def main():
    """Main entry point"""
    print("\n" + "="*60)
    print("WELCOME TO AI COACHING PLATFORM")
    print("="*60)
    print("Natural, Professional Coaching with AI")
    print("="*60)
    
    try:
        chat = ChatInterface()
        chat.start_chat()
    except Exception as e:
        print(f"Application error: {str(e)}")

if __name__ == "__main__":
    main()