import streamlit as st
import random

# Try importing AI, fallback to offline mode if failed
try:
    from transformers import pipeline
    ai_available = True
except ImportError:
    ai_available = False

# Load AI model if available
@st.cache_resource
def load_model():
    try:
        return pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
    except:
        return None

generator = load_model() if ai_available else None

# Tarot cards and meanings
cards = {
    "🌞 Sun": "Happiness and good fortune will come your way.",
    "🌙 Moon": "Mysteries await to be revealed in your life.",
    "⭐ Star": "A new hope will shine in your journey.",
    "🔥 Fire": "Passion and energy will rise, but handle emotions carefully.",
    "💧 Water": "Peace and calmness will surround you.",
    "🌳 Tree": "Growth and health will flourish in your life.",
    "💎 Gem": "A surprise in finances is coming your way.",
    "⚡ Lightning": "Sudden changes are ahead, be ready to face them."
}

# Offline templates for fallback
offline_templates = {
    "Mystic": [
        "In the quiet winds of fate, a secret path unfolds under starlit skies.",
        "Shadows whisper of change, where dreams awaken and destiny stirs.",
        "Through mist and moonlight, your future waits, veiled in mystery."
    ],
    "Funny": [
        "Brace yourself, life’s about to be as chaotic as a soap opera with no script!",
        "The stars say: buy coffee, you’ll need it for the upcoming plot twists.",
        "Destiny is laughing at you… in a good way, probably."
    ],
    "Serious": [
        "Your path shows change and opportunity. Take each step with clarity and resolve.",
        "The signs point toward growth—steady, patient, and certain.",
        "Life opens its next chapter; face it with wisdom and calm courage."
    ]
}

# Style instructions for AI
style_instructions = {
    "Mystic": "Write a short, poetic, and mysterious prophecy in 50 words or less.",
    "Funny": "Write a short, humorous tarot reading in 50 words or less, like a stand-up comedy line.",
    "Serious": "Write a short, wise, and meaningful tarot reading in 50 words or less, like life advice from a mentor."
}

# Post-processing to clean weird output
def clean_output(text):
    if "." in text:
        text = text.split(".")[0] + "."
    return text.strip()

# App Title
st.markdown("<h1 style='text-align: center;'>🔮 AI-Powered Tarot Reading (Hybrid)</h1>", unsafe_allow_html=True)
name = st.text_input("Enter your name:")
style = st.selectbox("Choose your reading style:", ["Mystic", "Funny", "Serious"])

# CSS for cards
st.markdown("""
    <style>
    .card {
        display: inline-block;
        margin: 10px;
        padding: 20px;
        font-size: 30px;
        border-radius: 12px;
        background: linear-gradient(145deg, #e6e6e6, #ffffff);
        box-shadow: 5px 5px 15px #c1c1c1, -5px -5px 15px #ffffff;
        animation: fadeIn 1s ease-in-out;
        transition: transform 0.3s;
    }
    .card:hover {
        transform: scale(1.1);
    }
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# Button to draw cards
if st.button("🎴 Draw Cards"):
    if not name:
        st.warning("Please enter your name for a personal reading!")
    else:
        chosen_cards = random.sample(list(cards.keys()), 3)
        
        # Show the cards
        st.subheader(f"{name}, your cards are:")
        for c in chosen_cards:
            st.markdown(f"<div class='card'>{c} → {cards[c]}</div>", unsafe_allow_html=True)
        
        reading = ""  # default empty

        # Try AI first
        if ai_available and generator:
            prompt = f"Based on these cards {', '.join(chosen_cards)}, {style_instructions[style]}"
            try:
                result = generator(
                    prompt,
                    max_length=80,
                    do_sample=True,
                    top_k=40,
                    top_p=0.9,
                    temperature=0.7,
                    clean_up_tokenization_spaces=True
                )
                reading = clean_output(result[0]['generated_text'])

                # Remove prompt repetition if AI repeats it
                if reading.lower().startswith(prompt.lower()):
                    reading = reading[len(prompt):].strip()

            except:
                reading = ""

        # Fallback if AI fails or output too short
        if not reading or len(reading.split()) < 4:
            reading = random.choice(offline_templates[style])
        
        # Show final reading
        st.success(f"{name}, {reading}")

else:
    st.info("Enter your name, choose a style, and click Draw Cards.")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit + Hugging Face GPT-Neo 125M")
