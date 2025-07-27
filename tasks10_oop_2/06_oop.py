class Movie:
    all_movies = []

    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating
        Movie.all_movies.append(self)

    def is_hit(self):
        if self.rating > 8:
            return f"Movie: {self.title} directed by {self.director} with rating {self.rating} is a hit {True}"
        else:
            return f"Movie: {self.title} directed by {self.director} with rating {self.rating} is a hit {False}"


m1 = Movie("Avatar", "James Cameron", 9)
print(m1.is_hit())
m2 = Movie("Titanic", "James Cameron", 8)
print(m2.is_hit())
