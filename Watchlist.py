import json
from Movie import Movie
from Wyjątki import *


class Watchlist():
    reversed = False
    
    def __init__ (self, movie_list = list()):
        self.movie_list = movie_list
    
    def addMovie(self, movie : Movie):
        self.movie_list.append(movie)
    def addMovieUser(self):
        title = input("Podaj tytuł ")
        director = input("Podaj reżysera ")
        year = int(input("Podaj rok produkcji "))
        genre = input("Podaj gatunek ")
        status = input("Obejrzany/Nieobejrzany ")
        review = input("Ocena 1-10 ")
        description = input("Opis ")
        for movie in self.movie_list:
            if title.lower().strip() in movie.title.lower().strip() and movie.year == year:
                raise MovieAlreadyExistError
        movie = Movie(title, director, year, genre, status,review, description=description)
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
            print("---")
            print(i)
        print("---")
            
    def editMovie(self, title : str, year : int):
        for movie in self.movie_list:
            try:
                if movie.title.lower().strip() == title.lower().strip() and movie.year == year:
                    new_title = input(f"Zmieniasz tytuł: {movie.title} na ") or movie.title
                    new_director =input(f"Zmieniasz dyrektor: {movie.director} na ") or movie.director 
                    new_year = (input(f"Zmienaisz rok produkcji: {movie.year} na ")) or movie.year
                    new_genre = input(f"Zmienaisz gatunek: {movie.genre} na ") or movie.genre
                    new_status = input(f"Zmieniasz status (obejrzany/nieobejrzany): {movie.status} na") or movie.status
                    new_review = input(f"Zmieniasz ocena: {movie.review} na ") or movie.review
                    new_description = input(f"Zmieniasz opis: {movie.description} na ") or movie.description
                    movie.title = new_title
                    movie.director = new_director
                    movie.year_of_production = new_year
                    movie.genre = new_genre
                    movie.status = new_status
                    movie.review = new_review
                    movie.description = new_description
                    print(movie)
                    return
            except ValueError:
                raise ValueError
            raise MovieNotFound


                            
    def save(self):
        toSave = [movie.to_dict() for movie in self.movie_list]
        with open("data.json","w",encoding="utf-8") as file:
            json.dump(toSave,file)
        print("Zapisano")
                
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
            Watchlist(toprint).allMovies()
                
    def filtr(self, attribute : str, value):
        try:
            filterd = list()
            if(type(value) != type(getattr(self.movie_list[0],attribute))):
                for movie in self.movie_list:
                    tmp = str(getattr(movie,attribute))
                    if (value in tmp):
                        filterd.append(movie)
                # value = int(value)
                # filterd = [movie for movie in self.movie_list if value == getattr(movie,attribute)]
            else:
                filterd = [movie for movie in self.movie_list if value.lower().strip() in getattr(movie,attribute).lower().strip()]
        except AttributeError:
            raise AttributeError
        if len(filterd) == 0:
            raise MovieNotFound
        return filterd
    
    def sort(self, attribute : str):
        try:
            #self.movie_list.sort([movie for movie in self.movie_list if type(getattr(x, attribute)) != type(None)])
            [movie for movie in self.movie_list if type(getattr(movie, attribute)) != type(None)].sort(key=lambda x:getattr(x, attribute), reverse=Watchlist.reversed)
            Watchlist.reversed = not Watchlist.reversed
        except AttributeError:
            raise AttributeError