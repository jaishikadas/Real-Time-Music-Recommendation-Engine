#  Music Recommendation Engine

Welcome to the **Music Recommendation Engine**, a sleek and intuitive app that helps you discover songs similar to your favorites!  
Check out the live demo here:

<img width="1365" height="635" alt="image" src="https://github.com/user-attachments/assets/f7e124c9-fac0-4369-886e-1b6790fb79c7" />


👉 **Live App:** [Try it now!](https://real-time-music-recommendation-engine-vrtr9pliztjzpg3ahygjs4.streamlit.app/)

---

##  Overview

This project harnesses music track data to generate recommendations based on similarity. Built with Streamlit, it's designed for both data exploration and user-friendly browsing.
The app suggests songs similar to your favorite track using **audio features** like danceability, energy, acousticness, tempo, etc.  
It uses **cosine similarity** to find and rank the most relevant songs from a Spotify daily charts dataset.

---

## 📌 Features
- 🎼 Select any song from the dataset and get **top 5 similar tracks**.
- 🎯 Uses **cosine similarity** for accurate recommendations.
- 🎨 Elegant, dark-themed user interface.
- ⚡ Fast and interactive, powered by **Streamlit**.
- 📊 Based on **Spotify Daily Charts** dataset.

---

## 🛠️ Tech Stack
- **Python 3**
- **Streamlit** – Web app framework
- **Pandas** – Data handling
- **Scikit-learn** – Cosine similarity & MinMax scaling
- **Spotify Dataset** – Song metadata & features

---

## 📂 Project Structure
app.py ──> recommender.py ──> requirements.txt ──> spotify_daily_charts_tracks.csv ──> seed_track.csv 

---


## ⚙️ Installation & Running Locally
1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/music-recommender.git
   cd music-recommender

2. Install dependencies
pip install -r requirements.txt

3.Run the app
streamlit run app.py
Open the local URL shown in the terminal (e.g., http://localhost:8501).


---

## Dataset
Source: Spotify Daily Charts dataset Features used for similarity:
danceability
energy
acousticness
liveness
valence
tempo
speechiness

---

##💡 Future Improvements
🎨 Add album cover art via Spotify API.
🔍 Search bar for quick song lookup.
📈 Add more datasets for broader recommendations.
🎛 Customizable number of recommendations.



