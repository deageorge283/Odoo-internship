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
    'data': [
             'security/security.xml',
             'security/ir.model.access.csv',
             'views/mall_store_view.xml',
             'views/mall_tenant_view.xml',
             'views/mall_contract_view.xml',
             'views/menu.xml',

        ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
