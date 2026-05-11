from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from models import db

from models.order import Order
from models.order_item import OrderItem

from models.product import Product
from models.customer import Customer

from utils.decorators import login_required


order_bp = Blueprint(
    'order',
    __name__,
    url_prefix='/orders'
)


@order_bp.route('/')
@login_required
def list_orders():

    orders = Order.query.order_by(
        Order.created_at.desc()
    ).all()

    return render_template(
        'orders/list.html',
        orders=orders
    )


@order_bp.route(
    '/create',
    methods=['GET', 'POST']
)
@login_required
def create_order():

    customers = Customer.query.all()

    products = Product.query.all()

    if request.method == 'POST':

        customer_id = request.form.get(
            'customer_id'
        )

        product_ids = request.form.getlist(
            'product_id'
        )

        quantities = request.form.getlist(
            'quantity'
        )

        order = Order(
            customer_id=customer_id,
            status='pending'
        )

        db.session.add(order)
        db.session.commit()

        total = 0

        for product_id, qty in zip(
            product_ids,
            quantities
        ):

            if not qty:
                continue

            qty = int(qty)

            if qty <= 0:
                continue

            product = Product.query.get(
                product_id
            )

            if qty > product.quantity:

                flash(
                    f'Not enough stock for '
                    f'{product.name}',
                    'danger'
                )

                return redirect(
                    url_for(
                        'order.create_order'
                    )
                )

            subtotal = (
                product.price * qty
            )

            item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=qty,
                price=product.price
            )

            product.quantity -= qty

            total += subtotal

            db.session.add(item)

        order.total_price = total

        db.session.commit()

        flash(
            'Order created.',
            'success'
        )

        return redirect(
            url_for('order.list_orders')
        )

    return render_template(
        'orders/create.html',
        customers=customers,
        products=products
    )


@order_bp.route('/detail/<int:id>')
@login_required
def order_detail(id):

    order = Order.query.get_or_404(id)

    return render_template(
        'orders/detail.html',
        order=order
    )


@order_bp.route(
    '/status/<int:id>/<string:status>'
)
@login_required
def update_status(id, status):

    order = Order.query.get_or_404(id)

    allowed_status = [
        'pending',
        'completed',
        'cancelled'
    ]

    if status not in allowed_status:

        flash(
            'Invalid order status.',
            'danger'
        )

        return redirect(
            url_for('order.list_orders')
        )

    order.status = status

    db.session.commit()

    flash(
        'Order status updated.',
        'success'
    )

    return redirect(
        url_for('order.list_orders')
    )