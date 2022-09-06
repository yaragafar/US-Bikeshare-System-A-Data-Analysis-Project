import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

acceptable_months=['all','january','february','march','april','may','june']
acceptable_days=['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Choose the city you want to filter by[chicago-new york city-washington]: ").strip().lower()
    while city not in CITY_DATA:
        city=input("Check your syntax!! Please enter one of the three cities: [chicago-new york city-washington] ").strip().lower()
        
    
    # get user input for month (all, january, february, ... , june
    month=input("Choose the month to filter by[all-january-february-...-june]:").strip().lower()
    while month not in acceptable_months:
        month=input("Check your syntax!! Please enter one of following months [all-january-february-...-june]: ").strip().lower()
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Choose the day to filter by[all-monday-tuesday-...-sunday]:").strip().lower()
    while day not in acceptable_days:
        day=input("Check your syntax!! Please Enter one of the following days ['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']: ").strip().lower()

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
    
    #loading the file according to the city the user chooses
    df=pd.read_csv(CITY_DATA[city])
    
    #converting the Start Time column to datetime module
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #creating new columns for both months and days of the week
    df['month']=df['Start Time'].dt.month
    df['day of week']=df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
    
    
    

    
    if(month!="all"):
        list_of_months=['january','february','march','april','may','june']
        month = list_of_months.index(month) + 1
       

        df=df[df['month'] == month]
        
    if(day!='all'):
        df=df[df['day of week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # display the most common month
    popular_month= df['month'].mode()[0]
    print('the most common month is: ',popular_month)

    # display the most common day of week
    popular_day= df['day of week'].mode()[0]
    print('the most common day is: ',popular_day)

    # display the most common start hour
    popular_hour= df['hour'].mode()[0]
    print('the most common hour is: ',popular_hour)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start=df['Start Station'].mode()[0]
    print('the most common start station is: ',popular_start)

    # display most commonly used end station
    popular_end=df['End Station'].mode()[0]
    print('the most common end station is: ',popular_end)


    # display most frequent combination of start station and end station trip
    #we first concatinate the two columns into a new one
    #then we get the most frequent value for this new column
    df["start and end combo"]=df["Start Station"]+' : '+df["End Station"]
    popular_combo=df["start and end combo"].mode()[0]
    print('the most common combination of start and end station is: ',popular_combo)

    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel=df['Trip Duration'].sum()
    print('Total travel time is: ',total_travel)
 
    # display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print('Mean travel time is: ',mean_travel)
    
    #display maximum travel time
    max_travel=df['Trip Duration'].max()
    print('Max travel time is: ',max_travel)
    
    #display minimum travel time
    min_travel=df['Trip Duration'].min()
    print('Min travel time is: ',min_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())
    
    # Display counts of gender (only if available)
    if'Gender' in df:
       print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    #(only if available)
    if 'Birth Year' in df:
       earliest_year=df['Birth Year'].min()
       print('Earliest Year of Birth: ',earliest_year)
       
       most_recent_year=df['Birth Year'].max()
       print('Most Recent Year of Birth: ',most_recent_year)
       
       popular_year=df['Birth Year'].mode()[0]
       print('Most Common Year of Birth: ',popular_year)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_data(df):
    """Prompts the user for an answer whether to show 5 raws of df repeatedly """
    n=0
    while True:
        show=input("Would you like to see a sample of the data?[yes/no]: ").strip().lower()
        if show=='yes':
            print(df[n:n+5])
            n+=5
        else:
            break    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        #Checking if user wants to show a sample of the data
        show_data(df)
        
        #Checking if user wants (time statistics)
        calc_time=input("Woyld you like to show time statistics for data? [yes/no]: ").strip().lower()
        if calc_time=='yes':
            time_stats(df)
     
        #Checking if user wants (station statistics)
        calc_station=input("Woyld you like to show station statistics for data? [yes/no]: ").strip().lower()
        if calc_station=='yes':
            station_stats(df)
       
        #Checking if user wants (trip duration statistics)
        calc_trip=input("Woyld you like to show trip durartion statistics for data? [yes/no]: ").strip().lower()
        if calc_trip=='yes':
            trip_duration_stats(df)
        
        #Checking if user wants (user statistics)
        calc_user=input("Woyld you like to show user statistics for data? [yes/no]: ").strip().lower()
        if calc_user=='yes':
            user_stats(df)

        #Cheching if user wants to restart or quit
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
