import webbrowser

# This is the main movie class
class Movie():
    # The constructor function
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # Helper function to open the trailer in a web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
