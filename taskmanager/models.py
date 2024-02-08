from taskmanager import db


class User(db.Model):
    # Schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"User('{self.username}', '{self.email}')"


class Movie(db.Model):
    # Schema for the Movie model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # Adjusted attribute name
    description_id = db.Column(db.Integer, db.ForeignKey('description.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    year_id = db.Column(db.Integer, db.ForeignKey('year.id'))
   
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"Movie('{self.title}')"

class Genre(db.Model):
    # Schema for the Genre model
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(50), unique=True, nullable=False)
    movies = db.relationship('Movie', backref='genre', lazy=True)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.genre_name


class Year(db.Model):
    # Schema for the Year model
    id = db.Column(db.Integer, primary_key=True)
    year_value = db.Column(db.Integer, unique=True, nullable=False)
    movies = db.relationship('Movie', backref='year', lazy=True)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return str(self.year_value)


class Description(db.Model):
    # Schema for the Description model
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    movies = db.relationship('Movie', backref='description', lazy=True)
    
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.content