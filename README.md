# Movie Trailer Website project.

created by Srikanth Sridhara on 23rd May 2017

## Files:

1. `entertainment_center.py`:

    Main file that creates the data for all movies and calls fresh_tomatoes.py.

2. `media.py`:

    This contains the Movie class that is used in entertainment_center.py.

3. `fresh_tomatoes.py`:

    This file converts a list of movie objects into a proper HTML page.

4. `fresh_tomatoes.html`:

    This is the html page that is generated dynamically by fresh_tomatoes.py

## Usage:
To run this project, follow these steps:
* Open a terminal.
* Go into the directory where these files are present.
* Run: `$ python entertainment_center.py`.
* The dynamically generated web page should open in a browser.
* The generated page will have movies with Title, Artwork and a Youtube trailer
 that is accessed by clicking on the artwork.

## Notes
* The method `fill_movie_object()` uses APIs from the website `www.tmdb.org`.
* First it queries tmdb for a movie. In the response, we get the movie ID.
* Next, using the movie id, we can query for the details of the movie where we
get the full title, video trailer link, poster image link, etc.
* Using these details, we create the movie object and populate the movie list.
