import webbrowser

class Movie():
    """fkjsakfdkhdf"""
    VALID_RATING = ["PG","R","kdl"]
    BOO =["a"]

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,cast,movie_genre,movie_rating,movie_director):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        self.cast_id=cast
        self.genre=movie_genre
        self.rating=movie_rating
        self.director=movie_director


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



