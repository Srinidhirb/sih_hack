from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create an empty dictionary to store user details
user_database = {}

# Replace this with your actual user authentication logic.
# For this example, we'll use a hardcoded username and password.
VALID_USERNAME = "srinidhi"
VALID_PASSWORD = "dhaarini"

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    userid = request.form.get("userid")
    password = request.form.get("password")

    if userid == VALID_USERNAME and password == VALID_PASSWORD:
        # Check if the user already exists in the dictionary
        if userid not in user_database:
            # If not, add the user to the dictionary with their password
            user_database[userid] = password

        # Redirect to a success page after successful login.
        return redirect(url_for("success"))
    else:
        # If login fails, you can redirect to an error page or display an error message.
        return render_template("registration.html", error_message="Invalid credentials")

@app.route("/success")
def success():
    return render_template("startup.html")

if __name__ == "__main__":
    app.run(debug=True)
