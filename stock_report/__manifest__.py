# -*- coding: utf-8 -*-
{
    'name': "RR Paper - Stock Report",

    'summary': """RR Paper Stock Report""",

    'description': """
    Stock Report
        - Stock Card Report with Lot
    """,

    'author': "Trinity Roots",
    'website': "http://www.trinityroots.co.th",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'jasper_reports',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'templates.xml',
        'wizard/stock_card_report_view.xml',
        'wizard/product_lot_report_view.xml',
    ],
}
