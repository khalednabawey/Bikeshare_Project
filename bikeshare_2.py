from calendar import month, month_name, week
import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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

    months = ["January", "February", "March", "April", "May", "June", "All"]
    days = ["Saturday", "Sunday", "Monday",
            "Tuesday", "Wednesday", "Thursday", "friday", "all"]

    # Cheking whether the city and time filter inputs are valid
    city, t_filter = None, None
    while True:
        city = input(
            "Which city you want to see data from? (chicago, new york city, washington)\n").lower().strip()
        if city not in ["chicago", "new york city", "washington"]:
            print("Please, Enter a valid City(chicago, new york city, washington)!\n")
            continue

        break

    while True:
        t_filter = input(
            "Do you want to filter data by month, day, both, none?\n").lower().strip()
        if t_filter not in ["month", "day", "both", "none"]:
            print("Please, Enter a valid time filter (month, day, both, none)!\n")
            continue

        break

    # Cheking whether the day and month inputs are valid
    month, day = None, None

    while True:

        if t_filter == "month":
            # get user input for month (january, february, ... , june)
            month = input(
                "Which month you want to see data from? (january, february, ... , june)\n").capitalize().strip()
            day = "all"
            if month not in months:
                print("Please, Enter a valid month!")
                continue
        elif t_filter == "day":
            # get user input for day of week (all, monday, tuesday, ... sunday)
            day = input(
                "Which day you want to see data from? (Saturday,Sunday,Monday,Tuesday,Wednesday,Thursday,friday)\n").capitalize().strip()
            month = "all"
            if day not in days:
                print("Please, Enter a valid day!")
                continue
        elif t_filter == "both":
            month = input(
                "Which month you want to see data from? (january, february, ... , june)\n").capitalize().strip()
            day = input(
                "Which day you want to see data from? (Saturday,Sunday,Monday,Tuesday,Wednsday,Thursday)\n").capitalize().strip()
            if day not in days or month not in months:
                print("Please, Enter a valid day or moth or both!")
                continue
        else:
            print("There's no time filter.")
            month, day = "all", "all"
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

    df = pd.read_csv(
        r"C:\Users\khale\OneDrive\Documents\all-project-files\{}".format(CITY_DATA[city]))

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month == "all" and day != "all":
        df = df[day == df['Start Time'].dt.day_name()]
    elif day == "all" and month != "all":
        df = df[month == df['Start Time'].dt.month_name()]
    elif day != "all" and month != "all":
        df = df[day == df['Start Time'].dt.day_name()]
        df = df[month == df['Start Time'].dt.month_name()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month (Start Time)

    # extracting the months from the start time column
    df['month'] = df['Start Time'].dt.month_name()

    # extracting the most common month

    popular_month = df['month'].value_counts().idxmax()

    print("most frequent month: {}".format(popular_month))

    # display the most common day of week (Start Time)

    # extracting the months from the start time column
    df['day'] = df['Start Time'].dt.day_name()

    # extracting the most common month

    popular_day = df['day'].value_counts().idxmax()

    print("most frequent day: {}".format(popular_day))

    # display the most common start hour (Start Time)

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # counting the most popular hour
    popular_hour = df['hour'].value_counts().idxmax()

    print('Most Frequent Start Hour: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # extracting the most frequent start station
    popular_start_station = df['Start Station'].value_counts().idxmax()

    # display most commonly used start station
    print("Most Frequent Start Station: {}".format(popular_start_station))

    # extracting the most frequent end station
    popular_end_station = df['End Station'].value_counts().idxmax()

    # display most commonly used end station

    print("Most Frequent End Station: {}".format(popular_end_station))

    # extracting the most frequent combination of start station and end station trip
    popular_start_end_station = df.groupby(['Start Station'])[
        'End Station'].value_counts().idxmax()

    # display most frequent combination of start station and end station trip
    print("Most Frequent start-end station combination: {}".format(popular_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_time = df['Trip Duration'].sum()

    print("Total Travel Time: {}".format(total_time))

    # display mean travel time

    mean_time = df['Trip Duration'].mean()

    print("Mean Travel Time: {}".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()

    print("User Types Count:\n{}\n".format(user_types))

    if 'Gender' and 'Birth Year' in df.columns:

        # Display counts of gender (chicago,NY only)

        gender_types = df['Gender'].value_counts()

        print("Each Gender Count:\n{}\n".format(gender_types))

        # Display earliest, most recent, and most common year of birth (chicago,NY only)

        earliest_year = int(df['Birth Year'].min())
        print("Earliest Year Of Birth: {}".format(earliest_year))

        most_recent_year = int(df['Birth Year'].max())
        print("Most Recent Year Of Birth: {}".format(most_recent_year))

        most_common_year = int(df['Birth Year'].value_counts().idxmax())
        print("Most Common Year Of Birth: {}".format(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):

    loc = 0
    while True:

        answer = input(
            "Do you want to see the first 5 rows of data? (yes,no)\n").lower()

        if answer not in ["yes", "no"]:
            continue

        break

    while answer == "yes":

        print("Row Data:\n")
        print(df[loc:loc + 5])

        while True:

            answer = input(
                "Do you want to see more row data? (yes,no)\n").lower()

            if answer not in ["yes", "no"]:
                continue

            break

        if answer == "yes":
            loc += 5
            continue

        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
