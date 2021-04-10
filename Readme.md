# Indexing and querying
To start the server, we need to perform the following 

## Starting the solr server 
1. cd into the directory : InformationRetrival\index_query\solr\solr-8.8.1\bin 
2. type in the command terminal: solr.cmd start 
3.  the server will be running on port 8983 on default 

**Dependencies**  <br>
we need the following to run solr 
- Java runtime environment of 1.8 and above

## Starting the bag of word server 
The bag of word feature needs its own server, to start it do the following 
1. cd into directory: InformationRetrival\index_query\bag of words server 
2. type python app.py to run server 

**Dependencies**  <br>
we need the following following dependencies to run it 
- python 3 and above 
- flask 
- wordcloud library 
- cv2 

## Starting the django frontend 
1. cd into the directory : InformationRetrival\index_query\twitter
2. to start the server, type :python manage.py runserver 
3. the frontend can be accessed through the url: localhost:8000/

**Dependencies**  <br>
we need the following to run the frontend UI  
- python 3 and above 
- django  
