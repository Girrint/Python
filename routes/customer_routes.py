from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from models import db
from models.customer import Customer

from utils.decorators import login_required


customer_bp = Blueprint(
    'customer',
    __name__,
    url_prefix='/customers'
)


@customer_bp.route('/')
@login_required
def list_customers():

    keyword = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)

    query = Customer.query

    if keyword:
        query = query.filter(
            Customer.name.contains(keyword) |
            Customer.phone.contains(keyword) |
            Customer.email.contains(keyword)
        )

    customers = query.paginate(page=page, per_page=10, error_out=False)

    return render_template(
        'customers/list.html',
        customers=customers
    )


@customer_bp.route(
    '/create',
    methods=['GET', 'POST']
)
@login_required
def create_customer():

    if request.method == 'POST':

        customer = Customer(
            name=request.form.get('name'),
            phone=request.form.get('phone'),
            email=request.form.get('email'),
            address=request.form.get('address')
        )

        db.session.add(customer)
        db.session.commit()

        flash(
            'Customer created.',
            'success'
        )

        return redirect(
            url_for('customer.list_customers')
        )

    return render_template(
        'customers/create.html'
    )


@customer_bp.route(
    '/edit/<int:id>',
    methods=['GET', 'POST']
)
@login_required
def edit_customer(id):

    customer = Customer.query.get_or_404(id)

    if request.method == 'POST':

        customer.name = request.form.get('name')

        customer.phone = request.form.get(
            'phone'
        )

        customer.email = request.form.get(
            'email'
        )

        customer.address = request.form.get(
            'address'
        )

        db.session.commit()

        flash(
            'Customer updated.',
            'success'
        )

        return redirect(
            url_for('customer.list_customers')
        )

    return render_template(
        'customers/edit.html',
        customer=customer
    )


@customer_bp.route('/delete/<int:id>')
@login_required
def delete_customer(id):

    customer = Customer.query.get_or_404(id)

    db.session.delete(customer)

    db.session.commit()

    flash(
        'Customer deleted.',
        'warning'
    )

    return redirect(
        url_for('customer.list_customers')
    )