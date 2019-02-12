# -*- coding: utf-8 -*-

import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, session, render_template, flash

app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY=os.environ.get('SECRET_KEY', 'development key')
))


class mortgagedefault():

    @app.route('/', methods=['GET', 'POST'])
    def index():

        if request.method == 'POST':
            ID = 999
            Age = request.form['Age']
            Gender = request.form['Gender']
            Status = request.form['Status']
            Children = request.form['Children']
            HomeOwner = request.form['Homeowner']
            EstIncome = request.form['Income']
            NetRealizedGainsYTD = request.form['Netrealizedgainsytd']
            NetRealizedLossesYTD = request.form['Netrealizedlossesytd']
            SmallestSingleTransaction = request.form[
              'Smallestsingletransaction']
            LargestSingleTransaction = request.form['Largestsingletransaction']
            TotalDollarValueTraded = request.form['Totaldollarvaluetraded']
            TotalUnitsTraded = request.form['Totalunitstraded']
            DaysSinceLastLogin = request.form['Dayssincelastlogin']
            DaysSinceLastTrade = request.form['Dayssincelasttrade']
            PercentageChangeCalculation = request.form[
              'Percentagechangecalculation']

            session['ID'] = ID
            session['Age'] = Age
            session['Gender'] = Gender
            session['Status'] = Status
            session['Children'] = Children
            session['HomeOwner'] = HomeOwner
            session['EstIncome'] = EstIncome
            session['NetRealizedGainsYTD'] = NetRealizedGainsYTD
            session['NetRealizedLossesYTD'] = NetRealizedLossesYTD
            session['SmallestSingleTransaction'] = SmallestSingleTransaction
            session['LargestSingleTransaction'] = LargestSingleTransaction
            session['TotalDollarValueTraded'] = TotalDollarValueTraded
            session['TotalUnitsTraded'] = TotalUnitsTraded
            session['DaysSinceLastLogin'] = DaysSinceLastLogin
            session['DaysSinceLastTrade'] = DaysSinceLastTrade
            session[
              'PercentageChangeCalculation'] = PercentageChangeCalculation

            scoring_href = os.environ.get('URL')
            mltoken = ('Bearer %s' % os.environ.get('TOKEN'))

            if not (scoring_href and mltoken):
                raise EnvironmentError('Env vars URL and TOKEN are required.')

            data = {
                "ID": ID,
                "Gender": Gender,
                "Status": Status,
                "Children": Children,
                "EstIncome": EstIncome,
                "HomeOwner": HomeOwner,
                "Age": Age,
                "TotalDollarValueTraded": TotalDollarValueTraded,
                "TotalUnitsTraded": TotalUnitsTraded,
                "LargestSingleTransaction": LargestSingleTransaction,
                "SmallestSingleTransaction": SmallestSingleTransaction,
                "PercentChangeCalculation": PercentageChangeCalculation,
                "DaysSinceLastLogin": DaysSinceLastLogin,
                "DaysSinceLastTrade": DaysSinceLastTrade,
                "NetRealizedGains_YTD": NetRealizedGainsYTD,
                "NetRealizedLosses_YTD": NetRealizedLossesYTD}

            payload_scoring = {"args": {"input_json": [data]}}
            print("DXK-Payload is ")
            print(payload_scoring)
            header_online = {
                'Cache-Control': 'no-cache',
                'Content-Type': 'application/json',
                'Authorization': mltoken}
            response_scoring = requests.post(
                scoring_href,
                verify=False,
                json=payload_scoring,
                headers=header_online)
            result = response_scoring.text
            print("DXK-Result is ")
            print(result)
            flash('Successful Prediction')
            return render_template(
                'score.html',
                result=result,
                response_scoring=response_scoring)

        else:
            return render_template('input.html')


load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
port = os.environ.get('PORT', '5000')
host = os.environ.get('HOST', '0.0.0.0')
if __name__ == "__main__":
    app.run(host=host, port=int(port))
