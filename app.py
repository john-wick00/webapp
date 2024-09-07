from flask import Flask, render_template, request , jsonify
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb+srv://tmaid6012:loniko0908@cluster0.e3nhbm0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['WAIFU-BOT']

WAIFUS_PER_PAGE = 10


@app.route('/')
def index():
    first_name = request.args.get('first_name')
    profile_pic_url = request.args.get('profile_pic_url')
    user_id = request.args.get('user_id')
    username = request.args.get('username')

    return render_template('index.html', first_name=first_name, profile_pic_url=profile_pic_url, user_id=user_id, username=username)

@app.route('/waifus')
def waifus():
    user_id = request.args.get('user_id')

    # Initial load without pagination
    return render_template('waifus.html', user_id=user_id)

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
                waifus.append({
                    "img_url": waifu_data.get("img_url"),
                    "name": waifu_data.get("name"),
                    "anime": waifu_data.get("anime"),
                    "rarity": waifu_data.get("rarity"),
                    "rarity_sign": waifu_data.get("rarity_sign")
                })
        logging.info(f"Waifus fetched: {waifus}")
        return jsonify({"waifus": waifus})
    except ValueError:
        logging.error("Invalid user_id")
        return jsonify({"error": "Invalid user_id"}), 400



if __name__ == '__main__':
    app.run(debug=True)
