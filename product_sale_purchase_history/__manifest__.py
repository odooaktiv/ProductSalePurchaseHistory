# © 2018-Today Aktiv Software (http://www.aktivsoftware.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Product Sale Purchase History',
    'version': '12.0.1.0.0',
    'description': '''
        This module will show the Sales and purchase history of products.
    ''',
    'category': 'Sales',
    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'depends': ['sale_management', 'purchase'],
    'data': [
        'views/product_views.xml'
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
