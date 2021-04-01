from flask import Flask, render_template , request , jsonify, send_from_directory
import requests
import json
import wordcloud
from wordcloud import WordCloud
import cv2

app = Flask(__name__, static_url_path='')


@app.route('/query' , methods=['POST'])
def hello():
    query = request.form["query"]
    x = requests.get(query)
    data = x.json()
    text = ""
    for x in data["response"]["docs"]:
        for y in x["catch_all"]:
            text = text + y
            # print(text)

    wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(text)
    wordcloud.to_file("wordCloud.png")
    return send_from_directory("./","wordCloud.png")

if __name__ == '__main__':
    app.run()
