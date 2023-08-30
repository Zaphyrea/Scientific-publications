from flask import Flask, render_template, request, redirect, url_for
from models.data import Data

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     filter_author = None
#     filter_year = None
#     filter_title = None
#     filter_booktitle = None
#     publications = []
#     # Get the publication count
#     publication_count = Data.get_publication_count()  

#     # Get the publications depending on the filters
#     if request.method == 'POST':
#         filter_author = request.form.get('author')
#         filter_year = request.form.get('year')
#         filter_title = request.form.get('title')
#         filter_booktitle = request.form.get('booktitle')
        
#         # Loop through the filters and get the publications
#         if filter_author:
#             publications = Data.filter_authors(filter_author)
#         elif filter_year:
#             publications = Data.filter_years(int(filter_year))
#         elif filter_title:
#             publications = Data.filter_titles(filter_title)
#         elif filter_booktitle:
#             publications = Data.filter_booktitles(filter_booktitle)
    
#     return render_template('index.html', filter_author=filter_author, filter_year=filter_year, filter_title=filter_title, filter_booktitle=filter_booktitle, publications=publications, publication_count=publication_count)


@app.route('/', methods=['GET', 'POST'])
def index():
    filter_search_term = None
    filter_option = None
    publications = []

    # Get the publication count
    publication_count = Data.get_publication_count()

    if request.method == 'POST':
        filter_search_term = request.form.get('search_term')
        filter_option = request.form.get('search_option')

        if filter_search_term and filter_option:
            if filter_option == 'author':
                publications = Data.filter_authors(filter_search_term)
            elif filter_option == 'year':
                publications = Data.filter_years(int(filter_search_term))
            elif filter_option == 'title':
                publications = Data.filter_titles(filter_search_term)

    return render_template('index.html', filter_search_term=filter_search_term, filter_option=filter_option, publications=publications, publication_count=publication_count)


# Add a new publication
@app.route('/insertion', methods=['GET', 'POST'])
def insertion():
    if request.method == 'POST':
        # Get form data from the request
        pub_type = request.form.get('type')
        title = request.form.get('title')
        year = int(request.form.get('year'))
        publisher = request.form.get('publisher')
        series = request.form.get('series')
        booktitle = request.form.get('booktitle')
        url = request.form.get('url')
        authors = request.form.getlist('authors')
        isbn = request.form.getlist('isbn')
        
        # Call the add_pub function to insert the publication
        Data.add_pub(pub_type, title, year, publisher, series, booktitle, url, authors, isbn)
        
        return "Votre publication a bien été ajoutée!"  
    return render_template('insertion.html')
 
if __name__ == '__main__':
    app.run(debug=True)