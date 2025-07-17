import sqlite3

class MovieRankerDB:
    def __init__(self, db_path='movie_ranker.db'):
        self.init_db()

    def db_connect(self):
        conn = sqlite3.connect('movie_ranker.db')
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        conn = self.db_connect()
        cursor = conn.cursor()

        # Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
        """)

        # Movies table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            backdrop_path TEXT,
            poster_path TEXT,
            original_language TEXT,
            title TEXT NOT NULL,
            overview TEXT,
            release_date TEXT,
            vote_average REAL,
            vote_count INTEGER,
            popularity REAL
        )
        """)

        # User_Movies table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_movies (
            user_id INTEGER,
            movie_id INTEGER,
            rating INTEGER NOT NULL,
            PRIMARY KEY (user_id, movie_id),
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (movie_id) REFERENCES movies(id)
        )
        """)

        # Genre_Map table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS genre_map (
            movie_id INTEGER,
            genre_id INTEGER,
            PRIMARY KEY (movie_id, genre_id),
            FOREIGN KEY (movie_id) REFERENCES movies(id)
        )
        """)

        conn.commit()
        conn.close()

    def add_movie(self, movie_data):
        conn = self.db_connect()
        cursor = conn.cursor()
        self.add_genres(movie_data['id'], movie_data.get('genre_ids', []))
        cursor.execute("""
        INSERT OR IGNORE INTO movies (id, backdrop_path, poster_path, original_language, title, overview, release_date, vote_average, vote_count, popularity)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            movie_data['id'], movie_data.get('backdrop_path'),
            movie_data.get('poster_path'), movie_data['original_language'], movie_data['title'],
            movie_data.get('overview'), movie_data.get('release_date'), movie_data.get('vote_average', 0),
            movie_data.get('vote_count', 0), movie_data.get('popularity', 0)
        ))
        conn.commit()
        conn.close()

    def add_user_movies_by_id(self, user_id, movie_id, rating):
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT OR REPLACE INTO user_movies (user_id, movie_id, rating)
        VALUES (?, ?, ?)
        """, (user_id, movie_id, rating))
        conn.commit()
        conn.close()

    def add_user_movies_by_name(self, user_name, movie_id, rating):
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT OR REPLACE INTO user_movies (user_id, movie_id, rating)
        VALUES ((SELECT id FROM users WHERE name = ?), ?, ?)
        """, (user_name, movie_id, rating))
        conn.commit()
        conn.close()

    def add_genre(self, movie_id, genre_id):
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT OR IGNORE INTO genre_map (movie_id, genre_id)
        VALUES (?, ?)
        """, (movie_id, genre_id))
        conn.commit()
        conn.close()

    def add_genres(self, movie_id, genre_ids):
        conn = self.db_connect()
        cursor = conn.cursor()
        for genre_id in genre_ids:
            self.add_genre(movie_id, genre_id)
        conn.close()

    def get_user_movies(self, user_name, sort_by="rating", ascending=False):
        conn = self.db_connect()
        cursor = conn.cursor()
        sort_fields = {
            "rating": "um.rating",
            "popularity": "m.popularity",
            "title": "m.title",
            "vote_average": "m.vote_average",
            "vote_count": "m.vote_count",
            "release_date": "m.release_date"
        }

        sort_column = sort_fields.get(sort_by)
        if not sort_column:
            raise ValueError(f"Invalid sort field '{sort_by}'. Must be one of: {', '.join(valid_sort_fields)}")

        order = "ASC" if ascending else "DESC"
        cursor.execute(f"""
            SELECT m.*, um.rating
            FROM users u
            JOIN user_movies um ON u.id = um.user_id
            JOIN movies m ON um.movie_id = m.id
            WHERE u.name = ?
            ORDER BY {sort_column} {order}
        """, (user_name,))
        results = cursor.fetchall()
        conn.close()
        return results
        
    def get_movie_data(self, movie_id):
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
        result = cursor.fetchone()
        conn.close()
        return result

    def rm_user_by_name(self, user_name):
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE name = ?", (user_name,))
        conn.commit()
        conn.close()

    def rm_user_by_id(self, user_id):
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()

    def rm_user_movie_by_name(self, user_name, movie_id):
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM user_movies
        WHERE user_id = (SELECT id FROM users WHERE name = ?) AND movie_id = ?
        """, (user_name, movie_id))
        conn.commit()
        conn.close()

    def rm_user_movie_by_id(self, user_id, movie_id):
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM user_movies
        WHERE user_id = ? AND movie_id = ?
        """, (user_id, movie_id))
        conn.commit()
        conn.close()

    def rm_movie(self, movie_id):
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
        conn.commit()
        conn.close()

    # Debug methods
    def print_all_users(self):
        '''Prints all users to the console.'''
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print("All Users:")
        for user in users:
            print(f"User ID: {user['id']}, Name: {user['name']}")
        conn.close()

    def print_all_movies(self):
        '''Prints all movies to the console.'''
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies")
        movies = cursor.fetchall()
        print("All Movies:")
        for movie in movies:
            print(f"Movie ID: {movie['id']}, Title: {movie['title']}, Rating: {movie['vote_average']}")
        conn.close()

    def print_all_user_movies(self, user_name):
        '''Prints all movies for a specific user to the console.'''
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.*, um.rating
            FROM users u
            JOIN user_movies um ON u.id = um.user_id
            JOIN movies m ON um.movie_id = m.id
            WHERE u.name = ?
        """, (user_name,))
        user_movies = cursor.fetchall()
        print(f"Movies for user '{user_name}':")
        for movie in user_movies:
            print(f"Movie ID: {movie['id']}, Title: {movie['title']}, Rating: {movie['rating']}")
        conn.close()

    def clear_database(self):
        '''Clears all data from the database.'''
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user_movies")
        cursor.execute("DELETE FROM genre_map")
        cursor.execute("DELETE FROM movies")
        cursor.execute("DELETE FROM users")
        conn.commit()
        conn.close()
