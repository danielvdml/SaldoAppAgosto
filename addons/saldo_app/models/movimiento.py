# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError



class Movimiento(models.Model):
    _name = "sa.movimiento" # sa_movimiento
    name = fields.Char("Movimiento")
    
    monto = fields.Float("Monto")

    tipo = fields.Selection(string="Tipo de Movimiento",selection = [("i","Ingreso"),("e","Egreso")])

    comprobante_pago = fields.Binary("Foto de Comprobante")

    fecha = fields.Date(string="Fecha de Movimiento")

    numero_comprobante = fields.Char(string="Número de Comprobante")
    #regex
    #B***-********
    #F***-********
    #*****@**.***

    categoria_ids = fields.Many2many("sa.categoria",string="Categorias")

    @api.onchange("tipo")
    def _onchange_tipo(self):
        if self.tipo == "i":
            self.name = "Ingreso: "
            self.monto = 100
        elif self.tipo == "e":
            self.name = "Egreso: "
            self.monto = 50

    @api.onchange("numero_comprobante")
    def _onchange_numero_comprobante(self):
        self.numero_comprobante = self.numero_comprobante.upper()

    @api.constrains("numero_comprobante")
    def _valido_numero_comprobante(self):
        n = self.numero_comprobante
        if n.upper()[0] not in ["B","F"]:
            raise UserError("El número de comprobante debe iniciar con 'B' o 'F'.")
