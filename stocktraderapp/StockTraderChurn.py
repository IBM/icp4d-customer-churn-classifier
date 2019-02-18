# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
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
            mltoken = os.environ.get('TOKEN')

            if not (scoring_href and mltoken):
                raise EnvironmentError('Env vars URL and TOKEN are required.')

            data = {
                "ID": ID,
                "GENDER": Gender,
                "STATUS": Status,
                "CHILDREN": Children,
                "ESTINCOME": EstIncome,
                "HOMEOWNER": HomeOwner,
                "AGE": Age,
                "TOTALDOLLARVALUETRADED": TotalDollarValueTraded,
                "TOTALUNITSTRADED": TotalUnitsTraded,
                "LARGESTSINGLETRANSACTION": LargestSingleTransaction,
                "SMALLESTSINGLETRANSACTION": SmallestSingleTransaction,
                "PERCENTCHANGECALCULATION": PercentageChangeCalculation,
                "DAYSSINCELASTLOGIN": DaysSinceLastLogin,
                "DAYSSINCELASTTRADE": DaysSinceLastTrade,
                "NETREALIZEDGAINS_YTD": NetRealizedGainsYTD,
                "NETREALIZEDLOSSES_YTD": NetRealizedLossesYTD}

            payload_scoring = {"args": {"input_json": [data]}}
            print("Payload is ")
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
            print("Result is ", result)
            result_json = json.loads(result)
            churn_risk = result_json["result"]["predictions"][0].lower()
            flash(
              'The risk of this customer churning is %s ' % churn_risk)
            return render_template(
                'score.html',
                result=result_json,
                churn_risk=churn_risk,
                response_scoring=response_scoring)

        else:
            return render_template('input.html')


load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
port = os.environ.get('PORT', '5000')
host = os.environ.get('HOST', '0.0.0.0')
if __name__ == "__main__":
    app.run(host=host, port=int(port))
