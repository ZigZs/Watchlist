import json
from Movie import Movie
from Wyjątki import *
from datetime import date

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
        comment = input("Komentarz ")
        description = input("Opis ")
        datewatched = input("Data obejrzenia ")
        for movie in self.movie_list:
            if title.lower().strip() in movie.title.lower().strip() and movie.year == year:
                raise MovieAlreadyExistError
        try:
            movie = Movie(title, director, year, genre, status,review, comment, description, datewatched)
        except WrongReviewError:
            raise WrongReviewError
        finally:
            self.addMovie(movie)
            print("Dodano film ", movie)


    def removeMovie(self, title :str, year : int):
        movie = self.findMovie(title,year)
        self.movie_list.remove(movie)
        print("Pomyślnie usunięto")

        
    def allMovies(self):
        print("wypisuje filmy")
        for i in self.movie_list:
            print("---")
            print(i)
        print("---")
            
    def editMovie(self, title : str, year : int):
        movie = self.findMovie(title,year)
        new_title = input(f"Zmieniasz tytuł: {movie.title} na ") or movie.title
        new_director =input(f"Zmieniasz dyrektor: {movie.director} na ") or movie.director 
        new_year = (input(f"Zmieniasz rok produkcji: {movie.year} na ")) or movie.year
        new_genre = input(f"Zmieniasz gatunek: {movie.genre} na ") or movie.genre
        new_status = input(f"Zmieniasz status (obejrzany/nieobejrzany): {movie.status} na") or movie.status
        new_review = input(f"Zmieniasz ocena: {movie.review} na ") or movie.review
        new_description = input(f"Zmieniasz opis: {movie.description} na ") or movie.description
        movie.title = new_title
        movie.director = new_director
        movie.year = new_year
        movie.genre = new_genre
        movie.status = new_status
        movie.review = new_review
        movie.description = new_description
        print(movie)


                            
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
        
    def findMovie(self, title : str, year : int):
        for movie in self.movie_list:
            if movie.title.lower().strip() == title.lower().strip() and movie.year == year:
                return movie
        raise MovieNotFound
    
    def watched(self, title : str, year : int):
        movie = self.findMovie(title,year)
        movie.status = "obejrzany"
        movie.datewatched = date.today()
        movie.review = int(input("podaj ocene (1-10) "))
        movie.comment = input("dodaj komentarz ")