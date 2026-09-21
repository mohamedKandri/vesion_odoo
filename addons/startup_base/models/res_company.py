from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    primary_color = fields.Char(default="#714B67")
    secondary_color = fields.Char(default="#017E84")
    tagline = fields.Char()
