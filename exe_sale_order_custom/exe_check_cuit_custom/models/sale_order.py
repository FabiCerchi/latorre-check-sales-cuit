# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.depends('partner_id.l10n_latam_identification_type_id')
    def _check_cuit_partner(self):
        tieneCuit = True if self.partner_id.l10n_latam_identification_type_id.name == 'CUIT' else False
        esCuitValido = True if len(self.partner_id.vat) > 0 else False
        self.check_cuit = True if tieneCuit and esCuitValido else False

    check_cuit = fields.Boolean('CUIT', compute='_check_cuit_partner', default = False)