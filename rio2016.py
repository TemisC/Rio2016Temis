# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2016 Temis CAstillo
# contact: temiscastillo@yahoo.es

######################################################################

from openerp import tools, api
from openerp.osv import fields, osv, orm
from datetime import time, datetime
from openerp.tools.translate import _


class rio2016_modelo(osv.osv):
    _name = 'rio2016.modelo'
    _description = 'Formulario de Atletas'

    def _sumar_medallas(self,cr,user,ids, gold, plata, bronce, context=None):
        total = gold + plata + bronce
        res = {
            'value': {# This sets the total price on the field standard_price.
                'total_M': total}}
        # Return the values to update it in the view.
        return res

    _columns = {
        # Campo oblidatorio para buscar , readonly = True
        'name': fields.char('Nombre', size=50, required=True, help='Este es el nombre'),
        'age' : fields.integer('Edad', size=50, required=True),
        'pais_id': fields.many2one('paises.modelo', 'Pais', required=True, select=True),
        'gold': fields.integer('Medalla de Oro', required=True),
        'plata': fields.integer('Medalla de Plata', required=True),
        'bronce': fields.integer('Medalla de Bronce', required=True),
        'total_M': fields.integer("Total medallas" , required=True ),
        # 'escuela_id': fields.many2one('product.template','Escuela', required=True),
        # utilizamos los socios de negocios
        # 'usuario_id' : fields.many2one('res.partner','Usuario' , required=True),
        # Campo para activar el registro es necesario
        'active': fields.boolean('Activo'),
        'state': fields.selection([('draft', 'Borrador'), ('confirmed', 'Confirmado'), ('cancel', 'Cancelado')]),
    }
    _defaults = {
        # 'state' : 'draft',
        'active': 'true',
    }

    def pulsar_pais(self, cr, ids, context=None):
        return {'value': {'name': '', 'gold': '', 'plata': '', 'bronce': ''}}


rio2016_modelo()


class paises_modelo(osv.osv):
    _name = 'paises.modelo'
    _description = 'Formulario de paises'

    _columns = {
        'image' : fields.binary("Image", attachment=True,
                              help="Flag of country, limited to 1024x1024px"),

        'name': fields.char('Nombre Pais', size=100),
        'continent': fields.char('Continente', size=100),
        'active': fields.boolean('Activo'),
        'pais_desarrollado': fields.boolean('Pais es Desarrollado'),
        'ciudades_ids': fields.one2many('ciudades.lines', 'ciudad_id', 'Ciudades'),

    }
    _defaults = {
        # 'state' : 'draft',
        'active': 'true',
        # 'pais_desarrollado': 'false',
    }


paises_modelo()


class ciudades_lines(osv.osv):
    _name = 'ciudades.lines'
    _description = 'Ciudades'
    _columns = {
        'ciudad_id': fields.many2one('paises.modelo', 'idreferencia'),
        'name': fields.char('Nombre de Ciudad', size=100),
        'poblacion': fields.integer('Poblacion', required=True),
        'ciudad_capital': fields.boolean('Es ciudad Capital?'),
        # 'flag':fields.image('Bandera'),
        # 'ciudades_ids':fields.one2many('ciudades.lines','paises_id','Ciudades')
    }
    _defaults = {

    }


ciudades_lines()
