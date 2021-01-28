# Defining class "Painting"
class Painting:
    museum = "Louvre" # Can be used in entire class // Class Attribute
    def __init__(self, title, artist, year): # __init__ method
        self.title = title # Instance Attribute
        self.artist = artist # Instance Attribute
        self.year = year # Instance Attribute
    
    def get_sentance(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the {Painting.museum}.')

painting_museum = Painting(input(), input(), input())
painting_museum.get_sentance()