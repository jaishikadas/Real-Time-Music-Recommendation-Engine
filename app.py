import streamlit as st
from recommender import MusicRecommender

# ---------------------------
# Page Config & Styling
# ---------------------------
st.set_page_config(
    page_title="🎵 Music Recommender",
    layout="wide",
    page_icon="🎧"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background-color: #1e1e1e;
            color: white;
        }
        h1, h2, h3 {
            color: #FFDD00;
        }
        .song-card {
            background-color: #2a2a2a;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 10px;
        }
        .similarity {
            color: #00FFB3;
        }
        .stSelectbox label {
            font-size: 18px;
            font-weight: bold;
            color: white;
        }
        .css-18ni7ap {
            background-color: #2a2a2a;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Title & Description
# ---------------------------
st.title("🎧 Music Recommendation Engine")
st.markdown("#### *Discover songs similar to your favorite track!*")

# ---------------------------
# Load recommender
# ---------------------------
recommender = MusicRecommender("spotify_daily_charts_tracks.csv")
track_list = sorted(recommender.df['track_name'].unique())

# Song Selection
selected_track = st.selectbox("🎼 Choose a song", track_list)

# ---------------------------
# Recommendation Button
# ---------------------------
if st.button("🔍 Get Recommendations", use_container_width=True):
    results = recommender.get_recommendations(selected_track)

    if not results.empty:
        st.subheader("🎯 Recommended Songs")

        # Display recommendations in a nice layout
        for _, row in results.iterrows():
            with st.container():
                st.markdown(f"""
                    <div class="song-card">
                        <h4>🎵 {row['track_name']}</h4>
                        <p>👤 {row['artist_name']}</p>
                        <p class="similarity">Similarity Score: {row['similarity']:.2f}</p>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ No recommendations found.")
