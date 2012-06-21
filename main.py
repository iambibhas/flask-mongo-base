from flask import Flask, render_template, abort
app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html', hellomsg = "SiteName")

if __name__ == "__main__":
    app.run(debug=True)