from odoo import api, fields, models


class VehicleBrand(models.Model):
    _name = "vehicle.brand"
    _description = "Vehicle Brand"

#   fields
    brand_name = fields.Char(string="Brand", required=True, index=True)

