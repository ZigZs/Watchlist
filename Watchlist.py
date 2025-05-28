import json
from Movie import Movie
from Wyjątki import *
from datetime import date
import matplotlib.pyplot as plt


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
        try:
            review = int(input("Ocena 1-10 "))
        except ValueError:
            review = None

        comment = input("Komentarz ")
        description = input("Opis ")
        datewatched = input("Data obejrzenia ")
        for movie in self.movie_list:
            if title.lower().strip() in movie.title.lower().strip() and movie.year == year:
                raise MovieAlreadyExistError
        try:
            movie = Movie(title, director, year, genre, status,review, comment, description, datewatched)
        except WrongReviewError:
            self.addMovie(movie)
            print("Dodano film ", movie)
            raise WrongReviewError
        except WrongStatusError:
            self.addMovie(movie)
            print("Dodano film ", movie)
            raise WrongStatusError

        self.addMovie(movie)
        print("Dodano film ", movie)


    def removeMovie(self):
        title = input("Podaj tytuł filmu do usunięcia ")
        year = int(input("Podaj rok producji "))
        movie = self.findMovie(title,year)
        self.movie_list.remove(movie)
        print("Pomyślnie usunięto")

        
    def allMovies(self):
        if not self.movie_list:
            raise EmptyListError
        print("wypisuje filmy")
        for i in self.movie_list:
            print("---")
            print(i)
        print("---")
            
    def editMovie(self):
        title = input("Podaj tytuł fimlu, który chcesz edytować ")
        year = int(input("Podaj date produkcji tego filmu "))
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


    def search(self):

        if not self.movie_list:
            raise EmptyListError
        title = input("Podaj tytuł szukanego filmu ")
        toprint = list()
        for i in self.movie_list:
            if title.lower().strip() in i.title.lower():
                toprint.append(i)
        if len(toprint)<=0:
            print("brak filmu o podanym tytule")
        else:
            print("znalezione filmy")
            Watchlist(toprint).allMovies()
                
    def filtr(self):

        if not self.movie_list:
            raise EmptyListError
        attribute = input("Podaj po jakim atrybucie chcesz filtorwać (title,director,year,genre) ")
        value = input("Podaj wartość atrybutu dla jakiego chcesz filtrować ")
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
    
    def sort(self):
        if not self.movie_list:
            raise EmptyListError
        attribute = input("Podaj po czym chcesz sortować (title,director,year,genre) ")

        try:
            #self.movie_list.sort([movie for movie in self.movie_list if type(getattr(x, attribute)) != type(None)])
            [movie for movie in self.movie_list if type(getattr(movie, attribute)) != type(None)].sort(key=lambda x:getattr(x, attribute), reverse=Watchlist.reversed)
            Watchlist.reversed = not Watchlist.reversed

        except AttributeError:
            raise AttributeError
        print("Posortowano")
        
    def findMovie(self, title : str, year : int):
        for movie in self.movie_list:
            if movie.title.lower().strip() == title.lower().strip() and movie.year == year:
                return movie
        raise MovieNotFound
    
    def watched(self):
        title = input("Podaj tytuł fimu, który obejrzałeś ")
        year = int(input("Podaj rok filmu,który obejrzałeś"))
        movie = self.findMovie(title,year)
        movie.status = "obejrzany"
        movie.datewatched = date.today()
        movie.review = int(input("podaj ocene (1-10) "))
        movie.comment = input("dodaj komentarz ")

    def stats(self):
        if not self.movie_list:
            raise EmptyListError
        genres = {}
        for movie in self.movie_list:
            genres[movie.genre] = genres.get(movie.genre, 0) + 1
        plt.figure(figsize=(8, 5))
        plt.bar(genres.keys(), genres.values())
        plt.title("Liczba filmów w poszczególnych gatunkach")
        plt.xlabel("Gatunek")
        plt.ylabel("Liczba filmów")
        plt.xticks(rotation=45, ha="right")
        max_y = max(genres.values())
        plt.yticks(range(0, max_y + 1))
        plt.tight_layout()
        plt.show()
        status_count = {"obejrzany": 0, "nieobejrzany": 0}

        for movie in self.movie_list:
                status_count[movie.status] += 1


        labels = list(status_count.keys())
        sizes = list(status_count.values())

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#ff9999'])
        plt.title("Rozkład statusu filmów")
        plt.axis('equal')
        plt.show()
        years_count = {}

        for movie in self.movie_list:
            years_count[movie.year] = years_count.get(movie.year, 0) + 1

        lata = sorted(years_count.keys())
        liczby = [years_count[year] for year in lata]

        plt.figure(figsize=(10, 5))
        plt.plot(lata, liczby, marker='o')
        plt.title("Liczba filmów według roku produkcji")
        plt.xlabel("Rok produkcji")
        plt.ylabel("Liczba filmów")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()