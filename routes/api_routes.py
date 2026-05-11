from flask import Blueprint
from flask import jsonify
from flask import request

from models import db
from models.product import Product


api_bp = Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)


# =========================================
# GET ALL PRODUCTS
# =========================================
@api_bp.route('/products', methods=['GET'])
def api_products():

    products = Product.query.all()

    data = []

    for product in products:

        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': product.quantity,
            'description': product.description,
            'image': product.image,
            'qr_code': product.qr_code
        })

    return jsonify(data)


# =========================================
# GET SINGLE PRODUCT
# =========================================
@api_bp.route('/products/<int:id>',
              methods=['GET'])
def api_product_detail(id):

    product = Product.query.get_or_404(id)

    return jsonify({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity,
        'description': product.description,
        'image': product.image,
        'qr_code': product.qr_code
    })


# =========================================
# CREATE PRODUCT
# =========================================
@api_bp.route('/products',
              methods=['POST'])
def api_create_product():

    data = request.json

    if not data.get('name'):

        return jsonify({
            'error': 'Name required'
        }), 400

    try:
        price = float(data.get('price', 0))

        quantity = int(
            data.get('quantity', 0)
        )

    except ValueError:

        return jsonify({
            'error': 'Invalid data'
        }), 400

    product = Product(
        name=data.get('name'),
        price=price,
        quantity=quantity,
        description=data.get('description')
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        'message': 'Product created',
        'product_id': product.id
    })


# =========================================
# UPDATE PRODUCT
# =========================================
@api_bp.route('/products/<int:id>',
              methods=['PUT'])
def api_update_product(id):

    product = Product.query.get_or_404(id)

    data = request.json

    product.name = data.get(
        'name',
        product.name
    )

    product.price = data.get(
        'price',
        product.price
    )

    product.quantity = data.get(
        'quantity',
        product.quantity
    )

    product.description = data.get(
        'description',
        product.description
    )

    db.session.commit()

    return jsonify({
        'message': 'Product updated'
    })


# =========================================
# DELETE PRODUCT
# =========================================
@api_bp.route('/products/<int:id>',
              methods=['DELETE'])
def api_delete_product(id):

    product = Product.query.get_or_404(id)

    db.session.delete(product)

    db.session.commit()

    return jsonify({
        'message': 'Product deleted'
    })