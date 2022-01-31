from flask import Flask

#flask object
app = Flask(__name__)

# use route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
def hello():
     return "Welcome to home page"

@app.route("/myself")
def index():
    return "This is Sanvi here"


if (__name__ == "__main__"):
     app.run(debug=True)
     #app.run(debug=True , port = 8000)