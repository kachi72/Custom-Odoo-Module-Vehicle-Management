from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class ParticularInfo(models.Model):
    _name = "particular.info"
    _description = "Information on company vehicles documents"

# fields
    platenumber_id = fields.Many2one(comodel_name='vehicle.info', string='Plate Number')
    document = fields.Selection([
        ('insurance', 'Insurance'),
        ('road worthiness', 'Road Worthiness'),
        ('tinted glass permit', 'Tinted Glass Permit'),
        ('hackney permit', 'Hackney Permit'),
        ('proof of ownership', 'Proof of Ownership'),
        ('vehicle licence', 'Vehicle Licence'),
        ('local government papers', 'Local Government Papers'),
        ('cmr certificate', 'CMR Certificate')
    ], required=True, string='Document Type')
    document_no = fields.Char(string='Document No', required=True)
    expiry_date = fields.Date(string='Expiry Date', required=True)

    @api.constrains('expiry_date')
    def _check_date_not_earlier_than_current_date(self):
        for record in self:
            if record.expiry_date and record.expiry_date < datetime.now().date():
                raise ValidationError("Date cannot be earlier than the current date!")


