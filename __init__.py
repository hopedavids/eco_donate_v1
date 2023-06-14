from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/shop_details')
def shop_details():
    return render_template('shop-details.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/single-portfolio')
def single_portfolio():
    return render_template('single-portfolio.html')

@app.route('/single-post')
def single_post():
    return render_template('single-post.html')

if __name__ == '__main__':
    app.run(debug=True)