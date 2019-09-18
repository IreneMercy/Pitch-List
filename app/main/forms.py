from flask_wtf import FlaskForm, Form
from wtforms import StringField,TextAreaField,SubmitField,validators
from wtforms.validators import Required



class PostPitch(FlaskForm):
    category = TextAreaField('Category',validators = [Required()])
    title= TextAreaField('Title',validators = [Required()])
    content= TextAreaField('Content',validators = [Required()])
    submit = SubmitField('Submit')

class CommentPitch(FlaskForm):
    content= TextAreaField('Comment',validators = [Required()])
    submit = SubmitField('Submit')
