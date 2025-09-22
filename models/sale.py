from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    es_proforma = fields.Boolean(string='Es Proforma', default=False)
    establecimiento_id = fields.Many2one('pcsa.establecimiento.anexo', string='Establecimiento Emisor')
    enviar_a_sunat = fields.Boolean(string='Enviar a SUNAT al confirmar', default=True)

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.enviar_a_sunat and not order.es_proforma:
                invoice = order._create_invoices()
                if invoice:
                    invoice.action_post()
                    # Simular envío a SUNAT
                    self.env['sunat.integration'].simulate_send_invoice(invoice.id)
        return res