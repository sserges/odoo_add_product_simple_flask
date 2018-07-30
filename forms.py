from wtforms import Form,StringField,validators

class ProductForm(Form):

    name=StringField('Name',[validators.Length(min=1,max=100)])
    barcode=StringField('Barcode',[validators.Length(min=1,max=100)])
