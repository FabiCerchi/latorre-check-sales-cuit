# -*- coding: utf-8 -*-
# from odoo import http


# class ExeSaleOrderCustom(http.Controller):
#     @http.route('/exe_sale_order_custom/exe_sale_order_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exe_sale_order_custom/exe_sale_order_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exe_sale_order_custom.listing', {
#             'root': '/exe_sale_order_custom/exe_sale_order_custom',
#             'objects': http.request.env['exe_sale_order_custom.exe_sale_order_custom'].search([]),
#         })

#     @http.route('/exe_sale_order_custom/exe_sale_order_custom/objects/<model("exe_sale_order_custom.exe_sale_order_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exe_sale_order_custom.object', {
#             'object': obj
#         })
