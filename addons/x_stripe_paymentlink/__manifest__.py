# -*- coding: utf-8 -*-
{
    'name': "x_stripe_paymentlink",

    'summary': "Provide Stripe payment link at checkout",

    'description': "Provide Stripe payment link at checkout",

    'author': "ShinobiCat",
    'website': "https://github.com/ShinobiCat",

    'category': 'Website',
    'version': '0.1',

    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'auto_install': False,

    'depends': ['base','payment'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
	'views/payment_link.xml',
	'views/product_views.xml',

    ],

    'demo': [
        'demo/demo.xml',
    ],
}
