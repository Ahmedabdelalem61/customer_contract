{
    'name': 'Customer Contract',
    'summary': " Customers Contract Summmary ",
    'version': '1.0',
    'author': "Itqan Systems",
    'website': "http://www.itqansystems.com",
    'category': 'Customers',
    'depends': ['base',],
    'data': [
        # Security files:
        'security/customer_contract_groups.xml',
        'security/customer_record_access.xml',
        'security/ir.model.access.csv',
        # Data files:

        # Root menu items files:

        # View files:
        'views/customer_contract_views.xml',
        'views/res_partner_view.xml',

        # Menu items files:
    ],
}
