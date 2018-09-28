## About
On November 1st, 2017 Yahoo discontinued access to their finance API. This didn't affect me much, but a few of the Python courses I was going through at the time were using the API alongside pandas-datareader. I had no idea why my code was breaking, but managed to finish those courses using CSV files provided by the instructors. Its been nearly a year since Yahoo discontinued their API, and in that time my skills have improved immensely. This project serves several functions. First, it presents my solution for quickly accessing financial data from yahoo, which will hopefully, and should only be used for educational purposes. Second, it serves as practice in web-scraping. and Third, I used this project as an opportunity to get familiar with graphQL. The graphQL server works as a simple, and effective, interface between users and the web scraper that gathers data from yahoo finance.


## Getting Started
This project uses several different third party Python packages, which include:
* Pipenv
* Requests
* Flask
* Flask-GraphQL
* Graphene

Pipenv is used to manage the virtual environment. Requests is used to get data from Yahoo Finance. Flask is responsible for running a simple web server. Lastly, Flask-GraphQL and graphene create the GraphiQL view and help define the graphQL schema respectively.

Start by cloning this repository.
```
$: git clone https://github.com/ytmimi/Yahoo-Finance-Scraper.git
```
If you don't already have pipenv installed, you can do so with:
```
$: pip install pipenv
```
Feel free to use any virtual environment you'd like. However,  since I've used pipenv it'll
save you the trouble of manually installing all the required packages.

If you've chosen to use pipenv, move into the directory where you cloned this repository and create a new virtual enviornemt by running:
 ```
 $: pipenv install
 ```
This will create a new Python 3 virtual environment and install all the packages specified in the Pipfile.lock.

After that, start the virtual environment with:
```
$: pipenv shell
```
## Testing
This project uses pytest for unit testing. Because This project is built around a web-scraper, it is almost guaranteed to break at some point. To ensure that the project is working correctly, you should run the test suite before you try to use it. This should include running tests that mock data, as well as, live tests.

Before running the tests you'll have to gather the mock data files. To do so run:

```
$: python test/generate_moch_data.py
```
This file will attempt to gather data from yahoo finance, and save them to json files in a newly created /mock_data directory. If the above script runs without any issues thats a good sign that everything should be working. To be 100% certain about the functionality of the program the full test suite should be run with pytest:
```
$: pytest
```
If all of the tests pass you can be sure that the graphQL server will work just fine!

## Running the GraphQL server
As previously mentioned this project was used to gain familiarity with graphQL. I've been very impressed with how flexible it is, and look forward to working on more projects that incorporate it.

Assuming that you're already inside the virtual environment and have all the required packages installed, running a local server from the root directory is as simple as:

```
$: python server/server.py
```
This will start a simple Flask app, and you should see an output that looks similar to the following:
```
* Serving Flask app "server" (lazy loading)
* Environment: production
  WARNING: Do not use the development server in a production environment.
  Use a production WSGI server instead.
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Now, in your browser head to http://127.0.0.1:5000/graphql in order to test out the graphQL API with GraphiQL.

For more clarity on the graphQL endpoint Check out the [documentation](./schema.md)!
