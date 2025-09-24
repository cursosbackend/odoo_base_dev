from odoo import models, fields

class Curso(models.Model):
    _name = 'gestion.curso'
    _description = 'Curso'

    name = fields.Char(string='Nombre del curso', required=True)
    description = fields.Text(string='Descripción')
    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha de término')
    activo = fields.Boolean(string='Activo', default=True)
