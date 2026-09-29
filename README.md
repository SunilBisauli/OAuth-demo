# Flask GitHub OAuth Login App

A lightweight, beginner-friendly web application built with **Python (Flask)** and **JavaScript** that demonstrates secure user authentication using **GitHub OAuth**, session management, and protected route redirection.

---

## Features

* **OAuth 2.0 Authentication:** Securely log in using a GitHub account without managing passwords.
* **Server-Side Sessions:** Encrypted session cookies via Flask to maintain user state.
* **Protected Routes:** Automatic redirection of unauthenticated users away from private dashboards.
* **Dynamic Frontend UI:** JavaScript-powered time-of-day greetings tailored to the logged-in user.
* **Clean & Responsive CSS:** Modern, centered layouts designed for clarity.

---

## Project Structure

```text
oauth-login-app/
├── app.py                 # Backend routing, OAuth exchange, and session logic
├── requirements.txt       # Project dependencies
├── templates/
│   ├── index.html         # Public landing page with login button
│   └── dashboard.html     # Protected dashboard page
└── static/
    ├── style.css          # Styling rules
    └── script.js          # Dynamic JavaScript logic