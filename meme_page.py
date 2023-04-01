#!/bin/python

import json
from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.get(url, timeout=100).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)


app.run(host="0.0.0.0", port=5001)