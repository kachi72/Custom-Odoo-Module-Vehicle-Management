from odoo import api, fields, models


class VehicleRepair(models.Model):
    _name = 'repairs.info'
    _description = 'Vehicle Repair Information'

#   fields
    platenumber_id = fields.Many2one(comodel_name='vehicle.info', string='Plate Number')
    fault = fields.Selection([
        ('mechanical', 'Mechanical'),
        ('electrical', 'Electrical'),
        ('gear', 'Gear'),
        ('interior', 'Interior'),
        ('external', 'External'),
        ('general servicing', 'General Servicing')], string='Fault', required=True)
    additional_info = fields.Char(string='Fault Info', required=True)
    parts_used = fields.Char(string='Parts Used', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    mechanic = fields.Html(string='Mechanic Info')
    cost = fields.Html(string='Cost Incurred')


