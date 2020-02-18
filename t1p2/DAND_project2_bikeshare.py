import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Filtering can be by month, by day of the week, or both. However it is not possible to filter by several months, or several days - either one or all.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        #defining interactive messages as string variables to facilitate consistency of input questions
        message1="Which city would you like to find out about - Chicago, New York or Washington? (C, N, W)"
        message2="To choose a city, simply enter the first letter of its name - type C, N or W for Chicago, New York, or Washington."
        message3="You chose to look at bike share data for {}."
        try:
            city=input(message1).lower()
            city = {'c': 'chicago', 'n':'new york city', 'w' : 'washington'}[city]
            break
        except:
            print(message2)     #more detail for how to input data if there's an error
        finally:
            #display the chosen city
            print(message3.format(city.capitalize()))


    # get user input for month (all, january, february, ... , june)
    print("The data can optionally be filtered by month and/or by day of the week.")
    while True:
        message1="If you would like to filter by month, please enter the month (Jan, Feb, Mar, Apr, May, Jun). Otherwise, just press enter."
        message2="To choose a month, simply enter the first 3 letters of its name : type Jan, Feb, Mar, Apr, May, Jun (there are no data are available after June. If you don't want to filter by month, hit enter."
        message3="You chose to look at data for {month_filtered}."
        try:
            month=input(message1).lower()
            if month=="":
                month="all"  #define the default value of "all" for no filtering
            else:
                month = {'jan' : 'january', 'feb' : 'february', 'mar' : 'march', 'apr' : 'april', 'may' : 'may', 'jun' : 'june'}[month]
            break
        except:
            print(message2)
        finally:
            #Display the by month filtering chosen, conditional on whether filtering has been set
            print(message3.format(month_filtered="all months" if month=="all" else month.capitalize()))


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        message1="If you would like to filter by day of the week, please enter the day (Mon, Tue, Wed, Thr, Fri, Sat, Sun). Otherwise just press enter."
        message2="If you want to filter by day, you need to choose a day: simply enter the first 3 letters of its name - type Mon, Tue, Wed, Thr, Fri, Sat, Sun.  If you don't want to filter by month, hit enter."
        message3="You chose to look at data for {day_filtered}."
        try:
            day=input(message1).lower()
            if day=="":
                day="all"  #define the default value of "all" for no filtering
            else:
                day = {'mon' : 'monday', 'tue' : 'tuesday', 'wed' : 'wednesday', 'thr' : 'thursday', 'fri' : 'friday', 'sat' : 'saturday', 'sun' : 'sunday'}[day]
            break
        except:
            print(message2)
        finally:
            #Display the day filter chosen, conditional on whether filtering has been set
            print(message3.format(day_filtered="all days of the week" if day=="all" else day.capitalize()))
    #give the user confirmation of their chosen filters.
    if month=='all' and day=='all':
        print("OK - let's look at all bikeshare data from {}. You chose no additional filters.".format(city.capitalize()))
    elif month!='all' and day!='all':
        print("OK - let's look at bikeshare data from {} filtered to only include data from {} and {}.".format(city.capitalize(),month.capitalize(),day.capitalize()))
    else:
        print("OK - let's look at bikeshare data from {} filtered to only include data from {filter}.".format(city.capitalize(),filter=month.capitalize() if month!='all' else day.capitalize()))


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month #format for month is 1-12, with jan=1
    # the new Series df['month'] is useful even if no filtering as it will be used in the function time_stats()
    df['day_of_week'] = df['Start Time'].dt.dayofweek	# format for day of the week is 0-6, with Mon = 0, Sun=6
    if month != 'all':
        month = 1 + ['january', 'february', 'march', 'april', 'may', 'june'].index(month) # get month as integer in same format as df['month'] Series, accounting for zero-based indexing
        df=df[df['month'] == month] # actual filtering step
    if day != 'all':
        day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'].index(day) # get day ow in dame format as df['day_of_week']
        df=df[df['day_of_week'] == day] # filtering applied to df

    return df


def time_stats(df,month='all',day='all'):
    """
    Displays statistics on the most frequent times of travel.
    The month and day arguments serve to check if data are filtered by month/day, to avoid misleadingly identifying the filter as most common month/day of travel.

    Args:
            df - Pandas DataFrame containing city data
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month=='all':         #only meaningful if data are not restricted to one month already
        popular_month = df['month'].mode()[0] # display the most common month
        print("The most frequent month of travel is {}.".format(['January', 'February', 'March', 'April', 'May', 'June'][popular_month-1])) #adjust for zero based indexing


    # display the most common day of week
    if day=='all':        #only meaningful if data are not restricted to one day of the week already
        popular_day = df['day_of_week'].mode()[0] # display the most common day of week
        print("The most frequent day of travel is {}.".format( ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][popular_day]))


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0] # display the most common start hour
    print("The most frequent hour to start a journey is {} hours.".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    In the case where there are two or more results for the most popular stations/trips, only one is displayed.
    If the possibility of tied most popular stations/trips is considered important, the function could trivially be adapted to display the top 2 or 3 most popular stations.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].value_counts().head(1) #value_counts returns ordered Series, in combination with head(1) method gives most popular station. If the possibility of tied most popular stations matters, consider using head(3) to display the top 3 most popular stations and their number of trips.
    print("The most popular start station is {}, where {} trips started.".format(popular_start.index[0], popular_start.values[0]))


    # display most commonly used end station
    popular_end = df['End Station'].value_counts().head(1)
    print("The most popular end station is {}, where {} trips finished.".format(popular_end.index[0], popular_end.values[0]))


    # display most frequent combination of start station and end station trip
    df['Journey'] = df['Start Station'] + " to " + df['End Station'] # using "to" already formats the journey appropriately for printing
    popular_journey = df['Journey'].value_counts().head(1)
    print("The most popular trip was cycling from {}, with {} trips.".format(popular_journey.index[0], popular_journey.values[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    For the average duration, both the mean and the median are given, as a relatively small number of lengthy trips can distort the mean as a measure of the average trip duration.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = int(df['Trip Duration'].sum())
    #convert to more meaningful format, using divmod()
    total_travel_time_years, remaining = divmod(total_travel_time,60*60*24*365)
    total_travel_time_days, remaining = divmod(remaining,60*60*24)
    total_travel_time_hours, remaining = divmod (remaining,60*60)
    total_travel_time_minutes, total_travel_time_seconds = divmod (remaining,60)
    print("The total travel time for all users is {} seconds. This corresponds to {} years, {} days, {} hours, {} minutes and {} seconds!".format(total_travel_time, total_travel_time_years, total_travel_time_days, total_travel_time_hours, total_travel_time_minutes, total_travel_time_seconds))


    # display mean travel time
    travel_time_mean = int(df['Trip Duration'].mean())
    travel_time_median = int(df['Trip Duration'].median())
    print("The mean travel time is {} minutes and {} seconds, while the median travel time is {} minutes and {} seconds.".format(*divmod(travel_time_mean,60),*divmod(travel_time_median,60)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Users break down into the following categories:")
    print(user_types.to_string(),"\n")


    # Display counts of gender
    if 'Gender' in df.columns: # does not exist for all datasets, check first
        user_gender = df['Gender'].value_counts()
        print("The gender distribution of users is as follows:")
        print(user_gender.to_string(),"\n")


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:  # does not exist for all datasets, check first
        born_earliest = int(df['Birth Year'].min())
        born_most_recent = int(df['Birth Year'].max())
        born_most_common = int(df['Birth Year'].mode())
        print("According to available data, the oldest user was born in {}, the youngest was born in {}, while the most common year of birth is {}.".format(born_earliest , born_most_recent, born_most_common))
        if born_earliest<1917 :
            print("There appear to be some rather elderly cyclists roaming the streets of {}!".format(city.capitalize()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    """show raw data for the .csv file of the city given in the argument, five lines at a time"""
    f = open(CITY_DATA[city], 'r') #open the city's .csv file - it will be closed at the end of the function
    message1="Would you like to see the raw data for {}? If so, hit enter. If not, press any key followed by enter."
    message2="Would you like to see more raw data? If so, hit enter. If not, press any other key followed by enter."
    display_raw=input(message1.format(city.capitalize())) #no error handling necessary as any input is valid
    counter=1
    while display_raw=="":
        for __ in range(counter,counter+5):     # a for loop is easiest for printing 5 lines at a time, but the __ variable isn't used in the loop
            print("line {} from file {}:".format(counter,CITY_DATA[city]))
            print(f.readline())
            counter += 1
        display_raw = input(message2)
    f.close()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
