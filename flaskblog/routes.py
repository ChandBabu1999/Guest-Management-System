from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, mail
from flaskblog.forms import Visitor_CheckIn_Form, Visitor_CheckOut_Form, HostForm
from flaskblog.models import Visitor, Host
from datetime import datetime
from flask_mail import Message

import os


@app.route("/host", methods=['GET', 'POST'])
def host():
    # validate here (Only admin can visit this page, ask for password, etc.)
    form = HostForm()
    if form.validate_on_submit():
        host = Host(name=form.host_name.data, email=form.email.data, 
                    ph_number=form.ph_number.data, address=form.Address.data)
        Host.query.delete() # delete the previous Host 
        db.session.add(host) # Add new Host
        db.session.commit()
        flash("Host Updated", "success")
        return redirect(url_for('check_in'))
    return render_template('flask_form.html', message='Register Host', title='host', form=form)


@app.route("/")
@app.route("/check_in", methods=['GET', 'POST'])
def check_in():
    # Don't display this page for login (optional)
    host_exist = Host.query.all()
    if not len(host_exist):
        flash("No Host Exist ...!",'danger')
        return redirect(url_for('check_in'))
    else: host = host_exist[0]

    form = Visitor_CheckIn_Form()
    if form.validate_on_submit():
        # check if he/she has already checked in?        
        visitor = Visitor(name=form.visitor_name.data,
            email=form.email.data, ph_number=form.ph_number.data)
        visitor_exist = Visitor.query.filter_by(email=form.email.data, check_out_time = None).first()

        if visitor_exist:
            flash(f"You are already Checked-In","danger")
            return redirect(url_for('check_in'))
        else:
            db.session.add(visitor)
            db.session.commit()
            flash(f'{form.visitor_name.data} checkd-in Successfully', 'success')

            msg = Message('Check-In Mail', sender = os.environ.get('EMAIL_ID', ''),
                    recipients = [host.email])
            msg.body = ('Visitor Checked-In\n'
                + '\nName : '+visitor.name
                + '\nEmail : '+visitor.email
                + '\nPhone : '+ str(visitor.ph_number)
                + '\nChek-in Time : '+str(visitor.check_in_time)+'\n')
            print('message', msg.body)
            mail.send(msg)
            flash(f'Email sent to the Host({host.email}, {host.name}), Successfully', 'success')
            
            return redirect(url_for('check_in'))
    return render_template('flask_form.html', message='Check-In Here', title='check-in', form=form)


@app.route("/check_out", methods=['GET', 'POST'])
def check_out():
    form = Visitor_CheckOut_Form()
    if form.validate_on_submit():
        # check if he/she has checked in or not?       
        visitor = Visitor.query.filter_by(email=form.email.data, check_out_time = None).first()
        if visitor:
            flash(f"You are Checked-Out Succeessfully","success")
            Visitor.query.filter_by(email=form.email.data, ph_number=form.ph_number.data).update(
                dict(check_out_time=datetime.now()))
            db.session.commit()
            
            host_exist = Host.query.all()
            host = host_exist[0]
            msg = Message('Viisiting Mail', sender = os.environ.get('EMAIL_ID', ''),
                    recipients = [visitor.email])
            msg.body = ('You Checked-Out\n'
                + '\nName : '+visitor.name
                + '\nPhone : '+ str(visitor.ph_number)
                + '\nChek-in Time : '+str(visitor.check_in_time)
                + '\nChek-in Time : '+str(visitor.check_in_time)
                + '\nHost Name : '+host.name 
                + '\nAddress visited : '+host.address +'\n')
            mail.send(msg)
            flash(f'Email sent to the Visitor({visitor.email},{visitor.name}), Successfully', 'success')
            
            return redirect(url_for('check_in'))
        flash(f'You have not checked-in yet (check mail, number)','danger')
    return render_template('flask_form.html', message='Check-Out Here', title='check-in', form=form)


@app.route("/vms")
def home():
    print('\n\n\n\n\n\nHost=', Host.query.all(),'\nVisitors :')
    vis = Visitor.query.all()
    for x in vis:
        print(x.name, x.email, x.ph_number, x.check_in_time, x.check_out_time)
    print()
    return redirect(url_for('check_in'))
