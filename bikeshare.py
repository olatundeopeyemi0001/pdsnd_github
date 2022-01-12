import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    #--requesting user to add city
    while True:
        city = input ('would you like to see data for Chicago, Newyork or Washington: ').lower()
        if city not in (CITY_DATA):
            print("\nOOPS! Sorry we cant help you with that, kindly pick another city.")
        else:
            break
    

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input('\nkindly specify month of choice in form of an integer with /  Jan ==> 1, Feb ==> 2 , or all. ').lower()
        if month not in ('1' , '2' , '3' , '4' ,'5' , ' 6' , 'all'):
            print ("\nOuch! that's not available at the moment , do check your input or select another month again.")
            
        else:
            break        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    #Asking the user for day of the week 
    while True:
        day = input ('Kindly pick your day of the week OR all: ').lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print('\nsorry, you put the wrong day, try again')
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    df['weekday'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        df = df[df['month'] == int(month)]
    if day != 'all':
        df = df[df['weekday'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month//// where mcm is an a short form of most_common month.
    mcm = df ['month'].mode()[0]
    print ('The most common month is : ', mcm)

    # TO DO: display the most common day of week/// mcd equals Most Common Day
    mcd = df ['weekday'].mode()[0]
    print ('\nThe most common day of the week is: ', mcd)
    
    # TO DO: display the most common start hour /// mch equals the most common hour
    mch = df ['Start Time'].dt.hour
    mch = mch.mode()[0]
    print ('\nThe most common hour of the day is: ', mch)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station/// mcus is equal to Most Common Used Start Station

    mcuss =  df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is: ', mcuss)
    
    # TO DO: display most commonly used end station
    mcues = df['End Station'].mode()[0]
    print ('\nThe most commonly used end station is: ', mcues)
    
    
    # TO DO: display most frequent combination of start station and end station trip//mcc is equal to most common combo
    mcc =  df['Start Station'] + 'and' + df['End Station']
    mcc = mcc.mode()[0]
    print ('\nThe most common combination of stations is:', mcc)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ('\nThe Total travel time of the duration is: {} seconds.'.format(total_travel_time))

    # TO DO: display mean travel time // mean trvavel talks about the mean average time calculated from the entire time date
    avg_travel_time = df['Trip Duration'].mean()
    print('\nThe mean or average travel time is: {} seconds.'.format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types// utc equal to user type count
    utc = df['User Type'].value_counts()
    print('\n The user type counts are: {}.'.format(utc))
    
    
    # TO DO: Display counts of gender

    while True:
        try:
            count_gender = df['Gender'].value_counts(dropna=False)
            print('\nThe gender counts available classifications are: {}.'.format(count_gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    # most common year of birth == mcy_birth
    # most recent year of birth == mry_birth
    # earliset  year of birth == ey_birth
    
            ey_birth = df['Birth Year'].min() #earliest
            mry_birth = df['Birth Year'].iloc[0] #most recent year
            mcy_birth = df['Birth Year'].mode()[0] #most common
    
            print('\nThe earliest year of birth is {}; The most recent year of birth is {}, and the most common year of birth is {}.'.format(ey_birth,mry_birth,mcy_birth))
                  
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            break
        except:
            print('\nGender and birth data for this month not found')
            break
        
def display_data_request(df):
    """ displays user request on bikeshare data"""
    pd.set_option('display.max_columns',200)  #use this line of code at the start of this function to enable pandas to display all the columns in your dataframe when printing.
    view_data = input('\nwould you be willing to view 10 rows of individual trip data? enter yes or no\n').lower()
    start_loc = 0
    while (view_data != 'no'):
        print(df.iloc[start_loc:start_loc+10])
        start_loc += 10
        view_data = input('\nwould you be willing to view 10 rows of individual trip data? enter yes or no\n').lower()        
 


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data_request(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    