from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    primary_color = fields.Char(related="company_id.primary_color", readonly=False)
    secondary_color = fields.Char(related="company_id.secondary_color", readonly=False)
    tagline = fields.Char(related="company_id.tagline", readonly=False)
