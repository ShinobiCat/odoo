{
    'name': 'Plant Nursery',
    'version': '1.0',
    'author': 'Croak',
    'license': 'LGPL-3',
    'website': 'https://github.com/ShinobiCat/odoo/tree/16.0/addons/x_gelato_connector',
    'category': 'Tools',
    'summary': 'Import products and place orders from Odoo to Gelato',
    'description': 'Import products and place orders from Odoo to Gelato',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
