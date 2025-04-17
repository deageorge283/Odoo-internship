from odoo import models, fields

class Pepsico(models.Model):
    _name = "pepsico"
    _description = "PepsiCo Sales Record"

    name = fields.Char(string="Distributor Name", required=True)
    region = fields.Selection([('north', 'North'),('south', 'South'),('east', 'East'),('west', 'West')], string="Sales Region", required=True)
    sale_date = fields.Date(string="Sale Date")
    active = fields.Boolean(string="Active", default=True)
    total_order_value = fields.Float(string="Order Value")
    notes = fields.Text(string="Additional Notes")
    product_ids = fields.Many2many('product.product','pepsico_sales_product_rel','sales_id', 'product_id',string="Products Sold")
    partner_id = fields.Many2one('res.partner', string="Distributor Contact")
    sale_order_ref = fields.Many2one('sale.order', string="Related Sale Order")
    







