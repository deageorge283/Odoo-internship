
from odoo import models, fields

class ModelOne(models.Model):
	
	_name = "model.one"
	_description = "Model One"
	
	name = fields.Char(string="Name", help='A normal name field')
	age = fields.Integer(string="Age")
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
	active = fields.Boolean('Active')
	description = fields.Text("Description")
	date = fields.Date("Date")
	partner_ids = fields.Many2many('res.partner',string="Partner")
	product_ids = fields.Many2many('product.template', 'model_one_product_rel', 'model_one_id', 'product_id',  string="Products")
	model_one_line_ids = fields.One2many('model.one.lines', 'model_one_id',  string="Products")
	sale_id = fields.Many2one('sale.order', string="Sales")

class ModelOneLines(models.Model):
	
	_name = "model.one.lines"
	_description = "Model One Lines"
	
	name = fields.Char(string="Name", help='You can add your name here')
	price = fields.Float(string="Price")
	product_id = fields.Many2one('product.template', string="Product")
	model_one_id = fields.Many2one('model.one', string="Model One", domain="['|', ('gender', '=', 'female'),('age', '>', 18)]")
