# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError



class Movimiento(models.Model):
    _name = "sa.movimiento" # sa_movimiento
    
    _inherit = ['mail.thread']
    
    name = fields.Char("Movimiento")
    
    monto = fields.Float("Monto",track_visibility='onchange')

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
        if type(self.numero_comprobante) == str:
            self.numero_comprobante = self.numero_comprobante.upper()

    @api.constrains("numero_comprobante")
    def _valido_numero_comprobante(self):
        n = self.numero_comprobante
        if n.upper()[0] not in ["B","F"]:
            raise UserError("El número de comprobante debe iniciar con 'B' o 'F'.")


    @api.multi
    def listar_nombre_de_movimientos(self):
        #self ->26,28,29
        d = [(record.name,record.monto) for record in self]
        return d
    
    
    def crear(self,values,categorias):
        if "tipo" in values and "name" in values:
            if values["tipo"] == "i":
                values.update({"name":"Ingreso: "+values["name"]})
            if values["tipo"] == "e":
                values.update({"name":"Egreso: "+values["name"]})

        
        #values.update({"categoria_ids":[categoria_id.id]})
        result = self.env["sa.movimiento"].create(values)
        categs = []

        for categoria in categorias:
            categoria_id = self.env["sa.categoria"].search([["name","=",categoria]])
            if not categoria_id.exists():
                categoria_id = self.env["sa.categoria"].create({"name":categoria})
            categs.append(categoria_id.id)

        result.categoria_ids = [(6,0,categs)]
        return {"id":result.id,"name":result.name}


    