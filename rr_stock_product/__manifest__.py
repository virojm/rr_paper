# -*- coding: utf-8 -*-
{
    'name': 'RR Paper Products: Stock Products',
    'version': '0.1',
    'category': 'Products',
    'author': 'Viroj, Technisoft Co., Ltd',
    'depends': [
        'stock',
        'product_barcode',
    ],
    'data': ['views/product_views.xml',
    ],
    'installable': True,
    'auto_install': False,

}

    # refer to rr_paper.product_barcode to generate barcode when create new item
