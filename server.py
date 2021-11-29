from logging import NullHandler
from flask import Flask, render_template, session, request
import random

from werkzeug.utils import redirect


app = Flask(__name__)
app.secret_key = 'guess the num'

high_num = 100

@app.route('/')
def index():  
   if "rand_num" not in session:
      session['high_num'] = high_num
      session['count'] = 0
      session['rand_num'] = random.randint(1, high_num)

      print (session['rand_num'])
   return render_template('index.html')

@app.route('/process-guess', methods=['POST'])
def process_guess():
   print('processing guess!')
   session['count'] += 1
   session['guess'] = int(request.form['guess'])
   return redirect('/')

@app.route('/reset')
def reset():
   session.clear() #guess and rand_num
   return redirect('/')

if __name__=="__main__":
   app.run(debug=True)