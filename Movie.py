class Movie:
    def __init__(self, title, director, year_of_production, genre, status = "nieobejrzany", review = None, comment = "",description = ""):
        self.title = title
        self.director = director
        self._year_of_production = year_of_production
        self.genre = genre
        self.status = status
        self.review = review
        self.comment = comment
        self.description = description
        
    @property
    def year(self):
        return self._year_of_production
    
    @year.setter
    def year_of_production(self, new_year):
        if not isinstance(new_year, int):
            try:
                new_year = int(new_year)
            except ValueError:
                raise ValueError
                
        if new_year < 0:
            raise ValueError
        self._year_of_production = new_year
        
    def __str__(self):
        return (
            f"Tytuł:{self.title}|"
            f"Reżyser:{self.director}|"
            f"Rok:{int(self.year_of_production)}|"
            f"Gatunek:{self.genre}|"
            f"Status:{self.status}|"
            f"Ocena:{self.review}|"
            f"Komentarz:{self.comment}|"
            f"Opis:{self.description}"
        )
        
    def to_dict(self):
        return {
            "title":self.title,
            "director":self.director,
            "year_of_production":self.year_of_production,
            "genre":self.genre,
            "status":self.status,
            "review":self.review,
            "description":self.description
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            title = data.get("title"),
            director = data.get("director"),
            year_of_production = data.get("year_of_production"),
            genre = data.get("genre"),
            status = data.get("status"),
            review = data.get("review"),
            description = data.get("description")
        )