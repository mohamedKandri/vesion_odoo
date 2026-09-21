from odoo import models


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        session_info = super().session_info()
        company = self.env.company
        session_info["startup_branding"] = {
            "name": company.name,
            "tagline": company.tagline or "",
            "primary_color": company.primary_color or "#0b1120",
            "secondary_color": company.secondary_color or "#017e84",
        }
        return session_info
