from flask_wtf import FlaskForm, Form
from wtforms import StringField,TextAreaField,SubmitField,validators
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PostPitch(FlaskForm):
    category = StringField('Category',validators=[Required()])
    title = StringField('Title',validators = [Required()])
    content= TextAreaField('Content',validators = [Required()])
    submit = SubmitField('Submit')
