from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/gallary")
def gallary():
    return render_template('gallary.html')

@app.route("/my_process")
def my_process():
    return render_template('my_process.html')

@app.route("/westminster_street")
def westminster_street():
    return render_template('westminster_street.html')

@app.route("/westport")
def westport():
    return render_template('westport.html')

@app.errorhandler(404)
def error404(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
  #app.run(debug=True)
  app.run()
