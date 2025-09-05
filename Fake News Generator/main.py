import random
import streamlit as st

# Page setup
st.set_page_config(page_title="Fake News Generator", layout="centered")

st.title("📰 Fake News Headline Generator")
st.write("Click the button below to generate a hilarious fake headline!")

# Data
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Shinchen",
    "A Mumbai cat",
    "A group of monkeys",
    "Doraemon",
    "Auto Rikshaw Driver from Delhi"
]

actions = [
    "launches",
    "jumps",
    "dances",
    "eats",
    "declares war",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai local train",
    "at plate of Samosa",
    "inside Parliament",
    "at Ganga Ghat",
    "during IPL match",
    "at India Gate"
]

# Button
if st.button("Generate Fake Headline"):
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    st.success(headline)













# import random 

# subjects = [
#     "Shahrukh Khan",
#     "Virat Kohli",
#     "Sinchen",
#     "A mumbai cat",
#     "A group of monkeys",
#     "Doraemon",
#     "Äuto Rikshaw Driver form Delhi"
     
# ]

# actions = [
#     "launches",
#     "jumps",
#     "dances ",
#     "eats",
#     "declares war",
#     "orders",
#     "celebrates"
# ]

# places_or_things = [
#     "at red fort",
#     "in Mumbai local train",
#     "at plate of Samosa",
#     "inside parliament",
#     "at Ganga ghat",
#     "during IPL match",
#     "at India gate"
# ]

# while True:
#     subject = random.choice(subjects)
#     action = random.choice(actions)
#     places_or_thing = random.choice(places_or_things)
    
#     headline = f"BREAKING NEWS: {subject} {action} {places_or_thing}"
#     print("\n" + headline)
    
#     user_inp = input("Do you want another headline? (yes/no)").strip().lower()
    
#     if user_inp == "no":
#         break
    
# print("\nThanks for using Fake News Headline Generator. Have a great day!")