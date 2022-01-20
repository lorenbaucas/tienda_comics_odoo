# -*- coding: utf-8 -*-
# from odoo import http


# class TiendaComicsOdoo(http.Controller):
#     @http.route('/tienda_comics_odoo/tienda_comics_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tienda_comics_odoo/tienda_comics_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tienda_comics_odoo.listing', {
#             'root': '/tienda_comics_odoo/tienda_comics_odoo',
#             'objects': http.request.env['tienda_comics_odoo.tienda_comics_odoo'].search([]),
#         })

#     @http.route('/tienda_comics_odoo/tienda_comics_odoo/objects/<model("tienda_comics_odoo.tienda_comics_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tienda_comics_odoo.object', {
#             'object': obj
#         })
