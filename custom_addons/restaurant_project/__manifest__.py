# -*- coding: utf-8 -*-
{
    'name': "Restaurant Project",
    'version' : "15.0.1",

    'summary': """Restaurant Project will help in the management of Restaurant""",
    'sequence' : -101,

    'description': """Manage All Data In your Description""",
    # Categories can be used to filter modules in modules listing
    'category': 'Learn',


    'author': "My Company",
    'website': "http://www.yourcompany.com",
     # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/staff_views.xml',
        'views/menu_views.xml',
        'views/sale_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license' : 'LGPL-3',
}
