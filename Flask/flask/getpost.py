from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def func():
      return "<html> <h1> This is homepage  ----</h1></html>"
@app.route("/index",methods=["GET"])
def index():
      return render_template("/index.html")
@app.route("/about")
def about():
      return render_template("about.html")
@app.route('/form',methods=["GET","POST"])
def form():
      if request.method=="POST":
            name=request.form["name"]
            email=request.form["email"]
            return f"""<html> 
            <h1> Hello {name} </h1>
            <h1> Your email is {email} </h1>
            </html>"""
      
      return render_template("form.html")



if(__name__=="__main__"):
      app.run(debug=True)