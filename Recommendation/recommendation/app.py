from flask import Flask, render_template, request
from recommendations import RecommendationSystem

app = Flask(__name__)
recommender = RecommendationSystem('C:/Users/Diwakar/Downloads/python/python programs/CodSoft/recommendation/data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        title = request.form['title']
        recommendations = recommender.get_recommendations(title)

    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
