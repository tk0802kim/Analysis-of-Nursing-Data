This is a work in progress to learn, practice, and showcase my data science skills. Thanks for visiting!

# Analysis-of-Nursing-Data

How can we attract more registered nurses to our state/city/institution? What can we do with availiable data to give us actionable insights?

This project aims to develop insights into the nursing workforce, primarily using the 2018 NSSRN survey data, along with other publicly available data. The survey can be downloaded from [here](https://data.hrsa.gov/DataDownload/NSSRN/GeneralPUF18/NSSRN2018_SAS_encoded_package.zip).

The Jupyter notebook file [nursing_analysis.ipynb](https://github.com/tk0802kim/Analysis-of-Nursing-Data/blob/master/nursing_analysis.ipynb) contains the results and findings. To run this on the local machine, download then entire project, download and unzip the survey data in the project folder, and run the Jupyter notebook. For the code scraping, I use NordVPN. If you have a different VPN or don't use one, comment that part out.


### Dependencies:
  Pandas, Numpy, scikit-learn, MatPlotLib, pyreadstat, Seaborn, tqdm, SciPy, pickle, dill, Spacy, PyMC3, bs4, nordvpn_switcher

### Things done and documented:

- Logistic regression of the survey data, and analysis of feature importance
- Analysis of nurse movements, including geographic and temporal analysis
- Nursing salary data scrap and analysis
- Baysian approach to quantifying the attractiveness of a state to nurse
- Linear regression for the said attractiveness with bootstrapping
- GBM classification of survery data, in place of random forest


### Things done, but not documented yet:


### Things to do:

- SVM, ANN, and other methods of boosting the power of predictive model
- Collection of other covariates for the attractiveness prediction model
- Multiple linear regression, with SINDy-like approach to linearize the covariates
- Apply other methods of machine learning to the attractiveness model