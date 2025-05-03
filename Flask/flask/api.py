
from flask import request, jsonify,Flask

app=Flask(__name__)


items=[
      {"id":1,"name":"item1","description":"this is item 1"},
      {"id":2,"name":"item2","description":"this is item 2"},
      {"id":3,"name":"item3","description":"this is item 3"},
      {"id":4,"name":"item4","description":"this is item 4"},
      {"id":5,"name":"item5","description":"this is item 5"},
]

@app.route("/")
def home():
      return "<h1> This is homepage </h1>"

##retrive all itms
@app.route("/items",methods=["GET"])
def get_items():
      return jsonify(items)

##retrive by a specific id
@app.route("/items/<int:item_id>",methods=["GET"])
def get_item(item_id):
      item=next((item for item in items if item["id"]==item_id),None)
      if item:
            return jsonify(item)
      else:
            return jsonify({"error":"Item not found"}),404
      
##post:create a new item
@app.route("/items",methods=["POST"])
def create_item():
      if not request.json or not "name" in request.json:
            return jsonify({"error":"Bad Request"}),400
      new_item={
            "id":items[-1]["id"]+1 if items else 1,
            "name":request.json["name"],
            "description":request.json["description"]
      }
      items.append(new_item)
      return jsonify(new_item)

##put:update an existing item
@app.route("/items/<int:item_id>",methods=["PUT"])
def update_item(item_id):
      item=next((item for item in items if item["id"]==item_id),None)
      if not item:
            return jsonify({"error":"Item not found"}),404
      if not request.json:
            return jsonify({"error":"Bad Request"}),400
      item["name"]=request.json.get("name",item["name"])
      item["description"]=request.json.get("description",item["description"])
      return jsonify(item)


##delete:delete an item
@app.route("/items/<int:item_id>",methods=["DELETE"])
def delete_item(item_id):
      item=next((item for item in items if item["id"]==item_id),None)
      if not item:
            return jsonify({"error":"Item not found"}),404
      items.remove(item)
      return jsonify({"message":"Item deleted successfully"})

      




if __name__=="__main__":
      app.run(debug=True)