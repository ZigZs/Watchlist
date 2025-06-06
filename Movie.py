from Wyjątki import *


class Movie:
    def __init__(self, title, director, year, genre, status = "nieobejrzany", review = None, comment = "",description = "",datewatched =""):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.status = status
        self.review = review
        self.comment = comment
        self.description = description
        self.datewatched = datewatched
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, new_year):
        if not isinstance(new_year, int):
            try:
                new_year = int(new_year)
            except ValueError:
                raise ValueError
                
        if new_year < 0:
            raise ValueError
        self._year = new_year
    @property
    def review(self):
        return self._review
    @review.setter
    def review(self, new_review : int):
        if new_review is None:
            self._review = None
            return
        if not 0<=new_review<=10:
            raise WrongReviewError
        self._review = new_review
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if not new_status:
            self._status = "nieobejrzany"
            return
        new_status = new_status.lower()
        if new_status not in ["nieobejrzany", "obejrzany"]:
            self._status = "nieobejrzany"

        self._status = new_status

    @property
    def comment(self):
        return self._comment
    @comment.setter
    def comment(self, new_comment : str):
        if len(new_comment) >200:
            raise CommentTooLong
        self._comment = new_comment
    def __str__(self):
        return (
            f"Tytuł: {self.title} | "
            f"Reżyser: {self.director} | "
            f"Rok: {self.year} | "
            f"Gatunek: {self.genre} | "
            f"Status: {self.status} | "
            f"Ocena: {self.review} | "
            f"Komentarz: {self.comment} | "
            f"Opis: {self.description} | "
            f"Data obejrzenia: {self.datewatched}"
        )
        
    def to_dict(self):
        return {
            "title": self.title,
            "director": self.director,
            "year": self.year,
            "genre": self.genre,
            "status": self.status,
            "review": self.review,
            "comment": self.comment,
            "description": self.description,
            "datewatched": self.datewatched
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            title=data.get("title"),
            director=data.get("director"),
            year=data.get("year"),
            genre=data.get("genre"),
            status=data.get("status"),
            review=data.get("review"),
            comment=data.get("comment", ""),
            description=data.get("description", ""),
            datewatched=data.get("datewatched", "")
        )