from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key='steppinondabeach'

@app.route('/')
def index():
	try:
		session['foundgold']
	except:
		session['foundgold'] = 0
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def money():
	if request.form['building'] == 'farm':
		session['gold'] = random.randrange(10,21)
	elif request.form['building'] == 'cave':
		session['gold'] = random.randrange(5,11)
	elif request.form['building'] == 'house':
		session['gold'] = random.randrange(2,6)
	elif request.form['building'] == 'HIGHROLLERYO':
		luck = random.randrange(1,100)
		session['gamble'] = random.randrange(0,51)
		session['gold'] = session['gamble']
	
	if request.form['building'] == 'HIGHROLLERYO':
		if luck < 50:
			session['foundgold'] -= session['gamble'] # IF LOST
			session['message'] = 'Lost gold!'
			
		if luck >= 50:
			session['foundgold'] += session['gamble'] # IF GAINED
			session['message'] = 'Found gold!'
	else:		
		session['foundgold'] += session['gold']
		session['message'] = 'Found gold!'

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['foundgold'] = 0
	return redirect('/')

app.run(debug=True)

