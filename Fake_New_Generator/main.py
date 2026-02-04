import random
import streamlit as st

# Page setup
st.set_page_config(page_title="Fake News Generator", layout="centered")

st.title("📰 Fake News Headline Generator")
st.write("Click the button below to generate a hilarious fake headline!")

# Data
subjects = [
    "Shahrukh Khan", "Virat Kohli", "A Mumbai cat", "A group of monkeys", "Doraemon", "Shinchan", "A chaiwala",
    "A software engineer", "A rickshaw driver", "A school teacher", "A college student", "A cricket fan",
    "A Bollywood director", "A street dog", "A shopkeeper", "A vegetable vendor", "A train conductor",
    "A local policeman", "A traffic warden", "A YouTuber", "A comedian", "A chef", "A tailor", "A painter",
    "A bus driver", "A librarian", "A professor", "A dancer", "A singer", "A drummer", "A DJ",
    "A magician", "A gamer", "A farmer", "A gardener", "A fruit seller", "A tourist", "A mountaineer",
    "A delivery boy", "A milkman", "A postman", "A fitness trainer", "A yoga teacher", "A news reporter",
    "A camera man", "A pilot", "A flight attendant", "A scientist", "A doctor", "A nurse", "A dentist",
    "A plumber", "An electrician", "A carpenter", "A mason", "A sweeper", "A dancer in Ganpati visarjan",
    "A metro commuter", "A local shop customer", "A mobile repair guy", "A rickshaw passenger", "A train announcer",
    "A school principal", "A headmaster", "A villager", "A fisherman", "A boatman", "A priest", "A temple visitor",
    "A tourist guide", "A park guard", "A traffic controller", "A bus conductor", "A child in playground",
    "A balloon seller", "A puppet show artist", "A street performer", "A kite flyer", "A cycle repairman",
    "A cobbler", "A beggar", "A musician at railway station", "A lassi seller", "A tea stall owner",
    "A pani puri wala", "A vada pav seller", "A dosa master", "A samosa lover", "A bhutta wala", "A kulfi vendor",
    "A street painter", "A college fresher", "A hostel warden", "A principal", "A gardener uncle",
    "A newspaper boy", "A watchman", "A gatekeeper", "A security guard", "A lady with groceries",
    "A bus traveler", "A railway ticket checker", "A chai lover"
]


actions = [
    "dances", "jumps", "runs", "sings", "laughs", "celebrates", "eats", "drinks", "claps",
    "whistles", "sleeps", "reads", "writes", "draws", "paints", "builds", "repairs", "teaches",
    "learns", "performs", "acts", "cooks", "drives", "cycles", "rides", "skates", "swims",
    "prays", "shouts", "cheers", "waves", "poses", "plays cricket", "plays football", "plays chess",
    "plays carrom", "plays drums", "plays guitar", "plays flute", "plays piano", "plants trees",
    "waters plants", "cleans", "mops", "washes dishes", "eats samosa", "eats vada pav", "eats jalebi",
    "drinks lassi", "drinks chai", "drinks coffee", "reads newspaper", "reads comic", "watches movie",
    "watches cricket", "watches football", "clicks selfie", "clicks photos", "films video",
    "uploads video", "posts selfie", "scrolls Instagram", "scrolls Facebook", "chats online",
    "sends email", "codes in Python", "debugs error", "solves math problem", "draws cartoon",
    "paints wall", "fixes bulb", "fixes fan", "repairs phone", "repairs cycle", "drives scooter",
    "drives rickshaw", "drives bus", "drives car", "flies kite", "makes puppet show",
    "performs magic", "sings bhajan", "sings rap", "sings lullaby", "dances in rain", "dances on street",
    "cheers for India", "shouts in train", "claps in theatre", "waves to crowd", "writes poetry",
    "writes exam", "writes homework", "writes love letter", "laughs loudly", "cracks jokes"
]


places_or_things = [
    "at Red Fort", "at India Gate", "in Mumbai local train", "inside Parliament", "at Ganga Ghat",
    "during IPL match", "at railway station", "at bus stop", "at metro station", "at tea stall",
    "at vada pav stall", "at pani puri cart", "at dosa counter", "in classroom", "in library",
    "in playground", "in park", "on stage", "at wedding", "at birthday party", "at Ganpati visarjan",
    "in Diwali mela", "in Holi ground", "at kite festival", "at Durga pandal", "at Navratri garba",
    "at temple", "at mosque", "at church", "at gurudwara", "at cinema hall", "in mall",
    "at shop", "at bazaar", "in street market", "at vegetable market", "in fish market",
    "in supermart", "in hostel", "in canteen", "in college", "in school", "at exam hall",
    "in tuition class", "at coaching center", "at cricket ground", "at football ground",
    "at tennis court", "in badminton hall", "in gym", "at yoga class", "at dance class",
    "in music school", "in art class", "in painting workshop", "at railway bridge", "on flyover",
    "on cycle track", "at jogging track", "at swimming pool", "at river bank", "at lake",
    "at beach", "at Marine Drive", "at Gateway of India", "at Bandra Worli Sea Link",
    "in Pune city", "in Delhi metro", "in Bangalore traffic", "at Mysore Palace", "at Charminar",
    "at Qutub Minar", "at Taj Mahal", "at Golden Temple", "at Kedarnath", "at Somnath",
    "at Meenakshi Temple", "at Hawa Mahal", "at Jantar Mantar", "in science fair",
    "in tech fest", "in cultural fest", "at music concert", "at food festival",
    "at book fair", "at art gallery", "at photography exhibition", "at zoo", "at circus",
    "in planetarium", "in museum", "at aquarium", "at hill station", "at railway bridge",
    "on rooftop", "on terrace", "in balcony", "in living room", "in kitchen", "in office"
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