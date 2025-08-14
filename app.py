import streamlit as st
from recommender import MusicRecommender

st.set_page_config(page_title="🎵 Music Recommender", layout="centered")

st.title("🎧 Music Recommendation Engine")
st.markdown("Find songs similar to your favorite!")

# Load recommender
recommender = MusicRecommender("spotify_daily_charts_tracks.csv")
track_list = recommender.df['track_name'].unique()

selected_track = st.selectbox("Choose a song", track_list)

if st.button("Get Recommendations"):
    results = recommender.get_recommendations(selected_track)
    if not results.empty:
        st.success("Recommended Songs:")
        for _, row in results.iterrows():
            st.write(f"🎵 **{row['track_name']}** by *{row['artist_name']}* — Similarity: {row['similarity']:.2f}")
    else:
        st.warning("No recommendations found.")
