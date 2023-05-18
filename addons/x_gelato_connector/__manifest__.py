{
    'name': 'Odoo Gelato Connector',
    'version': '0.1',
    'author': 'Croak',
    'license': 'LGPL-3',
    'website': 'https://github.com/ShinobiCat/odoo/tree/16.0/addons/x_gelato_connector',
    'category': 'Extra Tools',
    'summary': 'Import products and place orders from Odoo to Gelato',
    'description': 'Import products and place orders from Odoo to Gelato',
    'depends': ['account', 'sale', 'sale_management', 'website', 'website_sale'],
    'data': [
        'views/gelato_product_view.xml',
        'views/gelato_order_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
