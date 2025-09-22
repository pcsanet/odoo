from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    sunat_estado = fields.Char(string='Estado SUNAT')
    sunat_cdr = fields.Char(string='CDR SUNAT')
    sunat_mensaje = fields.Text(string='Mensaje SUNAT')
    metodo_pago = fields.Selection([
        ('001', 'Depósito en cuenta'),
        ('005', 'Transferencia bancaria'),
        ('008', 'Yape'),
        ('009', 'Plin'),
        ('010', 'Efectivo'),
        ('011', 'Tarjeta de débito'),
        ('012', 'Tarjeta de crédito'),
    ], string='Método de Pago SUNAT', default='010')

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    metodo_pago = fields.Selection(related='move_id.metodo_pago', string='Método de Pago', readonly=False)
    referencia_pago = fields.Char(string='Referencia (Operación/Yape/Plin)')