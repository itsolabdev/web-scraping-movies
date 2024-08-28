# Importing necessary libraries
import requests
from bs4 import BeautifulSoup


# Define the URL of the webpage to scrape
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


# Send an HTTP GET request to the specified URL
response = requests.get(URL)


# Extract the HTML content from the response object
website_html = response.text


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")


# Find all <h3> tags with the class "title" which contain movie titles
all_movies = soup.find_all(name="h3", class_="title")


# Extract the text from each <h3> tag and store it in a list
movie_titles = [movie.getText() for movie in all_movies]


# Reverse the list to get the movies in descending order (1 to 100 instead of 100 to 1)
movies = movie_titles[::-1]


# Open a file in write mode to save the movie titles
with open("movies.txt", mode="w") as file:
    # Iterate over the reversed list of movie titles
    for movie in movies:
        # Write each movie title to the file followed by a newline character
        file.write(f"{movie}\n")

# End of the script
