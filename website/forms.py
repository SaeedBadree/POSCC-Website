from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, TelField, BooleanField, RadioField  # Ensure SubmitField is imported here
from wtforms.fields import DateField
from wtforms.validators import DataRequired,Length

class ChangeOwnershipForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    cemetery = StringField('Cemetery', validators=[DataRequired()])
    block_number = StringField('Block Number', validators=[DataRequired()])
    grave_space = StringField('Grave Space Number', validators=[DataRequired()])
    owner_details = TextAreaField('Owner Details (Name & Address)', validators=[DataRequired()])
    contact_number = TelField('Contact Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RemoveOwnershipForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    cemetery = StringField('Cemetery', validators=[DataRequired()])
    block_number = StringField('Block Number', validators=[DataRequired()])
    grave_space = StringField('Grave Space Number', validators=[DataRequired()])
    owner_details = TextAreaField('Owner Details (Name & Address)', validators=[DataRequired()])
    contact_number = TelField('Contact Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

class IncludeOwnershipForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    cemetery = StringField('Cemetery', validators=[DataRequired()])
    block_number = StringField('Block Number', validators=[DataRequired()])
    grave_space = StringField('Grave Space Number', validators=[DataRequired()])
    additional_owner_details = TextAreaField('Additional Owner Details (Name & Address)', validators=[DataRequired()])
    contact_number = TelField('Contact Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TransferAllotmentForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    cemetery = StringField('Cemetery', validators=[DataRequired()])
    block_number = StringField('Block Number', validators=[DataRequired()])
    grave_space = StringField('Grave Space Number', validators=[DataRequired()])
    transfer_to = TextAreaField('Transfer To (Name & Address)', validators=[DataRequired()])
    transfer_reason = TextAreaField('Reason for Transfer', validators=[DataRequired()])
    contact_number = TelField('Contact Number', validators=[DataRequired()])
    submit = SubmitField('Submit')


class FoodHandlersForm(FlaskForm):
    date = DateField('Date', format='%d/%m/%Y', validators=[DataRequired()], render_kw={"placeholder": "dd/mm/yyyy"})
    name = StringField('Name', validators=[DataRequired()])
    sex = RadioField('Sex', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    home_address = TextAreaField('Home Address', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', format='%d/%m/%Y', validators=[DataRequired()], render_kw={"placeholder": "dd/mm/yyyy"})
    identification_no = StringField('Identification No.', validators=[DataRequired()])
    telephone = StringField('Telephone', validators=[DataRequired()])
    business_name = StringField('Name of Business', validators=[DataRequired()])
    business_type = StringField('Type of Business', validators=[DataRequired()])
    business_address = TextAreaField('Address of Business', validators=[DataRequired()])

    # Family History
    family_typhoid = BooleanField('Typhoid (Family)')
    family_tuberculosis = BooleanField('Tuberculosis (Family)')
    family_jaundice = BooleanField('Jaundice (Family)')
    family_chronic_cough = BooleanField('Chronic Cough (Family)')
    family_hospitalization = BooleanField('Hospitalization (Family)')
    family_other = StringField('Other (Family)')

    # Personal History
    personal_typhoid = BooleanField('Typhoid (Personal)')
    personal_tuberculosis = BooleanField('Tuberculosis (Personal)')
    personal_jaundice = BooleanField('Jaundice (Personal)')
    personal_chronic_cough = BooleanField('Chronic Cough (Personal)')
    personal_hospitalization = BooleanField('Hospitalization (Personal)')
    personal_asthmatic_attacks = BooleanField('Asthmatic Attacks (Personal)')
    personal_allergies = BooleanField('Allergies, Skin disease, Ulcers')
    personal_other = StringField('Other (Personal)')

    # Declaration and Authorization
    declaration = BooleanField('I declare that the information I provided is correct.', validators=[DataRequired()])
    applicant_signature = StringField('Applicant Signature', validators=[DataRequired()])
    applicant_signature_date = DateField('Date', format='%d/%m/%Y', validators=[DataRequired()], render_kw={"placeholder": "dd/mm/yyyy"})

    submit = SubmitField('Submit')
    
    
class PublicComplaintForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()], format='%Y-%m-%d')
    premises = StringField('Premises', validators=[DataRequired(), Length(max=255)])
    nature_of_complaint = TextAreaField('Nature of Complaint', validators=[DataRequired()])
    complainant_name = StringField('Complainant Name', validators=[DataRequired(), Length(max=255)])
    contact_details = StringField('Contact Details', validators=[DataRequired(), Length(max=255)])
    action_taken = TextAreaField('Action Taken (optional)')
    submit = SubmitField('Submit') 