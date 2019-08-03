# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Movimiento(models.Model):
    _name = "sa.movimiento" # sa_movimiento
    name = fields.Char("Movimiento")
    
    monto = fields.Float("Monto")

    tipo = fields.Selection(string="Tipo de Movimiento",selection = [("i","Ingreso"),("e","Egreso")])