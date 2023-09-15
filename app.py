# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Eric" 
    age = "15" 

    return render_template('me.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    name = "Jack"
    age = "56"

    return render_template('father.html' , name = name , age = age)
# define the route to mother webpage
@app.route("/mother")
def mother():
    name = "Beth"
    age = "53"

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def friend():
    name = "James"
    age = "14"

    return render_template('friend.html' , name = name , age = age)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
