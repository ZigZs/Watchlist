from Movie import Movie
from Watchlist import Watchlist

a = Movie("Test","Nolan",1999,"Akcji")
b = Movie("Test 2","Nolan",2001,"Akcji")
c = Movie("The Test","Nolan",2002,"Akcji")
d = Movie("Skibidi christmas", "Zigzs",42069,"Komedia")
filmweb = Watchlist()
filmweb.addMovie(a)
filmweb.addMovie(b)
filmweb.addMovie(c)
filmweb.addMovie(d)
# filmweb.addMovie(a)

# filmweb.allMovies()

# filmweb.removeMovie(a)

# filmweb.allMovies()

# filmweb.addMovie(Movie("StarWars","Lucas",1972,"sci-fy"))

# filmweb.allMovies()

filmweb.save()
filmweb.search("Test")

filmweb.load()

filmweb.allMovies()