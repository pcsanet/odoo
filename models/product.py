from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tipo_sunat = fields.Selection([
        ('producto', 'Producto'),
        ('servicio', 'Servicio'),
    ], string='Tipo SUNAT', default='producto')