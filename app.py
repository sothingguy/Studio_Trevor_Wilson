from flask import Flask, render_template
app = Flask(__name__)

if __name__ == '__main__':
    run_app = app.create_app()
    run_app.run(debug=True) 

@app.route("/")
def home():
    return render_template('home.html')

