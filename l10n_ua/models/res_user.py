# -*- coding: utf-8 -*-

from odoo import fields, models


class Users(models.Model):
    _inherit = "res.users"

    facsimile = fields.Binary(string='Facsimile')
