import streamlit as st
import pickle
import random

# ===============================
# Load trained ML model
# ===============================
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ===============================
# Keyword-based emotion lists
# ===============================
positive_words = [
    "happy", "good", "great", "excited", "joy",
    "confident", "awesome", "fantastic", "relaxed"
]

negative_words = [
    "sad", "stress", "stressed", "anxious", "depressed",
    "tired", "angry", "nervous", "worried", "bored", "lonely"
]

neutral_words = [
    "normal", "okay", "fine", "alright", "average"
]

emergency_words = [
    "suicid", "give up", "worthless", "end everything"
]

# ===============================
# Keyword emotion detection
# ===============================
def keyword_emotion(text):
    text = text.lower()

    if any(word in text for word in emergency_words):
        return "emergency"
    if any(word in text for word in negative_words):
        return "negative"
    if any(word in text for word in positive_words):
        return "positive"
    if any(word in text for word in neutral_words):
        return "neutral"
    return "ml"

# ===============================
# Responses
# ===============================
responses = {
    "positive": [
        "That's wonderful to hear! 🌟 Keep going!",
        "I'm really happy for you 😊",
        "Great! Stay confident and positive 💪",
        "Keep smiling, you're doing great 😄"
    ],
    "negative": [
        "I'm sorry you're feeling this way 💙",
        "That sounds tough. You're not alone 🤍",
        "I'm here for you. Take a deep breath 🌸"
    ],
    "neutral": [
        "I understand. Tell me more.",
        "I'm listening.",
        "Okay, let's talk about it."
    ]
}

# ===============================
# Relaxation tips
# ===============================
tips = [
    "Try deep breathing for 1 minute 🌬️",
    "Take a short walk and relax 🚶",
    "Listen to calming music 🎧",
    "Drink some water and rest 💧",
    "Stretch your body gently 🧘"
]

# ===============================
# Jokes (extended list)
# ===============================
jokes = [
    "Why don’t scientists trust atoms? Because they make up everything 😄",
    "Why was the computer tired? It needed a break 💻😂",
    "Why did the math book look sad? Too many problems 😅",
    "Why did the scarecrow win an award? He was outstanding in his field 😂",
    "Why can’t programmers tell jokes? Because they take everything literally 😆",
    "Why did the phone go to therapy? It lost its connection 📱😄"
]

# ===============================
# Streamlit UI
# ===============================
st.title("🧠 Mental Health Companion Chatbot")
st.write("A safe space to share your feelings 💬")

user_input = st.text_input("How are you feeling today?")

# Session states
if "ask_joke" not in st.session_state:
    st.session_state.ask_joke = False

if "show_joke" not in st.session_state:
    st.session_state.show_joke = False

if "feedback_done" not in st.session_state:
    st.session_state.feedback_done = False

# ===============================
# Main logic
# ===============================
if user_input:
    detected = keyword_emotion(user_input)

    # Emergency handling
    if detected == "emergency":
        st.error("⚠️ You matter. Please talk to someone you trust immediately.")
        st.info("📞 Mental Health Helpline (India): 9152987821")

    else:
        # ML fallback
        if detected == "ml":
            text_vec = vectorizer.transform([user_input])
            emotion = model.predict(text_vec)[0]
        else:
            emotion = detected

        # Positive
        if emotion == "positive":
            st.write("🤖 Chatbot:", random.choice(responses["positive"]))

        # Negative
        elif emotion == "negative":
            reply = random.choice(responses["negative"])
            reply += "\n\n💡 Tip: " + random.choice(tips)
            st.write("🤖 Chatbot:", reply)
            st.session_state.ask_joke = True

        # Neutral
        else:
            st.write("🤖 Chatbot:", random.choice(responses["neutral"]))

# ===============================
# Joke permission
# ===============================
if st.session_state.ask_joke:
    choice = st.radio(
        "Would you like to hear a joke to feel better? 😄",
        ["No", "Yes"]
    )

    if choice == "Yes":
        st.session_state.show_joke = True
        st.session_state.ask_joke = False
    else:
        st.session_state.ask_joke = False

# ===============================
# Show joke
# ===============================
if st.session_state.show_joke:
    st.success("😂 Joke: " + random.choice(jokes))
    st.session_state.show_joke = False

# ===============================
# Feedback Section
# ===============================
st.markdown("---")
st.subheader("📋 Feedback")

feedback = st.radio(
    "Did this chatbot help you?",
    ["Yes", "No"]
)

comment = st.text_area("Any suggestions or comments (optional):")

if st.button("Submit Feedback"):
    st.success("🙏 Thank you for your feedback!")
    st.session_state.feedback_done = True
