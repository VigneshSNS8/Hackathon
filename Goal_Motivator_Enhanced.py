import streamlit as st
import random
from datetime import datetime
import uuid

# Define goal categories and associated data
GOAL_CATEGORIES = {
    "fitness": {
        "tips": [
            "Aim for 30 minutes of moderate exercise today, like a brisk walk or yoga session.",
            "Stay hydrated! Drink at least 8 glasses of water throughout the day.",
            "Try a new healthy recipe to keep your meals exciting and nutritious.",
            "Schedule a rest day to let your body recover and prevent burnout.",
            "Track your steps today and aim for 10,000 to stay active!"
        ],
        "quote_templates": [
            "Push your limits today! 💪 Your stronger self is waiting!",
            "Every step counts! 🏃 Keep moving toward your fitness goals!",
            "Sweat now, shine later! 🔥 Stay committed to your journey!",
            "Your body is capable of amazing things! 🥗 Fuel it right!",
            "Consistency is key! 🏋️‍♀️ Keep showing up for yourself!"
        ],
        "image_url": "https://source.unsplash.com/featured/?fitness,motivation"
    },
    "career": {
        "tips": [
            "Spend 30 minutes learning a new skill relevant to your job today.",
            "Network with a colleague or professional in your field this week.",
            "Set a small, achievable work goal for today to build momentum.",
            "Review your resume or LinkedIn profile and update one section.",
            "Read an industry article to stay updated on trends."
        ],
        "quote_templates": [
            "Your career is a journey! 🚀 Take one bold step today!",
            "Success is built daily! 📈 Keep grinding toward your dreams!",
            "Your skills are your superpower! 💼 Shine bright in your work!",
            "Embrace challenges! 🌟 They lead to career growth!",
            "Stay focused and rise! 🧑‍💼 Your goals are within reach!"
        ],
        "image_url": "https://source.unsplash.com/featured/?career,professional"
    },
    "personal": {
        "tips": [
            "Practice 10 minutes of mindfulness or meditation today.",
            "Write down three things you’re grateful for this morning.",
            "Try a new hobby or activity to spark creativity this week.",
            "Connect with a friend or family member for a meaningful chat.",
            "Set aside time to declutter one area of your space today."
        ],
        "quote_templates": [
            "Grow a little every day! 🌱 Your journey is beautiful!",
            "Embrace who you are! 😊 Your uniqueness is your strength!",
            "Small steps lead to big changes! 🌈 Keep going!",
            "You are enough! 💖 Shine in your own way!",
            "Live with purpose! 🌟 Today is your day to thrive!"
        ],
        "image_url": "https://source.unsplash.com/featured/?personal,growth"
    }
}

def generate_daily_tip(category):
    """Generate a daily tip based on the goal category."""
    if category in GOAL_CATEGORIES:
        return random.choice(GOAL_CATEGORIES[category]["tips"])
    return random.choice([
        "Break your goal into small tasks and tackle one today.",
        "Reflect on your progress and celebrate small wins!",
        "Stay consistent with one action toward your goal today."
    ])

def generate_motivational_quote(category):
    """Generate a motivational quote based on the goal category."""
    if category in GOAL_CATEGORIES:
        return random.choice(GOAL_CATEGORIES[category]["quote_templates"])
    return random.choice([
        "Keep pushing forward! 🚀 Your goals are worth it!",
        "Every effort counts! 🌟 Stay focused on your dream!",
        "You’ve got this! 💪 Take one step closer today!"
    ])

def get_category_image(category):
    """Get the image URL for the category."""
    return GOAL_CATEGORIES.get(category, {"image_url": "https://source.unsplash.com/featured/?motivation"})["image_url"]

def main():
    """Main function to run the enhanced Streamlit app."""
    # Custom CSS for better styling
    st.markdown("""
        <style>
        .main { background-color: #f0f2f6; }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .quote-box {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin: 10px 0;
        }
        .tip-box {
            background-color: #e6f3ff;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
        }
        .sidebar .sidebar-content {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 15px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state for goal history
    if "goal_history" not in st.session_state:
        st.session_state.goal_history = []
    if "progress" not in st.session_state:
        st.session_state.progress = 0

    st.title("🚀 Ultimate Goal Motivator")
    st.markdown("Your personalized hub for daily inspiration and progress tracking!")

    # Sidebar for inputs
    with st.sidebar:
        st.header("Set Your Goal")
        category = st.selectbox(
            "Choose your goal category:",
            ["fitness", "career", "personal", "custom"],
            index=0,
            help="Select a category or create a custom one."
        )

        if category == "custom":
            custom_category = st.text_input("Enter your custom goal category:", key="custom_category")
            category = custom_category.lower().strip() if custom_category else "personal"
        
        goal = st.textInput("Describe your specific goal:", key="goal")
        
        if st.button("Generate Motivation"):
            if not goal:
                st.error("Please enter a specific goal.")
            else:
                # Update progress and save goal to history
                st.session_state.progress = min(st.session_state.progress + 10, 100)
                st.session_state.goal_history.append({
                    "id": str(uuid.uuid4()),
                    "date": datetime.now().strftime("%B %d, %Y"),
                    "category": category.capitalize(),
                    "goal": goal
                })

    # Main content
    if st.session_state.goal_history and st.session_state.goal_history[-1]["goal"] == goal:
        today = datetime.now().strftime("%B %d, %Y")
        st.markdown(f"### Your Motivation for {today}")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write(f"**Goal Category**: {category.capitalize()}")
            st.write(f"**Your Goal**: {goal}")
            
            # Generate and display daily tip
            daily_tip = generate_daily_tip(category)
            st.markdown("#### Daily Progress Tip")
            st.markdown(f"<div class='tip-box'>{daily_tip}</div>", unsafe_allow_html=True)
            
            # Generate and display motivational quote
            motivational_quote = generate_motivational_quote(category)
            st.markdown("#### Motivational Quote")
            st.markdown(f"<div class='quote-box'><strong>{motivational_quote}</strong></div>", unsafe_allow_html=True)
        
        with col2:
            # Display category-specific image
            image_url = get_category_image(category)
            st.image(image_url, caption="Inspiration Visual", use_column_width=True)
        
        # Progress bar
        st.markdown("#### Your Progress")
        st.progress(st.session_state.progress)
        st.write(f"You're {st.session_state.progress}% closer to your goal!")

        # Confetti animation
        st.balloons()

        # Display goal history
        with st.expander("View Goal History"):
            for entry in reversed(st.session_state.goal_history):
                st.write(f"**{entry['date']}** - {entry['category']}: {entry['goal']}")

if __name__ == "__main__":
    main()