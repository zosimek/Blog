class AuthorQueryset:
    def __init__(self, roundabout, authors):
        self.roundabout = roundabout
        self.authors = authors

class UltimateQueryset:
    def __init__(self, roundabout, thumbnail, latest, quote):
        self.roundabout = roundabout
        self.thumbnail = thumbnail
        self.latest = latest
        self.quote = quote

class ArtQueryset:
    def __init__(self, roundabout, thumbnail, latest, quote, art_categories):
        self.roundabout = roundabout
        self.thumbnail = thumbnail
        self.latest = latest
        self.quote = quote
        self.art_categories = art_categories

class LiteratureQueryset:
    def __init__(self, roundabout, books_volumes, thumbnail, latest, quote, literature_genre):
        self.roundabout = roundabout
        self.books_volumes = books_volumes
        self.thumbnail = thumbnail
        self.latest = latest
        self.quote = quote
        self.literature_genre = literature_genre