# Data Analyst Nanodegree Program

## Overview
Projects for Udacity Data Analyst Nanodegree Program (DAND)

|Term, Project, Topic|Project Description | Link |
| ------------------ |:---------------------:| :-------:|
|Term 1, Project 1 - *Welcome* |Brief introductory project using SQL and spreadsheet software to compare local with global temperature trends| [Explore Weather Trends](t1p1/termperature_trends.pdf)|
|Term 1, Project 2 - *Intro to Python* | Simple interactive script to calculate descriptive statistics on bike share data using Python 3, NumPy, and pandas | [Explore US bikeshare data](t1p2/README.md)|
|Term 1, Project 3 - *Intro to Data Analysis* | Investigation of a curated dataset with Python, Pandas in a Jupyter notebook| [Hospital No-show appointments](t1p3/dand-project-investigate-a-dataset_final.ipynb)|
|Term 1, Project 4 - *Practical statistics* | Analyse the results of an A/B test run by an e-commerce website| [Analyse A/B test](t1p4/Analyze_ab_test_results_notebook.ipynb)|
|Term 2, Project 1 - *Term Welcome* | Short introductory analysis of the Stroop effect| [Test A Perceptual Phenomenon](t2p1/Test_a_Perceptual_Phenomenon.ipynb)|
|Term 2, Project 2 - *Exploratory Data Analysis* |Performing a complete exploratory data analysis using R, using as dataset campaign contribution to the 2016 US presidential campaign | [EDA - 2016 US Campaign Finance](t2p2/dand_t2p2_campaign_finance.html)|
|Term 2, Project 3 - *Data Wrangling* |Gathering, cleaning, analysing data from the WeRateDogs Twitter account| [WeRateDogs Twitter Data Wrangling](t2p3/README.md)|
|Term 2, Project 4 - *Data Story Telling*|Using Tableau for explanatory data visualisation of Prosper P2P lending | [Project report (pdf)](t2p4/DAND_t2p4_report_Prosper.pdf), [Actual story hosted by Tableau](https://public.tableau.com/profile/pierre.hentges#!/vizhome/ProsperStory_15544624601900/ProsperStoryver2)|

## Degree certificate
![DAND Certificate](DAND_Certificate.png)

[Link](https://confirm.udacity.com/STRQEDGC) for the degree certificate 

# Projects details

## [t1p1] - Explore Weather Trends
This is a brief introductory project. The purpose is to compare local with global temperature trends using temperature data starting in the 18th century. The project involves using SQL and spreadsheet software 

#### screenshot
![weather trends](t1p1/screenshot.png)

[Direct Link to the Project (pdf file)](t1p1/termperature_trends.pdf)

## [t1p2] - Introduction to Python: Explore US bikeshare data
The purpose of the project was to make use of Python to explore data fom Motivate, a bike share system provider, compute a variety of descriptive statistics and build a very basic interactive environment where a user chooses the data and filter for a dataset to analyze. The data relate to bike share systems for three US cities : Chicago, New York City, and Washington. 

#### files:
* DAND_project2_bikeshare.py: Python script
* chicago.csv, new_york_city.csv, washington.csv: data files

#### screenshot
![US bikeshare data](t1p2/screenshot.png)

[Link to the Project - Explore US bikeshare data](t1p2/README.md)

## [t1p3] - Introduction to Data Analysis: Hospital appointments
This module is aimed at learning about the data analysis process of questioning, wrangling, exploring, analyzing, and communicating data.

The project itself was to conduct data analysis on a dataset, answering a number of questions and create a file to share the findings. I learnt how to work with data in Python using libraries like NumPy and Pandas, as well as Pyplot and Seaborn for visualisation. These were carried out in a Jupyter notebook.

I chose a dataset for analysis about medical appointments and factors that influence wether patients turn up. This dataset collects information from 100k hospital appointments in Brazil. A number of characteristics about the patient are included in each row. The project didn't include inferential statistics or machine learning, so these were tentative findings.

#### files:
* dand-project-investigate-a-dataset_final.ipynb: Jupter notebook
* noshowappointments-kagglev2-may-2016.csv: dataset
* requirements.txt: libraries used (conda)
* readme_submission_notes.txt: submission notes

#### screenshot
![Hospital appointements](t1p3/screenshot.png)

[Direct link to the Project (Jupyter notebook)](t1p3/dand-project-investigate-a-dataset_final.ipynb)|

## [t1p4] - Practical statistics: A/B test
This module was about learning how to apply inferential statistics and probability to real-world scenarios.
The project was an analysis of results from an A/B Test run by an e-commerce website, aiming to help the company understand if they should implement the new page design or not. Approaches encompassed probability, a z-test and linear regression.

### files:
* Analyze_ab_test_results_notebook.ipynb: Jupyter notebook
* ab_data.csv, countries.csv: datasets

#### screenshot
![A/B test](t1p4/screenshot.png)

[Direct Link to the project's Jupyter notebook](t1p4/Analyze_ab_test_results_notebook.ipynb)




## [t2p1] - Second Term Intro
Short introductory project for the second term. The aim was to use a Jupyter notebook to compute descriptive statistics and perform a statistical test on a dataset based on a classic phenomenon from experimental psychology, the Stroop Effect.

In psychology, the Stroop effect is a demonstration of interference in the reaction time of a task. When the name of a color (e.g., "blue", "green", or "red") is printed in a color which is not denoted by the name (i.e., the word "red" printed in blue ink instead of red ink), naming the color of the word takes longer and is more prone to errors than when the color of the ink matches the name of the color. The effect is named after John Ridley Stroop, who first published the effect in English in 1935. (Wikipedia)

### files:
* Test_a_Perceptual_Phenomenon.ipynb: Jupter notebook
* stroopdata.csv: datasets

#### screenshot
![Stroop effect](t2p1/screenshot.png)

[Direct link to the Project notebook](t2p1/Test_a_Perceptual_Phenomenon.ipynb)|



## [t2p2] - Exploratory Data Analysis: WeRateDogs Twitter data
Performing a complete exploratory data analysis using R, using as dataset campaign contribution to the 2016 US presidential campaign 

[EDA - 2016 US Campaign Finance](t2p2/dand_t2p2_campaign_finance.html)|

![2016 US presidential primaries](t2p2/screenshot.png)

## [t2p3] - Data Wrangling
This module was about learn the entire data wrangling process of gathering, assessing, and cleaning data. In the project I learnt how to use Python to wrangle data programmatically and prepare it for deeper analysis.

Data from three sources and in a variety of formats were used. After assessing its quality and tidiness, data was subjected to data cleaning and then combined into a single dataset. This was then analysed and visualised.

### Files
* README.md: outline
* wrangle_act.ipynb: Jupyter notebook containing all the data wrangling, analysis and visualsations steps
* act_report.pdf: Report summarising insights and visualizations
* wrangle_report.pdf: Describes data wrangling and cleaning efforts plus some reflections
* image-predictions.tsv: dataset downloaded from Udacity
* tweet_json.txt: dataset with JSON data obtained from the Twitter API using tweepy
* twitter-archive-enhanced.csv: dataset downloaded from Udacity
* twitter_archive_master.csv : dataframe obtained after data cleaning

![2016 WeRateDogs](t2p3/screenshot.png)

[Link to Project overview](t2p3/README.md)

[Direct link to Jupyter notebook](t2p3/wrangle_act.ipynb)

[Direct link to main project report (pdf file)](t2p3/act_report.pdf)



## [t2p4] - Data Story Telling: Tableau Story about P2P lending
Data visualisation is the most compelling way of communicating insight about data. This module was about learning to apply sound design and data visualization principles to the data analysis process. 

In the module's project, Tableau Public was used for analysis and visualizations to tell a story with data.I chose a dataset about [P2P lending](https://en.wikipedia.org/wiki/Peer-to-peer_lending) from [Prosper](https://en.wikipedia.org/wiki/Prosper_Marketplace) for the years 2005-2014. This dataset contains data about 113,937 loans with 81 variables on each loan, including loan amount, borrower rate (or interest rate), current loan status, borrower income, and many others.

The final project aimed at creating an explanatory data visualization from a data set that communicates a clear finding or that highlights relationships or patterns in a data set. The work should be a reflection of the theory and practice of data visualization, and the final deliverable was a write up along with a Tableau Public workbook. The report documented changes made to the original version of the Tableau story after feedback from 2 people.

My visualisation investigates the P2P lending company Prosper and how borrowers use this novel finance facility. The focus is the large proportion of borrowers who use Prosper for debt consolidation – usually successfully in the sense that they subsequently manage to pay off the loan.

### Files and Links
* The final report: [Pdf file hosted on Github](t2p4/DAND_t2p4_report_Prosper.pdf)
* The first version of the Tableau story: [Story hosted by Tableau](https://public.tableau.com/profile/pierre.hentges#!/vizhome/ProsperStory_15544624601900/ProsperStoryver1)
* The final version of the Tableau story with improvements after feedback: [Story hosted by Tableau](https://public.tableau.com/profile/pierre.hentges#!/vizhome/ProsperStory_15544624601900/ProsperStoryver2)
* Dataset used - Prosper P2P loans: [ https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv.](https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv)
* Explanation of the variables used in the Propser dataset [https://docs.google.com/spreadsheets/d/1gDyi_L4UvIrLTEC6Wri5nbaMmkGmLQBk-Yx3z0XDEtI/](https://docs.google.com/spreadsheets/d/1gDyi_L4UvIrLTEC6Wri5nbaMmkGmLQBk-Yx3z0XDEtI/edit#gid=0)

![Prosper P2P Lending](t2p4/screenshot.png)
