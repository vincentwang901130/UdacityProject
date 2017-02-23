import webbrowser


# movie class
class Movie():
        # class init func
	def __init__(self, movie_title,\
                movie_storyline,\
                poster_image, \
                trailer_youtube):
            # Movie title
            self.title = movie_title
            # Movie storyLine
            self.storyline = movie_storyline
            # Movie poster image url
            self.poster_image_url = poster_image
            # Movie trailer url
            self.trailer_youtube_url = trailer_youtube

	# call webbrowser.open func to show youtube trailer
        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
