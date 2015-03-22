import webbrowser

#########################################################################
#
# Larry Mello
# Full Stack Nanodegree - Udacity
# 3/22/2015
#
#########################################################################
class Movie:
    """This class defines what movie is and what it can do in the system"""

    def __init__(self, title, storyline, poster_url, trailer_url):
        # this is a special method that defines and initializes the instance variables
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        # this instance method opens the movie's trailer in a web browser
        webbrowser.open(self.trailer_youtube_url)
