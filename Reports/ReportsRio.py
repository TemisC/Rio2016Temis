# -*- coding: utf-8 -*-

from openerp.report import report_sxw
from openerp.osv import osv

class reportes_atletas(report_sxw.rml_parse):
    def __init__(self,cr,uid,name,context):
        super(reportes_atletas,self).__init__(cr,uid,name,context)

class reporte_atleta(osv.AbstractModel):
    _name="report.rio.atleta_rio"
    _inherit="report.abstract_report"
    _template="rio.atleta_rio"
    _wrapped_report_class=reportes_atletas