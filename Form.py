from wtforms import Form, TextAreaField, TextField, validators


class ENS_domainForm(Form):
    name = TextField('Name', [validators.Length(min=7)])
