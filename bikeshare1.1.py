import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    while True:
        # start of error handling
        try:
            # asking for input
            city = input("Enter the name of the city you want to explore. You can select from \n" \
                         "    chicago\n" \
                         "    new york city\n" \
                         "    washington\n" \
                         "\nWhere to? ").strip().lower()
        except:
            # sending back to input for exceptions
            print("That doesn't seem to be a valid input. Choose again!")
            continue
        if city in ("chicago", "new york city", "washington"):
            # break loop for valid input
            print("\nYour choice: {}\n".format(city))
            break
        # strengthen code against invalid input
        elif city == nyc:
            # dissolve abbreviation for New York City
            city = "new york city"
            # break loop for valid input
            print("\nYour choice: {}\n".format(city))
            break
        else:
            # sending back to input if input not valid
            print("That doesn't seem to be a valid input. " \
                  "Choose again and try to macht the exact spelling!")
            continue


    # get user input for month (all, january, february, ... , june)
    while True:
        # start of error handling
        try:
            # asking for input
            month = input("Enter the name of the month you want to explore. You can select from \n" \
                         "    all\n" \
                         "    january\n" \
                         "    february\n" \
                         "    march\n" \
                         "    april\n" \
                         "    may\n" \
                         "    june\n" \
                         "\nMarty is waiting in the DeLorean: ").strip().lower()
        except:
            # sending back to input for exceptions
            print("That doesn't seem to be a valid input. Choose again!")
            continue
        if month in MONTHS or month == 'all':
            # break loop for valid input
            print("\nYour choice: {}\n".format(month))
            break
        else:
            # sending back to input if input not valid
            print("That doesn't seem to be a valid input. " \
                  "Choose again and try to macht the exact spelling!")
            continue


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        # start of error handling
        try:
            # asking for input
            day = input("Enter the name of the day you want to explore. You can select from \n" \
                         "    all\n" \
                         "    monday\n" \
                         "    tuesday\n" \
                         "    wednesday\n" \
                         "    thursday\n" \
                         "    friday\n" \
                         "    saturday\n" \
                         "    sunday\n" \
                         "\nIt's up to you: ").strip().lower()
        except:
            # sending back to input for exceptions
            print("That doesn't seem to be a valid input. Choose again!")
            continue
        if day in DAYS or day == 'all':
            # break loop for valid input
            print("\nYour choice: {}\n".format(day))
            break
        else:
            # sending back to input if input not valid
            print("That doesn't seem to be a valid input. " \
                  "Choose again and try to macht the exact spelling!")
            continue



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

    # load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the MONTHS list to get the corresponding int
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # use the index of the DAYS list to get the corresponding int
        day = DAYS.index(day)

        # filter by day of week to create the new dataframe
        df = df[df['weekday'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # find the most common month
    popular_month = df['month'].mode()[0]
    # convert into month name
    popular_month = MONTHS[popular_month - 1]
    # display the most common month
    print(popular_month.title(), " is the most common month.\n")

    # find the most common day of week
    popular_day = df['weekday'].mode()[0]
    # convert into month name
    popular_day = DAYS[popular_day]
    # display the most common day of week
    print(popular_day.title(), " is the most common weekday.\n")

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common start hour
    popular_hour = df['hour'].mode()[0]
    # display the most common start hour
    print(popular_hour, " is the most common start hour.\n")


    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # find most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    # display most commonly used start station
    print(popular_start_station, " is the most commonly used start station.\n")


    # find most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    # display most commonly used start station
    print(popular_end_station, " is the most commonly used end station.\n")


    # find most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' - ' + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    # display most frequent combination of start station and end station trip
    print(popular_trip, " is the most frequent combination of start station and end station trip.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # calculate total travel time
    total_travel_time = int(df['Trip Duration'].sum())
    ttt_hours = total_travel_time // 3600 # get hours
    ttt_minutes = (total_travel_time % 3600) // 60 # get remaining minutes
    ttt_seconds = (total_travel_time % 3600) % 60 # get remaining seconds
    # display total travel time
    print("The total travel time was {} h {} m {} s.\n".format(ttt_hours, ttt_minutes, ttt_seconds))

    # calculate mean travel time
    mean_travel_time = int(df['Trip Duration'].mean())
    mtt_minutes = mean_travel_time // 60 # get minutes
    mtt_seconds = mean_travel_time % 60 # get remaining seconds
    # display mean travel time
    print("The mean travel time was {} m {} s.\n".format(mtt_minutes, mtt_seconds))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # calculate counts of user types
    user_types = df['User Type'].value_counts()
    # Display counts of user types
    print("User types and their counts:\n", user_types)




    try:
        # calculate counts of gender
        gender = df['Gender'].value_counts()
        # Display counts of gender
        print("\nGender and their counts:\n", gender)
    except KeyError:
        print("\nNo information about gender available for Washington.")



    try:
        # calculate earliest year of birth
        yob_early = df['Birth Year'].min()
        # calculate most recent year of birth
        yob_recent = df['Birth Year'].max()
        #calculate most common year of birth
        yob_mode = df['Birth Year'].mode()
        # Display earliest, most recent, and most common year of birth
        print("\n{} is the earliest year of birth, \n{} the most recent, \n{} the most common\n".format(yob_early, yob_recent, yob_mode))
    except KeyError:
        print("\nNo information about year of birth available for Washington.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Allow users to see raw data"""

    count = 0

    while True:
        answer = input('\nWould you like to see 5 lines of raw data? Enter yes or skip raw data with any key: ')
        # Check if response is yes, print the raw data and increment count by 5
        if answer.strip().lower() == 'yes':
            print('\nRows with index {} to {}:\n'.format(count, count+4))
            print(df.truncate(before = count, after = count+4))
            count += 5

        # otherwise break
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes to restart or any key to exit.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
