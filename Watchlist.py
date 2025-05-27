import json
from Movie import Movie

class Watchlist():
    def __init__ (self, movie_list = list()):
        self.movie_list = movie_list
    
    def addMovie(self, movie):
        self.movie_list.append(movie)
        
    def removeMovie(self, movie):
        self.movie_list.remove(movie)
        
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
            if title.lower() in i.title.lower():
                toprint.append(i)
        if len(toprint)<=0:
            print("brak filmu")
        else:
            print("znalezione filmy")
            for i in toprint:
                print(i)
