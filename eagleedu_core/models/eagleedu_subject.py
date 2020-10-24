# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduSubject(models.Model):
    _name = 'eagleedu.subject'
    _description = "Subject "
    name = fields.Char(string='Subject Name', required = True, help="Enter the Name of the Subject")
    # code = fields.Char(string='Subject Code', compute='set_sub_code', help="Enter the Code of the Subject")
    code = fields.Char(string='Subject Code', required = True, help="Enter the Code of the Subject")
    subjects_ids = fields.Char(string='Subject Code', help="Enter the Code of the Subject")
    subjects_ids = fields.Many2many('eagleedu.subject', 'eagleedu_subject_rel', 'subjects_ids')

    #
    # @api.onchange('name')
    # def set_sub_code(self):
    #     self.code = self.name