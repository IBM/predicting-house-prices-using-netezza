# Build a Machine learning web application for predicting house rental prices with Netezza in-database analytics and Streamlit

## Project Description:
- In this repository, you will learn how to leverage Netezza Python in-database analytics (nzpyida) and Streamlit to quickly build and deploy in-database machine learning applications. While nzpyida allows users to push custom ML inside Netezza database, Streamlit allows users to build beautiful web applications for such ML models.  We will use US housing rental prediction use-case as an example scenario to illustrate all the steps in detail, connecting to the Netezza Performance server, performing data analysis, creating the machine learning model, and integration of the machine learning model with a web application. 
- The housing dataset which is publicly available (housing_data) is a collection of rental records for various houses in several cities/towns across the United States.  Based on the dependent variables in the dataset (housing type, bds, baths etc.), the target variable, rent of the house (price) is to be predicted. Since the price of one-bedroom apartment in San Francisco varies a lot from that of a one-bedroom apartment in Idaho, it might be helpful to build a ML model catering to each location separately rather than having one single model built for all the locations. Netezza with its powerful MPP (Massively Parallel Processing) architecture is ideally suited to handle such scenarios. 
- Our goal is to perform the following steps: transform the data (impute the columns by assigning default values for null values), build ML models on location basis (build a gradient-boosting regressor for the transformed data), then build web application to interact with predictions (using Streamlit). The web application can easily be downloaded and replicated on your local machine.

## Steps for installing and running the repository:

1. Make sure your local machine has python installed.

``` python --version ```


2. Use venv to setup a virtual environment in which your application will reside.

``` python3 -m venv /the-folder-your-application-will-reside-in ```


3. Download the code available in this repository either by downloading a  zip file or clone the repository.

``` git clone https://github.ibm.com/pratik-joseph-dabre/housing_model.git ```

4. Navigate to the folder where the repository resides and download the dependencies required to run the application.

```pip3 install -r requirements.txt```

5. After successful installation of all the dependencies, start the streamlit application.

``` cd streamlit```

```streamlit run main.py```

## Output in the browser:


### 1. Model training: 



 

- Instead of training the model by a set of commands, we can trigger the model training from the data application using just a single click. 

 
<img width="1715" alt="Screen Shot 2022-07-13 at 11 30 52 AM" src="https://media.github.ibm.com/user/396331/files/bffcc000-0da9-11ed-9b13-d27bb26b6dea">


 
<img width="1716" alt="Screen Shot 2022-07-13 at 11 31 12 AM" src="https://media.github.ibm.com/user/396331/files/a78ca580-0da9-11ed-93b8-2ea4a04f162a">

 

### 2. Selecting the attributes to find houses for: 

<img width="1712" alt="Screen Shot 2022-07-14 at 11 44 48 AM" src="https://media.github.ibm.com/user/396331/files/cb4feb80-0da9-11ed-9430-70cbef10f6de">


 

 

 

### 3. Visualizing the results: 


 

-  After selecting the parameters, you get back all the houses matching your description in a table format. 

 

-  Using streamlit-aggrid, an interactive, customizable grid is rendered on the browser, on which you can perform multiple operations. 

 <img width="1716" alt="Screen Shot 2022-07-14 at 11 46 02 AM" src="https://media.github.ibm.com/user/396331/files/d0ad3600-0da9-11ed-88a0-3658be44adba">


 

 

- Based on various parameters, you can filter out the rows as per your needs. 

 

 

 

- After filtering out the records, a user can perform operations on the records. 

 <img width="1718" alt="Screen Shot 2022-07-13 at 11 29 38 AM" src="https://media.github.ibm.com/user/396331/files/09e5a600-0daa-11ed-93c7-c3d13e3963ec">


(For example, here the user is able to visualize all the records selected on a map) 

 <img width="1713" alt="Screen Shot 2022-07-13 at 11 28 56 AM" src="https://media.github.ibm.com/user/396331/files/e7538d00-0da9-11ed-99f0-04852a569d2d">


 

 
