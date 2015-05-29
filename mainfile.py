from __future__ import print_function
import glob
import os
import guessit
import imdb
from imdb import Movie
import urllib2
import sys
import re
import media
import urlparse
import fresh_tomatoes


###########
#### imdb working here, the print statement prints out the whole summary of the movie
#### We need to just give this section a string with the proper movie name
ia=imdb.IMDb()
##def getSummary(s):
##    ia=imdb.IMDb()
##    r_set=ia.search_movie(s,results=1)
##    for x in r_set:
##        ia.update(x)
##        info=[]
##        info=x.summary()
##        print (info)
##
#### imdb working here ENDS here
###############
##
####### This section prints out all 
##

#movie_title,movie_storyline,poster_image,trailer_youtube,cast,movie_genre,movie_rating,movie_director
def make_movie_object(s):
    acess=imdb.IMDb()
    r_set=ia.search_movie(s,results=1)
    movie = acess.get_movie(r_set[0].movieID)
    caststring=""
    genrestring=""
    directorstring=""
    titlestring=""
    coverstring=""
    plotstring=""
    plotstring=movie['plot'][0]
    titlestring=movie['title']+ "(" +str(movie['year'])+")"
    coverstring=str(movie['cover url'])
    for x in movie['genre']:
        genrestring+=x+" "
    print(genrestring)
    caststring+=str(movie['cast'][0]) +", "+str(movie['cast'][1])+ ", "+str(movie['cast'][2])
    #caststring=str(movie['cast'][0])
    print (caststring)
    for y in movie['director']:
        directorstring+=str(y) + " "
    print(directorstring)
    print(titlestring)
    print (coverstring)
    x=media.Movie( titlestring,plotstring,coverstring,"https://www.youtube.com/watch?v=d1_JBMrrYw8",caststring,genrestring,str(movie['rating']),directorstring)
    all_movies.append(x)





from guessit import guess_file_info
os.chdir("C:\Movies")
raw_movies=[]
for file in glob.glob("*.*"):
    raw_movies.append(file)


movie_names=[]
movie_names_set=set()
for x in raw_movies:
    path = x
    guess = guessit.guess_movie_info(path, info=['filename'])
    name=guess.get('title')
    if name not in movie_names_set:
        movie_names.append(name)
        movie_names_set.add(name)



all_movies=[]
for n in movie_names:
    print (n)
    make_movie_object(n)

    



fresh_tomatoes.open_movies_page(all_movies)


##s="3 idiots"
##all_movies=[]
##acess=imdb.IMDb()
##r_set=ia.search_movie(s,results=1)
##movie = acess.get_movie(r_set[0].movieID)
##caststring=""
##genrestring=""
##directorstring=""
##titlestring=""
##coverstring=""
##titlestring=movie['title']+ "(" +str(movie['year'])+")"
##coverstring=str(movie['cover url'])
##for x in movie['genre']:
##    genrestring+=x+" "
##print(genrestring)
##    #caststring+=str(movie['cast'][0]) +", "+str(movie['cast'][1])+ ", "+str(movie['cast'][1])
##caststring=str(movie['cast'][0])
##print (caststring)
##for y in movie['director']:
##    directorstring+=str(y) + " "
##print(directorstring)
##print(titlestring)
##print (coverstring)
##x=media.Movie( titlestring, "abcd",coverstring,"https://www.youtube.com/watch?v=d1_JBMrrYw8",caststring,genrestring,str(movie['rating']),directorstring)
##all_movies.append(x)




##print ("title: %s year: %s" % (movie['title'], movie['year']))
##print ("Cover url: %s" % movie['cover url'])
##print ("Cover url: %s" % movie['plot'][0])
##print(movie['director'][0])
##print (movie['rating'])
##s=""
##for x in movie['genre']:
##    s+=x+" "
##print (s)

    




##print (getSummary('3 idiots'))




##ia=imdb.IMDb()
###movieObject=[]
####m=Movie.Movie()
##
###print (type(m))
###print (m['information'])
####ia.update(m, ['quotes', 'goofs'])
####print (m)
##
##r_set=ia.search_movie('3 idiots',results=1)
####print (type(r_set))
####print(r_set)
####movie_id=r_set[0]
####ia.update(movie_id)
####print (r_set)
####print (type(movie_id.summary()))
##for x in r_set:
##    ia.update(x)
##    info=[]
##    info=x.summary()
##    print (info)
##
