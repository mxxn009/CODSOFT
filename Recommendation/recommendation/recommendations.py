import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationSystem:
    def __init__(self, data_path):
        
        self.data = pd.read_csv(data_path)
        self.data.columns = self.data.columns.str.strip()  

        self.data['overview'] = self.data['overview'].fillna('')  
        
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.data['overview'])  
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

        self.data['title_lower'] = self.data['title'].str.lower()

    def get_recommendations(self, title):
        title_lower = title.lower()
        
        if title_lower not in self.data['title_lower'].values:
            return []
        
        idx = self.data.index[self.data['title_lower'] == title_lower][0]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:16]  

        recommended_indices = [i[0] for i in sim_scores]
        return self.data['title'].iloc[recommended_indices].tolist()
