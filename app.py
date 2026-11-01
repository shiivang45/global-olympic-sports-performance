
from flask import Flask, render_template

# Create Flask application
app = Flask(__name__)

# Home page route
@app.route("/")
def home():
    return render_template("index.html")

# Run the website
if __name__ == "__main__":
    app.run(debug=True)
