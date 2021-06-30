from app import app
from flask import render_template # ADDED
from models.items import order

@app.route('/order')
def index():
    return render_template('index.html', title='My Order List', order=order)