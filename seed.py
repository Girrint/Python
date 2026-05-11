from app import app
from models import db, Product, Customer, Order, OrderItem
from faker import Faker
import random

fake = Faker('vi_VN')

with app.app_context():
    OrderItem.query.delete()
    Order.query.delete()
    Customer.query.delete()
    Product.query.delete()
    db.session.commit()

    products = [
        Product(name="Laptop Dell Inspiron", price=15000000, quantity=random.randint(5, 20), description=fake.text(max_nb_chars=100)),
        Product(name="Chuột Logitech MX Master", price=350000, quantity=random.randint(10, 30), description=fake.text(max_nb_chars=100)),
        Product(name="Bàn phím cơ Keychron K8", price=1200000, quantity=random.randint(5, 15), description=fake.text(max_nb_chars=100)),
        Product(name="Tai nghe Sony WH-1000XM4", price=2200000, quantity=random.randint(5, 15), description=fake.text(max_nb_chars=100)),
        Product(name="Màn hình Samsung 27 inch", price=5000000, quantity=random.randint(3, 10), description=fake.text(max_nb_chars=100)),
        Product(name="SSD Samsung 1TB", price=1800000, quantity=random.randint(8, 20), description=fake.text(max_nb_chars=100)),
        Product(name="RAM Kingston 16GB", price=800000, quantity=random.randint(10, 25), description=fake.text(max_nb_chars=100)),
        Product(name="Card đồ họa RTX 3060", price=8000000, quantity=random.randint(2, 8), description=fake.text(max_nb_chars=100)),
        Product(name="Bàn phím không dây Logitech", price=600000, quantity=random.randint(12, 25), description=fake.text(max_nb_chars=100)),
        Product(name="Loa Bluetooth JBL GO 3", price=450000, quantity=random.randint(15, 30), description=fake.text(max_nb_chars=100)),
        Product(name="Ổ cứng ngoài Seagate 2TB", price=1200000, quantity=random.randint(5, 15), description=fake.text(max_nb_chars=100)),
        Product(name="Webcam Logitech C920", price=700000, quantity=random.randint(8, 18), description=fake.text(max_nb_chars=100)),
        Product(name="Router WiFi TP-Link", price=300000, quantity=random.randint(10, 20), description=fake.text(max_nb_chars=100)),
        Product(name="Bộ sạc nhanh Anker", price=250000, quantity=random.randint(20, 40), description=fake.text(max_nb_chars=100)),
        Product(name="Tai nghe gaming Razer", price=1500000, quantity=random.randint(5, 12), description=fake.text(max_nb_chars=100)),
        Product(name="Laptop HP Pavilion", price=12000000, quantity=random.randint(5, 15), description=fake.text(max_nb_chars=100)),
        Product(name="Màn hình LG 24 inch", price=3500000, quantity=random.randint(4, 12), description=fake.text(max_nb_chars=100)),
        Product(name="SSD Kingston A400", price=1500000, quantity=random.randint(8, 18), description=fake.text(max_nb_chars=100)),
        Product(name="RAM Corsair 16GB", price=900000, quantity=random.randint(10, 20), description=fake.text(max_nb_chars=100)),
        Product(name="Chuột gaming SteelSeries", price=800000, quantity=random.randint(6, 16), description=fake.text(max_nb_chars=100)),
        Product(name="Bàn phím mechanical Ducky", price=2000000, quantity=random.randint(3, 10), description=fake.text(max_nb_chars=100)),
        Product(name="Tai nghe Bose QuietComfort", price=5000000, quantity=random.randint(2, 8), description=fake.text(max_nb_chars=100)),
        Product(name="Webcam 4K Razer", price=2000000, quantity=random.randint(4, 10), description=fake.text(max_nb_chars=100)),
        Product(name="Router gaming ASUS", price=4000000, quantity=random.randint(2, 8), description=fake.text(max_nb_chars=100)),
        Product(name="Loa Bluetooth UE Boom", price=1200000, quantity=random.randint(8, 20), description=fake.text(max_nb_chars=100)),
        Product(name="Ổ cứng ngoài WD 4TB", price=2500000, quantity=random.randint(3, 10), description=fake.text(max_nb_chars=100)),
        Product(name="Card đồ họa RTX 4060", price=7000000, quantity=random.randint(2, 6), description=fake.text(max_nb_chars=100)),
        Product(name="CPU Intel i7 13700K", price=15000000, quantity=random.randint(1, 5), description=fake.text(max_nb_chars=100)),
        Product(name="Mainboard ASUS Z790", price=4500000, quantity=random.randint(2, 6), description=fake.text(max_nb_chars=100)),
        Product(name="Power Supply Corsair 850W", price=3000000, quantity=random.randint(3, 8), description=fake.text(max_nb_chars=100)),
        Product(name="PC Case Lian Li", price=2000000, quantity=random.randint(3, 10), description=fake.text(max_nb_chars=100)),
        Product(name="Laptop Lenovo ThinkPad", price=18000000, quantity=random.randint(2, 8), description=fake.text(max_nb_chars=100)),
        Product(name="Chuột cơ học Glorious", price=950000, quantity=random.randint(8, 18), description=fake.text(max_nb_chars=100)),
        Product(name="Mousepad SteelSeries", price=400000, quantity=random.randint(12, 25), description=fake.text(max_nb_chars=100)),
        Product(name="USB Hub Anker 7 cổng", price=500000, quantity=random.randint(10, 20), description=fake.text(max_nb_chars=100)),
        Product(name="Cáp HDMI 2.1", price=150000, quantity=random.randint(20, 50), description=fake.text(max_nb_chars=100)),
        Product(name="Adapter Type-C", price=200000, quantity=random.randint(20, 40), description=fake.text(max_nb_chars=100)),
        Product(name="Monitor gaming 144Hz", price=8000000, quantity=random.randint(2, 8), description=fake.text(max_nb_chars=100)),
        Product(name="Bộ dock Thunderbolt", price=3500000, quantity=random.randint(2, 6), description=fake.text(max_nb_chars=100)),
        Product(name="Laptop Asus VivoBook", price=13000000, quantity=random.randint(4, 12), description=fake.text(max_nb_chars=100)),
    ]

    db.session.bulk_save_objects(products)
    db.session.commit()

    customers = []
    for _ in range(50):
        customer = Customer(
            name=fake.name(),
            phone=fake.phone_number(),
            email=fake.email(),
            address=fake.address()
        )
        customers.append(customer)

    db.session.bulk_save_objects(customers)
    db.session.commit()

    for _ in range(40):
        customer = random.choice(customers)
        order = Order(customer_id=customer.id, total_price=0)
        db.session.add(order)
        db.session.commit()

        num_items = random.randint(1, 6)
        selected_products = random.sample(products, min(num_items, len(products)))
        total = 0
        for product in selected_products:
            quantity = random.randint(1, min(3, product.quantity))
            unit_price = product.price
            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=quantity,
                price=unit_price
            )
            db.session.add(order_item)
            total += quantity * unit_price

        order.total_price = total
        db.session.commit()

    print("Fake data inserted: 40 products, 50 customers, 40 orders!")
