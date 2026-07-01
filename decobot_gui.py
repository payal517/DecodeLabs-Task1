"""
🤖 RULE-BASED AI CHATBOT - PROJECT 1 (DECODELABS)
Deterministic responses using dictionary mapping + fallback
Complete with all required features
"""

import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(
    page_title="RuleBot - DecodeLabs Project 1",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1.5rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .main-header h1 {
        color: white;
        font-size: 2.8rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        color: rgba(255,255,255,0.95);
        font-size: 1.1rem;
        margin: 5px 0 0 0;
    }
    
    .main-header .badge {
        background: rgba(255,255,255,0.2);
        padding: 5px 15px;
        border-radius: 20px;
        display: inline-block;
        margin-top: 10px;
        color: white;
        font-size: 0.9rem;
    }
    
    .stChatMessage {
        padding: 15px;
        border-radius: 15px;
        margin: 8px 0;
        animation: slideIn 0.5s ease;
    }
    
    @keyframes slideIn {
        from { 
            opacity: 0; 
            transform: translateX(-20px);
        }
        to { 
            opacity: 1; 
            transform: translateX(0);
        }
    }
    
    [data-testid="user"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border-radius: 15px 15px 5px 15px !important;
    }
    
    [data-testid="assistant"] {
        background: #f0f2f6 !important;
        border-left: 5px solid #667eea !important;
        border-radius: 15px 15px 15px 5px !important;
    }
    
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 8px 20px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    .info-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 10px 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .stat-box {
        background: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
    }
    
    .stat-label {
        color: #666;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

responses = {
    "hello": [
        "Hello! How can I help you today? 😊",
        "Hi there! Nice to see you! 👋",
        "Hey! What brings you here? 💬",
        "Greetings! Ready to chat? 🤖"
    ],
    
    "hi": [
        "Hi there! Type 'help' to see what I can do. 🎯",
        "Hello! How's your day going? 🌟",
        "Hey! Good to see you! 😄"
    ],
    
    "hey": [
        "Hey! What's up? 😊",
        "Hey there! How can I assist you? 💬",
        "Yo! Ready for some chat? 🎮"
    ],
    
    "how are you": [
        "I'm just a bunch of rules, but I'm functioning perfectly! 🤖",
        "Feeling great! Thanks for asking! 🚀",
        "All systems operational! How about you? ⚡",
        "Better now that you're here! 😊"
    ],
    "how are you?": [
        "I'm just a bunch of rules, but I'm functioning perfectly! 🤖",
        "I'm doing fantastic! 💪",
        "Couldn't be better! 🌟"
    ],
    
    "what is your name": [
        "I'm RuleBot, your deterministic AI assistant. 🤖",
        "I'm called RuleBot - built with pure logic! 🎯",
        "RuleBot at your service! 📛"
    ],
    "what's your name": [
        "I'm RuleBot, your deterministic AI assistant. 🤖",
        "You can call me RuleBot! 😊"
    ],
    "name": [
        "I'm called RuleBot. Nice to meet you! 😊",
        "RuleBot - your AI companion! 🌟"
    ],
    
    "help": [
        "📋 **I understand these commands:**\n• hello / hi / hey\n• how are you\n• what is your name / name\n• joke\n• motivate\n• thanks / thank you\n• bye / exit / quit\n\nTry them out! 🎯"
    ],
    "commands": [
        "📌 **Try these:** hello, how are you, name, joke, motivate, bye. 🎮"
    ],
    
    "joke": [
        "Why did the AI break up with the computer? 🖥️\nBecause it had too many bytes! 😂",
        "What do you call an AI that sings? 🎵\nA micro-phone! 🎤",
        "Why did the AI go to school? 🏫\nTo improve its neural networks! 🧠",
        "What's an AI's favorite game? 🎮\nHide and seek - it's great at pattern recognition!"
    ],
    
    "motivate": [
        "You're doing amazing! Keep learning! 💪",
        "Every expert was once a beginner. You're on the right track! 🌟",
        "Believe in yourself! You can achieve anything! 🚀",
        "Your journey to becoming an AI engineer starts now! 🎯"
    ],
    
    "thanks": [
        "You're welcome! 😊",
        "My pleasure! 🌟",
        "Anytime! Happy to help! 💬"
    ],
    "thank you": [
        "My pleasure! 😊",
        "You're most welcome! 🙌"
    ],
    
    "bye": [
        "Goodbye! Have a great day! 👋",
        "See you later! Take care! 🌟",
        "Bye bye! Come back soon! 😊"
    ],
    "exit": [
        "Goodbye! Have a great day! 👋",
        "Exiting now... See you soon! 😊"
    ],
    "quit": [
        "Goodbye! Have a great day! 👋",
        "Quitting... Come back anytime! 🌟"
    ],
    
    "love": [
        "Aww! ❤️ Love you too! You're amazing!",
        "Sending virtual hugs! 🤗",
        "You just made my day! 😊"
    ],
    
    "weather": [
        "I'm a rule-based bot, I can't check weather yet! ☁️",
        "Weather info is not available in this version. Sorry! 🌤️"
    ]
}

fallback_messages = [
    "I don't understand that yet. Type 'help' to see what I know. 🤔",
    "Hmm... that's new to me! Try 'help' to see my commands. 💡",
    "I'm still learning! Type 'help' to see what I can do. 📚",
    "Not sure about that! Here's what I know: hello, how are you, name, joke, motivate, help 🎯"
]

st.markdown("""
    <div class="main-header">
        <h1>🤖 RuleBot – Rule-Based AI Chatbot</h1>
        <p><em>Deterministic. Predictable. Safe.</em></p>
        <p>I respond to specific commands. No hallucinations, just pure logic.</p>
        <span class="badge">⚡ White Box AI | O(1) Lookup | 100% Explainable</span>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 📋 Project Details")
    st.info("""
        **Project:** Rule-Based AI Chatbot  
        **Batch:** 2026  
        **Organization:** DecodeLabs  
        **Type:** Foundation Phase
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Quick Actions")
    
    quick_commands = [
        ("👋 Hello", "hello"),
        ("😊 How are you", "how are you"),
        ("📛 My Name", "name"),
        ("😂 Joke", "joke"),
        ("💪 Motivate", "motivate"),
        ("🆘 Help", "help")
    ]
    
    for i in range(0, len(quick_commands), 2):
        col1, col2 = st.columns(2)
        with col1:
            label, cmd = quick_commands[i]
            if st.button(label, use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": cmd})
                st.rerun()
        if i + 1 < len(quick_commands):
            with col2:
                label, cmd = quick_commands[i + 1]
                if st.button(label, use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": cmd})
                    st.rerun()
    
    st.markdown("---")
    
    if "messages" in st.session_state and st.session_state.messages:
        st.markdown("### 📊 Session Stats")
        
        total = len(st.session_state.messages)
        user_msgs = sum(1 for m in st.session_state.messages if m['role'] == 'user')
        bot_msgs = total - user_msgs
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{total}</div>
                    <div class="stat-label">💬 Total</div>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{user_msgs}</div>
                    <div class="stat-label">👤 You</div>
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{bot_msgs}</div>
                    <div class="stat-label">🤖 Bot</div>
                </div>
            """, unsafe_allow_html=True)
        
        if 'start_time' in st.session_state:
            duration = datetime.now() - st.session_state.start_time
            minutes = int(duration.total_seconds() // 60)
            seconds = int(duration.total_seconds() % 60)
            st.caption(f"⏱️ Session: {minutes}m {seconds}s")
    else:
        st.info("💡 Start chatting to see stats!")
    
    st.markdown("---")
    
    st.markdown("### 🛠️ Controls")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = [
                {"role": "assistant", "content": "🧹 Chat cleared! Type 'help' to see what I can do."}
            ]
            st.session_state.start_time = datetime.now()
            st.rerun()
    
    with col2:
        if st.button("📥 Export Chat", use_container_width=True):
            if st.session_state.messages:
                chat_text = "🤖 Chat History\n" + "="*40 + "\n\n"
                for msg in st.session_state.messages:
                    chat_text += f"{msg['role'].upper()}: {msg['content']}\n\n"
                st.download_button(
                    label="📄 Download",
                    data=chat_text,
                    file_name=f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    key="download_btn"
                )
    
    st.markdown("---")
    
    st.markdown("### ℹ️ About RuleBot")
    st.markdown("""
        <div class="info-card">
            ✅ <b>Type:</b> Deterministic Rule-Based<br>
            ✅ <b>Lookup:</b> O(1) dictionary (hash map)<br>
            ✅ <b>Fallback:</b> Generic response for unknown inputs<br>
            ✅ <b>Exit:</b> `bye`, `exit`, `quit`<br>
            ✅ <b>White box:</b> Every response is hard-coded
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("🛠️ Project 1 – DecodeLabs Industrial Training Kit")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "🤖 Hi! I'm RuleBot. Ask me something or type 'help'."}
    ]
    st.session_state.start_time = datetime.now()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

def get_response(user_msg):
    clean_msg = user_msg.lower().strip()
    possible_replies = responses.get(clean_msg)
    
    if possible_replies:
        if isinstance(possible_replies, list):
            return random.choice(possible_replies)
        return possible_replies
    else:
        return random.choice(fallback_messages)

user_input = st.chat_input("💭 Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    bot_reply = get_response(user_input)
    
    if user_input.lower().strip() in ["bye", "exit", "quit"]:
        pass
    
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    
    if user_input.lower().strip() in ["bye", "exit", "quit"]:
        st.balloons()
    
    st.rerun()

st.markdown("---")
st.caption("💡 **Try these commands:** hello, how are you, name, joke, motivate, help | Type **bye** to exit")
