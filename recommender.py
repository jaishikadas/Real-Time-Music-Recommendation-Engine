import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

class MusicRecommender:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.feature_cols = ['danceability', 'energy', 'acousticness', 'liveness',
                             'valence', 'tempo', 'speechiness']
        self.prepare_data()

    def prepare_data(self):
        self.df.dropna(subset=self.feature_cols, inplace=True)
        scaler = MinMaxScaler()
        self.df_scaled = self.df.copy()
        self.df_scaled[self.feature_cols] = scaler.fit_transform(self.df[self.feature_cols])

    def get_recommendations(self, track_name, top_n=5):
        if track_name not in self.df_scaled['track_name'].values:
            return []

        selected = self.df_scaled[self.df_scaled['track_name'] == track_name]
        similarity = cosine_similarity(selected[self.feature_cols], self.df_scaled[self.feature_cols])
        self.df_scaled['similarity'] = similarity[0]
        results = self.df_scaled.sort_values(by='similarity', ascending=False).head(top_n + 1)

        return results[results['track_name'] != track_name][['track_name', 'artist_name', 'similarity']]
