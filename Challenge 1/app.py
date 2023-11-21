from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'logged_in' in session and session['logged_in']:
        session.pop('logged_in', None)
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        loweruser=username.lower()
        lowerpass=password.lower()
        invalid_entries = ['=','<','>', ';', '-', "'1",' 1', ' true',"'true", ' or',"'or", ' and',"'and","'like",' like', '%00',"'where",' where']
        matching_value = next((value for value in invalid_entries if value in loweruser or value in lowerpass), None)
        if matching_value:
            error = f'Invalid entry ({matching_value}) in username and/or password fields. Please try again.'
            return render_template('login.html', error=error)
        
        conn = sqlite3.connect('chal.db')
        cursor = conn.cursor()

        query = f"SELECT secret FROM login_details WHERE username = '{username}' AND password = '{password}';"

        result = cursor.execute(query)
        user = result.fetchone()[0]

        conn.close()

        if user:
            session['logged_in'] = True
            session['username'] = username
            session['secret']=user
            return redirect(url_for('profile'))
            #return render_template('profile.html', username=username, secret=session['secret'])
        else:
            error = 'Invalid login credentials. Please try again.'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/')
def index():
    if 'logged_in' in session and session['logged_in']:
        session.pop('logged_in', None)
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'logged_in' in session and session['logged_in']:
        username = session['username']
        secret = session.get('secret')
        return render_template('profile.html', username=username, secret=secret)
    else:
        error = 'You are not logged in. Please log in first.'
        return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return render_template('login.html')

@app.after_request
def add_cache_control(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

if __name__ == '__main__':
    app.run(debug=True)
