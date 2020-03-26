from flask_wtf import Form
from wtforms import TextField
from wtforms import Form, BooleanField, StringField, PasswordField, RadioField, SelectField,  DateField, IntegerField, SubmitField, validators, FileField
from wtforms.validators import DataRequired, InputRequired

disease_choices = [('Trouble breathing or shortness of breath' , 'Ongoing chest pain or pressure') , ('Can’t wake up' , 'Bluish lips or face
') , ('Coughing up sputum, or thick phlegm, from the lung' , 'Coughing up sputum, or thick phlegm, from the lung') , ('Fever' , 'Fever') , ('Dry cough' , 'Dry cough') , ('Diphtheria' , 'Diphtheria') , ('Dysentery' , 'Dysentery') , ('Food Poisoning' , 'Food Poisoning') , ('Gastroenteritis (< 2years)' , 'Gastroenteritis (< 2years)') , ('Hepatitis A' , 'Hepatitis A') , ('Sore throat' , 'Sore throat') , ('Hepatitis Unspecified' , 'Hepatitis Unspecified') , ('Legionnaires Disease' , 'Legionnaires Disease') , ('Leptospirosis' , 'Leptospirosis') , ('Malaria' , 'Malaria') , ('Measles' , 'Measles') , ('Meningococcal Septicaemia' , 'Meningococcal Septicaemia') , ('Mumps' , 'Mumps') , ('Paratyphoid Fever' , 'Paratyphoid Fever') , ('Coughing up blood' , 'Coughing up blood') , ('Poliomyelitis (Paralytic)' , 'Poliomyelitis (Paralytic)') , ('Poliomyelitis (Acute)' , 'Poliomyelitis (Acute)') , ('Rabies', 'Rabies') , ('Relapsing Fever' , 'Relapsing Fever') , ('Rubella' , 'Rubella') , ('Scarlet Fever' , 'Scarlet Fever') , ('Smallpox' , 'Smallpox') , ('Tetanus' , 'Tetanus') , ('Tuberculosis (Pulmonary)' , 'Tuberculosis (Pulmonary)') , ('Tuberculosis (Non Pulmonary)' , 'Tuberculosis (Non Pulmonary)') , ('Typhoid' , 'Typhoid') , ('Typhus' , 'Typhus') , ('Viral Haemorraghic Fever' , 'Viral Haemorraghic Fever') , ('Whooping Cough' , 'Whooping Cough') , ('Yellow Fever' , 'Yellow Fever')]
class AdminSignUpForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    first_name = StringField('First Name', [validators.Length(min=6, max=35)])
    last_name = StringField('Last Name', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password')
    file = FileField('Upload ID', validators=[InputRequired()])
    #admin_type = StringField('Administrator Type', [validators.Length(min=6, max=35)])

    submit = SubmitField('Submit')

class AdminLoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    submit = SubmitField('Submit')

class ReportDiseaseForm(Form):
    disease_name = SelectField('Name of Disease' ,choices = disease_choices, validators=[InputRequired()])
    date = DateField('Date of Report', validators=[InputRequired()])
    age = IntegerField('Age of patient')
    gender = RadioField('Gender' , choices = [('male', 'Male') , ('female', 'Female')])
    file = FileField('Upload Report File', validators=[InputRequired()])
    submit = SubmitField('Submit')

class ReportDeathForm(Form):
    disease_name = SelectField('Cause of death' ,choices = disease_choices, validators=[InputRequired()])
    date = DateField('Date of Report', validators=[InputRequired()])
    age = IntegerField('Age of patient')
    gender = RadioField('Gender' , choices = [('male', 'Male') , ('female', 'Female')])
    file = FileField('Upload Certificate', validators=[InputRequired()])
    submit = SubmitField('Submit')
    
    
