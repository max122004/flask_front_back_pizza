from flask import Blueprint, render_template

from pizza.dao.model.pizza import Pizza

product_blueprint = Blueprint('product', __name__, template_folder='templates')

@product_blueprint.route('/product', methods=['GET'])
def get():
    # product_name = Pizza.query.order_by(Pizza.name).all()
    # product_price = Pizza.query.order_by(Pizza.price).all()
    # product_descriprion = Pizza.query.order_by(Pizza.descriprion).all()
    # product_pic = Pizza.query.order_by(Pizza.pic).all()
    pizza = Pizza.query.order_by(Pizza.name).all()
    return render_template('product.html', data=pizza)

 # name = product_name, price = product_price, descriprion = product_descriprion, pic = product_pic