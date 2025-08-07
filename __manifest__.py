{
    'name': 'Cotización Producción - Ocultar Precios',
    'version': '1.0',
    'summary': 'Reporte de cotización para producción sin mostrar precios',
    'description': 'Duplicado del reporte de cotizaciones de sale.order, manteniendo sólo producto, descripción, cantidad, unidad y fechas.',
    'author': '',
    'depends': ['sale'],
    'data': [
        'report/sale_cotizacion_produccion_report.xml',
        'views/sale_cotizacion_produccion_views.xml', 
    ],
    'installable': True,
    'application': False,
}
