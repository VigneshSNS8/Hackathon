import streamlit as st
import random
from datetime import datetime

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
        ]
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
        ]
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
        ]
    }
}

def generate_daily_tip(category):
    """Generate a daily tip based on the goal category."""
    if category in GOAL_CATEGORIES:
        return random.choice(GOAL_CATEGORIES[category]["tips"])
    else:
        return random.choice([
            "Break your goal into small tasks and tackle one today.",
            "Reflect on your progress and celebrate small wins!",
            "Stay consistent with one action toward your goal today."
        ])

def generate_motivational_quote(category):
    """Generate a motivational quote based on the goal category."""
    if category in GOAL_CATEGORIES:
        return random.choice(GOAL_CATEGORIES[category]["quote_templates"])
    else:
        return random.choice([
            "Keep pushing forward! 🚀 Your goals are worth it!",
            "Every effort counts! 🌟 Stay focused on your dream!",
            "You’ve got this! 💪 Take one step closer today!"
        ])

def main():
    """Main function to run the Streamlit app."""
    st.title("Personal Goal Motivator 🎯")
    st.write("Select a goal category and describe your goal to get a daily tip and motivational quote!")

    # User input section
    category = st.selectbox(
        "Choose your goal category:",
        ["fitness", "career", "personal", "custom"],
        index=0
    )

    if category == "custom":
        custom_category = st.text_input("Enter your custom goal category:", key="custom_category")
        category = custom_category.lower().strip() if custom_category else "personal"
    
    goal = st.text_input("Describe your specific goal:", key="goal")

    if st.button("Generate Motivation"):
        if not goal:
            st.error("Please enter a specific goal.")
        else:
            # Display current date
            today = datetime.now().strftime("%B %d, %Y")
            st.markdown(f"### Daily Motivation for {today}")
            st.write(f"**Goal Category**: {category.capitalize()}")
            st.write(f"**Your Goal**: {goal}")

            # Generate and display daily tip
            daily_tip = generate_daily_tip(category)
            st.markdown("#### Daily Progress Tip")
            st.write(daily_tip)

            # Generate and display motivational quote
            motivational_quote = generate_motivational_quote(category)
            st.markdown("#### Motivational Quote")
            st.markdown(f"**{motivational_quote}**")

if __name__ == "__main__":
    main()