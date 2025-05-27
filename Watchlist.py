import json
from Movie import Movie
from Wyjątki import MovieNotFound


class Watchlist():
    def __init__ (self, movie_list = list()):
        self.movie_list = movie_list
    
    def addMovie(self, movie : Movie):
        self.movie_list.append(movie)
    def addMovieUser(self):
        title = input("Podaj tytuł ")
        director = input("Podaj reżysera ")
        year = input("Podaj rok produkcji ")
        genre = input("Podaj gatunek ")
        movie = Movie(title, director, year, genre)
        self.addMovie(movie)
        print("Dodano film ",movie)

    def removeMovie(self, title :str):
        znaleziony = False
        for movie in self.movie_list:
            if movie.title == title:
                self.movie_list.remove(movie)
                znaleziony = True
        if  not znaleziony:
            raise MovieNotFound

        
    def allMovies(self):
        print("wypisuje filmy")
        for i in self.movie_list:
            print(i)
            
    def editMovie(self, oldMovie, newMovie):
        for i in range(len(self.movie_list)):
            if self.movie_list[i] == oldMovie:
                self.movie_list[i] = newMovie            
    def save(self):
        toSave = [movie.to_dict() for movie in self.movie_list]
        with open("data.json","w",encoding="utf-8") as file:
            json.dump(toSave,file)
                
    def load(self):
        with open("data.json", "r",encoding="utf-8") as file:
                loaded = json.load(file)
        self.movie_list = [Movie.from_dict(item) for item in loaded]


    def search(self, title : str):
        toprint = list()
        for i in self.movie_list:
            if title.lower().strip() in i.title.lower():
                toprint.append(i)
        if len(toprint)<=0:
            print("brak filmu o podanym tytule")
        else:
            print("znalezione filmy")
            for i in toprint:
                print(i)
