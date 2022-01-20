from odoo import models, fields, api


class tienda(models.Model):
    _name = 'tienda_comics_odoo.tienda'
    _description = 'model tienda'

    name = fields.Char('Nombre',required=True)
    calle = fields.Char(String='Calle',required=True)

class comic(models.Model):
    _name = 'tienda_comics_odoo.comic'
    _description = 'model comic'

    name = fields.Char('Nombre',required=True)
    isbn = fields.Char(String='ISBN',required=True)
    precio = fields.Char(String='Precio',required=True)

class cliente(models.Model):
    _name = 'tienda_comics_odoo.cliente'
    _description = 'model cliente'

    name = fields.Char('Nombre',required=True)
    dni = fields.Char(String='DNI',required=True)
