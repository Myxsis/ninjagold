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
	session['farm_arr'] = []
	session['cave_arr'] = []
	session['house_arr'] = []
	session['casino_arr'] =[]
	if request.form['building'] == 'farm':
		session['gold'] = random.randrange(10,21)
		session['found'] = 'Found ' + str(session['gold']) + ' gold from farm!'
		session['farm_arr'].append(session['found'])
		session['foundgold'] += session['gold']
		session['message'] = 'Found gold from farm!'
	elif request.form['building'] == 'cave':
		session['gold'] = random.randrange(5,11)
		session['cave_arr'].append(session['gold'])
	elif request.form['building'] == 'house':
		session['gold'] = random.randrange(2,6)
	elif request.form['building'] == 'HIGHROLLERYO':
		luck = random.randrange(1,100)
		session['gamble'] = random.randrange(0,51)
		session['gold'] = session['gamble']
	
	if request.form['building'] == 'HIGHROLLERYO':
		if luck < 50:
			session['foundgold'] -= session['gamble'] # IF LOST
			session['message'] = 'Lost gold from casino!'

		if luck >= 50:
			session['foundgold'] += session['gamble'] # IF GAINED
			session['message'] = 'Found gold from casino!'
	# elif:

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['foundgold'] = 0
	return redirect('/')

app.run(debug=True)

