from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        return redirect(url_for('thank_you'))

    return render_template('contact.html')

@app.route('/thank_you')
def thank_you():
    return 'Thank you for contacting us!'

if __name__ == "__main__":
    app.run(debug=True)