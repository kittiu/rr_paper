# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        domain=[('customer', '=', True)],
    )
