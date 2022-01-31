from flask import Flask, jsonify, request
app = Flask(__name__)
alltask = [
     {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Water the plants',
        'description': u'taking care of plants', 
        'done': False
    },
     {
        'id': 1,
        'title': u'School Assignments',
        'description': u'Maths, English', 
        'done': False
    },
]

@app.route("/")
def hello():
    return "Welcome to the homepage"

@app.route("/add-data" , methods = ["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': alltask[-1]['id'] + 1,
        'title': request.json['title'], 
        'description': request.json.get('description', ""),
        'done': False
    }
    alltask.append(task)
    return jsonify({
        "status":"succes",
        "message":"Task added succesfully",
    })

@app.route("/get-data")
def gettask():
    return jsonify({
        "data":alltask
    })

if (__name__ == "__main__"):
    app.run(debug= True)


