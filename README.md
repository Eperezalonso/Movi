# 🎬 Movi - Movie Ranking & Discovery App

A comprehensive web application for discovering, rating, and getting personalized recommendations for movies and TV shows, powered by the TMDB API and AI-driven insights.

🚀 **Live Site**: [https://movi-xhh4.onrender.com/](https://movi-xhh4.onrender.com/)

## ✨ Features

### 🎯 Core Functionality
- **🔍 Smart Search**: Search for movies and TV shows by title with real-time results
- **📺 Mixed Media Discovery**: Browse popular movies and TV shows on the discover page
- **💾 Personal Library**: Save and manage your watched movies and TV shows
- **⭐ Rating System**: Rate movies on a 1-10 scale and track your ratings
- **📊 Detailed Information**: View comprehensive movie/show details including genres, ratings, and overviews

### 🤖 AI-Powered Features
- **🎯 Personalized Recommendations**: Get intelligent movie suggestions based on your rating history
- **💬 Interactive Chatbot**: Discuss movies and get recommendations through natural conversation
- **🔄 Dynamic Model Updates**: Recommendation system automatically retrains as you add new ratings

### 🎨 User Experience
- **👤 User Authentication**: Secure registration and login system
- **📱 Responsive Design**: Beautiful, modern UI that works on all devices
- **🎬 Video Integration**: Watch trailers and videos directly in the app
- **🔄 Real-time Updates**: Fresh recommendations and dynamic content loading

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask (Python)
- **Database**: SQLite with custom ORM
- **Authentication**: Werkzeug password hashing
- **Session Management**: Flask sessions with UUID tracking

### APIs & External Services
- **TMDB API**: Movie and TV show data, genres, videos
- **Google Generative AI (Gemini)**: Chatbot functionality
- **YouTube API**: Video content integration

### Machine Learning
- **scikit-learn**: Content-based recommendation system
- **pandas**: Data manipulation and analysis
- **TF-IDF Vectorization**: Movie content understanding
- **Joblib**: Model persistence and caching

### Frontend
- **HTML5**: Semantic markup with Jinja2 templating
- **CSS3**: Custom styling with modern design patterns
- **JavaScript**: Dynamic content loading and user interactions
- **Bootstrap**: Responsive grid system and components

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- TMDB API key (v3)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Movi.git
   cd Movi
   ```

2. **Run the setup script**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Configure environment variables**
   Create a `.env` file in the project root:
   ```
   TMDB_API_KEY=your_tmdb_v3_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Activate virtual environment and run**
   ```bash
   source venv/bin/activate
   python app.py
   ```

5. **Access the application**
   Open your browser and go to `http://localhost:5000`

### Manual Installation (Alternative)

If you prefer manual setup:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## 📖 Usage Guide

### Getting Started
1. **Register/Login**: Create a new account or log in to existing account
2. **Explore Content**: Browse the discover page for popular movies and TV shows
3. **Search**: Use the search bar to find specific titles
4. **Rate Movies**: Click on any movie/show to view details and add your rating

### Advanced Features
- **Personal Library**: View all your rated movies in "My Movies"
- **AI Recommendations**: Get personalized suggestions based on your taste
- **Chat with AI**: Ask the chatbot about movies, get recommendations, or discuss films
- **Refresh Recommendations**: Get new suggestions by refreshing the recommendation model

### Rating System
- Rate movies on a scale of 1-10
- Ratings are used to train the recommendation algorithm
- Your ratings are displayed alongside TMDB ratings
- The system learns from your preferences over time

## 🔧 Configuration

### Environment Variables
- `TMDB_API_KEY`: Your TMDB API v3 key (required)
- `GOOGLE_API_KEY`: Google API key for chatbot (optional)

### Database
- SQLite database (`movie_ranker.db`) is created automatically
- Contains user data, movie ratings, genres, and chat history
- No manual database setup required

## 🧪 Testing

Test the recommendation system:
```bash
python test_model.py
```

## 📁 Project Structure

```
Movi/
├── app.py                 # Main Flask application
├── database.py           # Database operations and schema
├── search.py             # TMDB API client and search functions
├── chatbot.py            # AI chatbot integration
├── model.py              # Recommendation system
├── setup.sh              # Automated setup script
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── search.html       # Search and discover page
│   ├── movie_detail.html # Movie/show detail page
│   ├── my_movies.html    # User's rated movies
│   ├── recommendations.html # AI recommendations
│   ├── chat.html         # Chatbot interface
│   ├── login.html        # Login page
│   └── register.html     # Registration page
├── static/               # Static assets
│   ├── style.css         # Custom styles
│   └── images/           # Images and icons
└── movie_ranker.db       # SQLite database (auto-generated)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is part of the SEO Tech Developer Program.

## 🐛 Troubleshooting

### Common Issues
- **"Invalid API key"**: Ensure you're using TMDB v3 API key, not v4 JWT token
- **"Module not found"**: Activate virtual environment and run `pip install -r requirements.txt`
- **Database errors**: Delete `movie_ranker.db` to reset (development only)
- **Setup script issues**: Make sure script is executable with `chmod +x setup.sh`

### Support
For issues and questions, please check the troubleshooting section above or create an issue in the repository.

---

*Built as part of the SEO Tech Developer Program*
