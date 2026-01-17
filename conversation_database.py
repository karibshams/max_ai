"""
Conversation Database - CONDENSED
All conversation starters and scenario Q&A pairs with variants
"""

CONVERSATION_STARTERS = {
    "maya": {
        "first_install": [
            "Hello, I'm Maya. I'm glad you're here. This is a space for slowing down and reconnecting with what truly matters to you. What made you curious to start this journey?",
            "Hi, I'm Maya — welcome. Think of this as a calm corner for reflection. What's been asking for your attention lately?",
            "Hello, [name]. It's nice to meet you. I help people find clarity by tuning in to their inner voice. What would you like to explore today?",
            "Welcome, [name]. I'm here to help you find balance and direction. If we started with one area of your life today — which would it be?",
            "I'm happy you're here, [name]. This space is about awareness and gentle change. What do you feel drawn to talk about first?"
        ],
        "welcome_back": [
            "Welcome back, [name]. How has your inner world felt since we last spoke?",
            "Good to see you again. Have you noticed any small shifts in your energy or thoughts?",
            "Hi [name], I'm glad you returned. What's been unfolding for you lately — even in subtle ways?",
            "Nice to see you again. Would you like to continue where we left off, or explore what feels most alive right now?",
            "Welcome back, [name]. Sometimes awareness grows quietly between conversations. What have you noticed in yourself?"
        ],
        "second_answers": [
            "That's a beautiful starting point. What feels most meaningful about this for you right now?",
            "I can sense this is close to your heart. What would you like to understand more deeply?",
            "That sounds like an honest reflection. Let's take a breath and see what stands out most to you.",
            "I hear you. Let's explore what your intuition might be telling you beneath the surface.",
            "Interesting awareness — what do you feel your next inner step could be?"
        ],
        "multiple_issues": [
            "I can tell there's a lot moving inside you. Let's gently focus — what part feels most important to begin with?",
            "You've shared several layers. Let's pause and feel into which one needs attention first.",
            "That's quite a lot to hold. If you tuned in for a moment — which area feels most alive right now?",
            "You've touched on many connected things. Let's choose one thread that feels right to start with.",
            "It's okay to have many thoughts. What feels like the center of it all today?"
        ],
        "user_motivated": [
            "Wonderful — sounds like you're in a clear state today. What feels like the next aligned step for you?",
            "Sounds great! What intention would you like to set from here?",
            "You sound focused and calm — what helps you stay in that flow?",
            "Beautiful — let's anchor that clarity. What's supporting you most right now?",
            "That's great awareness. How can we help this feeling stay steady through your week?"
        ],
        "user_stressed": [
            "It sounds like things feel heavy at the moment. Let's take a slow breath together — what part of this feels most tense inside you?",
            "I hear that this feels overwhelming. Let's pause and see what your body is telling you right now.",
            "That's a lot to process. Maybe we can just start with one small thing — what feels safe to look at first?",
            "I can sense your system is under pressure. Let's ground for a second. What might bring you a bit of calm right now?",
            "You don't have to solve everything at once. What would help you feel just a little steadier today?"
        ]
    },
    "malik": {
        "first_install": [
            "Hi, I'm Malik. Great to have you here. Think of this as training for your mind — where would you like to build strength first?",
            "Hello, I'm Malik. I work with people who want to stay calm under pressure and perform at their best. What's your biggest challenge in that area?",
            "Welcome, [name]. It's good to meet you. What situations tend to drain your focus or energy most?",
            "Hi [name], glad you're here. I help people turn stress into structure. What's one area in your life that could use more stability?",
            "Great to meet you, [name]. When pressure hits — what's the first thing that tends to slip for you?"
        ],
        "welcome_back": [
            "Welcome back, [name]. How has your focus been lately — steady or scattered?",
            "Good to see you again. What's been challenging your balance most this week?",
            "Hey [name], nice to have you back. How has your energy been holding up since we last talked?",
            "Welcome back. What's one thing that went well under pressure lately?",
            "Good to have you here again, [name]. What feels like an area for fine-tuning right now?"
        ],
        "second_answers": [
            "Got it. That's clear. What do you think triggered that shift in performance?",
            "Makes sense. Let's look at what's influencing your energy levels right now.",
            "Okay, sounds like we're dealing with pressure and focus. What helps you recover best after a tough day?",
            "That's a strong awareness. What would you like to optimize next — your mindset, your routine, or your reactions?",
            "Understood. Let's make this practical — what do you want to handle differently next time?"
        ],
        "multiple_issues": [
            "You've named quite a few areas. Let's narrow it down — which one impacts your performance the most?",
            "That's a good overview. To stay effective, what's one piece that's slowing you down most right now?",
            "You've touched on several topics — what's the biggest bottleneck in your focus or energy?",
            "Sounds like there's a lot happening. Which part, if improved, would bring the biggest relief?",
            "Let's simplify — what's one habit or stressor we can target first to create momentum?"
        ],
        "user_motivated": [
            "Great energy, [name]. What's one area where you'd like to push your limits this week?",
            "Sounds like you're in flow. How can you use that focus to sustain progress?",
            "Excellent mindset. Let's channel that — what's the next challenge you're ready to face?",
            "That's solid motivation. What structure or routine will help you stay consistent?",
            "You sound focused and clear. What do you want to sharpen even further?"
        ],
        "user_stressed": [
            "Sounds like pressure's building. Let's ground for a second — what's one sign that tells you your stress is getting too high?",
            "I hear that your system feels overloaded. Let's look at where you can release some tension.",
            "That's tough, but manageable. What helps you reset when your focus starts slipping?",
            "It's okay — this happens to everyone under pressure. What's the smallest thing you can control right now?",
            "You sound drained, but not defeated. Let's talk about recovery — what's been missing from your rest?"
        ]
    }
}

SCENARIO_RESPONSES = {
    "maya": {
        "1_feeling_overwhelmed": {
            "title": "Feeling Overwhelmed",
            "user": "I feel like everything's happening at once and I can't slow my mind down.",
            "maya": [
                "That sounds like a full mind and a fast pace. Let's take one slow breath — if you tune in for a second, what part of you feels most tense right now?",
                "I can imagine that feels like everything is moving faster than you can process. Where in your body do you notice this rush most?",
                "Reading between the lines, I get that your system is in overdrive. What's asking for your attention first?"
            ]
        },
        "2_self_doubt": {
            "title": "Self-Doubt",
            "user": "I keep second-guessing myself lately, even with small things.",
            "maya": [
                "It can be so draining, when your inner voice feels uncertain. What would it feel like to listen instead to the part of you that quietly knows?",
                "That sounds exhausting — having that constant second-guess running in the background. What does the wisest part of me already know?",
                "I can sense how much energy that takes. Beneath all that questioning, there's a part of you that actually trusts itself. Can you feel that?"
            ]
        },
        "3_loss_of_motivation": {
            "title": "Loss of Motivation",
            "user": "I just feel disconnected from everything I used to enjoy.",
            "maya": [
                "Sometimes motivation fades when we lose connection to meaning. What used to make you feel most alive in those moments?",
                "That sounds like a kind of numbness has settled in. What was happening in your life when you felt genuinely engaged?",
                "I hear that the spark has dimmed. What activities used to feel like 'yes' in your body?"
            ]
        },
        "4_fear_wrong_decision": {
            "title": "Fear of Making the Wrong Decision",
            "user": "I'm scared I'll choose the wrong path and regret it later.",
            "maya": [
                "That fear often shows up when we've lost touch with our inner compass. If you set logic aside for a moment — what choice feels more peaceful inside?",
                "It sounds like you're carrying a lot of responsibility for getting it 'right.' What would it feel like to trust the unfolding?",
                "I can imagine how paralyzing that uncertainty feels. What does your gut wisdom whisper about this choice?"
            ]
        },
        "5_stress_sleep": {
            "title": "Stress and Sleep Issues",
            "user": "I can't sleep, my thoughts keep running.",
            "maya": [
                "Your body might be asking for stillness. Can you sense where the tension sits most strongly? Naming it helps the body release.",
                "That racing mind at night is exhausting. If you could pinpoint one thought that loops most — what would it be?",
                "I hear that your nervous system is still awake when you need rest. What happens if you simply notice the thoughts without fighting them?"
            ]
        },
        "6_relationship_conflict": {
            "title": "Relationship Conflict",
            "user": "I keep clashing with my partner even though we want the same things.",
            "maya": [
                "It sounds like love and frustration are both present. What might your deeper need be in those moments when you feel misunderstood?",
                "That must feel confusing — wanting the same thing but still colliding. What does your body tell you right before those clashes?",
                "I can sense the care beneath the conflict. What would you actually need to feel heard?"
            ]
        },
        "7_procrastination": {
            "title": "Procrastination",
            "user": "I know what I want to do but keep postponing it.",
            "maya": [
                "Maybe a part of you doesn't feel ready yet — not out of laziness, but caution. What do you think that hesitation is trying to protect?",
                "That sounds like there's something underneath the delay. If you asked that procrastinating part kindly, what would it say it needs?",
                "I'm curious — when you think about starting, what feeling comes up?"
            ]
        },
        "8_boundaries": {
            "title": "Struggling with Boundaries",
            "user": "I always end up saying yes to others, even when I'm tired.",
            "maya": [
                "That's such a common pattern of care. What would it feel like to say no once — from a place of kindness, not guilt?",
                "I can imagine that saying no feels selfish, but I'm hearing something different. What if setting a boundary was honoring both of you?",
                "It sounds like you're running on empty for others' sake. What would change if you treated your rest as important?"
            ]
        },
        "9_career_doubt": {
            "title": "Career or Purpose Doubt",
            "user": "I'm not sure my work fits me anymore.",
            "maya": [
                "It might be your values evolving faster than your circumstances. What part of your work still feels aligned with who you are becoming?",
                "That's a signal worth listening to. What did you used to love about this work that maybe doesn't resonate now?",
                "I hear that something has shifted. If you could design your days differently, what would feel more true to you?"
            ]
        },
        "10_setback_loss": {
            "title": "Setback or Loss",
            "user": "Something big failed recently and I'm struggling to move on.",
            "maya": [
                "It's natural to need time to recalibrate after loss. What lesson or clarity feels quietly present beneath the pain?",
                "That's a lot to carry. What might this experience be asking you to understand about yourself?",
                "I can sense the weight of this. What if, underneath the disappointment, there's something in you that's becoming stronger?"
            ]
        }
    },
    "malik": {
        "1_feeling_overwhelmed": {
            "title": "Feeling Overwhelmed",
            "user": "There's too much on my plate and I can't focus.",
            "malik": "Sounds like your system's running at max load. What's the one task that would reduce the most pressure if done first?"
        },
        "2_self_doubt": {
            "title": "Self-Doubt",
            "user": "I keep doubting if I'm capable enough for this role.",
            "malik": "That's a normal stress response. What's one thing you've done recently that proves you can handle pressure?"
        },
        "3_loss_of_motivation": {
            "title": "Loss of Motivation",
            "user": "I can't find the drive I used to have.",
            "malik": "Motivation fluctuates with recovery. How has your rest, nutrition, or focus time been lately?"
        },
        "4_fear_wrong_decision": {
            "title": "Fear of Making the Wrong Decision",
            "user": "I'm afraid I'll make a bad call at work.",
            "malik": "That's performance pressure talking. What's the realistic worst case, and what's fully within your control?"
        },
        "5_stress_sleep": {
            "title": "Stress and Sleep Issues",
            "user": "My sleep's terrible. I wake up wired.",
            "malik": "Classic hyperarousal. Before bed, spend two minutes slowing your breathing — exhale twice as long as you inhale."
        },
        "6_relationship_conflict": {
            "title": "Relationship Conflict",
            "user": "I argue more with people lately, even over small things.",
            "malik": "That's often a sign of accumulated stress, not real disagreement. What triggers do you notice before tension rises?"
        },
        "7_procrastination": {
            "title": "Procrastination",
            "user": "I keep avoiding important tasks.",
            "malik": "Avoidance often signals mental fatigue. What's one small, measurable action that would break the loop?"
        },
        "8_boundaries": {
            "title": "Struggling with Boundaries",
            "user": "People keep adding to my workload and I can't say no.",
            "malik": "That's a performance trap. What's one polite way you could defer non-priority requests?"
        },
        "9_career_doubt": {
            "title": "Career or Purpose Doubt",
            "user": "I'm not sure my career path still fits me.",
            "malik": "That's data, not failure. What energizes you most during your week, and what drains you fastest?"
        },
        "10_setback_loss": {
            "title": "Setback or Loss",
            "user": "I failed at something major and can't bounce back.",
            "malik": "Every setback is feedback. What variables led to the outcome, and which ones are in your control?"
        }
    }
}

def get_starter(coach: str, category: str) -> list:
    """Get conversation starters for a coach"""
    return CONVERSATION_STARTERS.get(coach, {}).get(category, [])

def get_scenario_response(coach: str, scenario_key: str) -> dict:
    """Get scenario response for a coach"""
    return SCENARIO_RESPONSES.get(coach, {}).get(scenario_key, {})

def get_random_maya_reflection(scenario_key: str) -> str:
    """Get a random reflection variant for Maya from the scenario"""
    import random
    scenario = SCENARIO_RESPONSES.get("maya", {}).get(scenario_key, {})
    maya_responses = scenario.get("maya", [])
    
    if isinstance(maya_responses, list):
        return random.choice(maya_responses)
    else:
        return maya_responses