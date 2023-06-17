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
    def __init__(self, roundabout, books_volumes, thumbnail, latest, quote, literature_genre, current_date, two_weeks_back):
        self.roundabout = roundabout
        self.books_volumes = books_volumes
        self.thumbnail = thumbnail
        self.latest = latest
        self.quote = quote
        self.literature_genre = literature_genre
        self.current_date = current_date
        self.two_weeks_back = two_weeks_back

class BookVolumeQueryset:
    def __init__(self, book_volume_info, book_volume_content):
        self.book_volume_info = book_volume_info
        self.book_volume_content = book_volume_content

class LastPoemBook:
    def __init__(self, post, last):
        self.post = post
        self.last = last

class Search:
    def __init__(self, sentence, art, literature, science, entertainment, title, content):
        self.sentence = sentence
        self.art = art
        self.literature = literature
        self.science = science
        self.entertainment = entertainment
        self.title = title
        self.content =content

class SearchResult:
    def __init__(self, art, book, volume, chapter, poem, science, post):
        self.art = art
        self.book = book
        self.volume = volume
        self.chapter = chapter
        self.poem = poem
        self.science = science
        self.Post = post