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