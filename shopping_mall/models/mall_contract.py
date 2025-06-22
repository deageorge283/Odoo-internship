from odoo import models, fields, api
from datetime import date

class MallContract(models.Model):
    _name = 'mall.contract'
    _description = 'Lease Contract'

    name = fields.Char(string='Contract ID', required=True, default=lambda self: self.env['ir.sequence'].next_by_code('mall.contract'))
    tenant_id = fields.Many2one('mall.tenant', string='Tenant', required=True)
    shop_id = fields.Many2one('mall.shop', string='Shop', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date')
    rent_amount = fields.Float(string='Monthly Rent')
