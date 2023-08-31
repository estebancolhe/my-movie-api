# permiten separar la logica de los routers
from models.movie import Movie as MovieModel
from schemas.movie import Movie
class MovieService():

    def __init__(self, db) -> None: # 'db' es paa que cuando se llame a ese servicio se le envie 
        # una session a la BD
        self.db = db # con esto ya la BD es accesible a otros metodos de este servicio

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def get_movies_by_category(self, category):
        result = self. db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    def create_movie(self, movie: Movie): # movie: Movie, 'Movie' es el objeto tipo schema que se 
        # le asigna a la variable 'movie'
        new_movie = MovieModel(**movie.dict()) # al modelo de 'MovieModel' se le pasa la variable 'movie' para que 
        # la convierta en diccionario y cree la pelicula
        self.db.add(new_movie) # guardamos la pelicula
        self.db.commit() # se realiza actualización
        return
    
    def update_movie(self, id: int, data: Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return
    
    def delete_movie(self, id:int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
        return