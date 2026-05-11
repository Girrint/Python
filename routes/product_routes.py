import os

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import current_app

from werkzeug.utils import secure_filename

from models import db
from models.product import Product

from utils.decorators import login_required
from utils.qr_generator import generate_qr


product_bp = Blueprint(
    'product',
    __name__,
    url_prefix='/products'
)

ALLOWED_EXTENSIONS = {
    'png',
    'jpg',
    'jpeg',
    'gif'
}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@product_bp.route('/')
@login_required
def list_products():

    keyword = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)

    query = Product.query

    if keyword:
        query = query.filter(
            Product.name.contains(keyword)
        )

    products = query.paginate(page=page, per_page=12, error_out=False)

    return render_template(
        'products/list.html',
        products=products
    )


@product_bp.route('/detail/<int:id>')
@login_required
def product_detail(id):

    product = Product.query.get_or_404(id)

    return render_template(
        'products/detail.html',
        product=product
    )


@product_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_product():

    if request.method == 'POST':

        name = request.form.get('name').strip()

        price = request.form.get('price')

        quantity = request.form.get('quantity')

        description = request.form.get('description')

        if not name:
            flash('Product name required.', 'danger')

            return redirect(
                url_for('product.create_product')
            )

        try:
            price = float(price)
            quantity = int(quantity)

            if price < 0 or quantity < 0:
                raise ValueError

        except ValueError:

            flash(
                'Invalid price or quantity.',
                'danger'
            )

            return redirect(
                url_for('product.create_product')
            )

        image_file = request.files.get('image')

        filename = None

        if image_file and allowed_file(
            image_file.filename
        ):

            filename = secure_filename(
                image_file.filename
            )

            image_path = os.path.join(
                current_app.config['UPLOAD_FOLDER'],
                filename
            )

            image_file.save(image_path)

        product = Product(
            name=name,
            price=price,
            quantity=quantity,
            description=description,
            image=filename
        )

        db.session.add(product)
        db.session.commit()

        qr_filename = generate_qr(
            product.id,
            product.name,
            current_app.config['QR_FOLDER']
        )

        product.qr_code = qr_filename

        db.session.commit()

        flash('Product created.', 'success')

        return redirect(
            url_for('product.list_products')
        )

    return render_template(
        'products/create.html'
    )


@product_bp.route('/edit/<int:id>',
                   methods=['GET', 'POST'])
@login_required
def edit_product(id):

    product = Product.query.get_or_404(id)

    if request.method == 'POST':

        product.name = request.form.get('name')

        product.price = float(
            request.form.get('price')
        )

        product.quantity = int(
            request.form.get('quantity')
        )

        product.description = request.form.get(
            'description'
        )

        image_file = request.files.get('image')

        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(
                current_app.config['UPLOAD_FOLDER'],
                filename
            )
            image_file.save(image_path)
            product.image = filename

        db.session.commit()

        flash('Product updated.', 'success')

        return redirect(
            url_for('product.list_products')
        )

    return render_template(
        'products/edit.html',
        product=product
    )


@product_bp.route('/delete/<int:id>')
@login_required
def delete_product(id):

    product = Product.query.get_or_404(id)

    db.session.delete(product)
    db.session.commit()

    flash('Product deleted.', 'warning')

    return redirect(
        url_for('product.list_products')
    )