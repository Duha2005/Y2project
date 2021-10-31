from flask import Flask, render_template, request
from database import *
import random 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'

@app.route("/")
def index():
  return render_template("home.html")



@app.route('/create', methods=['GET', 'POST'])
def that_quiz():
    if request.method == 'GET':
        return render_template("quiz.html")
    else:
      # gender = request.form['gender']
      # social = request.form['social']
      # salary = request.form['salary']
      # family = request.form['family']
      # if gender == "Man" and social == "married" and family == "Yes":
        return render_template("mar_man.html")
      # elif gender == "Man" and social=="married" and  family == "No":
      #   return render_template("mar2_man.html")
      # elif gender == "Man" and social == "unmarried" and family == "No":
      #   return render_template("unmar_man.html")
      # elif gender == "Woman" and social == "married" and family == "Yes":
      #   return render_template("mar_wom.html")
      # elif gender== "Woman" and social=="married" and family == "No":
      #   return render_template("mar2_wom.html")
      # elif gender == "Woman" and social == "unmarried" and family == "No":
      #   return render_template ("unmar_wom.html")
      # else:
      #   return render_template("index.html")



@app.route('/profile', methods=['POST'])
def find_profile():
  house = request.form['house']
  wife = request.form['wife']
  kids = request.form['kids']
  yourself = request.form['yourself']
  salary = request.form['salary']

  money_left = int(salary) - (int(house) + int(wife) + int(kids) + int(yourself))

  return render_template("profile.html", money = money_left)
  
  

    
  




        













@app.route('/Sign_up', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'GET':
    return render_template("sign_up.html")
  else:
    name = request.form['Name']
    password = request.form['Password']
    add_user(name, password)
    return render_template("quiz.html",name=name)


@app.route('/Log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == 'GET':
        return render_template("log_in.html")
    else:
      userfound = find_user(Name = request.form['Name'])
      password = request.form['Password']
      if userfound and userfound.password == password:
        return render_template("profile.html")
      else:
        print("Wrong user or password")
        return render_template("index.html")


@app.route('/Quiz', methods=['GET', 'POST'])
def quiz():
  if request.method == 'GET':
    return render_template("quiz.html")
  else:
    genger = request.form['gender']
    social = request.form['social']
    salary = request.form['salary']
    family = request.form['family']
    add_user(Name, password)
    return render_template("You completed the quiz!")



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
    debug=True
	)