from models.connection import MongoAccess
from models.publication import Publication
from datetime import datetime
# from connection import MongoAccess
# from publication import Publication

# # Connect to MongoDB using your custom class
# db = MongoAccess.connect()
# # Access the "publis" collection
# collection = db['publis']

class Data :
    
    def filter_authors(author):
        client = MongoAccess.connect()
        collection = client['publis']  
        publications = collection.find({'authors': author})
        
        results = []
        for publi in publications:
            publication = Publication(publi)
            results.append(publication)
        
        MongoAccess.disconnect()
        return results


    def filter_years(start_year):
        client = MongoAccess.connect()
        collection = client.publis 

        current_year = datetime.now().year
        query = {'year': {'$gte': start_year, '$lte': current_year}} 
        publications = collection.find(query)

        results = []
        for publi in publications:
            publication = Publication(publi)
            results.append(publication)

        MongoAccess.disconnect()
        return results
    

    def filter_titles(title):
        client = MongoAccess.connect()
        collection = client.publis  
        publications = collection.find({'title': title})

        results = []
        for publi in publications:
            publication = Publication(publi)
            results.append(publication)

        MongoAccess.disconnect()
        return results
    


    def get_publication_count():
        client = MongoAccess.connect()  # Connect to the MongoDB instance
        collection = client.publis
        count = collection.count_documents({})

        MongoAccess.disconnect()  
        return count


    def add_pub (type, title, year, publisher, series, booktitle, url, authors, isbn):
        client = MongoAccess.connect()
        pub = {
            'type': type,
            'title': title,
            'year': year,
            'publisher': publisher,
            'series': series,
            'booktitle': booktitle,
            'url': url,
            'authors': authors,
            'isbn': isbn,
        }
        client.publis.insert_one(pub)
        MongoAccess.disconnect()
        
