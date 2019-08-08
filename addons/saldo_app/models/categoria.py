from odoo import api,fields,models

class Categoria(models.Model):
    _name = "sa.categoria"
    _description = "Categoria"

    name = fields.Char(string="Categoria")
    