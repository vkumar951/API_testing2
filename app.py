from flask import Flask,jsonify,request,render_template

app=Flask(__name__)

stores=[

    {
        'name':'My store',
        'items':[
                 {
                 'name':'My item' ,
                  'price':15.99   }

                ]
    }

]

@app.route('/')
def home():
    return render_template('index.html')

#POST /store data:{name:}
@app.route('/store',methods=['POST'])
def create_store():
    request_data=request.get_json()
    new_store={
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>/
@app.route('/store/<string:name>')
def get_store(name):
    #iterate over stores and if that store matches with the name given , return that store.
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message':'store not found'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

# POST /store/<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data=request.get_json()
    print(request_data)
    for store in stores:
        if store['name']==name:
            print(name)
            new_item= {
            'name':request_data['name'],
            'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'})



if __name__ == '__main__':
    app.run(debug=True)
