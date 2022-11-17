from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'fdofied98fe7f867dg'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def grab_data():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def display():
    return render_template('results.html', name = session['name'], location = session['location'], language = session['language'], comments = session['comments'])

if __name__ == '__main__':
    app.run(debug=True)