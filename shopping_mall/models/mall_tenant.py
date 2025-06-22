from odoo import models, fields

class MallTenant(models.Model):
    _name = 'mall.tenant'
    _description = 'Tenant (Shop Owner)'

    name = fields.Char(string='Tenant Name', required=True)
    contact = fields.Char(string='Contact Number')
    email = fields.Char(string='Email')
    shop_ids = fields.One2many('mall.shop','tenant_id', string='Shops')
