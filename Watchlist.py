import json
from Movie import Movie
from Wyjątki import MovieNotFound


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
            
    def editMovie(self, title : str, year : int):
        for movie in self.movie_list:
            try:
                if movie.title == title and movie.year_of_production == year:
                    new_title = input(f"Zmieniasz tytuł: {movie.title} na ") or movie.title
                    new_director =input(f"Zmieniasz dyrektor: {movie.director} na ") or movie.director 
                    new_year = (input(f"Zmienaisz rok produkcji: {movie.year_of_production} na ")) or movie.year_of_production
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
                
    def filtrByGenre(self, genre : str):
        return [movie for movie in self.movie_list if movie.genre == genre]
    
    
    def sortByYear(self):
        self.movie_list.sort(key=lambda x: x.year_of_production, reverse=Watchlist.reversed)
        Watchlist.reversed = not Watchlist.reversed
