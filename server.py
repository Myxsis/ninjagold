from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key='steppinondabeach'

@app.route('/')
def index():
	try:
		session['foundgold']
		session['message']
	except:
		session['foundgold'] = 0
		session['message'] = []
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def money():
	if request.form['building'] == 'farm':
		session['gold'] = random.randrange(10,21)
		loot = 'Found ' + str(session['gold']) + ' gold from farm!'
		session['message'].insert(0, loot)
		session['foundgold'] += session['gold']
	elif request.form['building'] == 'cave':
		session['gold'] = random.randrange(5,11)
		loot = 'Found ' + str(session['gold']) + ' gold from cave!'
		session['message'].insert(0, loot)
		session['foundgold'] += session['gold']
	elif request.form['building'] == 'house':
		session['gold'] = random.randrange(2,6)
		loot = 'Found ' + str(session['gold']) + ' gold from house!'
		session['message'].insert(0, loot)
		session['foundgold'] += session['gold']
	elif request.form['building'] == 'HIGHROLLERYO':
		luck = random.randrange(1,100)
		session['gamble'] = random.randrange(0,51)
		session['gold'] = session['gamble']
	
	if request.form['building'] == 'HIGHROLLERYO':
		if luck < 50:
			session['foundgold'] -= session['gamble'] # IF LOST
			loot = 'Found ' + str(session['gold']) + ' gold from casino!'
			session['message'].insert(0, loot)
			session['foundgold'] += session['gold']

		if luck >= 50:
			session['foundgold'] += session['gamble'] # IF GAINED
			loot = 'Lost ' + str(session['gold']) + ' gold from casino!'
			session['message'].insert(0, loot)
			session['foundgold'] -= session['gold']
	# elif:

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['foundgold'] = 0
	session['message'] = []
	return redirect('/')

app.run(debug=True)

