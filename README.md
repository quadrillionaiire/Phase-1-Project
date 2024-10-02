![dataset cover](./images/dataset-cover.png)

# National UFO Reporting Center Data Analysis

## Overview

This project analyzes UFO sighting data collected by the National UFO Reporting Center (NUFORC), which has recorded over 80,000 reports from 1949 to 2013. By conducting a descriptive analysis of sighting locations, timings, and characteristics, we aim to uncover patterns and trends in UFO sightings. Our analysis explores key questions such as the most commonly reported UFO shapes, the times and places where sightings are most frequent, and whether any correlations exist between the time of sighting and the likelihood of a UFO encounter.

## Business Problem 
![ufo image from nuforc](images/S178691_1.jpg)

By identifying patterns in UFO sightings, the National UFO Reporting Center can enhance its ability to communicate findings to researchers, enthusiasts, and governmental entities. Providing clear, data-driven visualizations of UFO sighting frequencies, shapes, and encounter characteristics will improve the understanding of these phenomena. This, in turn, will support strategic decisions related to future research, public education, and potential resource allocation for investigating UFO encounters.

## Data Understanding 

The dataset contains detailed information on UFO sightings reported globally. It includes key features like the date and time of the sighting, geographic information (country, region, and locale), descriptions of the UFO (shape and encounter duration), and other attributes that can be used for exploratory data analysis and predictive modeling.
Given the diverse nature of this dataset, we will focus on cleaning and processing the data to answer three key business questions:

1. What regions and times have the highest frequency of UFO sightings?
     - We will use the Country, Region, Locale, Year, Month, Hour, and Season columns to find the hotspots for UFO activity.
2. Are there notable patterns in UFO shapes, descriptions, or lengths of encounters?
     - The columns UFO_shape, length_of_encounter_seconds, and Description will be analyzed to explore common shapes, durations, and narratives in the reported encounters.
3. Can any correlations be drawn between the timing (season, time of day) and the likelihood of a sighting?
     - We will explore correlations between the Season, Month, Hour, and length_of_encounter_seconds to see if UFO sightings show patterns based on the time of day or season of the year.

## Data Preparation

This project applies descriptive analysis to understand patterns in UFO sightings, utilizing visualizations to examine trends over time, geographic hotspots, and sighting characteristics such as shape and encounter duration. Correlation analysis was also conducted to investigate potential relationships between the timing of sightings and their duration.


## Analysis & Results

Geographic Trends: The United States, particularly California, has the highest number of reported UFO sightings, followed by Washington and Florida. Sightings are most frequent during the summer months, peaking in July.

Sighting Characteristics: The most commonly reported UFO shape is "light," followed by "triangle" and "circular." Most sightings are brief, with a median encounter length of 180 seconds.

Time-Based Correlations: There is a weak negative correlation (-0.04) between the length of sightings and the time of day, suggesting little connection between sighting duration and the hour of occurrence.


## Conclusions

- **UFO Sightings by Region and Time**:  
  The United States, especially California, leads in UFO sightings by a significant margin. Sightings peak during the summer months, particularly in July and August, and are more frequent in coastal and densely populated areas. The trend over the years shows a rise in sightings after 2010, with a peak in 2012, followed by a decline.

- **Patterns in UFO Shapes and Descriptions**:  
  The most commonly reported UFO shape is "light," followed by "triangle" and "circular" forms. The descriptions often include terms like "light," "moving," and "sky." The distribution of the length of encounters suggests most sightings are brief, with a median duration of around 180 seconds.

- **Correlation Between Timing and Sightings**:  
  There is no strong correlation between the time of day (hour) and the duration of encounters, with a weak negative correlation (-0.04). This suggests that while there may be certain times with more sightings, the length of these encounters does not significantly vary based on the time.



### Next Steps

- **Deeper Analysis of Shape and Duration**:  
  Further analysis could explore whether specific shapes, such as "triangle" or "light," correlate with longer or shorter sighting durations, which may provide more insight into the nature of these sightings.

- **Predictive Modeling for Sightings**:  
  Building a predictive model that uses variables like time, season, region, and shape to predict future UFO sightings could aid governmental or research bodies in anticipating and preparing for possible events.

- **Anomaly Detection for False Positives**:  
  Applying anomaly detection techniques to the dataset could help identify potential "false positives" in the reports, distinguishing between legitimate sightings and potential misinterpretations.

- **Targeted Communication Strategies**:  
  Developing communication strategies based on the most common shapes and descriptions could enhance public awareness and provide clearer guidelines for reporting future sightings. This would improve data quality for researchers and policy-makers.

## For More Information

See the full analysis in the [Jupyter Notebook](https://github.com/quadrillionaiire/Phase-1-Project/blob/main/notebooks/clean_notebook.ipynb) or review this [presentation](url)

Tableau Dashboard link 

[Original data source from Kaggle](https://www.kaggle.com/datasets/jonwright13/ufo-sightings-around-the-world-better/data)

## Repository Structure 

```
├── dashboard
├── data
├── images
├── notebooks
├── presentations
├── src
├── .gitignore
```


# Phase-1-Project
Key things to include:
Project Overview
#Stakeholder & Business QUESTIONS
#Data Soucres 
#Links to notebooks, preentations, and dashboards 

Additional Notes
Business Problem: A clear statement of the business problem you are solving.

Dataset Information: A description of your dataset(s) and how you plan to use it.

Methods: Brief explanation of your analysis steps.

Results and Recommendations: What insights and recommendations are you providing to the stakeholder?

Links: Include links to the Jupyter notebook, dashboard, and presentation files.

Remember no code just visuals non techical

Example Template:

Project Title
1. Overview
A concise summary of the project, including the purpose, the problem it addresses, and the key findings.

Goal of the project: Clearly state the objective.
Context: Brief background or motivation for the project.
Main results/insights: Summarize key outcomes or insights from your analysis.

2. Repository Structure (Probably should go at the bottom
Provide an outline of the repository, explaining what each folder and file contains.
📁 /data              # Contains raw and cleaned datasets
📁 /notebooks         # Jupyter Notebooks or code scripts used in analysis
📁 /scripts           # Python or other scripts for data cleaning and modeling
📁 /images            # Graphs, figures, Tableau dashboard files
📄 README.md          # Documentation of the project
📄 requirements.txt   # Packages and dependencies needed to run the code
📄 presentation.pdf   # Final presentation slides

/data: A brief description of the datasets used, including sources.
/notebooks: Notebooks detailing data exploration, cleaning, analysis, and modeling.
/scripts: Python scripts for automating tasks like data processing.
/images: Contains final visuals, plots, or links to Tableau dashboards.

3. Data Science Steps
Outline the key steps taken during the project:

Data Collection: How data was sourced (e.g., APIs, web scraping, public datasets).
Data Cleaning: Techniques used for cleaning and preprocessing data (e.g., handling missing values).
Exploratory Data Analysis (EDA): Summary of insights found during the EDA phase.
Modeling: Brief overview of the models used and their performance.
Results: Main findings from the analysis or predictive models.

4. Instructions for Use
Guide users on how to navigate the repository, including how to replicate the project on their local machine: (git clone link)

5. Tableau Dashboard
Include a link to the Tableau dashboard:

Tableau Dashboard   
6. Presentation
Provide a link to the final project presentation:

7. Sources

List any references or external data sources used:
Data Source 1(Kaggle)

8. Commit History
Provide an overview of the commit history to demonstrate project development and collaboration. Link to the repository’s commit history for detailed tracking:

View commit history



