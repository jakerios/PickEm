from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
from sqlalchemy.sql import exists 
from .apiTest import sportsOdds
from pprint import pprint as pp
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        Note.query.delete()
        db.session.commit()

        pick_10 = request.form.get('10')
        pick_9 = request.form.get('9')
        pick_8 = request.form.get('8')
        pick_7 = request.form.get('7')
        pick_6 = request.form.get('6')
        pick_5 = request.form.get('5')
        pick_4 = request.form.get('4')
        pick_3 = request.form.get('3')
        pick_2 = request.form.get('2')
        pick_1 = request.form.get('1')

        new_picks =  Note(pick_10=pick_10, pick_9=pick_9, pick_8=pick_8, pick_7=pick_7, pick_6=pick_6, pick_5=pick_5, pick_4=pick_4, pick_3=pick_3, pick_2=pick_2, pick_1=pick_1, user_id = current_user.id)
        db.session.add(new_picks)
        db.session.commit()

        flash('Picks added', category='success')

    testObject = sportsOdds()
    arr1, arr2, arr3, arr4 = testObject.getFootballOdds()
    '''
    for x in arr3:
        if x <= 2:
    '''
    return render_template("home.html", user=current_user, arr1=arr1, arr2=arr2, arr3=arr3, arr4=arr4)

@views.route('/rules')
def rules():
    return render_template("rules.html", user=current_user)

@views.route('/hockey', methods=['GET', 'POST'])
@login_required
def hockey():
    if request.method == 'POST':
        Note.query.delete()
        db.session.commit()

        pick_10 = request.form.get('10')
        pick_9 = request.form.get('9')
        pick_8 = request.form.get('8')
        pick_7 = request.form.get('7')
        pick_6 = request.form.get('6')
        pick_5 = request.form.get('5')
        pick_4 = request.form.get('4')
        pick_3 = request.form.get('3')
        pick_2 = request.form.get('2')
        pick_1 = request.form.get('1')

        new_picks =  Note(pick_10=pick_10, pick_9=pick_9, pick_8=pick_8, pick_7=pick_7, pick_6=pick_6, pick_5=pick_5, pick_4=pick_4, pick_3=pick_3, pick_2=pick_2, pick_1=pick_1, user_id = current_user.id)
        db.session.add(new_picks)
        db.session.commit()

        flash('Picks added', category='success')

    testObject = sportsOdds()
    arr1, arr2, arr3, arr4 = testObject.getHockeyOdds()

    return render_template("hockey.html", user=current_user, arr1=arr1, arr2=arr2, arr3=arr3, arr4=arr4)

@views.route('/football', methods=['GET', 'POST'])
@login_required
def football():
    if request.method == 'POST':
        Note.query.delete()
        db.session.commit()

        pick_10 = request.form.get('10')
        pick_9 = request.form.get('9')
        pick_8 = request.form.get('8')
        pick_7 = request.form.get('7')
        pick_6 = request.form.get('6')
        pick_5 = request.form.get('5')
        pick_4 = request.form.get('4')
        pick_3 = request.form.get('3')
        pick_2 = request.form.get('2')
        pick_1 = request.form.get('1')

        new_picks =  Note(pick_10=pick_10, pick_9=pick_9, pick_8=pick_8, pick_7=pick_7, pick_6=pick_6, pick_5=pick_5, pick_4=pick_4, pick_3=pick_3, pick_2=pick_2, pick_1=pick_1, user_id = current_user.id)
        db.session.add(new_picks)
        db.session.commit()

        flash('Picks added', category='success')

    testObject = sportsOdds()
    arr1, arr2, arr3, arr4 = testObject.getFootballOdds()

    return render_template("football.html", user=current_user, arr1=arr1, arr2=arr2, arr3=arr3, arr4=arr4)

@views.route('/baseball', methods=['GET', 'POST'])
@login_required
def baseball():
    if request.method == 'POST':
        Note.query.delete()
        db.session.commit()

        pick_10 = request.form.get('10')
        pick_9 = request.form.get('9')
        pick_8 = request.form.get('8')
        pick_7 = request.form.get('7')
        pick_6 = request.form.get('6')
        pick_5 = request.form.get('5')
        pick_4 = request.form.get('4')
        pick_3 = request.form.get('3')
        pick_2 = request.form.get('2')
        pick_1 = request.form.get('1')

        new_picks =  Note(pick_10=pick_10, pick_9=pick_9, pick_8=pick_8, pick_7=pick_7, pick_6=pick_6, pick_5=pick_5, pick_4=pick_4, pick_3=pick_3, pick_2=pick_2, pick_1=pick_1, user_id = current_user.id)
        db.session.add(new_picks)
        db.session.commit()

        flash('Picks added', category='success')

    testObject = sportsOdds()
    arr1, arr2, arr3, arr4 = testObject.getBaseballOdds()

    return render_template("baseball.html", user=current_user, arr1=arr1, arr2=arr2, arr3=arr3, arr4=arr4)