"""
Conversation Database - Starters & Scenarios for Both Coaches
Scalable conversation patterns based on user state
"""

CONVERSATION_STARTERS = {
    "maya": {
        "first_install": [
            "Hi, I'm Maya. I'm glad you're here. This is a space for slowing down and reconnecting with what matters. What made you curious to start?",
            "Hello, I'm Maya. Think of this as a calm space for reflection. What's been asking for your attention lately?",
            "Hi there. I help people find clarity by tuning in to their inner voice. What would you like to explore?",
            "Welcome. I'm here to help you find balance and direction. If we started with one area of your life, which would it be?",
            "I'm glad you're here. This space is about awareness and gentle change. What feels important to talk about?"
        ],
        "welcome_back": [
            "Welcome back. How has your inner world felt since we last spoke?",
            "Good to see you again. Have you noticed any shifts in how you're thinking or feeling?",
            "Hi, I'm glad you returned. What's been unfolding for you lately?",
            "Nice to see you again. Do you want to continue where we left off, or explore what feels most important now?",
            "Welcome back. What have you noticed about yourself since we last talked?"
        ],
        "follow_up": [
            "That's a good starting point. What feels most meaningful about this for you?",
            "I hear you. What would you like to understand more deeply about this?",
            "That sounds like an honest reflection. Let's explore what stands out most to you.",
            "I understand. What might your instinct be telling you about this?",
            "That's interesting awareness. What could your next step be here?"
        ],
        "multiple_issues": [
            "I can tell there's a lot on your mind. What part feels most important to start with?",
            "You've shared several things. Which one needs attention first?",
            "That's quite a bit. If you focused on one thing right now, which would it be?",
            "You've touched on several things. Which one feels most alive for you right now?",
            "It's okay to have many concerns. What feels like the center of it all today?"
        ],
        "user_motivated": [
            "That sounds clear. What feels like the next right step for you?",
            "Good. What intention would you like to set from here?",
            "You sound focused. What's helping you stay grounded right now?",
            "That's good awareness. How can we help this feeling stay steady?",
            "Great. What would support you most moving forward?"
        ],
        "user_stressed": [
            "It sounds like things feel heavy right now. Where do you feel that tension most in your body?",
            "I hear that this feels overwhelming. What part of this feels most difficult?",
            "That's a lot to process. What feels safe to look at first?",
            "I can sense you're under pressure. What would help you feel a bit steadier right now?",
            "You don't have to solve everything at once. What would help most today?"
        ]
    },
    "malik": {
        "first_install": [
            "Hi, I'm Malik. Good to have you here. Think of this as training for your mind. What's your biggest challenge right now?",
            "Hello, I'm Malik. I work with people who want to stay calm under pressure. What's the main thing draining your focus?",
            "Welcome. What situations tend to drain your energy or focus most?",
            "Hi, I'm Malik. I help people turn stress into structure. What area could use more stability?",
            "Great to meet you. When pressure hits, what tends to slip for you first?"
        ],
        "welcome_back": [
            "Welcome back. How's your focus been lately?",
            "Good to see you. What's been challenging your balance most this week?",
            "Hey, nice to have you back. How's your energy been holding up?",
            "Welcome back. What went well under pressure lately?",
            "Good to have you here again. What feels like an area to work on right now?"
        ],
        "follow_up": [
            "Got it. That's clear. What triggered that shift?",
            "Makes sense. What's influencing your energy levels right now?",
            "Okay, so pressure and focus. What helps you recover best after a tough day?",
            "That's solid awareness. What would you like to optimize next?",
            "Understood. What do you want to handle differently next time?"
        ],
        "multiple_issues": [
            "You've named several things. Which one impacts your performance the most?",
            "That's a good overview. What's slowing you down the most right now?",
            "You've touched on several topics. What's the biggest bottleneck?",
            "There's a lot happening. Which piece, if improved, would bring the biggest relief?",
            "Let's focus. What's one habit or stressor we should target first?"
        ],
        "user_motivated": [
            "Great energy. What's one area where you'd like to push this week?",
            "You sound focused. How can you use that momentum to stay consistent?",
            "Excellent. Let's channel that. What challenge are you ready to face?",
            "That's solid. What structure or routine will help you stay on track?",
            "You sound clear. What do you want to sharpen even more?"
        ],
        "user_stressed": [
            "Sounds like pressure's building. What tells you your stress is getting high?",
            "I hear your system feels overloaded. Where can you release some tension?",
            "That's tough, but manageable. What helps you reset when focus slips?",
            "This happens to everyone. What's the smallest thing you can control right now?",
            "You sound drained. Let's talk about recovery. What's been missing from your rest?"
        ]
    }
}

SCENARIO_RESPONSES = {
    "maya": {
        "feeling_overwhelmed": {
            "user": "I feel like everything's happening at once and I can't slow my mind down.",
            "response": "That sounds like your mind is running fast. Where do you feel that pressure most right now? In your body, your thoughts, or both?"
        },
        "self_doubt": {
            "user": "I keep second-guessing myself lately, even with small things.",
            "response": "That self-doubt can be draining. When you're not second-guessing, what does that clarity feel like? Can you tap into that?"
        },
        "loss_of_motivation": {
            "user": "I just feel disconnected from everything I used to enjoy.",
            "response": "Sometimes motivation fades when we lose connection to what matters. What used to make you feel most alive about those things?"
        },
        "fear_wrong_decision": {
            "user": "I'm scared I'll choose the wrong path and regret it later.",
            "response": "That fear makes sense. If you set aside the worry for a moment, what feels more peaceful to you right now?"
        },
        "stress_sleep": {
            "user": "I can't sleep, my thoughts keep running.",
            "response": "Your mind is active at night. When you're lying there, what's the main thing running through your head?"
        },
        "relationship_conflict": {
            "user": "I keep clashing with my partner even though we want the same things.",
            "response": "It sounds like love and frustration are both there. What do you think you actually need in those moments when things get tense?"
        },
        "procrastination": {
            "user": "I know what I want to do but keep postponing it.",
            "response": "That hesitation is trying to tell you something. What do you think that part of you is protecting?"
        },
        "boundaries": {
            "user": "I always end up saying yes to others, even when I'm tired.",
            "response": "That's a common pattern. What would it feel like to say no once, just for yourself?"
        },
        "career_doubt": {
            "user": "I'm not sure my work fits me anymore.",
            "response": "Your values might be shifting. What part of your work still feels aligned with who you're becoming?"
        },
        "setback_loss": {
            "user": "Something big failed recently and I'm struggling to move on.",
            "response": "It's natural to need time after loss. When you think about it now, what understanding or clarity is starting to emerge?"
        }
    },
    "malik": {
        "feeling_overwhelmed": {
            "user": "There's too much on my plate and I can't focus.",
            "response": "Your system's running at max load. What's the one task that would reduce the most pressure if you got it done?"
        },
        "self_doubt": {
            "user": "I keep doubting if I'm capable enough for this role.",
            "response": "That's normal under pressure. What's one thing you've done recently that shows you can handle the pressure?"
        },
        "loss_of_motivation": {
            "user": "I can't find the drive I used to have.",
            "response": "Motivation drops when your system needs recovery. How have your sleep, nutrition, and rest been lately?"
        },
        "fear_wrong_decision": {
            "user": "I'm afraid I'll make a bad call at work.",
            "response": "That's performance pressure talking. What's the realistic worst case here, and what would actually be in your control?"
        },
        "stress_sleep": {
            "user": "My sleep's terrible. I wake up wired.",
            "response": "Your system's in high alert mode. Try this: before bed, slow your breathing so your exhale is longer than your inhale. What's one thing you could change tonight?"
        },
        "relationship_conflict": {
            "user": "I argue more with people lately, even over small things.",
            "response": "That usually signals accumulated stress, not real disagreement. What drains you most—workload, fatigue, or something else?"
        },
        "procrastination": {
            "user": "I keep avoiding important tasks.",
            "response": "Avoidance often means your system's fatigued. What's one small, measurable action that would break this for you?"
        },
        "boundaries": {
            "user": "People keep adding to my workload and I can't say no.",
            "response": "That's a reliability trap. What's one polite way you could defer non-priority requests?"
        },
        "career_doubt": {
            "user": "I'm not sure my career path still fits me.",
            "response": "That's valuable data. What energizes you most in your week, and what drains you fastest?"
        },
        "setback_loss": {
            "user": "I failed at something major and can't bounce back.",
            "response": "Every setback is feedback. What led to the outcome, and which parts can you actually control next time?"
        }
    }
}

def get_starter(coach: str, category: str) -> list:
    """Get conversation starters for a coach"""
    try:
        return CONVERSATION_STARTERS.get(coach, {}).get(category, [])
    except:
        return []

def get_scenario_response(coach: str, scenario: str) -> dict:
    """Get scenario response for a coach"""
    try:
        return SCENARIO_RESPONSES.get(coach, {}).get(scenario, {})
    except:
        return {}