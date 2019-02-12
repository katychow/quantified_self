# quantified_self
katy's fitbit capstone &amp; personal project for quantified self work

## Analyzing Sleep Data: a [Quantified Self](https://medium.com/quantified-self-dublin/quantified-self-health-wellness-now-into-f853e68c5d72) Study

---
### Executive Summary

---
There are many motivations behind self-tracking, but with the rise of newer technologies coupled with recent trends in physical/mental improvement, it is natural to want to study yourself.  For me, this obsession started with trying to figure out if I had some gastrointestinal issues in 2017.  At first, I told myself perhaps it was my age since I am no longer in my early 20s.  As I researched further, I found the [Nourish Balance Thrive Podcast](http://www.nourishbalancethrive.com/podcasts/nourish-balance-thrive/).  ***Voila!*** My passion of self improvement through nutrition and sleep was ignited.  This podcast spoke to me because the host, Christopher Kelly, was a data scientist turned health pioneer.  I also worked in the field of data science and needed answers about my health.  In the past year, I have played around with my sleep but not intensely tracking it.  Since the beginning of my data science immersive with [General Assembly](https://generalassemb.ly/), I started tracking my sleep with a Fitbit.  With that said, the purpose of this analysis, is two fold.  I want to be able to see if a consistent week of good sleep will lead to more good sleep, and I would like to look at my sleep data not only on a daily view but track my sleep over a long period.  


### The Problem Statement: 

---
We are trying to make several inferences with this sleep data.  Perhaps we can predict if I will have more or less sleep than the average, but it doesn't necessarily give me much information about what my sleep patterns are.  For simplicity, I have several questions I want to answer with this analysis.
 - Does consistently good sleep lead to more good sleep?  
 - What other factors can impact sleep?
 - What should we explore next?


### The Data:

---
The data is a downloadable zip file provided by Fitbit.  Fitbit also offers an API option, but due to time constraints, I chose to just download the zip file of all of my data.  The data came in a JSON format, and I used a python library to parse the data into two main datasets.  The first dataset that I also use for my model consists of each nights sleeping data.  The second dataset I created from the JSON files consisted of the times that I had different sleeping activity which can be linked back to the first dataset (the header dataset) via the logID.  Sleeping activity varies between minutes asleep, restless, and awake.  Below are two tables representing the data and its layouts.  In addition to the sleep data from January 7th to January 30th, there was caffeine intake data to be linked to the sleep data by date.  Each row was a coffee, tea, or wine that was included in the dataset.  I added alcohol consumption due to my physical reaction to alcohol.  Each coffee, tea, latte, and other form of caffeine was transformed into mg of caffeine per drink.    

#### Header Table

|Column Name|Data Type|Description|
|---|---|---|
|asleep_cnt|int64|counts of continuous sleep periods for 1 night|
|asleep_min|int64|minutes of sleep for 1 night|
|awake_cnt|int64|counts of continuous awake periods for 1 night|
|awake_min|int64|minutes being awake for 1 night|
|dateOfSleep|datetime64|date of sleep|
|duration|int64|duration of sleep|
|efficiency|int64|efficiency of sleep|
|endTime|object|end of time sleep (when you wake up and get out of bed)|
|infoCode|int64|n/a|
|logID|int64|unique id for each night's sleep|
|minutesAfterWakeup|int64|minutes in bed after you wake up|
|minutesAsleep|int64|minutes spent asleep|
|minutesAwake|int64|minutes awake during sleep|
|minutesToFallAsleep|int64|minutes to fall asleep|
|restless_cnt|int64|counts of continuous restless periods for 1 night|
|restless_min|int64|minutes of restlessness for 1 night|
|startTime|object|when Fitbit infers when you feel asleep|
|timeInBed|int64|total time spent in bed for 1 night of sleep|
|type|object|n/a|

#### Sleep Table

|Column Name|Data Type|Description|
|---|---|---|
|dateTime|datetime64| timestamp YYYY-MM-DDTHH:mm:ss.nnn|
|level|object|description of sleep activity|
|logID|int64|unique id for each night's sleep|
|seconds|int64|seconds in specific level|

#### Caffeine Intake Table
|Column Name|Data Type|Description|
|---|---|---|
|Date|object|Date MM/DD/YYY|
|Time|object|Time AM/PM|
|Type|object|Coffee,Tea,Wine|
|Volume (oz)|float64|Volume if caffeine intake|
|Kind|object|Brand/Format of Caffeine|
|Prep Type|object|How caffeine was prepared|
|Notes|object|Notes|

### Methodology

---
#### 1. Gather Data
Gathering data was much more difficult than I had expected.  What made the gathering data the most difficult, was actually keeping the Fitbit on my wrist.  Another challenge was when the Fitbit needed to be charged.  There are days where sleep data is missing because I accidentally took off my Fitbit to shower/wash my hands and the band never made it back onto my wrist.  The opposite of this would be I would remember to wear my Fitbit but not realize that it was dead and needed to be charged.  This made gathering data much more difficult that originally expected.  Additionally, this created gaps in the sleep study.  Where I should have had 120 days of sleep data, I had 83 days of sleep data.  

#### 2. Cleaning Data & Initial EDA
The process of parsing the data from the downloadable zip file was fairly simple.  Using the Python dictionary parsing method, I created simple datasets as mentioned above from the sleep information.  EDA is a large portion of the project.  Due to small amounts of data points the ability to fit a good model was challenging.  I had to back fill the missing nights of sleep with the median of sleep minutes, restlessness minutes, and awake minutes for the nights that were missing.  We will show different trends of the data as a part of the EDA due to lack of data.  

#### 3. Modeling
For the modeling, I tried several models.  I tried a time series, regression, and a recurrent neural network.  Using the caffeine data, I tried to predict minutes of sleep given mg intake of caffeine.  For this prediction, I tried a linear regression but the R-squared score after 5 fold cross validation, was in the negatives.  The next method I tried, was time series modeling with a SARIMAX model to account for seasonality, possible lags, and sudden shocks in the minutes asleep.  This model performed reasonably and I used a RMSE and MAE to calculate goodness of fit.  Similarly with the recurrent neural network, it performed like the time series model.  If time permits, I may rerun a classicification model to determine whether or not we can predict more or less sleep than the average nights sleep.  


### Challenges

---
One major challenge was data leakage.  Using time awake or time restless included data leakage issues, due to incorporating sleep information to predict minutes asleep.  Another challenge was the granularity of the data.  From other studies of sleep, time series models are rather good at predicting sleep when you can observe 24 hours of activity.  The fitbit sleep data only gives information about the inferred sleep periods.  Lastly, there were outlier challenges, where fitbit would infer sleep if the device was taken off midday and not put back on.  THe most challenging piece is most likely the user error problem.  If I were more consistent with recording data, I would have less gaps in the observations and also keeping the device on at all times would limit outliers in my dataset.

### Conclusions

---
For the data available, modeling proved to be inconclusive due to lack of granular data.  Using the available, we can easily make a lot of statistical inferences with visualizations to be seen in the presentation.  The value in the analysis is using the code anyone can easily look at their sleep patterns.  A simple run of the data cleansing scripts will allow anyone to have data in nice dataframe to manipulate to give different inferences they are interested in.  If a user has enough data, they will be able to recycle the modeling code to model the next nights sleep or use the time series methods to look at their sleep cycle.  Overall, the objective of this project was to create usable scripts so that other people can make interesting inferences about their sleep while answering some questions presented above.  In the section below, I will answer the questions for myself.  

 - Does consistently good sleep lead to more good sleep?  For me personally, sleep start time seemed to be the biggest indicator of getting enough minutes in bed and time asleep.  
 - What other factors can impact sleep?  Caffeine for me did not have major impacts in my sleep.
 - What should we explore next?  See section below! 

### Next Steps

---
For future improvements for modeling, I recommend the following:
1. Take more measurements overall!  Having more consistency on keeping device on at all times.
2. Continue to take caffeine intake measurements
3. Continue to measure sleep
4. Include activity file for modeling purposes
5. Take more granular data overall
6. Start to include food intake
7. Try classification model for prediction of more or less sleep than average.
8. Write wrapper or use DASH python package to create dashboard for sleep visualizations. 

### The Files

---
The files are organized in 3 folders.  Each folder has a subset of folders that describe a different portion of the analysis.  Because this is a two part project each subfolder is related to a different aspect such as the dashboard creation/interactive tool, the data cleaning, or the modeling.  Within each folder, there will be another README explaining the organization of the folder. 

1. [Code](https://github.com/katychow/quantified_self/tree/master/Code)
2. [Data](https://github.com/katychow/quantified_self/tree/master/Data)
3. [Presentation Materials](https://github.com/katychow/quantified_self/tree/master/Presentation Materials)
