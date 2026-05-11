import os

import qrcode


def generate_qr(
    product_id,
    product_name,
    qr_folder
):

    data = f'''
    Product ID: {product_id}
    Product Name: {product_name}
    '''

    qr = qrcode.make(data)

    filename = f'product_{product_id}.png'

    path = os.path.join(
        qr_folder,
        filename
    )

    qr.save(path)

    return filename