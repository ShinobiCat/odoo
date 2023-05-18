# -*- coding: utf-8 -*-
{
    'name': "x_gelato_connector",
    'version': '0.1',
    'author': 'Croak',
    'license': 'LGPL-3',
    'website': 'https://github.com/ShinobiCat/odoo/tree/16.0/addons/x_gelato_connector',
    'summary': 'Import products and place orders from Odoo to Gelato',
    'description': 'Import products and place orders from Odoo to Gelato',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoicing',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
