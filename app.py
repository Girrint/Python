import os

from flask import Flask

from config import Config

from models import db

from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.product_routes import product_bp
from routes.customer_routes import customer_bp
from routes.order_routes import order_bp
from routes.api_routes import api_bp
from flask import render_template
from models import Product

app = Flask(__name__)

app.config.from_object(Config)

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['QR_FOLDER'], exist_ok=True)
os.makedirs('instance', exist_ok=True)


db.init_app(app)

with app.app_context():
    from models.user import User
    from models.product import Product
    from models.customer import Customer
    from models.order import Order
    from models.order_item import OrderItem

    db.create_all()


app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(product_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(order_bp)
app.register_blueprint(api_bp)


if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)