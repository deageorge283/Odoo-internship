
{
    'name': 'Pepsico',
    'version': '18.0.0.0',
    'summary': 'This Module is created for food industry Pepsico',
    'description': """ This Module is for training purposes.
    """,
    'category':'',
    'author': ' Dea George',
    'website': 'www.zbeanztech.com',
    "license": "LGPL-3",
    'depends': ['sale','product'],
    'data': [
               
                'security/pepsico_security.xml',
                'security/ir.model.access.csv',
                'views/pepsico_view.xml',
                'views/pepsico_menu.xml'


        ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
