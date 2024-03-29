import time
import pandas as pd
import numpy as np

CITY_DATA = {   'washington': 'washington.csv',
                'chicago': 'chicago.csv',
                'new york': 'new_york_city.csv'
               }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input('Would you like to see data for Chicago, New York, or Washington?').lower()
        if city not in ('chicago', 'new York','washington'):
            print ( '      Be sure you enter vaild city with Capitile letter' )
            continue
        else:
         break



    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        month = input('Which month All - January, February, March, April, May, or June?').lower()
        if month in ('all', 'january', 'february', 'march', 'april', 'may',  'june' ):
            break
        else:
            print ( '      Be sure you enter vaild month with Capitile letter ' )
            continue


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input('Which day All - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').lower()
        if day not in ('all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print ( '      Be sure you enter vaild day with Capitile letter ' )
            continue
        else:
         break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may',  'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month= df['month'].mode()[0]
    print('Common Month:',common_month)

    # TO DO: display the most common day of week
    common_day= df['day'].mode()[0]
    print('Common Day:',common_day)


    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Popular Hour:',popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df["Start Station"].mode()[0]
    print (popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station=df["End Station"].mode()[0]
    print (popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination= df.groupby(['Start Station','End Station']).count().idxmax().head(1)
    print('most frequent combination of start station and end station trip : \n',frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('start time',start_time)

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].count()
    print('total travel time',total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('user_types:', user_types)

    # TO DO: Display counts of gender

    try:
        Gender = df['Gender'].value_counts()
        print('Gender:\n',Gender)
    except KeyError :
        print ( 'Gender: \nsorry no Gender data for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].max()
        m_recent = df['Birth Year'].min()
        common_year = df['Birth Year'].mode()
        print ('Earliest year of birth:',earliest,'\n most recent year of birth:',m_recent,'\n common year of birth:',common_year)
    except KeyError :
        print ( 'birth of yesr: \nsorry no data of birth of yesr for this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        show_data = input('\nWould you like to see the raw data? Enter yes or no.\n')
        start = 0
        end = 5
        while show_data.lower() == 'yes':
           print(df.iloc[start:end])
           show_data1 = input('\nWould you like to see the raw data again? Enter yes or no.\n')
           if show_data1.lower() == 'yes':
                start+= 5
                end += 5
           else:
                break



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
   main()
