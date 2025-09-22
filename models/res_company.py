from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    establecimiento_anexo_ids = fields.One2many(
        'pcsa.establecimiento.anexo',
        'company_id',
        string='Establecimientos Anexos'
    )

class PCSAEstablecimientoAnexo(models.Model):
    _name = 'pcsa.establecimiento.anexo'
    _description = 'Establecimiento Anexo SUNAT'

    name = fields.Char(string='Nombre del Local', required=True)
    codigo = fields.Char(string='Código SUNAT', required=True, help="Ej: 0001, 0002")
    direccion = fields.Char(string='Dirección Completa', required=True)
    ubigeo = fields.Char(string='Ubigeo SUNAT', size=6)
    company_id = fields.Many2one('res.company', string='Empresa', default=lambda self: self.env.company)
    active = fields.Boolean(default=True)