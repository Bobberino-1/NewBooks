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

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name
        }

# class LinkBookAuthor(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    BookId = db.Column(db.Integer)
#    AuthorId = db.Column(db.Integer)
