# 🎬 Movie Recommendation System

This repository contains a **Movie Recommendation System** built with Python, using **TF-IDF Vectorizer** and **Cosine Similarity**. The project provides movie recommendations based on text similarity, taking the user's input to suggest movies that closely match their preferences. A **Flask** web interface enables an interactive and user-friendly experience.

## 🚀 Features

- **Recommendation Engine**: Uses TF-IDF Vectorizer and Cosine Similarity to find and suggest similar movies based on a user's input.
- **Flask Web Interface**: Simple, responsive web interface to interact with the recommendation system.
- **Search for Recommendations**: Users can input a movie name, and the system returns a list of similar movies.

## 📁 Project Structure

- `app.py`: Main Flask application file to run the web interface.
- `movie_data.csv`: Contains movie data used for recommendations.
- `recommendation.py`: Contains the recommendation logic using TF-IDF and Cosine Similarity.
- `templates/`: Directory containing HTML templates for the web interface.
- `static/`: Folder for static files (e.g., CSS, images) used in the web interface.

## ⚙️ Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    python app.py
    ```

4. Open your web browser and go to `http://127.0.0.1:5000/` to use the Movie Recommendation System.

## 🛠️ Usage

1. Enter the name of a movie you like in the search bar.
2. Click "Get Recommendations."
3. The system will display a list of movies similar to your input.

## 📊 Technical Details

- **TF-IDF Vectorizer**: Converts movie descriptions into numerical vectors based on term frequency and inverse document frequency.
- **Cosine Similarity**: Measures similarity between movie vectors to identify the closest matches to the user's input.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📝 Acknowledgments

Thanks to [TMDb](https://www.themoviedb.org/) for providing the movie dataset.
