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

        '''Put the name of the select in as the string'''
        game1Pick = request.form.get('game1Pick')
        game2Pick = request.form.get('game2Pick')
        game3Pick = request.form.get('game3Pick')
        game4Pick = request.form.get('game4Pick')
        game5Pick = request.form.get('game5Pick')
        game6Pick = request.form.get('game6Pick')
        game7Pick = request.form.get('game7Pick')
        game8Pick = request.form.get('game8Pick')
        game9Pick = request.form.get('game9Pick')
        game10Pick = request.form.get('game10Pick')
        game11Pick = request.form.get('game11Pick')
        game12Pick = request.form.get('game12Pick')
        game13Pick = request.form.get('game13Pick')
        game14Pick = request.form.get('game14Pick')
        game15Pick = request.form.get('game15Pick')
        game16Pick = request.form.get('game16Pick')

        new_picks =  Note(game1Pick = game1Pick, game2Pick = game2Pick, game3Pick = game3Pick, 
                          game4Pick = game4Pick, game5Pick = game5Pick, game6Pick = game6Pick, 
                          game7Pick = game7Pick, game8Pick = game8Pick, game9Pick = game9Pick, 
                          game10Pick = game10Pick, game11Pick = game11Pick, game12Pick = game12Pick, 
                          game13Pick = game13Pick, game14Pick = game14Pick, game15Pick = game15Pick, 
                          game16Pick = game16Pick, user_id = current_user.id)
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

@views.route('/odds')
def odds():
    oddsObject = sportsOdds()
    arr1, arr2, arr3, arr4 = oddsObject.getFootballOdds()

    return render_template("odds.html", user=current_user, arr1=arr1, arr2=arr2, arr3=arr3, arr4=arr4)


