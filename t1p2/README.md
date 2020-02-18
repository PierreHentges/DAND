# DAND Term 1, Project 2: Introduction to Python

The purpose of the project was to make use of Python to explore data fom Motivate, a bike share system provider, and compute a variety of descriptive statistics. The data related to bike share systems for three US cities : Chicago, New York City, and Washington. 

## Files
* DAND_project2_bikeshare.py: Python script
* chicago.csv, new_york_city.csv, washington.csv: data files


## Statistics Computed: 
* 1 Popular times of travel (i.e., occurs most often in the start time)
  * most common month
  * most common day of week
  * most common hour of day

* 2 Popular stations and trip
  * most common start station
  * most common end station
  * most common trip from start to end (i.e., most frequent combination of start station and end station)

* 3 Trip duration
  * total travel time
  * average travel time

* 4 User info
  * counts of each user type
  * counts of each gender (only available for NYC and Chicago)
  * earliest, most recent, most common year of birth (only available for NYC and Chicago)


You will write code to import the data and answer interesting questions about it by computing descriptive statistics. You will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

takes in raw input to create an interactive experience in the terminal that answers questions about the dataset


## Submission notes
In the code for the function station_stats(), the idea of combining value_counts() with head(1) was inspired by a discussion on stackexchange: https://codereview.stackexchange.com/a/151817

The use of divmod to convert seconds into years/days/hours/minutes/seconds in trip_duration_stats() derives from https://stackoverflow.com/a/775075
 
The code in get_filters(), load_data(), time_stats() is based on the lessons and practice problems.

The Python and Pandas documentation sites were also consulted,
e.g. http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_string.html
https://docs.python.org/3/library/string.html#format-specification-mini-language



## Project Rubric
CRITERIA   :   MEETS SPECIFICATIONS

Functionality of code : All code cells can be run without error.

Choice of data types and structures : Appropriate data types (e.g. strings, floats) and data structures (e.g. lists, dictionaries) are chosen to carry out the required analysis tasks.

Use of loops and conditional statements: Loops and conditional statements are used to process the data correctly.

Use of packages: Packages are used to carry out advanced tasks.

Use of functions: Functions are used to reduce repetitive code.

Use of good coding practices: Docstrings, comments, and variable names enable readability of the code.




