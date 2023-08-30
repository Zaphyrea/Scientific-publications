
# class Publication:
#     def __init__(self, publis):
#         self.id = publis['_id']
#         self.type = publis['type']
#         self.titre = publis['title']
#         self.pages = publis['pages']
#         self.date = publis['year']
#         self.titre_livre = publis['booktitle']
#         self.url = publis['url']
#         self.editeur = publis['publisher']
#         self.series = publis['series']
#         self.auteur = publis['authors']
#         self.isbn = publis['isbn']

#     def to_json(self):
#         return {
#             '_id': self.id,
#             'type': self.type,
#             'title': self.titre,
#             'pages': self.pages,
#             'year': self.date,
#             'booktitle': self.titre_livre,
#             'url': self.url,
#             'publisher': self.editeur,
#             'series': self.series,
#             'authors': self.auteur,
#             'isbn': self.isbn
#         }




class Publication:
    def __init__(self, publis):
        self.id = publis['_id']
        self.type = publis.get('type', 'Unknown Type')
        self.title = publis.get('title', 'Unknown Title')
        self.year = publis.get('year', 0)
        self.publisher = publis.get('publisher', 'Unknown Publisher')
        self.series = publis.get('series', 'Unknown Series')
        self.booktitle = publis.get('booktitle', 'Unknown Booktitle')
        self.url = publis.get('url', 'Unknown URL')
        self.authors = publis.get('authors', [])
        self.isbn = publis.get('isbn', [])

        # Handle 'editor' and 'pages' fields
        pages_data = publis.get('pages')
        # Handle if pages data are string or numerical
        if isinstance(pages_data, dict):
            self.pages_start = pages_data.get('start', 0)
            self.pages_end = pages_data.get('end', 0)
        elif isinstance(pages_data, str):
            # Handle string data accordingly
            self.pages_start = 0  # Set a default value or perform a different action
            self.pages_end = 0
        # This part is just for precaution, it should not be necessary
        else:
            # Handle other cases as needed
            self.pages_start = 0
            self.pages_end = 0

    # def __str__(self):
    #     authors_str = ', '.join(self.authors) if self.authors else 'Unknown Authors'
    #     return f"Title: {self.title}\nAuthors: {authors_str}\nPublisher: {self.publisher}\nYear: {self.year}\nType: {self.type}\nSeries: {self.series}\nBooktitle: {self.booktitle}\nURL: {self.url}\nEditor: {self.editor}\nPages: {self.pages_start}-{self.pages_end}\nISBN: {', '.join(self.isbn)}"



    # Convert a Publication object to a JSON object. It will display only available data
    def to_json(self):
        data = {'_id': self.id}

        if self.type:
            data['type'] = self.type
        if self.title:
            data['title'] = self.title
        if self.year:
            data['year'] = self.year
        if self.publisher:
            data['publisher'] = self.publisher
        if self.series:
            data['series'] = self.series
        if self.booktitle:
            data['booktitle'] = self.booktitle
        if self.url:
            data['url'] = self.url
        if self.authors:
            data['authors'] = self.authors
        if self.isbn:
            data['isbn'] = self.isbn
        if self.editor:
            data['editor'] = self.editor
        if self.pages_start or self.pages_end:
            data['pages'] = {'start': self.pages_start, 'end': self.pages_end}

        return data

























# class Publication:

    
#     def __init__(self, publis):
#         self.id = publis['_id']
#         self.type = publis.get('type', '')  # Handle missing 'type' field
#         self.title = publis.get('title', '')
#         self.year = publis.get('year', 0)
#         self.publisher = publis.get('publisher', '')
#         self.series = publis.get('series', '')
#         self.booktitle = publis.get('booktitle', '')
#         self.url = publis.get('url', '')
#         self.authors = publis.get('authors', [])
#         self.isbn = publis.get('isbn', [])

#         # Handle 'editor' and 'pages' fields
#         self.editor = publis.get('editor', '')
#         self.pages_start = publis.get('pages', {}).get('start', 0)
#         self.pages_end = publis.get('pages', {}).get('end', 0)
    
#     def __str__(self):
#         return f"Title: {self.title}\nAuthors: {', '.join(self.authors)}\nPublisher: {self.publisher}"
#         # Customize the output format as needed

# # Convert a Publication object to a JSON object. It will display only available data
#     def to_json(self):
#         data = {'_id': self.id}

#         if self.type:
#             data['type'] = self.type
#         if self.title:
#             data['title'] = self.title
#         if self.year:
#             data['year'] = self.year
#         if self.publisher:
#             data['publisher'] = self.publisher
#         if self.series:
#             data['series'] = self.series
#         if self.booktitle:
#             data['booktitle'] = self.booktitle
#         if self.url:
#             data['url'] = self.url
#         if self.authors:
#             data['authors'] = self.authors
#         if self.isbn:
#             data['isbn'] = self.isbn
#         if self.editor:
#             data['editor'] = self.editor
#         if self.pages_start or self.pages_end:
#             data['pages'] = {'start': self.pages_start, 'end': self.pages_end}

#         return data
