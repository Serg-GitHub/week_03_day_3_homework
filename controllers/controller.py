from flask import render_template
from app import app
from models.items import order
from models.items import order_1

@app.route('/')
def index():
    return render_template('index.html', title='My Order List', order=order)

@app.route('/order')
def orders():
    return render_template('order_1.html', title='My Second Order', order_1=order_1)
