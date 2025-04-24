from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

# Test your classes
a1 = Author("Jane Doe")
m1 = Magazine("Tech Talk", "Technology")
article1 = Article(a1, m1, "The Future of AI")

print(article1.title)       # Should print: The Future of AI
print(article1.author.name) # Should print: Jane Doe
print(article1.magazine.name) # Should print: Tech Talk
