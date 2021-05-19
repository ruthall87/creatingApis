from flask import Flask, jsonify

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
    pass


# GET /STORE/ 
@app.route('/store/<string:name>')
def get_store(name):
    pass


# GET /STORE/ 
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST STORE / <STRING: NAME>/item {name: price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


# GET / STORE / <STRING: NAME>/item 
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass


app.run(port=5000)