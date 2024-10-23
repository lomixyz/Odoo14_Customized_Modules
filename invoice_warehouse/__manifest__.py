{
    'name': 'Invoice Warehouse Show',
    'category': 'Accounting',
    'author': 'Allam Bushra',
    'summary': 'Show User Default Warehouse in Invoices',
    'description': 'Displays the property_warehouse_id from the user preferences in the Invoices form view.',
    'depends': ['account'],
    'data': [
        'views/account_move_view.xml',
    ],
    'installable': True,
    'application': True,
}
