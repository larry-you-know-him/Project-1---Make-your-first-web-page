import fresh_tomatoes
import media
import turtle

# movie 1 definition (URLs for movie posters are from the web and trailers are from You Tube)
jaws = media.Movie("Jaws",
                   "A great-white shark terrorizes a summer beach community",
                   "https://upload.wikimedia.org/wikipedia/en/e/eb/JAWS_Movie_poster.jpg",
                   "https://www.youtube.com/watch?v=U1fu_sA7XhE")

# movie 2 definition (URLs for movie posters are from the web and trailers are from You Tube)
seven = media.Movie("Se7en",
                   "Two cops track down a killer that uses the seven deadly sins",
                   "http://www.impawards.com/1995/posters/seven_ver1.jpg",
                   "https://www.youtube.com/watch?v=J4YV2_TcCoE")

# movie 3 definition (URLs for movie posters are from the web and trailers are from You Tube)
whiplash = media.Movie("Whiplash",
                   "A jazz drummer studies under an abusive teacher to become great",
                   "http://ia.media-imdb.com/images/M/MV5BMTU4OTQ3MDUyMV5BMl5BanBnXkFtZTgwOTA2MjU0MjE@._V1_SX640_SY720_.jpg",
                   "https://www.youtube.com/watch?v=7d_jQycdQGo")

# movie 4 definition (URLs for movie posters are from the web and trailers are from You Tube)
shawshank_redemption = media.Movie("Shawshank Redemption",
                   "A accountant wrongly convicted of murder liberates himself and those around him",
                   "http://loftcinema.com/files/2014/11/the-shawshank-redemption-movie-poster-1994-1020260139.jpg",
                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

# movie 5 definition (URLs for movie posters are from the web and trailers are from You Tube)
la_confidential = media.Movie("L.A. Confidential",
                   "1950s corrupt L.A. police move in on Mickey Cohen's drug empire",
                   "http://thedomesticpeach.com/wp-content/uploads/2014/06/LA-Con.jpg",
                   "https://www.youtube.com/watch?v=4r8hM6u8h3A")

# movie 6 definition (URLs for movie posters are from the web and trailers are from You Tube)
about_a_boy = media.Movie("About A Boy",
                   "How a boy and an adult man help each other to grow up",
                   "http://www.impawards.com/2002/posters/about_a_boy_xlg.jpg",
                   "https://www.youtube.com/watch?v=-apwoGTpi7E")

# put these movies into a list
movies = [jaws,seven,whiplash,shawshank_redemption,la_confidential,about_a_boy]

# pass the list of movies into another Python module that generates a web page based on those movies
fresh_tomatoes.open_movies_page(movies)

