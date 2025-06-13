
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import random

# Configure the app
st.set_page_config(
    layout="wide",
    page_title="GameVerse - Discover & Play",
    page_icon="🎮",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .header {
        color: #FF4B4B;
        text-align: center;
        font-size: 3em;
        margin-bottom: 0.5em;
    }
    .subheader {
        color: #1F77B4;
        font-size: 1.5em;
        margin-top: 1em;
    }
    .game-card {
        padding: 15px;
        margin-bottom: 5px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    .game-card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    .feature-box {
        background-color: #f0f2f6;
        border-radius: 5px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 5px;
        padding: 0.5em 1em;
        margin: 0.5em 0;
    }
    .stSelectbox>div>div>select {
        padding: 8px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and preprocess game data"""
    try:
        # Replace with your actual data source
        df = pd.read_csv("game.csv")
        
        # Data cleaning
        df = df.dropna(subset=["Name", "Icon URL"])
        df["Average User Rating"] = pd.to_numeric(df["Average User Rating"], errors="coerce").fillna(0)
        df["User Rating Count"] = pd.to_numeric(df["User Rating Count"], errors="coerce").fillna(0)
        
        # Create combined features for recommendation
        df["features"] = (
            df["Genres"] + " " +
            df["Primary Genre"] + " " +
            df["Description"].fillna("") + " " +
            df["Developer"].fillna("") + " " +
            df["Average User Rating"].astype(str) + " " +
            df["User Rating Count"].astype(str)
        )
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return pd.DataFrame()

@st.cache_resource
def build_recommendation_model(df):
    """Build TF-IDF model and similarity matrix"""
    try:
        vectorizer = TfidfVectorizer(
            max_features=1000,
            stop_words="english",
            ngram_range=(1, 2)
        )
        
        tfidf_matrix = vectorizer.fit_transform(df["features"])
        cosine_sim = cosine_similarity(tfidf_matrix)
        return vectorizer, cosine_sim
        
    except Exception as e:
        st.error(f"Error building model: {str(e)}")
        return None, None

def display_game_card(game, col, show_similarity=False, similarity_score=None):
    """Display a game card in the UI"""
    with col:
        with st.container():
            st.markdown(f"<div class='game-card'>", unsafe_allow_html=True)
            
            # Display game image
            try:
                response = requests.get(game["Icon URL"])
                img = Image.open(BytesIO(response.content))
                st.image(img, width=150)
            except:
                st.image("https://via.placeholder.com/150", width=150)
            
            # Display game info
            st.markdown(f"<h4>{game['Name']}</h4>", unsafe_allow_html=True)
            
            # Rating stars
            rating = game['Average User Rating']
            stars = '⭐' * int(round(rating)) + '☆' * (5 - int(round(rating)))
            st.markdown(f"{stars} {rating:.1f}")
            
            # Reviews count
            st.caption(f"📊 {game['User Rating Count']:,} reviews")
        
            # Developer
            st.caption(f"👨‍💻 {game['Developer']}")
            
            # Genres
            st.caption(f"🎮 {game['Primary Genre']}")
            
            # Similarity score if showing recommendations
            if show_similarity and similarity_score:
                st.progress(similarity_score)
                st.caption(f"Match: {similarity_score:.0%}")
            
            st.markdown("</div>", unsafe_allow_html=True)

def show_featured_games(df):
    """Display featured games section"""
    st.markdown("<h2 class='header'>🎮 Featured Games</h2>", unsafe_allow_html=True)
    
    # Select featured games (top rated with many reviews)
    featured = df.sort_values(by=["Average User Rating", "User Rating Count"], ascending=False).head(10)
    
    # Display in 2 rows of 5 columns
    for i in range(0, len(featured), 5):
        cols = st.columns(5)
        for j in range(5):
            if i+j < len(featured):
                display_game_card(featured.iloc[i+j], cols[j])

def show_recommendation_section(df, vectorizer, cosine_sim):
    """Display game recommendation section"""
    st.markdown("<h2 class='header'>🔍 Find Your Next Favorite Game</h2>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🎯 Based on a Game You Like", "✨ Custom Preferences"])
    
    with tab1:
        st.markdown("<h3 class='subheader'>Find similar games</h3>", unsafe_allow_html=True)
        selected_game = st.selectbox(
            "Select a game you enjoy:",
            df["Name"].sort_values().unique(),
            index=random.randint(0, len(df)-1)
        )
        
        if st.button("Find Similar Games", key="similar_btn"):
            try:
                game_idx = df[df["Name"] == selected_game].index[0]
                sim_scores = list(enumerate(cosine_sim[game_idx]))
                sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]  # Top 5 similar
                
                st.markdown(f"<h4>Games similar to <span style='color:#FF4B4B'>{selected_game}</span>:</h4>", unsafe_allow_html=True)
                
                cols = st.columns(5)
                for i, (idx, score) in enumerate(sim_scores):
                    display_game_card(df.iloc[idx], cols[i], show_similarity=True, similarity_score=score)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    with tab2:
        st.markdown("<h3 class='subheader'>Tell us what you like</h3>", unsafe_allow_html=True)
        
        with st.form("preferences_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                genres = st.text_input("Favorite genres (comma separated)", "Adventure, Action")
                min_rating = st.slider("Minimum rating", 0.0, 5.0, 3.5, 0.1)
                
            with col2:
                keywords = st.text_input("Keywords you like in games", "explore, puzzle")
                min_reviews = st.number_input("Minimum reviews", min_value=0, value=100)
            
            submitted = st.form_submit_button("Find Games For Me")
            
            if submitted:
                try:
                    # Create query from user preferences
                    query = f"{genres} {keywords} {min_rating} {min_reviews}"
                    query_vector = vectorizer.transform([query])
                    
                    # Calculate similarity
                    sim_scores = cosine_similarity(query_vector, vectorizer.transform(df["features"]))
                    sim_scores = list(enumerate(sim_scores[0]))
                    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
                    
                    # Filter by rating and reviews
                    filtered = []
                    for idx, score in sim_scores:
                        game = df.iloc[idx]
                        if (game['Average User Rating'] >= min_rating and 
                            game['User Rating Count'] >= min_reviews):
                            filtered.append((idx, score))
                    
                    if not filtered:
                        st.warning("No games match all your criteria. Try relaxing your filters.")
                    else:
                        st.markdown("<h4>Recommended games for you:</h4>", unsafe_allow_html=True)
                        
                        # Show top 5 matches
                        cols = st.columns(5)
                        for i, (idx, score) in enumerate(filtered[:5]):
                            display_game_card(df.iloc[idx], cols[i], show_similarity=True, similarity_score=score)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

def show_game_browser(df):
    """Display game browser section"""
    st.markdown("<h2 class='header'>📚 Game Browser</h2>", unsafe_allow_html=True)
    
    # Filters
    with st.expander("🔍 Filter Games", expanded=False):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            genre_filter = st.selectbox(
                "Genre",
                ["All"] + sorted(df["Primary Genre"].unique().tolist())
            )
            
        with col2:
            rating_filter = st.slider(
                "Minimum Rating",
                0.0, 5.0, 3.0
            )
            
        with col3:
            reviews_filter = st.number_input(
                "Minimum Reviews",
                min_value=0,
                value=100
            )
    
    # Apply filters
    filtered_df = df.copy()
    if genre_filter != "All":
        filtered_df = filtered_df[filtered_df["Primary Genre"] == genre_filter]
    filtered_df = filtered_df[filtered_df["Average User Rating"] >= rating_filter]
    filtered_df = filtered_df[filtered_df["User Rating Count"] >= reviews_filter]
    
    # Sort options
    sort_option = st.selectbox(
        "Sort by",
        ["Rating (High to Low)", "Reviews (High to Low)", "Alphabetical"]
    )
    
    if sort_option == "Rating (High to Low)":
        filtered_df = filtered_df.sort_values("Average User Rating", ascending=False)
    elif sort_option == "Reviews (High to Low)":
        filtered_df = filtered_df.sort_values("User Rating Count", ascending=False)
    else:
        filtered_df = filtered_df.sort_values("Name")
    
    # Display games
    st.markdown(f"<h4>Showing {len(filtered_df)} games:</h4>", unsafe_allow_html=True)
    
    for i in range(0, 50, 5):
        cols = st.columns(5)
        for j in range(5):
            if i+j < 50:
                display_game_card(filtered_df.iloc[i+j], cols[j])

def main():
    """Main app function"""
    # Load data and build model
    df = load_data()
    if df.empty:
        st.error("Failed to load game data. Please check your data file.")
        return
    
    vectorizer, cosine_sim = build_recommendation_model(df)
    if vectorizer is None:
        st.error("Failed to build recommendation model.")
        return
    
    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/150x50.png?text=GameVerse", width=150)
        st.markdown("<h2>Discover New Games</h2>", unsafe_allow_html=True)
        st.markdown("""
        <p>Find your next favorite game based on:</p>
        <ul>
            <li>Games you already like</li>
            <li>Your preferred genres</li>
            <li>Game features you enjoy</li>
        </ul>
        <p>Information about developers </p>
        """, unsafe_allow_html=True)
        
       
        st.markdown("---")
        st.markdown("<small>contact</small>", unsafe_allow_html=True)
    
    # Main content
    show_featured_games(df)
    st.markdown("---")
    show_recommendation_section(df, vectorizer, cosine_sim)
    st.markdown("---")
    show_game_browser(df)

if __name__ == "__main__":
    main()