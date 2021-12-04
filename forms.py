from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, message="Password must me at least 8 character long")])
    name = StringField(label="Name", validators=[DataRequired()])
    submit = SubmitField(label="Register")


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")


class CommentForm(FlaskForm):
    comment = CKEditorField("Leave a Comment", validators=[DataRequired()])
    submit = SubmitField(label="Submit Comment")
