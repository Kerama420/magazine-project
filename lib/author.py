from lib.article import Article  # this goes at the top to avoid circular import later

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        # Returns a list of all Article objects for this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Returns a list of unique Magazine instances the author has written for
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        # Creates a new Article instance and associates it with this author
        return Article(self, magazine, title)

    def topic_areas(self):
        # Returns a unique list of the magazine categories the author has contributed to
        if not self.articles():
            return None
        return list({magazine.category for magazine in self.magazines()})
