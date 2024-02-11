from taskmanager import db


class User(db.Model):
    # User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    movies = db.relationship("Movie", backref="user_movies", 
                             cascade="all, delete", lazy=True)
    
    def __repr__(self):
        return "#{0} - username: {1} | password: {2}".format(
            self.username, self.password)
        

class Movie(db.Model):
    #Movie model
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100), nullable=False)
    movie_genre = db.Column(db.String(100), nullable=False) 
    movie_description = db.Column(db.String(100), nullable=False) 
    movie_year = db.Column(db.Integer, nullable=False)
    user = db.relationship("User", backref="user_movies", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    
    def __repr__(self):
        return "#{0} - User: {1} | Movie: {2}".format(
        self.id, self.movie_title, self.movie_genre, self.movie_description, self.movie_year)


