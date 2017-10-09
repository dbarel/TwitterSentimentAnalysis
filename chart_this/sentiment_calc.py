import csv
import datetime


def sentiment_calc(file):
    """Open csv file and will return the:
    monthly, daily, hourly count of sentiment as dict"""

    now = float((datetime.datetime.utcnow() - datetime.datetime(2017, 1, 1)).total_seconds())

    hour = day = month = {'1': 0, '0': 0, '-1': 0}
    with open(file, newline='') as csv_file:
        for row in reversed(list(csv.reader(csv_file, delimiter=','))):

            time_delta = now - float(row[0])
            if time_delta <= 2592000:  # in month there are  60s*60m*24h*30d
                month[row[1]] += 1
                if time_delta <= 86400:
                    day[row[1]] += 1
                    if time_delta <= 3600:
                        hour[row[1]] += 1
            else:
                break

    return month, day, hour


if __name__ == '__main__':
    monthly_collection, day_collection, hour_collection = sentiment_calc(file='sentiment.csv')
    print(monthly_collection)
    print(day_collection)
    print(hour_collection)
