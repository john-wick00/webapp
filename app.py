from flask import Flask, render_template, request , jsonify
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['WAIFU-BOT']

WAIFUS_PER_PAGE = 10


@app.route('/')
def home():
    first_name = request.args.get('first_name')
    profile_pic_url = request.args.get('profile_pic_url')
    user_id = request.args.get('user_id')
    username = request.args.get('username')

    logging.info(f"Rendering home page with user_id: {user_id}, first_name: {first_name}, username: {username}, profile_pic_url: {profile_pic_url}")
    
    return render_template('index.html', first_name=first_name, profile_pic_url=profile_pic_url, user_id=user_id, username=username)

@app.route('/waifus')
def waifus():
    first_name = request.args.get('first_name')
    profile_pic_url = request.args.get('profile_pic_url')
    user_id = request.args.get('user_id')
    username = request.args.get('username')

    # Pass these parameters to the template as well
    return render_template('waifus.html', first_name=first_name, profile_pic_url=profile_pic_url, user_id=user_id, username=username)


@app.route('/load_waifus')
def load_waifus():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "No user ID provided"}), 400

    try:
        logging.info(f"Fetching waifus for user_id: {user_id}")
        user_data = db.Collection.find_one({"user_id": int(user_id)})
        if not user_data or "images" not in user_data:
            logging.info("No waifus found for this user.")
            return jsonify({"waifus": []})

        waifus = []
        for waifu in user_data.get("images", []):
            waifu_data = db.Characters.find_one({"id": waifu["image_id"]})
            if waifu_data:
                waifus.append({"img_url": waifu_data.get("img_url")})
        logging.info(f"Waifus fetched: {waifus}")
        return jsonify({"waifus": waifus})
    except ValueError:
        logging.error("Invalid user_id")
        return jsonify({"error": "Invalid user_id"}), 400




if __name__ == '__main__':
    app.run(debug=True)
