from api import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "author_id": self.author_id
        }


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    books = db.relationship('Book', backref='author')


    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "publisher_id": self.publisher_id
        }


class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publisher_name = db.Column(db.String)
    publisher_city = db.Column(db.String)
    authors = db.relationship('Author', backref='publisher')

    def to_dict(self):
        return {
            "id": self.id,
            "publisher_name": self.publisher_name,
            "publisher_city": self.publisher_city
        }


# class LinkBookAuthor(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    BookId = db.Column(db.Integer)
#    AuthorId = db.Column(db.Integer)

'''
class booksAuthor(db.Model):
    __tablename__ = "BooksAuthor"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    best_friend_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    user = db.relationship('users', foreign_keys='bestFriends.user_id')
    best_friend = db.relationship('users', foreign_keys='bestFriends.best_friend_id')

    def __init__(self, user_id, best_friend_id):
        self.user_id = user_id
        self.best_friend_id = best_friend_id

    def __repr__(self):
        return '{}-{}-{}-{}'.format(self.user_id, self.best_friend_id)
'''
