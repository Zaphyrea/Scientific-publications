# Scientific-publications

The objective of this work was to create a small module for simple access to scientific publications for a research centre.
We have been asked to set up a document-oriented MongoDB database to manage access to these publications. We were to test the data using a small Python script.

There are 3 filters available (title, author and year). This may be the most beautiful interface you have ever seen... or maybe not.
The application is deployable from a docker-compose.


## Make it work
First you have to unzip the file. Then you can deploy the Docker container using this command :

    docker-compose up --build -d
Take care to be in 'mongauteurs' folder in your terminal when you enter the command

Then you can go and enjoy at :  http://127.0.0.1:5000/
