"""
Streamlit Web Interface - Live Chat with Maya & Malik
FIXED: Proper response handling for dict-based crisis protocol
"""

import os
import streamlit as st
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

# Page configuration
st.set_page_config(
    page_title="AI Coaching Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'maya' not in st.session_state:
    st.session_state.maya = MayaUmani(MAYA_SYSTEM_PROMPT, SCENARIO_RESPONSES)
if 'malik' not in st.session_state:
    st.session_state.malik = MalikNadir(MALIK_SYSTEM_PROMPT, SCENARIO_RESPONSES)
if 'current_coach' not in st.session_state:
    st.session_state.current_coach = None
if 'coach_name' not in st.session_state:
    st.session_state.coach_name = None
if 'coach_type' not in st.session_state:
    st.session_state.coach_type = None
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'user_name' not in st.session_state:
    st.session_state.user_name = "User"
if 'crisis_stage' not in st.session_state:
    st.session_state.crisis_stage = 1
if 'chat_disabled' not in st.session_state:
    st.session_state.chat_disabled = False

# Header
st.markdown("=" * 60)
st.title("🧠 AI COACHING PLATFORM")
st.markdown("=" * 60)
st.markdown("**Natural, Professional Coaching with AI**")
st.markdown("**EXACT 100% Responses + Creative Novel Questions**")
st.markdown("=" * 60)

# Sidebar for navigation
with st.sidebar:
    st.markdown("## 📋 Menu")
    
    menu_choice = st.radio(
        "Select an option:",
        options=["Chat", "View Conversation Starters", "View Example Scenarios", "Reset"],
        index=0
    )
    
    if st.session_state.current_coach:
        st.markdown(f"### ✓ Connected with {st.session_state.coach_name}")
        if st.button("🔄 Switch Coach", use_container_width=True):
            st.session_state.current_coach = None
            st.session_state.coach_name = None
            st.session_state.coach_type = None
            st.session_state.messages = []
            st.session_state.crisis_stage = 1
            st.session_state.chat_disabled = False
            st.rerun()
        
        if st.button("🗑️ Clear Conversation", use_container_width=True):
            st.session_state.current_coach.reset_conversation()
            st.session_state.messages = []
            st.session_state.crisis_stage = 1
            st.session_state.chat_disabled = False
            st.success("Conversation cleared!")
            st.rerun()

# Main content area
if menu_choice == "Chat":
    if not st.session_state.current_coach:
        # Coach selection
        st.markdown("## Select Your Coach")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🧘 Maya Umani\n(Life Coach - Mindfulness)", use_container_width=True, key="maya_btn"):
                st.session_state.current_coach = st.session_state.maya
                st.session_state.coach_name = "Maya Umani"
                st.session_state.coach_type = "maya"
                st.session_state.messages = []
                st.session_state.crisis_stage = 1
                st.session_state.chat_disabled = False
                st.rerun()
        
        with col2:
            if st.button("💪 Malik Nadir\n(Performance Coach - Resilience)", use_container_width=True, key="malik_btn"):
                st.session_state.current_coach = st.session_state.malik
                st.session_state.coach_name = "Malik Nadir"
                st.session_state.coach_type = "malik"
                st.session_state.messages = []
                st.session_state.crisis_stage = 1
                st.session_state.chat_disabled = False
                st.rerun()
    
    else:
        # Chat interface
        st.markdown(f"## Chat Session with {st.session_state.coach_name}")
        
        # Display conversation history
        chat_container = st.container()
        
        with chat_container:
            for message in st.session_state.messages:
                if message["role"] == "user":
                    st.chat_message("user").write(message["content"])
                else:
                    st.chat_message("assistant").write(message["content"])
        
        # Show warning if chat is disabled
        if st.session_state.chat_disabled:
            st.error("⚠️ This conversation has been ended for your safety. Please reach out to professional support.")
        else:
            # User input
            user_input = st.chat_input(f"You: ")
            
            if user_input:
                # Add user message to display
                st.session_state.messages.append({
                    "role": "user",
                    "content": user_input
                })
                
                # Get coach response with proper parameters
                with st.spinner(f"{st.session_state.coach_name} is thinking..."):
                    response = st.session_state.current_coach.get_response(
                        user_input,
                        crisis_stage=st.session_state.crisis_stage,
                        user_name=st.session_state.user_name
                    )
                
                # Handle response (can be dict or string)
                if isinstance(response, dict):
                    message_content = response.get("message", "")
                    
                    # Check if this is a crisis response
                    if "stage" in response:
                        # Update crisis stage for next response
                        if response.get("next_stage"):
                            st.session_state.crisis_stage = response.get("next_stage")
                        
                        # Check if chat should be disabled
                        if response.get("block_chat"):
                            st.session_state.chat_disabled = True
                else:
                    message_content = response
                
                # Add coach response to display
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": message_content
                })
                
                st.rerun()

elif menu_choice == "View Conversation Starters":
    st.markdown("## Conversation Starters")
    
    for coach_name in ["maya", "malik"]:
        coach_display = "🧘 MAYA UMANI" if coach_name == "maya" else "💪 MALIK NADIR"
        
        with st.expander(coach_display, expanded=False):
            for category, starters in CONVERSATION_STARTERS[coach_name].items():
                st.markdown(f"### {category.replace('_', ' ').upper()}")
                for i, starter in enumerate(starters, 1):
                    st.markdown(f"{i}. {starter}")

elif menu_choice == "View Example Scenarios":
    st.markdown("## Example Scenarios")
    
    for coach_name in ["maya", "malik"]:
        coach_display = "🧘 MAYA UMANI" if coach_name == "maya" else "💪 MALIK NADIR"
        
        st.markdown(f"### {coach_display}")
        
        scenarios = SCENARIO_RESPONSES.get(coach_name, {})
        
        for scenario_key in list(scenarios.keys()):
            scenario = scenarios[scenario_key]
            title = scenario.get("title", "")
            user_input = scenario.get("user", "")
            response_key = "maya" if coach_name == "maya" else "malik"
            coach_response = scenario.get(response_key, "")
            
            with st.expander(f"📌 {title}", expanded=False):
                st.markdown("**User:**")
                st.write(user_input)
                st.markdown("**Coach Response:**")
                st.write(coach_response)

elif menu_choice == "Reset":
    st.markdown("## Reset Application")
    
    if st.button("🔄 Reset All Sessions", use_container_width=True):
        st.session_state.maya = MayaUmani(MAYA_SYSTEM_PROMPT, SCENARIO_RESPONSES)
        st.session_state.malik = MalikNadir(MALIK_SYSTEM_PROMPT, SCENARIO_RESPONSES)
        st.session_state.current_coach = None
        st.session_state.coach_name = None
        st.session_state.coach_type = None
        st.session_state.messages = []
        st.session_state.crisis_stage = 1
        st.session_state.chat_disabled = False
        st.success("All sessions reset successfully!")
        st.rerun()

# Footer
st.markdown("=" * 60)
st.markdown("**Thank you for using AI Coaching Platform**")
st.markdown("=" * 60)