import pendulum

most_recent = pendulum.datetime(2022, 8, 20)
end_date = pendulum.datetime(2023, 2, 1)

msrf = most_recent.to_formatted_date_string()
esrf = end_date.to_formatted_date_string()

period = pendulum.period(most_recent, end_date)

print("{} weeks from dates {} to {}".format(
    end_date.diff(most_recent).in_weeks(),
    msrf, esrf))

for dt in period.range('weeks'):
    print(dt.to_formatted_date_string())