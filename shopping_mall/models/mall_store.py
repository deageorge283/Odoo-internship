from odoo import models, fields

class MallStore(models.Model):
    _name = 'mall.store'
    _description = 'Mall Store / Tenant Info'
    _rec_name = 'name'  # optional: tells Odoo which field to display as the record name

    name = fields.Char(string='Store Name', required=True)
    store_type = fields.Selection([
        ('retail', 'Retail'),
        ('fnb', 'Food and Beverage'),
        ('entertainment', 'Entertainment'),
        ('services', 'Services')
    ], string='Store Type', required=True)

    tenant_name = fields.Char(string='Tenant Name', required=True)
    category = fields.Char(string='Category')
    lease_start = fields.Date(string='Lease Start Date')
    lease_end = fields.Date(string='Lease End Date')

    open_time = fields.Float(string='Opening Hour')   # 9.5 = 9:30 AM
    close_time = fields.Float(string='Closing Hour')  # 21.0 = 9:00 PM

    contact_person = fields.Char(string='Contact Person')
    contact_phone = fields.Char(string='Phone')
    contact_email = fields.Char(string='Email')

    rent_type = fields.Selection([
        ('fixed', 'Fixed Monthly Rent'),
        ('variable', 'Variable (Sales Based)')
    ], string='Rent Type', required=True)

    rent_amount = fields.Float(string='Monthly Rent (if Fixed)')
    sales_percentage = fields.Float(string='Sales % (if Variable)')

