from odoo import api,models,fields

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
