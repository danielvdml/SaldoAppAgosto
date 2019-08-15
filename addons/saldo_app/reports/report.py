from odoo import api,models 
import os

class MovimientoReporte(models.AbstractModel):
    _name = "report.saldo_app.sa_report_movimiento"

    @api.model
    def _get_report_values(self,docids,data=None):
        #docids = [5,6,7,10]
        #docids = [2]
        os.system("echo '%s'"%(str(docids)))
        movimientos = self.env["sa.movimiento"].browse(docids)
        def mensaje(nombre):
            return "hola, {}".format(nombre)

        return {
            "titulo":"General",
            "movimientos":movimientos,
            "mensaje":mensaje
        }   