from flask import Flask, redirect, url_for, request, render_template
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_cors import CORS, cross_origin
import json
from summariser import *

app = Flask(__name__, static_folder="templates/static")
app.secret_key = "mysecretkey123"
blueprint = make_twitter_blueprint(
    api_key="grf2NRP19gooYGpi6BMxdnkib",
    api_secret="miUhmHZgqsLkxdgXAgocoYaBFbFVZxdEZFxE4FkeACUXuSoD6m",
)
app.register_blueprint(blueprint, url_prefix="/login")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/settings.json")
    # assert resp.ok
    # return redirect("file:///home/isha/PSOSM/SperrowProject/projectBackend/templates/index.html")
    # return redirect('/home/isha/PSOSM/SperrowProject/projectBackend/templates/index.html')
    # return home(resp.json()["screen_name"])
    # return render_template('index.html')
    return "You are @{screen_name} on Twitter".format(screen_name=resp.json()["screen_name"])

@app.route('/getSummaryData', methods=['GET','POST'])
def getSummaryData():
    if request.method == "POST":
        print(request)
        tweet = request.data.decode("utf-8")
        print(tweet, "tweet is here")
        # summary = "blahhhhhhhhhhhhhhhhhhhhhhhhhhh"
        summary = get_summary(tweet)
        print(summary)
        return json.dumps({"abcd": summary})

if __name__ == '__main__':
    app.run()