from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    tipo_servicio = fields.Selection([
        ('mantenimiento', 'Mantenimiento Preventivo'),
        ('reparacion', 'Reparación Correctiva'),
        ('instalacion', 'Instalación de Software/Hardware'),
    ], string='Tipo de Servicio')

    equipo_cliente = fields.Char(string='Equipo del Cliente')
    diagnostico = fields.Text(string='Diagnóstico Inicial')
    solucion = fields.Text(string='Solución Aplicada')
    horas_trabajadas = fields.Float(string='Horas Trabajadas', default=1.0)
    proforma_id = fields.Many2one('sale.order', string='Proforma Asociada')

    def action_generar_proforma(self):
        self.ensure_one()
        proforma = self.env['sale.order'].create({
            'partner_id': self.partner_id.id,
            'client_order_ref': f"PROFORMA-SERV-{self.id}",
            'order_line': [(0, 0, {
                'product_id': self.env.ref('pcsa_erp.product_servicio_tecnico').id,
                'product_uom_qty': self.horas_trabajadas,
                'price_unit': 50.0,  # Precio por hora
            })],
        })
        self.proforma_id = proforma.id
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'res_id': proforma.id,
            'view_mode': 'form',
            'target': 'current',
        }