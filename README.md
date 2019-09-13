# Infuse AI into your application

In this code pattern, we will create and deploy a customer churn prediction model using IBM Cloud Pak for Data. The basis for our model is a data set that contains customer demographics and trading activity data. We will use a Jupyter notebook to visualize the data, build hypotheses for prediction, and then build, test, and save a prediction model. Finally, we will enable a web service and use the model from an app.

> This code pattern has been updated to include images from the latest version of Cloud Pak for Data, v2.1.0.2.

The use case describes a stock trader company that can use churn prediction to target offers for at-risk customers. Once deployed, the model can be used for inference from an application using the REST API. A simple app is provided to demonstrate using the model from a Python app.

When the reader has completed this code pattern, they will understand how to:

* Load customer data into Db2 Warehouse
* Run a Jupyter notebook
* Visualize data using Brunel
* Create a model using Spark ML library
* Deploy the model as a web service
* Access the model from an external app for inference (churn risk prediction)

![architecture](doc/source/images/architecture.png)

## Flow

1. Data is loaded locally, or optionally into Db2 Warehouse
1. Jupyter notebook accesses data
1. Jupyter notebook uses Brunel for information visualization
1. Jupyter notebook uses Spark ML library to create a model
1. Jupyter notebook saves the model to the repository for deployment
1. Applications access the model via the REST API

## Watch the Video

[![video](https://img.youtube.com/vi/rnoqAagpRaM/0.jpg)](https://www.youtube.com/watch?v=rnoqAagpRaM)

## Prerequisites

The instructions in this code pattern assume you are using IBM Cloud Pak for Data.

## Steps

Sign in to your IBM Cloud Pak for Data web client. All of the steps are performed using the web client unless stated otherwise.

1. [Clone the repo](#1-clone-the-repo)
2. [Set up an analytics project](#2-set-up-an-analytics-project)
3. [Create the notebook](#3-create-the-notebook)
4. [Insert pandas DataFrame](#4-insert-pandas-dataframe)
5. [Initialize Watson Machine Learning client](#5-initialize-watson-machine-learning-client)
6. [Run the notebook](#6-run-the-notebook)
7. [Analyze the results](#7-analyze-the-results)
8. [Test the model in the UI](#8-test-the-model-in-the-ui)
9. [Deploy the model](#9-deploy-the-model)
10. [Use the model in an app](#10-use-the-model-in-an-app)
11. [(OPTIONAL) Use Db2 Warehouse to store customer data](#11-optional-use-db2-warehouse-to-store-customer-data)

### 1. Clone the repo

Clone the `icp4d-customer-churn-classifier` repo locally. In a terminal, run the following command:

```bash
git clone https://github.com/IBM/icp4d-customer-churn-classifier
```

### 2. Set up an analytics project

To get started, open the `Projects` page and set up an analytics project to hold the assets that you want to work with, and then get data for your project.

#### Create a project

- [ ] Go to the `Projects` list and click `+ New project`.
- [ ] Make sure `Analytics project` is select.
- [ ] Provide a `Project name`.
- [ ] Click `OK`.
- [ ] Stay on the `New` tab.
- [ ] Optionally, add a `Description`
- [ ] Click `Create`.

#### Add the data asset

> NOTE: You can optionally load the data into Db2 Warehouse. For instuctions, go to [use Db2 Warehouse to store customer data](#11-optional-use-db2-warehouse-to-store-customer-data).

- [ ] Use the left menu to go back to `Projects`.
- [ ] Select the project you created.
- [ ] In your project, using the `Assets` tab, click `Data sets`.
- [ ] Click on `+ Add Data Set`.
- [ ] Using the `Local File` tab, use drag-and-drop or click `Select from your local file system` and select the `data/mergedcustomers.csv` data file from your cloned repo.

### 3. Create the notebook

To create and open the notebook from a file:

- [ ] In your project, using the `Assets` tab, click `Notebooks`.
- [ ] Click on `+ Add Notebook`.
- [ ] Select the `From File` tab:
- [ ] Provide a notebook `Name` and `Description`.
- [ ] Use drag-and-drop or click `browse` and open the `notebooks/TradingCustomerChurnClassifierSparkML.jupyter-py36.ipynb` file from your cloned repo.
- [ ] Click `Create`.

### 4. Insert pandas DataFrame

Now that you are in the notebook, add generated code to insert the data as a DataFrame and fix-up the notebook reference to the DataFrame.

- [ ] Place your cursor at the last line of the following cell:

  ```python
  # Use the find data 10/01 icon and under your remote data set
  # use "Insert to code" and "Insert Pandas DataFrame
  # here.
  import os, pandas as pd
  # Add asset from file system
  ```

- [ ] Click the *find data* `10/01` icon on the menu bar (last icon).
- [ ] Using the `Remote` tab under `10/01`, find the data set that you added to the project, click `Insert to code` and `Insert Pandas DataFrame`.

  ![insert_spark_dataframe.png](doc/source/images/insert_spark_dataframe.png)

- [ ] The inserted code will result in a DataFrame assigned to a variable named `df1` or `df_data_1` (perhaps with a different sequence number). Find the code cell like the following code block and edit the `#` to make it match the variable name.

  ```python
  # After inserting the pandas DataFrame code above, change the following
  # df_data_# to match the variable used in the above code. df_churn_pd is used
  # later in the notebook.
  df_churn_pd = df_data_#
  ```

### 5. Initialize Watson Machine Learning client

The Watson Machine Learning client is required to save and deploy our customer churn predictive model, and should be available on your IBM Cloud Pak for Data platform. Insert the required credentials in the following cell:

  ```python
  from watson_machine_learning_client import WatsonMachineLearningAPIClient

  # get URL, username and password from your IBM Cloud Pak for Data administrator
  wml_credentials = {
    "url": "https://X.X.X.X",
    "instance_id": "icp",
    "username": "****",
    "password": "****"
  }

  client = WatsonMachineLearningAPIClient(wml_credentials)
  ```

### 6. Run the notebook

- [ ] Run the entire notebook using the menu `Cell ▷ Run All` or run the cells individually with the play button as shown here.

   ![press_play.png](doc/source/images/press_play.png)

### 7. Analyze the results

#### When the notebook was created

* A pod was instantiated – which means loading a complete compute Jupyter notebook environment (7+ GB) with all the artifacts from the private ICP-D registry.
* This pod is scheduled on any VM in your cluster – wherever CPU and memory resources are available.
* IP addresses and connections are all configured automatically.
* The same working environment can be used by multiple users. If a single pod's resources are not sufficient, another environment is created automatically.
* When the number of users grow, you can add more machines to the ICP-D cluster and scheduling of resources is handled automatically.
* ICP-D's scale-out model is pretty effective.
* You no longer have to wait days or even weeks to get the compute resources.
* More users can be accommodated with same compute capacity. As one task completes, its resources are freed up to work on next one.

#### When you ran the notebook

* During the execution of a cell in a Jupyter notebook, an asterisk `[*]` displays in the square bracket which changes to a sequence number when execution of that cell completes.

* The mix of documentation, code, and output can make a Jupyter output self-explanatory. This also makes it a great environment to "show your work" if you have a hypothesis, do some analysis, and come up with a conclusion.

<!--  TODO: describe and show more key output/analysis
 -->
* Example Brunel chart:

  ![churn_risk_chart.png](doc/source/images/churn_risk_chart.png)

* The model was saved and deployed to the Watson Machine Learning service. Next, we will test the model in the UI. Later, we'll deploy the model for external use.

  ![save_model.png](doc/source/images/save_model.png)

#### Sample notebook output

See the notebook with example output [here](https://nbviewer.jupyter.org/github/IBM/icp4d-customer-churn-classifier/blob/master/examples/TradingCustomerChurnClassifierSparkML.jupyter-py36.ipynb).

### 8. Test the model in the UI

IBM Cloud Pak for Data provides various options for analytics models such as testing, scoring, evaluating, and publishing.

#### Interactive testing

You can use real-time scoring to test your model with different input values in a easy-to-use user interface.

- [ ] In your project, using the `Assets` tab, click `Models`.
- [ ] Click on the action menu (vertical 3 dots) and select `Real-time score`.
  ![model_actions.png](doc/source/images/model_actions.png)
- [ ] Change some test values and click `Submit`. Use the upper-right icons to select a pie chart or bar chart.
  ![wml_test.png](doc/source/images/wml_test.png)

### 9. Deploy the model

Next, we'll create a project release and tag the model under version control. We'll use model management and deployment to make the released model available as a web service (REST API).

#### Commit the project changes

- [ ] Go back to the project homepage. You can see a "**Changes made**" message. Click on `commit and push`.

   ![changes_made.png](doc/source/images/changes_made.png)

- [ ] You will see there is a list of the assets that are created in this project. Provide a `Commit message` to identify and make note of changes being pushed.

   ![commit.png](doc/source/images/commit.png)

- [ ] Click the `Commit` button.

- [ ] You will see a success message, and a prompt to `push` the changes. Click on `push`.

   ![push_changes.png](doc/source/images/push_changes.png)

- [ ] Provide a version tag under `Create version tag for release`. Please note that the tag and commit message are both very important to identify and deploy the changes.

- [ ] Click the `Push` button.

#### Create a project release

Now that we have a committed and tagged version of the project, we can create a project release to deploy our model.

- [ ] Use the left menu's `Administer` drop-down list and click on `Manage deployments`.

   ![manage_deployments.png](doc/source/images/manage_deployments.png)

- [ ] Click on `+ Add Project Release` to create the deployment.

- [ ] Give it a name that you can easily track. `Route` will be a part of the url. It should be lowercase. Select your project as the `Source project`, and set `Tag` to the release tag you just created. Click the `Create` button.

   ![release.png](doc/source/images/release.png)

This project release is created.

#### Create an online and batch deployment for the deployed model

- [ ] Under the `Assets` tab for your project release, select the model you just created and then click the upper-right `+ web service` button. This will add an online deployment service for this model.

   ![add_web_service.png](doc/source/images/add_web_service.png)

- [ ] Choose whether you want to reserve resources and how many replicas you want for this job.

- [ ] Click the `Create` button.

   ![create_web_service.png](doc/source/images/create_web_service.png)

   > Note: At this time, the online deployment is created. On the deployment panel, you can see the REST API URL `ENDPOINT` and the `DEPLOYMENT TOKEN`.

   ![deployment_token.png](doc/source/images/deployment_token.png)

The deployment is still not active. We need to launch and enable it before it can be used.

#### Launch deployment

- [ ] Under the `Deployments` tab for your project release, your new deployment will be set to `Disabled`. To enable it, you must first bring all of your deployments on-line by clicking the `Launch` button located at the top of the panel.

   ![launch_button.png](doc/source/images/launch_button.png)

- [ ] Then use the action menu (vertical 3 dots) for your deployment and select `Enable`.

   ![enable_service.png](doc/source/images/enable_service.png)

   > Note: For any additional changes made to your project release, use the update button to save your changes.

   ![update.png](doc/source/images/update.png)

#### Deployment testing in the UI

Test the model in the API interface.

- [ ] Click the enabled deployment. Under the `API` tab, we can test the model.

- [ ] Use the default values or use your own values to test the model.

   ![deployment_test.png](doc/source/images/deployment_test.png)

- [ ] Click `Submit`. The result is shown on right with inputs and prediction results.

- [ ] You can click the `< > Generate Code` button to get the code for [deployment testing using curl](#deployment-testing-with-curl).

- [ ] In the top section of the panel, you can copy the POST API endpoint and deployment token. Save it for [using the model in an app](#10-use-the-model-in-an-app).

#### Deployment testing with curl

Using curl on the command line is a good way to test the REST APIs before integrating them with more complicated code. To access the model, use the generated code obtained during [deployment testing in the UI](#deployment-testing-in-the-ui).

For example, in a terminal run a `curl` command like the following:

```bash
curl -k -X POST \
  https://169.48.4.137:31843/dmodel/v1/tradingcustomerchurn/pyscript/onlineservice/score \
  -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFja2FnZU5hbWUiOiJUcmFkaW5nQ3VzdG9tZXJDaHVybkFuYWx5c2lzIiwicGFja2FnZVJvdXRlIjoidHJhZGluZ2N1c3RvbWVyY2h1cm4iLCJpYXQiOjE1NjgyMTM2ODd9.Xnpf3Jf0G3FMAzXCrfm80Au2ucyCcHvuvmz-R5QbrZeRBcfFc9lGyGrDupadSVudAfSGSHG51xAcDKCGB8w1HmqY-Fr5Xt-fxkfOKp0SgZQJFJV2aLiCqIfkSh-XDpD_Br_HMQ6LDjrUwtXky3O_b1684fF_Tb70AswoqQp5tLS_VJU0er8idYv6pwhpuUmtyRSxN0gKV_mQV0tQ0OZ8bCC-uk6W2pkd7MCBuJq6D0ab1m-8oRwvr2oCy7bXXAXZWpZP2v4b-rsyzpbom7pgPmRR91uWdm1jkE24fVp9NJ8x-g1B8rjGxJCO9o8DDptSwD5lyDW5Qekvc2d6aGClKw' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{"args":{"input_json":[{"ID":4,"GENDER":"F","STATUS":"M","CHILDREN":2,"ESTINCOME":52004,"HOMEOWNER":"N","AGE":25,"TOTALDOLLARVALUETRADED":5030,"TOTALUNITSTRADED":23,"LARGESTSINGLETRANSACTION":1257,"SMALLESTSINGLETRANSACTION":125,"PERCENTCHANGECALCULATION":3,"DAYSSINCELASTLOGIN":2,"DAYSSINCELASTTRADE":19,"NETREALIZEDGAINS_YTD":0,"NETREALIZEDLOSSES_YTD":251}]}}'
```

#### Deployment dashboard

The Dashboard shows all of the deployment results. This includes the performance of each evaluation. The thresholds you defined for evaluation will indicate how the deployed model is performing in real-time. “Green” indicates good performance, “amber” indicates mediocre and “red” indicates a poorly performing model. For underperforming models, you can go back to the notebook, make changes until the model performs well, and then reploy the updated model. That’s how the dashboard helps with the machine learning model life cycle management.

   ![dashboard.png](doc/source/images/dashboard.png)

### 10. Use the model in an app

You can also access the web service directly through the REST API. This allows you to use your model for inference in any of your apps.

#### Running the example Python web app

##### Install dependencies

The general recommendation for Python development is to use a virtual environment ([venv](https://docs.python.org/3/tutorial/venv.html)). To install and initialize a virtual environment, use the `venv` module on Python 3 (you install the virtualenv library for Python 2.7):

- [ ] In a terminal go to the cloned repo directory.

   ```bash
   cd icp4d-customer-churn-classifier
   ```

- [ ] Initialize a virtual environment.

   ```bash
   # Create the virtual environment using Python. Use one of the two commands depending on your Python version.
   # Note, it may be named python3 on your system.

   python -m venv venv       # Python 3.X
   virtualenv venv           # Python 2.X

   # Source the virtual environment. Use one of the two commands depending on your OS.

   source venv/bin/activate  # Mac or Linux
   ./venv/Scripts/activate   # Windows PowerShell
   ```

   > **TIP** :bulb: To terminate the virtual environment use the `deactivate` command.

- [ ] Install the Python requirements.

   ```bash
   cd stocktraderapp
   pip install -r requirements.txt
   ```

- [ ] Copy the env.sample to .env.

   ```bash
   cp env.sample .env
   ```

- [ ] Edit the .env file to provide the `URL` and `TOKEN`.

  * `URL` is your web service URL for scoring.
  * `TOKEN` is your deployment access token.
  ```bash
  # Copy this file to .env.
  # Edit the .env file with the required settings before starting the app.

  # Required: Provide your web service URL for scoring.
  # E.g., URL=https://9.10.222.3:31843/dmodel/v1/project/pyscript/tag/score

  URL=

  # Required: Provide your web service deployment access token.
  #           This TOKEN should start with "Bearer ".
  # E.g., TOKEN=Bearer abCdwFghIjKLMnO1PqRsTuV2wWX3YzaBCDE4.fgH1r2... (and so on, tokens are long).

  TOKEN=

  # Optional: You can override the server's host and port here.

  HOST=0.0.0.0
  PORT=5000
  ```

- [ ] Start the flask server.

   ```bash
   python StockTraderChurn.py
   ```

- [ ] Use your browser to go to http://0.0.0.0:5000 and try it out.

- [ ] Use `CTRL-C` to stop the flask server when you are done.

#### Sample Output

The prediction screen:

   ![sample_output.png](doc/source/images/sample_output.png)

Pressing `Reset` allows you to enter new values:

   ![sample_output_reset.png](doc/source/images/sample_output_reset.png)

### 11. (OPTIONAL) Use Db2 Warehouse to store customer data

This section provides an alternative to accessing a local csv file in your notebook. This requires that you have created a Db2 Warehouse database deployment in your IBM Cloud Pak for Data cluster. With it, you can access the integrated database console to complete common tasks, such as loading data into the database.

#### Open the database

- [ ] Use the left menu's `Collect` drop-down list and click on `My data`.
- [ ] Click on the `Databases` tab.
- [ ] You should see a Db2 Warehouse tile with a status of `Available` (otherwise revisit the prerequisites and ensure your userid has access to a database).
- [ ] Click on the tile action menu (vertical 3 dots) and select `Open`.

#### Load the data

- [ ] Click on the upper-right `☰ Menu` and select `Load`.
- [ ] Use drag-and-drop or click `browse files` and open the `data/mergedcustomers.csv` file from your cloned repo.
- [ ] Click `Next`.
- [ ] Select or create the schema to use for the data.
- [ ] Select or create the table to use for the data.
- [ ] Click `Next`.
- [ ] Ensure that the data is being properly interpreted. For example, specify that the first row in the CSV file is a header and ensure that the comma separator is used.
- [ ] Click `Next`.
- [ ] Review the summary and click `Begin Load`.

#### Collect the database URL and credentials

- [ ] Go back to `Collect ▷ My data ▷ Databases ▷ Db2 Warehouse` tile.
- [ ] Click on the tile action menu (vertical 3 dots) and select `Details`.
- [ ] Copy the `Username`, `Password`, and `JDBC Connection URL` to use later.

#### Add the data asset

- [ ] If needed, create a project using the instructions in [set up an analytics project](#2-set-up-an-analytics-project).
- [ ] Use the left menu to go back to `Projects`.
- [ ] Select the project you created.
- [ ] In your project, use the `Data Sources` tab, and click `+ Add Data Source`.
- [ ] Provide a `Data source name` and `Description`.
- [ ] Use the `Data source type` drop-down list to select `Db2 Warehouse on Cloud`.
- [ ] Fill in the `JDBC URL`, `Username`, and `Password` that you collected earlier.
- [ ] Click the `Test Connection` button and make sure your test connection passed.
- [ ] Click on `+ Add remote data set`.
- [ ] Provide a `Remote data set name` and a `Description`.
- [ ] Provide a `Schema`. This is the schema that you used when you created the table.
- [ ] Provide the table name (that you used when you loaded the CSV data).
- [ ] Click `Create`.

#### Insert a Spark DataFrame in your notebook

Follow the instructions above for creating your project and notebook. Then, in your notebook, add generated code to insert the data as a DataFrame and fix-up the notebook reference to the DataFrame.

- [ ] Place your cursor at the last line of the following cell:

  ```python
  # Use the find data 10/01 icon and under your remote data set
  # use "Insert to code" and "Insert Spark DataFrame in Python"
  # here.

  ```

- [ ] Click the *find data* `10/01` icon on the menu bar (last icon).
- [ ] Using the `Remote` tab under `10/01`, find the data set that you added to the project, click `Insert to code` and `Insert Spark DataFrame in Python`.

  ![insert_spark_dataframe.png](doc/source/images/insert_spark_dataframe.png)

- [ ] The inserted code will result in a DataFrame assigned to a variable named `df1` or `df_data_1` (perhaps with a different sequence number). Find the code cell like the following code block and edit the `#` to make it match the variable name.

  ```python
  # After inserting the Spark DataFrame code above, change the following
  # df# to match the variable used in the above code. df_churn is used
  # later in the notebook.
  df_churn = df#
  ```
#### Complete the code pattern

Once the notebook completes and your model is created, you can deploy and access your model just as before, starting with the step [test the model in the UI](#8-test-the-model-in-the-ui).

## License

This code pattern is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)
