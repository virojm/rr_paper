# -*- coding: utf-8 -*-
{
    'name': 'RR Paper Products: Order Sales',
    'version': '0.1',
    'category': 'Sales',
    'author': 'Viroj, Technisoft Co., Ltd',
    'depends': [
        'sale_stock',
        'product_sales',
        'sale_order_dates',
    ],
    'data': [
        'views/sale_view.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,

}
