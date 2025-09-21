{
    'name': 'PCSA ERP - Personal Computer Servicios y Análisis EIRL',
    'version': '1.0',
    'summary': 'Sistema CRM/ERP integrado con SUNAT para venta de productos y servicios técnicos',
    'description': """
        Módulo personalizado para PCSA EIRL.
        Incluye:
        - Gestión de clientes, ventas, compras, almacén, contabilidad.
        - Manejo de pagos: efectivo, Yape, Plin, depósito.
        - Servicios técnicos con registro de tiempo.
        - Generación de facturas, boletas, notas, guías de remisión.
        - Integración automática con SUNAT (solo ventas).
        - Multi-establecimiento (anexos).
        - Multi-usuario con niveles de seguridad.
    """,
    'author': 'Desarrollado para PCSA EIRL',
    'website': 'https://pcsa.com.pe',
    'category': 'ERP',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'sale_management',
        'purchase',
        'stock',
        'account',
        'project',
        'hr_timesheet',
    ],
    'data': [
        'security/pcsa_security.xml',
        'security/ir.model.access.csv',
        'data/company_data.xml',
        'data/demo_data.xml',
        'views/res_company_views.xml',
        'views/sale_views.xml',
        'views/purchase_views.xml',
        'views/account_views.xml',
        'views/stock_views.xml',
        'views/project_views.xml',
        'views/menus.xml',
        'report/sale_report.xml',
        'report/guia_remision.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}