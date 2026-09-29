from flask import Flask, redirect, request, session, url_for, render_template
import requests

app = Flask(__name__)
# The secret key encrypts the session cookies so users can't tamper with them
app.secret_key = "super_secret_random_key_for_development" 

# --- YOUR GITHUB CREDENTIALS ---
CLIENT_ID = 'paste_your_client_id_here'
CLIENT_SECRET = 'paste_your_client_secret_here'


@app.route('/')
def index():
    # If the user is already logged in, send them straight to the dashboard
    if 'user' in session:
        return redirect(url_for('dashboard')
    return render_template('index.html')

@app.route('/login')
def login():
    # Step 1 of OAuth: Send the user to GitHub's login page
    github_auth_url = f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}"
    return redirect(github_auth_url)

@app.route('/callback')
def callback():
    # Step 2 of OAuth: GitHub sends the user back here with a special "code"
    code = request.args.get('code')
    
    # Step 3: We securely trade that code for an "access token" behind the scenes
    token_url = "https://github.com/login/oauth/access_token"
    headers = {'Accept': 'application/json'}
    data = {'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'code': code}
    
    response = requests.post(token_url, headers=headers, data=data)
    access_token = response.json().get('access_token')

    # Step 4: Use the access token to fetch the user's public GitHub profile
    user_url = "https://api.github.com/user"
    user_headers = {'Authorization': f'Bearer {access_token}'}
    user_response = requests.get(user_url, headers=user_headers)
    user_data = user_response.json()

    # Step 5: Save the username in our Flask session and send them to the dashboard
    session['user'] = user_data['login']
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    # Security check: Kick the user back to home if they aren't logged in
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html', username=session['user'])

@app.route('/logout')
def logout():
    # Clear the session memory, effectively logging the user out
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(debug=True, port=5000)