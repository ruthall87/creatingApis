from types import new_class
from flask import Flask, jsonify, request


app = Flask(__name__)
stores = [
    {
        'name': 'my store',
        'items': [
            {
                'name': 'My Item',
                'price': 18.88
            }
        ]
    }
]



# POST / STORE DATA: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request_data_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /STORE/<store:name>
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores
    for store in stores:
    # if the store name matches, return it
        if store['name'] == name:
            return jsonify(store)
    # If none match, return an error message
    return jsonify({'message': 'store not found'})
    


# GET /STORE/ 
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST STORE / <STRING: NAME>/item {name: price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'}) 


# GET / STORE / <STRING: NAME>/item 
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify/({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)