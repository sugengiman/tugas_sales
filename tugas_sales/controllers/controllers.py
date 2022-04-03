# -*- coding: utf-8 -*-
# from odoo import http


# class ModelKosongan(http.Controller):
#     @http.route('/_model_kosongan/_model_kosongan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/_model_kosongan/_model_kosongan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('_model_kosongan.listing', {
#             'root': '/_model_kosongan/_model_kosongan',
#             'objects': http.request.env['_model_kosongan._model_kosongan'].search([]),
#         })

#     @http.route('/_model_kosongan/_model_kosongan/objects/<model("_model_kosongan._model_kosongan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('_model_kosongan.object', {
#             'object': obj
#         })
