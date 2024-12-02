from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, TelField  # Ensure SubmitField is imported here
from wtforms.fields import DateField
from wtforms.validators import DataRequired

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
