{
    'name': 'User languages',
    'description': 'personal languages of user',
    'author': 'Klimets',
    'data': [
        'views/mo_user_languages_views.xml',
        'views/mo_translate_languages_views.xml',
        'views/mo_product_view.xml',
    ],
    'depends': ['base', 'product', 'stock'],
    'application': True,
    'installable': True,
    'auto_install': True,
}