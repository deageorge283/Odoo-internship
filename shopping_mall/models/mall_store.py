from odoo import models, fields

class MallShop(models.Model):
    _name = 'mall.shop'
    _description = 'Shop in Mall'

    name = fields.Char(string='Shop Name', required=True)
    shop_number = fields.Char(string='Shop Number', required=True)
    floor = fields.Selection([('G', 'Ground'), ('1', 'First'), ('2', 'Second')], default='G')
    area_sqft = fields.Float(string='Area (sqft)')
    tenant_id = fields.Many2one('mall.tenant', string='Current Tenant')

