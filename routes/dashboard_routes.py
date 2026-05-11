from flask import Blueprint, render_template

from models.product import Product
from models.order import Order
from models.customer import Customer

from utils.decorators import login_required


dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
@login_required
def dashboard():
    total_products = Product.query.count()

    total_orders = Order.query.count()

    total_customers = Customer.query.count()

    total_revenue = sum(order.total_price for order in Order.query.all())

    return render_template(
        'dashboard.html',
        total_products=total_products,
        total_orders=total_orders,
        total_customers=total_customers,
        total_revenue=total_revenue
    )