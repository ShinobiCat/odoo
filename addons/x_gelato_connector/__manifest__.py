{
    'name': 'Gelato Connector',
    'version': '0.1',
    'author': 'ShinobiCat',
    'license': 'LGPL-3',
    'website': 'https://github.com/ShinobiCat',
    'category': 'Extra Tools',
    'summary': 'Odoo app to import products from Gelato and place orders with Gelato',
    'description': 'Odoo app to import products from Gelato and place orders with Gelato',
    'depends': ['base', 'sale_management'],
    'data': [
    #    'security/ir.model.access.csv',
        'views/gelato_product_view.xml',
        'views/gelato_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
