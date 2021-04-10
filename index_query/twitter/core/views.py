from django.shortcuts import render
import requests
import os
import io
from PIL import Image
from django.shortcuts import HttpResponse
import time 
# Create your views here.
#def get_html_content(tweet):
    #session = requests.Session()
   # query = tweet.replace(' ','%20')
   # html_content = requests.get(f'http://127.0.0.1:8983/solr/Search_Twitter/select?q=catch_all%3A%20{query}&rows=1000').json()
    #html_content = requests.get('https: // api.covid19api.com / countries').json
  #  return html_content

def home(request):

        start_time = time.time()
        tweet= request.GET.get('tweet')
        if(not tweet):
          tweet = "covid"
        search = str(tweet.replace(' ', '%20'))
        print('running home')
        query = f"http://127.0.0.1:8983/solr/Search_Twitter/select?q=catch_all%3A%20{search}&rows=1000"
        response = requests.get(query).json()


          #  'http://localhost:8983/solr/Search_Twitter/select?q=catch_all%3A%20vaccine%20frea123k&rows=1000').json
        #return render(request, 'Home.html', {'response':response1})
        #response1 = requests.get(
        url = "http://localhost:5000/query"

        payload = {'query': query}
        files = [

        ]
        headers = {}

        im = requests.request("POST", url, headers=headers, data=payload, files=files)

        image = Image.open(io.BytesIO(im.content))
        # image.show()
        image.save(os.path.abspath(os.getcwd()) + "\static\images\wordcloud.png")
        print("--- %s seconds ---" % (time.time() - start_time))
        return render(request, 'home1.html', {'response': response})
def query(request):

    if 'tweet' in request.GET:
        tweet = request.GET.get('tweet')
        print(tweet)
        query = tweet.replace(' ', '%20')
        print(query)

    #print(response)
        # return render(html_content, 'home1.html', {'html_content': html_content})







