from flask import Flask
app=Flask(__name__)

@app.route("/")
def func():
      return "welcome to  my web app  and hello world____!"
@app.route("/index")
def index():
      return "this is index page__"


if(__name__=="__main__"):
      app.run(debug=True)