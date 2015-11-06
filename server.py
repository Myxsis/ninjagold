from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key='steppinondabeach'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process_money')
def money():
	return redirect('/')