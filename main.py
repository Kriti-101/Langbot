from flask import Flask, render_template, url_for, request, jsonify, session
import openai
from openai import OpenAI
import time
import random

app = Flask(__name__, static_url_path='/static')

word_image_database = {
    'English': [
        ('apple', 'apple.jpeg'),
        ('table', 'table.jpeg'),
        ('bottle', 'bottle.jpeg'),
        ('watch', 'watch.jpeg'),
        ('bat', 'bat.jpeg')
    ],
    'Hindi': [
        ('सेब', 'apple.jpeg'),
        ('मेज़', 'table.jpeg'),
        ('बोतल', 'bottle.jpeg'),
        ('घड़ी', 'watch.jpeg'),
        ('बैट', 'bat.jpeg')
    ],
    'French': [
        ('pomme', 'apple.jpeg'),
        ('table', 'table.jpeg'),
        ('bouteille', 'bottle.jpeg'),
        ('montre', 'watch.jpeg'),
        ('chauve-souris', 'bat.jpeg')
    ],
    'German': [
        ('Apfel', 'apple.jpeg'),
        ('Tisch', 'table.jpeg'),
        ('Flasche', 'bottle.jpeg'),
        ('Uhr', 'watch.jpeg'),
        ('Fledermaus', 'bat.jpeg')
    ],
    'Kannada': [
        ('ಸೇಬು', 'apple.jpeg'),
        ('ಟೇಬಲ್', 'table.jpeg'),
        ('ಬಾಟಲ್', 'bottle.jpeg'),
        ('ಗಡಿಯಾರ', 'watch.jpeg'),
        ('ಪಟಗಳು', 'bat.jpeg')
    ]
}
# Get word and image list for a specific language (e.g., English)
english_words_images = word_image_database['English']


# Print the word and image pairs
for word, image in english_words_images:
    english_word_image_pairs = [{'word': word, 'image': image} for word, image in english_words_images]


@app.route("/")
def home():
    return render_template("index.html",url_for=url_for)  

@app.route("/conversation")
def conversation():
    return render_template("converstion.html") 

@app.route('/pictionary', methods=['GET', 'POST'])
def pictionary():
    language = request.args.get('language', 'English')     

    for i in word_image_database.get(language, []):
        if request.method == 'POST':
            guess_word = request.form['guess_word']
            if guess_word.lower() == word.lower():
                message = 'Correct!'   

            else:
                message = 'Incorrect! Try again.'
        
        else:
            message = ''
        
    return render_template('pictionary.html', language=language, word=word, image=image, message=message)

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/oral')
def oral():
    return render_template('oral.html')

def openai_endpoint():
    message = request.json.get('message')
    # Use OpenAI logic here to generate response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=50
    )
    return jsonify({'message': response['choices'][0]['text']})

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)