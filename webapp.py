import random
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image

# Author: Albert Jozsa-Kiraly
# The code generates 3 random numbers which correspond to 3 random images, and
# gets the id, title, and author of each of the 3 images from the image_info
# dictionary. There is a route to the home page where these 3 images and their
# titles are displayed. Additionally, there are 3 other routes to each of the
# 3 images, so when the user clicks on an image title or the image itself,
# they are redirected to a new page displaying the full image with some
# additional information. When the home page is refreshed, 3 new random
# pictures and their titles are displayed.

# The provided image information
image_info = [
    {
        "id" : "34694102243_3370955cf9_z",
        "title" : "Eastern",
        "flickr_user" : "Sean Davis",
        "tags" : ["Los Angeles", "California", "building"]
    },
    {
        "id" : "37198655640_b64940bd52_z",
        "title" : "Spreetunnel",
        "flickr_user" : "Jens-Olaf Walter",
        "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
    },
    {
        "id" : "36909037971_884bd535b1_z",
        "title" : "East Side Gallery",
        "flickr_user" : "Pieter van der Velden",
        "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
    },
    {
        "id" : "36604481574_c9f5817172_z",
        "title" : "Lombardia, september 2017",
        "flickr_user" : "Mónica Pinheiro",
        "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
    },
    {
        "id" : "36885467710_124f3d1e5d_z",
        "title" : "Palazzo Madama",
        "flickr_user" : "Kevin Kimtis",
        "tags" : [ "Rome", "Italy", "window", "road", "building"]
    },
    {
        "id" : "37246779151_f26641d17f_z",
        "title" : "Rijksmuseum library",
        "flickr_user" : "John Keogh",
        "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
    },
    {
        "id" : "36523127054_763afc5ed0_z",
        "title" : "Canoeing in Amsterdam",
        "flickr_user" : "bdodane",
        "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
    },
    {
        "id" : "35889114281_85553fed76_z",
        "title" : "Quiet at dawn, Cabo San Lucas",
        "flickr_user" : "Erin Johnson",
        "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
    },
    {
        "id" : "34944112220_de5c2684e7_z",
        "title" : "View from our rental",
        "flickr_user" : "Doug Finney",
        "tags" : ["Mexico", "ocean", "beach", "palm"]
    },
    {
        "id" : "36140096743_df8ef41874_z",
        "title" : "Someday",
        "flickr_user" : "Thomas Hawk",
        "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
    }
]

# static in home.html will point to the images folder
app = Flask(__name__, static_folder = "images")
Bootstrap(app)

# These lists will store the title, author, and image name of each of the
# 3 randomly chosen image
titles = []
authors = []
image_names = []

# There are 10 images indexed 0 to 9 in image_info, so this is the
# maximum boundary when generating a random number
max_number = 9

# Generate 3 random numbers between 0 and 9 inclusive
for i in range(0, 3, 1):
	random_number = random.randint(0, max_number)
	
	# Get the title of the image at the generated index and add it to titles
	titles.append(image_info[random_number]["title"])

	# Get the author of the image and add it to the authors list
	authors.append(image_info[random_number]["flickr_user"])

	# Get the name of the image. We know that all images are jpg.
	image_name = image_info[random_number]["id"] + ".jpg"

	image_names.append(image_name)

# Route to the home page
@app.route('/')
def home():

	# Remove the contents of the titles, authors, and image_names lists.
	# This is needed, so when we refresh the home page, new random pictures
    # and their text will be displayed.
	del titles[:]
	del authors[:]
	del image_names[:]

	# Generate 3 new random numbers between 0 and 9 inclusive. Get the title,
    # author, and name of each image. Store these in the corresponding lists.
	for i in range(0, 3, 1):
		random_number = random.randint(0, max_number)

		titles.append(image_info[random_number]["title"])
		authors.append(image_info[random_number]["flickr_user"])

		image_name = image_info[random_number]["id"] + ".jpg"
		image_names.append(image_name)

	return render_template('home.html', image_names = image_names, titles = titles)

# Route to the first image
@app.route('/picture/' + image_names[0])
def picture1():

	image = Image.open("images/" + image_names[0])
	mode = image.mode
	format = image.format
	width = image.width
	height = image.height

	return render_template('pictures.html', title = titles[0], author = authors[0], name = image_names[0], mode = mode, format = format, width = width, height = height)

# Route to the second image
@app.route('/picture/' + image_names[1])
def picture2():

	image = Image.open("images/" + image_names[1])
	mode = image.mode
	format = image.format
	width = image.width
	height = image.height

	return render_template('pictures.html', title = titles[1], author = authors[1], name = image_names[1], mode = mode, format = format, width = width, height = height)

# Route to the third image
@app.route('/picture/' + image_names[2])
def picture3():

	image = Image.open("images/" + image_names[2])
	mode = image.mode
	format = image.format
	width = image.width
	height = image.height

	return render_template('pictures.html', title = titles[2], author = authors[2], name = image_names[2], mode = mode, format = format, width = width, height = height)
