
# main.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/concepts')
def concepts():
  return render_template('concepts.html')

@app.route('/algorithms')
def algorithms():
  return render_template('algorithms.html')

@app.route('/applications')
def applications():
  return render_template('applications.html')

@app.route('/exercises')
def exercises():
  return render_template('exercises.html')

@app.route('/submit_exercise', methods=['POST'])
def submit_exercise():
  # handle exercise submission and provide feedback
  return redirect(url_for('exercises'))

if __name__ == '__main__':
  app.run(debug=True)
