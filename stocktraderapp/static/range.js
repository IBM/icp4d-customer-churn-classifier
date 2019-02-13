/**
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License. You may obtain
 * a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */

function show_value_Income(x)
{
 document.getElementById("slider_value_Income").innerHTML='$'+x;
}
function add_one_Income()
{
  document.getElementById('Income').value=parseInt(document.getElementById('Income').value)+10000;
  show_value_Income(document.getElementById('Income').value);
}
function subtract_one_Income()
{
 document.getElementById('Income').value=parseInt(document.getElementById('Income').value)-10000;
  show_value_Income(document.getElementById('Income').value);
}

function show_value_YearCurrentAddress(x)
{
 document.getElementById("slider_value_YearCurrentAddress").innerHTML=x;
}
function add_one_YearCurrentAddress()
{
  document.getElementById('YearCurrentAddress').value=parseInt(document.getElementById('YearCurrentAddress').value)+1;
  show_value_YearCurrentAddress(document.getElementById('YearCurrentAddress').value);
}
function subtract_one_YearCurrentAddress()
{
 document.getElementById('YearCurrentAddress').value=parseInt(document.getElementById('YearCurrentAddress').value)-1;
  show_value_YearCurrentAddress(document.getElementById('YearCurrentAddress').value);
}

function show_value_YearsCurrentEmployer(x)
{
 document.getElementById("slider_value_YearsCurrentEmployer").innerHTML=x;
}
function add_one_YearsCurrentEmployer()
{
  document.getElementById('YearsCurrentEmployer').value=parseInt(document.getElementById('YearsCurrentEmployer').value)+1;
  show_value_YearsCurrentEmployer(document.getElementById('YearsCurrentEmployer').value);
}
function subtract_one_YearsCurrentEmployer()
{
 document.getElementById('YearsCurrentEmployer').value=parseInt(document.getElementById('YearsCurrentEmployer').value)-1;
  show_value_YearsCurrentEmployer(document.getElementById('YearsCurrentEmployer').value);
}

function show_value_NumberOfCards(x)
{
 document.getElementById("slider_value_NumberOfCards").innerHTML=x;
}
function add_one_NumberOfCards()
{
  document.getElementById('NumberOfCards').value=parseInt(document.getElementById('NumberOfCards').value)+1;
  show_value_NumberOfCards(document.getElementById('NumberOfCards').value);
}
function subtract_one_NumberOfCards()
{
 document.getElementById('NumberOfCards').value=parseInt(document.getElementById('NumberOfCards').value)-1;
  show_value_NumberOfCards(document.getElementById('NumberOfCards').value);
}

function show_value_CCDebt(x)
{
 document.getElementById("slider_value_CCDebt").innerHTML='$'+x;
}
function add_one_CCDebt()
{
  document.getElementById('CCDebt').value=parseInt(document.getElementById('CCDebt').value)+1000;
  show_value_CCDebt(document.getElementById('CCDebt').value);
}
function subtract_one_CCDebt()
{
 document.getElementById('CCDebt').value=parseInt(document.getElementById('CCDebt').value)-1000;
  show_value_CCDebt(document.getElementById('CCDebt').value);
}

function show_value_LoanAmount(x)
{
 document.getElementById("slider_value_LoanAmount").innerHTML='$'+x;
}
function add_one_LoanAmount()
{
  document.getElementById('LoanAmount').value=parseInt(document.getElementById('LoanAmount').value)+10000;
  show_value_LoanAmount(document.getElementById('LoanAmount').value);
}
function subtract_one_LoanAmount()
{
 document.getElementById('LoanAmount').value=parseInt(document.getElementById('LoanAmount').value)-10000;
  show_value_LoanAmount(document.getElementById('LoanAmount').value);
}

function show_value_SalePrice(x)
{
 document.getElementById("slider_value_SalePrice").innerHTML='$'+x;
}
function add_one_SalePrice()
{
  document.getElementById('SalePrice').value=parseInt(document.getElementById('SalePrice').value)+10000;
  show_value_SalePrice(document.getElementById('SalePrice').value);
}
function subtract_one_SalePrice()
{
 document.getElementById('SalePrice').value=parseInt(document.getElementById('SalePrice').value)-10000;
  show_value_SalePrice(document.getElementById('SalePrice').value);
}



