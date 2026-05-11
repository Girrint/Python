# Store Management System

## Hệ thống quản lý cửa hàng được xây dựng bằng Flask + SQLite + Bootstrap 5.

### Dự án hỗ trợ quản lý:

- Sản phẩm
- Khách hàng
- Đơn hàng
- Dashboard thống kê
- QR Code sản phẩm
- Upload ảnh sản phẩm
- API cơ bản
- Giao diện hệ thống

### Chức năng chính

- Đăng nhập / Đăng ký tài khoản
- Quản lý sản phẩm
- Quản lý khách hàng
- Quản lý đơn hàng
- Dashboard thống kê doanh thu
- Sinh QR Code cho sản phẩm
- Upload hình ảnh sản phẩm
- Tìm kiếm và phân trang dữ liệu

### Công nghệ sử dụng
- Python 3.12+
- Flask
- Flask-SQLAlchemy
- SQLite
- Bootstrap 5
- Faker
- Pillow
- QRCode

### Cấu trúc thư mục

```
store-management/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── init_db.py
├── seed.py
│
├── instance/
│   └── store.db
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── product.py
│   ├── customer.py
│   ├── order.py
│   └── order_item.py
│
├── routes/
│   ├── auth_routes.py
│   ├── dashboard_routes.py
│   ├── product_routes.py
│   ├── customer_routes.py
│   ├── order_routes.py
│   └── api_routes.py
│
├── templates/
│
├── static/
│   ├── css/
│   ├── uploads/
│   └── qrcodes/
│
└── utils/
```

### Tạo môi trường ảo (venv)

Windows PowerShell
```
python -3.12 -m venv venv
```

### Kích hoạt venv:
```
.\venv\Scripts\activate
```

### Cài thư viện
```
pip install -r requirements.txt
```

### Khởi tạo database
```
python init_db.py
```

### Tạo dữ liệu giả (Fake Data)

Project có file seed.py để sinh dữ liệu mẫu.

```
python seed.py
```

### Chạy website
```
python app.py
```

### Mở trình duyệt:
```
http://127.0.0.1:5000
```
