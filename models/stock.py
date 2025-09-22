from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    guia_remision = fields.Char(string='Nro. Guía Remisión SUNAT')
    motivo_traslado = fields.Selection([
        ('01', 'Venta'),
        ('02', 'Compra'),
        ('13', 'Traslado entre establecimientos'),
    ], string='Motivo de Traslado', default='01')
    establecimiento_origen_id = fields.Many2one('pcsa.establecimiento.anexo', string='Establecimiento Origen')
    establecimiento_destino_id = fields.Many2one('pcsa.establecimiento.anexo', string='Establecimiento Destino')