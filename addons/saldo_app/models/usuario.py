from odoo import api,models,fields
import os
from odoo.http import request

class Usuario(models.Model):
    _name = "usuario"

    #Char - Cadena de Texto
    name = fields.Char("Nombre",required=True) #Campo Especial - name

    email = fields.Char(string="Correo",index=True)
    password = fields.Char(string="Password")

    #Solo Fecha
    fecha_registro = fields.Date(string="Fecha de Registro")

    #Fecha y Hora
    fecha_registro_hora = fields.Datetime(string="Fecha y hora de registro")

    #Edad
    edad = fields.Integer(string="Edad",default=15)

    #Descripcion texto largo
    descripcion = fields.Text("Descripción")

    #Descripción personalizada en Html
    descripcion_html = fields.Html("Descripción Personalizada")


#Inserción de Nuevos atributos y métodos a la clase res.users
class ResUsers(models.Model):
    _inherit = "res.users"

    edad = fields.Integer("Edad")
    description_html = fields.Html("Descripción Personalizada")

    def ver_mis_movimientos(self):
        view_tree_movimiento_id = self.env.ref("saldo_app.view_tree_movimientos").id

        return {
            "type":"ir.actions.act_window",
            "view_mode":"tree",
            "views_id":[(view_tree_movimiento_id,"tree")],
            "target":"new",
            "res_model":"sa.movimiento",
            "domain":[("create_uid","=",self.env.uid)]
        }
    
        
    def actualizar_datos(self):
        view_form_user_temporal_id = self.env.ref("saldo_app.views_form_usuario_temporal").id

        return {
            "type":"ir.actions.act_window",
            "view_mode":"form",
            "views_id":[(view_form_user_temporal_id,"form")],
            "target":"new",
            "res_model":"sa.usertemporal",
            "context":{"default_edad_x":self.edad,"default_desc_html":self.description_html,"default_res_users_id":self.id}
        }
    
    def ver_mi_perfil(self):
        user_id = self.env.uid
        return {
            "type":"ir.actions.act_window",
            "view_mode":"form",
            "target":"self",
            "res_id": user_id,
            "res_model":"res.users",
            "view_id":self.env.ref("base.view_users_form").id
        }


class UserTemporal(models.TransientModel):
    _name = 'sa.usertemporal'
    _description = 'Usuario Temporal'

    res_users_id = fields.Many2one("res.users",string="Usuario")
    edad_x = fields.Integer("Edad")
    desc_html = fields.Html("Descripción Personalizada")

    def guardar_datos(self):
        self.res_users_id.edad = self.edad_x
        self.res_users_id.description_html = self.desc_html
#Herencia
"""
class ResUsers2(models.Model):
    _inherit = "res.users"
    _name = "res.users2"

    edad = fields.Integer("Edad")
    description_html = fields.Html("Descripción Personalizada")
"""




