{
    'name': 'Tabs Building Block',
    'category': 'Website',
    'summary': 'Tabs Building Block',
    'version': '1.0',
    'description': """
Tabs Building Block for Odoo CMS
======================================
This custom module adds tabs building block to Odoo CMS.
        """,
    'author': 'Nedas Žilinskas <nedas.zilinskas@gmail.com>',
    'depends': ['website'],
    'data': [
        'views/assets.xml',
        'views/snippet.xml'
    ],
    'installable': True
}
