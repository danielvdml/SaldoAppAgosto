# -*- coding: utf-8 -*-
from odoo import fields,api,models


class MovimientoReportWizard(models.TransientModel):
    _name = 'movimiento.report.wizard'

    fecha_inicio = fields.Date("Fecha de inicio")
    fecha_fin = fields.Date("Fecha Fin")
    tipo_movimiento = fields.Selection(selection = [("i","Ingreso"),("e","Egreso"),("a","Ambos")])

    def menu_reporte_movimientos(self):
        view_form = self.env.ref("saldo_app.view_form_movimiento_report_wizard")
        return {
            "type":"ir.actions.act_window",
            "res_model":"movimiento.report.wizard",
            "view_id":view_form.id,
            "view_mode":"form",
            "target":"new"
        }
    
    def imprimir_reporte(self):
        report_obj = self.env.ref("saldo_app.sa_report_movimiento_report")
        #Plantilla del reporte html
        #report = report_obj._get_report_from_name("saldo_app.sa_report_movimiento")
        #Datos que se van a colocar en el reporte
        tipo_movimientos = []
        if self.tipo_movimiento == 'i':
            tipo_movimientos.append("i")
        elif self.tipo_movimiento == 'e':
            tipo_movimientos.append("e")
        elif self.tipo_movimiento == 'a':
            tipo_movimientos.append("i")
            tipo_movimientos.append("e")

        movimientos = self.env["sa.movimiento"].search([
                ["fecha",">=",self.fecha_inicio],
                ["fecha","<",self.fecha_fin],
                ["tipo","in",tipo_movimientos]])
        
        return report_obj.report_action(movimientos)
