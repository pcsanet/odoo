from odoo import http
from odoo.http import request
import json

class SunatAPIController(http.Controller):

    @http.route('/web/ping_sunat', type='json', auth='user')
    def ping_sunat(self, invoice_id=None):
        if not invoice_id:
            return {'error': 'No se envió ID de factura'}

        result = request.env['sunat.integration'].simulate_send_invoice(invoice_id)
        return {'success': result}