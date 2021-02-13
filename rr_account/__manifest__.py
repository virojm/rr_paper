# -*- coding: utf-8 -*-
{
    'name': 'RR Paper Products: Invoicing',
    'version': '0.1',
    'category': 'Accounting',
    'author': 'Viroj, Technisoft Co., Ltd',
    'depends': [
        'account',
    ],
    'data': ['views/account_invoice_view.xml',
    ],
    'installable': True,
    'auto_install': False,

}
    # to add customer order to tree view need to call account module for the field
