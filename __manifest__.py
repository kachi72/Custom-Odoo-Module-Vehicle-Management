{
    'name': "Vehicle Management",
    'version': '1.0',
    'depends': ['base'],
    'sequence': -100,
    'summary': "Management of company vehicles and vehicle documents",
    'description': '''Management of Company Vehicles''',
    'author': "Systemtech Services Limited",
    'category': 'Inventory',
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/vehicle_view.xml',
        'views/particulars_view.xml',
        'views/repairs_view.xml',
        'views/brands_view.xml'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'

}