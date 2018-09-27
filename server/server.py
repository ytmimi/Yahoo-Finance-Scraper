from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    	)
	)
	
@app.route('/api')
def graphQL_api():
	return 'Hello world'



if __name__ == '__main__':
	app.run(debug=True)