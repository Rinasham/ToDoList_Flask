from crypt import methods
from flask import Flask, render_template, request, redirect
import datetime


app = Flask(__name__)

todo_list =['shopping', 'eat']

@app.route('/')
def index():
  day = datetime.datetime.now()
  today = day.strftime('%A,%B%H,%Y')
  return render_template('index.html', today = today, list = todo_list)

@app.route('/', methods=['POST'])
def add_new_todo():
  new_todo = request.form.get('new_todo')
  todo_list.append(new_todo)
  return redirect('/')



app.run(debug=True)