import os, random
from flask import (Flask, url_for, render_template, jsonify)
from settings import (IMAGES_FOLDER, IMAGES_URL, API_BASE)

### Init
app = Flask(__name__)

### Helpers

def get_image(waifu_name):
	return '{}/{}/{}'.format(IMAGES_URL, waifu_name, random.choice(os.listdir('{}/{}'.format(IMAGES_FOLDER, waifu_name))))

### Routes

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/lily')
def lily():
    image_url = get_image('lily')
    title = 'Cute Cute Cute'
    return render_template('picture.html', title = title, response = url_for('lily'), url = image_url)

@app.route('/sad')
def sad():
    image_url = get_image('sad')
    title = 'So It Goes'
    return render_template('picture.html', title = title, response = url_for('sad'), url = image_url)

@app.route(API_BASE + '/waifu/<waifu_name>')
def get_random_image(waifu_name):
    image_url = get_image(waifu_name)
    return jsonify({'url': image_url, 'waifu': waifu_name})
