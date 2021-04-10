import requests
import json
import wordcloud
from wordcloud import WordCloud


x = requests.get('http://localhost:8983/solr/Search_Twitter/select?q=catch_all%3A%20testing&rows=1000')
data = x.json()
text = ""
for x in data["response"]["docs"]:
    for y in x["catch_all"]:
        text = text + y
        # print(text)

wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(text)
wordcloud.to_file("img/wordCloud.png")


# print(data["response"]["docs"][0]["catch_all"])