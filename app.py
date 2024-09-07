from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    first_name = request.args.get('first_name')
    profile_pic_url = request.args.get('profile_pic_url')
    user_id = request.args.get('user_id')
    username = request.args.get('username')

    return render_template('index.html', first_name=first_name, profile_pic_url=profile_pic_url, user_id=user_id, username=username)

@app.route('/waifus')
def waifus():
    first_name = request.args.get('first_name')
    profile_pic_url = request.args.get('profile_pic_url')
    user_id = request.args.get('user_id')
    username = request.args.get('username')
    return render_template('waifus.html', first_name=first_name, profile_pic_url=profile_pic_url, user_id=user_id, username=username)

if __name__ == '__main__':
    app.run(debug=True)
