from flask import Flask, render_template, request, jsonify  # Add jsonify here
import random

app = Flask(__name__)

@app.route('/')
def index():
    first_name = request.args.get('first_name', 'User')
    profile_pic_url = request.args.get('profile_pic_url', None)
    return render_template('index.html', first_name=first_name, profile_pic_url=profile_pic_url)

@app.route('/guess', methods=['POST'])
def guess():
    number = random.randint(1, 10)
    guess = int(request.form['guess'])
    
    if guess == number:
        result = 'Congratulations! You guessed it right!'
    else:
        result = f'Sorry, the correct number was {number}. Try again!'
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
