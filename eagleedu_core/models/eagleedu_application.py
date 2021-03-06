# -*- coding: utf-8 -*-

from eagle import models, fields, api, _
from eagle.exceptions import UserError
from eagle.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


class EagleeduApplication(models.Model):
    _name = 'eagleedu.application'
    _description = 'This is Student Application Form'
    # _order = 'id desc'
    _inherit = ['mail.thread']

    application_no = fields.Char(string='Application No.', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    application_date = fields.Datetime('Application Date', default=lambda self: fields.datetime.now())  # , default=fields.Datetime.now, required=True
    name = fields.Char(string='Student Name', required=True, help="Enter Name of Student")
    st_name_b = fields.Char(string='Student Bangla Name')
    st_image = fields.Binary(string='Image', help="Provide the image of the Student")
    st_father_name = fields.Char(string="Father's Name", help="Proud to say my father is", required=False)
    st_father_name_b = fields.Char(string="বাবার নাম", help="Proud to say my father is")
    st_father_occupation = fields.Char(string="Father's Occupation", help="father Occupation")
    st_father_email = fields.Char(string="Father's Email", help="father Occupation")
    father_mobile = fields.Char(string="Father's Mobile No", help="Father's Mobile No")
    st_mother_name = fields.Char(string="Mother's Name", help="Proud to say my mother is", required=False)
    st_mother_name_b = fields.Char(string="মা এর নাম", help="Proud to say my mother is")
    st_mother_occupation = fields.Char(string="Mother Occupation", help="Proud to say my mother is")
    st_mother_email = fields.Char(string="Mother Email", help="Proud to say my mother is")
    mother_mobile = fields.Char(string="Mother's Mobile No", help="mother's Mobile No")
    date_of_birth = fields.Date(string="Date Of birth", help="Enter your DOB")
    age = fields.Char(compute="get_student_age", string="Age", store=True, help="Enter your DOB")
    st_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                                string='Gender', required=False, track_visibility='onchange', help="Your Gender is ")
    st_blood_group = fields.Selection([('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('o+', 'O+'), ('o-', 'O-'),
                                    ('ab-', 'AB-'), ('ab+', 'AB+')], string='Blood Group', track_visibility='onchange', help="Your Blood Group is ")
    st_passport_no = fields.Char(string="Passport No.", help="Proud to say my father is", required=False)
    nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict',default=19, help="Select the Nationality")
    academic_year = fields.Many2one('eagleedu.academic.year', string='Academic Year',  help="Choose Academic year for which the admission is choosing")
    register_id = fields.Many2one('eagleedu.register', string="Admission Register", required=True, help="Enter the admission register Name")
    import_id=fields.Many2one('eagleedu.import.previous.student', string="Import Student")

# todo all Name in bangla unicode should auto fill and translate to bangla language
    # for translate in unicode
    # @api.onchange('name')
    # def set_st_name_b(self):
    #     self.st_name_b = self.name
    #



    #
    # @api.model
    # def create(self, vals):
    #     record = super(IrTranslation, self).create(vals)
    #     name = vals.get('name', False)  # name of the field to translate
    #     lang = vals.get('lang', False)  # creating record for this language
    #     if 'context' in dir(self.env):
    #         cur_lang = self.env.context.get('lang', False)  # current used language
    #         if name == 'eagleedu.application,st_father_name_b' and lang == cur_lang:
    #             langs = self.env['ir.translation']._get_languages()
    #             langs = [l[0] for l in langs if l[0] != cur_lang]  # installed languages
    #
    #             for l in langs:
    #                 if self.env.eagleedu.application.st_father_name_b:
    #                     t = self.env['ir.translation'].search([
    #                         ('lang', '=', l),
    #                         ('type', '=', 'model'),
    #                         ('name', '=', 'eagleedu.application,st_father_name_b')
    #                     ])
    #                     if t:
    #                         self.env['ir.translation'].create({
    #                             'lang': l,
    #                             'type': 'model',
    #                             'name': 'eagleedu.application,st_father_name_b',
    #                             'res_id': record.res_id,
    #                             'src': record.src,
    #                             'value': t.value,
    #                             'state': 'translated',
    #                         })
    #









    # def _get_default_ay(self, cr, uid, context=None):
    #     res = self.pool.get('eagleedu.academic.year').search(cr, uid, [('name', '=', academic_year)], context=context)
    #     return
    #     return res and res[0] or False
    #
    #
    # _defaults = {
    #     'academic_year': _get_default_ay,
    # }


    # user_id = fields.Many2one('res.users', 'User', default=lambda self: self.env.user)
    # application_date = fields.Datetime('Application Date', default=lambda self: fields.datetime.now())  # , default=fields.Datetime.now, required=True

    # self.env.ref('module_name.reference_record_id').id

    house_no = fields.Char(string='House No.', help="Enter the House No.")
    road_no = fields.Char(string='Area/Road No.', help="Enter the Area or Road No.")
    post_office = fields.Char(string='Post Office', help="Enter the Post Office Name")
    city = fields.Char(string='City', help="Enter the City name")
    bd_division_id = fields.Many2one('eagleedu.bddivision', string= 'State / Division')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',default=19, help="Select the Country")
    if_same_address = fields.Boolean(string="Permanent Address same as above", default=True, help="Tick the field if the Present and permanent address is same")
    per_village = fields.Char(string='Village Name', help="Enter the Village Name")
    per_po = fields.Char(string='Post Office Name', help="Enter the Post office Name ")
    per_ps = fields.Char(string='Police Station', help="Enter the Police Station Name")
    per_dist_id = fields.Many2one('eagleedu.bddistrict', string='District', help="Enter the City of District name")
    per_bd_division_id = fields.Many2one('eagleedu.bddivision', string='State / Division', help="Enter the City of District name")
    per_country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', default=19, help="Select the Country")
    guardian_name = fields.Char(string="Guardian's Name", help="Proud to say my guardian is")
    guardian_relation = fields.Many2one('eagleedu.guardian.relation', string="Relation to Guardian", help="Tell us the Relation toyour guardian")
    guardian_mobile = fields.Char(string="guardian's Mobile No", help="guardian's Mobile No")
    religious_id = fields.Many2one('eagleedu.religious', string="Religious", help="My Religion is ")
    class_id = fields.Many2one('eagleedu.class')
    academic_year_id = fields.Many2one('eagleedu.academic.year', related='register_id.academic_year',string='Academic Year',
                                       help="Choose Academic year for which the admission is choosing")
    #academic_year = fields.Many2one('eagleedu.academic.year', string='Academic Year')
    group_division = fields.Many2one('eagleedu.group_division')
    student_id=fields.Char('Student Id')
    roll_no = fields.Integer('Roll No')
    section=fields.Char('Section')
    state = fields.Selection([('draft', 'Draft'), ('verification', 'Verify'), ('approve', 'Approve'), ('done', 'Done')],
                              string='Status', required=True, default='draft', track_visibility='onchange')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)
    email = fields.Char(string="Student Email", help="Enter E-mail id for contact purpose")
    phone = fields.Char(string="Student Phone", help="Enter Phone no. for contact purpose")
    mobile = fields.Char(string="Student Mobile", help="Enter Mobile num for contact purpose")
    #nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict',default=19,
    #                              help="Select the Nationality")

    verified_by = fields.Many2one('res.users', string='Verified by', help="The Document is verified by")

    @api.onchange('guardian_relation')
    def guardian_relation_changed(self):
        for rec in self:
            if rec.guardian_relation.name:
                if  rec.guardian_relation.name=='Father':
                    rec.guardian_mobile=rec.father_mobile
                    rec.guardian_name=rec.st_father_name
                elif  rec.guardian_relation.name=='Mother':
                    rec.guardian_mobile = rec.mother_mobile
                    rec.guardian_name = rec.st_mother_name



    # @api.depends('application_no', 'application_no.birthday', 'application_date')
    @api.depends('date_of_birth', 'application_date')
    def get_student_age(self):
        for rec in self:
            age = ''
            if rec.date_of_birth:
                end_data = rec.application_date or fields.Datetime.now()
                delta = relativedelta(end_data, rec.date_of_birth)
                if delta.years <= 25:
                    age = str(delta.years) + _(" Years  ") + str(delta.months) + _(" Month  ") + str(delta.days) + _(
                        " Days")
                else:
                    age = str(delta.years) + _(" Year")
            rec.age = age



    @api.model
    def create(self, vals):
        """Overriding the create method and assigning the the sequence for the record"""
        if vals.get('application_no', _('New')) == _('New'):
            vals['application_no'] = self.env['ir.sequence'].next_by_code('eagleedu.application') or _('New')
        res = super(EagleeduApplication, self).create(vals)
        return res

#    @api.model
    def send_to_verify(self):
        """Return the state to done if the documents are perfect"""
        for rec in self:
            rec.write({
                'state': 'verification'
            })


#    @api.model
    def application_verify(self):
        """Return the state to done if the documents are perfect"""
        for rec in self:
            rec.write({
                'state': 'approve'
            })

#todo show group division when select the class 1 to 8 only
    # def group_division_show(self):
    #     """Return the state to done if the documents are perfect"""
    #     for rec in self:
    #         rec.write({
    #             'state': 'approve'
    #         })


    # def get_group_name_auto(self):
    #     for rec in self:
    #         rec.name = str(rec.admitted_class.name) + '(Assign on ' + str(rec.assign_date) +')'
    #         #rec.name = rec.admitted_class.name #+ '(assigned on '+ rec.assign_date +')'


#    @api.model
    def create_student(self):
        """Create student from the application and data and return the student"""
        for rec in self:
            values = {
                'name': rec.name,
                'st_name_b': rec.st_name_b,
                'st_image': rec.st_image,
                'application_no': rec.id,
                'st_father_name': rec.st_father_name,
                'st_father_name_b': rec.st_father_name_b,
                'father_mobile': rec.father_mobile,
                'st_father_occupation': rec.st_father_occupation,
                'st_mother_name': rec.st_mother_name,
                'st_mother_name_b': rec.st_mother_name_b,
                'mother_mobile': rec.mother_mobile,
                'st_mother_occupation': rec.st_mother_occupation,
                'st_gender': rec.st_gender,
                'date_of_birth': rec.date_of_birth,
                'st_blood_group': rec.st_blood_group,
                'st_passport_no': rec.st_passport_no,
                'nationality': rec.nationality.id,
                'academic_year': rec.academic_year.id,
                'class_id': rec.class_id.id,
                'admission_class': rec.register_id.standard.id,
                'group_division': rec.group_division.id,
                'house_no': rec.house_no,
                'road_no': rec.road_no,
                'post_office': rec.post_office,
                'city': rec.city,
                'bd_division_id': rec.bd_division_id.id,
                'country_id': rec.country_id.id,
                'per_village': rec.per_village,
                'per_po': rec.per_po,
                'per_ps': rec.per_ps,
                'per_dist_id': rec.per_dist_id.id,
                'per_bd_division_id': rec.per_bd_division_id.id,
                'per_country_id': rec.per_country_id.id,
                'guardian_name': rec.guardian_name,
                'religious_id': rec.religious_id.id,
                # 'is_student': True,
                'student_id': rec.student_id,
                'roll_no': rec.roll_no,
                'application_no': rec.application_no,
            }
            student = self.env['eagleedu.student'].create(values)
            rec.write({
                'state': 'done'
            })
            return {
                'name': _('Student'),
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'eagleedu.student',
                'type': 'ir.actions.act_window',
                'res_id': student.id,
                'context': self.env.context
            }



class EagleeduBddivision(models.Model):
    _name = 'eagleedu.bddivision'
    _description = 'This the Bangladesh Division'
    name = fields.Char()

class EagleeduBddistrict(models.Model):
    _name = 'eagleedu.bddistrict'
    _description = 'This the Bangladesh District'
    name = fields.Char()

class EagleeduReligious(models.Model):
    _name = 'eagleedu.religious'
    _description = 'This the Religion'
    name = fields.Char()

class EagleeduOrganization(models.Model):
    _description = 'This the Organization'
    _inherit = 'res.company'

class EagleeduGuardianRelation(models.Model):
    _name = 'eagleedu.guardian.relation'
    _description = 'This the Guardian'

    name = fields.Char(string="Relation Title")
    gender=fields.Selection([('male',"Male"), ('female','Female')])

    relation=fields.Char(string='Relation',required=False)
    reverse_male=fields.Char(string='Reverse  Relation (Male)',required=False)
    reverse_female=fields.Char(string='Reverse Relation (Female)',required=False)


