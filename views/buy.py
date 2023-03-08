from flask import Blueprint, render_template, request, redirect

from pizza.dao.model.user import User
from pizza.setup_db import db

buy_blueprint = Blueprint('buy', __name__, template_folder='templates')

@buy_blueprint.route('/buy', methods=['POST', 'GET'])
def get():
    if request.method == "POST":
        title = request.form['title']
        fio = request.form['fio']
        number = request.form['number']
        email = request.form['email']
        address = request.form['address']

        user = User(title=title, fio=fio, number=number, email=email, address=address)

        db.session.add(user)
        db.session.commit()
        return redirect('/')


    else:
        return render_template('buy.html')