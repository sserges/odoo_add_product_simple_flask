from flask import Flask,render_template,request,session,url_for,redirect,logging,flash
from forms import *
from myapi import OdooAPI

url,db,username,password="http://0.0.0.0:8069","test","admin","admin"



app=Flask(__name__)
api=OdooAPI(url,db,username,password)

@app.route('/')
def index():
	data=api.search_read('ir.module.module',[['state','=','installed']],['name','state'])
	return render_template('index.html',data=data)

@app.route('/add',methods=['GET','POST'])
def register():
	form=ProductForm(request.form)
	if request.method=="POST" and form.validate():
		name=form.name.data
		barcode=form.barcode.data
		id=api.create('product.template',{'name': name,'barcode':barcode})
		flash("inserted in odoo","success")
		return redirect(url_for('index'))
	return render_template('add.html',form=form)
if __name__=="__main__":
	app.secret_key = '@%^&(*9867ahsh)'
	app.run(debug=True)
