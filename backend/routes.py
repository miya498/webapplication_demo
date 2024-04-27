from flask import render_template, request, redirect, url_for
from . import app
from .models import db, Report

@app.route('/')
def index():
    reports = Report.query.all()
    return render_template('index.html', reports=reports)

@app.route('/new_report', methods=['POST'])
def new_report():
    title = request.form['report-title']
    date = request.form['report-date']
    content = request.form['report-content']

    new_report = Report(title=title, date=date, content=content)
    db.session.add(new_report)
    db.session.commit()

    return redirect(url_for('index'))
