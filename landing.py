from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/dojos/new')
def dojos():
    return render_template("dojos.html")

@app.route('/signup',methods=['POST'])
def signup():
    print "You have successfully signed up for ninjas!"
    print request.form['name']
    print request.form['email']
    return redirect('/ninjas')

app.run(debug=True)
