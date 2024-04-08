from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class VehicleInfo(models.Model):
    _name = "vehicle.info"
    _description = "Information on company vehicles"

# fields
    platenumber = fields.Char(string='Plate number', required=True)
    colour = fields.Char(string="Car Colour", required=True)
    brand = fields.Char(string="Vehicle Brand", required=True)
    model = fields.Char(string='Car Model', required=True)
    model_year = fields.Char(string="Model Year")
    car_type = fields.Selection([
        ('pickup', 'Pickup'),
        ('minivan', 'Minivan'),
        ('sedan', 'Sedan'),
        ('subcompact', 'Subcompact')], string='Car Type', required=True)
    miles = fields.Integer(string='Distance Covered(Miles)', required=True)
    date_of_purchase = fields.Date(string="Purchased Date")

    @api.constrains('miles')
    def _check_miles_not_negative(self):
        for record in self:
            if record.miles < 0:
                raise ValidationError("Miles cannot be negative!")

    @api.constrains('date_of_purchase')
    def _check_date_not_earlier_than_current_date(self):
        for record in self:
            if record.date_of_purchase and record.date_of_purchase < datetime.now().date():
                raise ValidationError("Date cannot be earlier than the current date!")

# Override the name_get method to display Platenumber in the Many2one dropdown list
    def name_get(self):
        result = []
        for record in self:
            name = record.platenumber
            result.append((record.id, name))
        return result

