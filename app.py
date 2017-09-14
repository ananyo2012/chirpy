from flask import Flask, request, jsonify
from flask_cors import CORS
import twitter

app = Flask(__name__)
CORS(app)
app.config.from_object('config')
api = twitter.Api(consumer_key=app.config["CONSUMER_KEY"],
					  consumer_secret=app.config["CONSUMER_SECRET"],
					  access_token_key=app.config["ACCESS_TOKEN_KEY"],
					  access_token_secret=app.config["ACCESS_TOKEN_SECRET"])

@app.route('/')
def index():
	return "Home Page"

@app.route('/timeline')
def timeline():
	username = str(request.args.get('username'))
	count = 25
	if(request.args.get('count')):
		valid_count = int(request.args.get('count'))
		if(valid_count > 0 and valid_count <= 200):
			count = valid_count
	statuses = api.GetUserTimeline(screen_name=username, count=count)
	json_statuses = [status._json for status in statuses]
	return jsonify(json_statuses)
