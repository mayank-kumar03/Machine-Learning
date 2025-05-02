##building url Dynamically
##variable routing
##jinja 2 tmplate engine
##rendering templates


from flask import Flask,render_template,request,redirect,url_for
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



@app.route('/submit',methods=["GET","POST"])
def submit():
      if request.method=="POST":
            name=request.form["name"]
            email=request.form["email"]
            return f"""<html> 
            <h1> Hello {name} </h1>
            <h1> Your email is {email} </h1>
            </html>"""
      return render_template("form.html")

#variable rules
@app.route('/success/<int:value>')
def success(value):
      res=""
      if(value>50):
            res="Passed"
      else:
            res="Failed"
      return render_template("success.html",results=res)


@app.route('/successres/<int:value>')
def successres(value):
      res=""
      if(value>50):
            res="Passed"
      else:
            res="Failed"
      exp={'value':value,'result':res}
      return render_template("successres.html",results=res)


@app.route("/add_value", methods=["GET", "POST"])
def add_value():
    if request.method == "POST":
        # Get the value from the form
        value = int(request.form["value"])
        
        # Redirect to the success route with the value
        return redirect(url_for("success", value=value))
    
    # Render the form to input the value
    return render_template("add_value.html")














if(__name__=="__main__"):
      app.run(debug=True)