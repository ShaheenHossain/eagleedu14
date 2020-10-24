from eagle import fields, models, api, _
from eagle.exceptions import ValidationError
from datetime import datetime

class EagleeduRegister(models.Model):
    _name='eagleedu.register'
    _description='this admission register book'
    name=fields.Char('Register Book Name', compute='get_name')
    class_id=fields.Many2one('eagleedu.class')
    academic_year=fields.Many2one('eagleedu.academic.year', "For the year" , required=True)
    start_time = fields.Datetime(string='Application Starts on',default=lambda self: fields.datetime.now())
    end_time = fields.Datetime(string='Application ends on',default=lambda self: fields.datetime.now())
    active=fields.Boolean('Is active', default='True')
    standard=fields.Many2one('eagleedu.class','Standard', required=True)
    # class_id=fields.Many2one('eagleedu.class','Class Name', required=True)

    # @api.onchange('class_id','academic_year')
    # def get_name(self):
    #     for rec in self:
    #         if rec.class_id and rec.academic_year:
    #             rec.name=rec.class_id.name +'-'+rec.academic_year.name+' '+'Admission'

    # @api.onchange('class_id','academic_year')
    # def get_name(self):
    #     for rec in self:
    #         if rec.class_id and rec.academic_year:
    #             rec.name=rec.class_id.name +'-'+rec.academic_year.name+' '+'Admission'



    @api.onchange('class_id','academic_year')
    def get_name(self):
        for rec in self:
            if rec.standard and rec.academic_year:
                rec.name=rec.standard.name +'-'+rec.academic_year.name+' '+'Admission'