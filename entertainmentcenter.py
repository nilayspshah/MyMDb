import media
import fresh_tomatoes


class x():
    fs="dfh"

toystory=media.Movie("Toy Story","story of a boy and his toy","http://en.wikipedia.org/wiki/Toy_Story#mediaviewer/File:Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc","some")
avatar=media.Movie("Avatar","Blue Dudes go mad","http://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8","steven")
threeidiots=media.Movie("3 Idiots","RAncho and friends","http://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg","https://www.youtube.com/watch?v=C86pLho1hlE","been there,done that\nalsfhjaf")
#print(toystory.storyline)
#print(avatar.storyline)

#avatar.show_trailer()
#threeidiots.show_trailer()


movies = [toystory, avatar, threeidiots]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATING)
#print (media.Movie.VALID_RATING)
#print(x.fs)

#print(media.Movie.__module__)
