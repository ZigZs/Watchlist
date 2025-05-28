from Movie import Movie
from Watchlist import Watchlist
from Wyjątki import CommandNotFound, MovieNotFound

a = Movie("Test","Nolan",1999,"Akcji")
b = Movie("Test 2","Nolan",2001,"Akcji")
c = Movie("The Test","Nolan",2002,"Akcji")
d = Movie("Skibidi christmas", "Zigzs",42069,"Komedia")
filmweb = Watchlist()
# filmweb.addMovie(a)
# filmweb.addMovie(b)
# filmweb.addMovie(c)
# filmweb.addMovie(d)
# filmweb.addMovie(a)

# filmweb.allMovies()

# filmweb.removeMovie(a)

# filmweb.allMovies()

# filmweb.addMovie(Movie("StarWars","Lucas",1972,"sci-fy"))

# filmweb.allMovies()

#filmweb.save()
#filmweb.search("Test")

# filmweb.load()

#filmweb.allMovies()
legenda = "Lista komend:\n Dodaj film: ADD\n Usuń film: REMOVE\n Zmień Status filmu: \n Edytuj film: EDIT\n Dodaj ocene i komentarz: RATE\n Wyszukaj film: SEARCH\n Wyświetl wszystkie filmy: SHOWALL\n Zapisz do pliku: SAVE\n Wczytaj z pliku: LOAD\n Wyjdź z programu: EXIT\n"
print("Witam w watchliście\n"+legenda)
filmweb.load()
while True:
    userinput = input("Podaj komende ")
    try:
        match userinput.strip().upper():
            case "ADD":
                filmweb.addMovieUser()
                pass
            case "REMOVE":
                usuwanie = input("Podaj tytuł filmu do usunięcia ")
                filmweb.removeMovie(usuwanie)
                pass
            case "EDIT":
                tytul = input("Podaj tytuł fimlu, który chcesz edytować ")
                rok = int(input("Podaj date produkcji tego filmu "))
                filmweb.editMovie(tytul,rok)
                pass
            case "RATE":
                
                pass
            case "SEARCH":
                szukanie = input("Podaj tytuł szukanego filmu ")
                filmweb.search(szukanie)
                pass
            case "SHOWALL":
                filmweb.allMovies()
                pass
            case "SAVE":
                filmweb.save()
                pass
            # case "LOAD":
            #     filmweb.load()
            case "LEGEND":
                print(legenda)
                pass
            case "FILTR":
                warunek = input("Podaj gatunek dla którego chcesz posortować")
                tmp = Watchlist(filmweb.filtrByGenre(warunek))
                tmp.allMovies()
                pass
            case "SORT":
                filmweb.sortByYear()
                pass
            case "EXIT":
                print("Zamykam program")
                break
            case _:
                raise CommandNotFound
    except CommandNotFound:
        print("Nieznana komenda aby wyświetlić legende wpisz LEGEND")
    except MovieNotFound:
        print("Film nie znaleziony")
    except ValueError:
        print("Błędny rok produkcji, musi być liczbą naturalna")
