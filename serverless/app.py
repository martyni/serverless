from chalice import Chalice
from geoip import geolite2
app = Chalice(app_name='serverless')


@app.route('/')
def index():
    return {'hello': 'world'}

#
# The view function above will return {"hello": "world"}
# whenver you make an HTTP GET request to '/'.
#
# Here are a few more examples:

@app.route('/hello/{name}')
def hello_name(name):
   # '/hello/james' -> {"hello": "james"}
   return {'hello': name}

@app.route('/request',methods=['GET', 'PUT', 'POST','DELETE'] )
def return_requst():
    return app.current_request.to_dict()

@app.route('/where_am_i')
def return_requst():
   return geoip.geolite2.lookup(app.current_request.to_dict()['context']['source-ip'])
# See the README documentation for more examples.
#
