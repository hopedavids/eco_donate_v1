from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/single-portfolio')
def single_portfolio():
    return render_template('single-portfolio.html')

@app.route('/single-post')
def single_post():
    return render_template('single-post.html')

if __name__ == '__main__':
    app.run(debug=True)