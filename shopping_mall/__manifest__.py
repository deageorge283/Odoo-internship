{
    'name': 'shopping mall',
    'version': '18.0.0.0',
    'summary': 'This Module is for training purpose of internship',
    'description': """ This Module is for training purposes.
    """,
    'category':'',
    'author': ' Zesty Beanz',
    'website': 'www.zbeanztech.com',
    "license": "LGPL-3",
    'depends': ['sale','product'],
    'data': ['security/ir.model.access.csv',
             'security/security.xml',
             'views/mall_store_view.xml',
             'views/menu.xml',

        ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
