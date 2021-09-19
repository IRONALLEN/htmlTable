from flask import Flask, render_template
app = Flask(__name__)

users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
@app.route('/<string:color>') # this localhost :5000/..... if you do ('/<string:name>/<int:loop>') typecast aka concactinating
def loop( color) :
    return render_template('htmlTable.html',users = users, color = color)

if __name__=="__main__" :
    app.run(debug=True)