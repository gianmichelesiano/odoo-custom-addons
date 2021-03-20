# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class HospitalPatiens(models.Model):
    _name = 'hospital.patiens'
    _description = 'Patient Record'
    _rec_name = 'patient_name'


    patient_name = fields.Char(string='Name', required=True)
    patient_age = fields.Integer('Age')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if not vals.get('name_seq') or vals['name_seq'] == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')

        result = super(HospitalPatiens, self).create(vals)
        return result
