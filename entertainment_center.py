import media, fresh_tomatoes, urllib, json

def fill_movie_object(name):
    # This is the API key needed to make API requests with 'themoviedb.org'.
    api_key = "81cd9f993126a0bbdab0729b26a0dffa"

    # First connection is to get the movie ID
    connection = urllib.urlopen("https://api.themoviedb.org/3/search/movie?"
                    + "api_key=" + api_key + "&query=" + name)
    output_string = connection.read()
    output_json = json.loads(output_string)
    connection.close()
    movie_id = output_json['results'][0]['id']

    # Using the movie id, we can retrieve the details of the movie:
    connection2 = urllib.urlopen("https://api.themoviedb.org/3/movie/"
                    + str(movie_id)
                    + "?api_key=" + api_key
                    + "&append_to_response=videos")
    output_string2 = connection2.read()
    output_json2 = json.loads(output_string2)
    connection2.close()

    # Get the movie parameters from the json:
    title = output_json2['original_title'].encode('utf-8')
    poster_image_url = ("https://image.tmdb.org/t/p/w640/"
                        + output_json2['poster_path'])
    trailer_youtube_url = ("https://www.youtube.com/watch?v="
                            + output_json2['videos']['results'][0]['key'])

    return media.Movie(title, poster_image_url, trailer_youtube_url)

# A sample of a few movies I like:
inception       = fill_movie_object("inception")
godfather       = fill_movie_object("godfather")
interstellar    = fill_movie_object("interstellar")
lotr            = fill_movie_object("return+of+the+king")
walle           = fill_movie_object("walle")
dark_knight     = fill_movie_object("the+dark+knight")

# Make a list of the movie objects to be passed to the fresh tomatoes function
movie_list = [godfather, lotr, inception, interstellar, walle, dark_knight]
# movie_list = [godfather, lotr, inception, interstellar, dark_knight]

# Invoke the function that opens the webpage with the list of movies as input
fresh_tomatoes.open_movies_page(movie_list)
