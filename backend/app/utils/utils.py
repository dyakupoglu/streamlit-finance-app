import random
import datetime


def generate_random_series(start_date, days=365):
    series_only = []
    series_with_strings = []

    for i in range(days):
        current_date = start_date + datetime.timedelta(days=i)
        val1 = random.uniform(10, 100)
        val2 = random.uniform(100, 200)
        val3 = random.uniform(-50, 50)
        series_only.append(
            {
                "date": current_date.isoformat(),
                "value1": val1,
                "value2": val2,
                "value3": val3,
            }
        )
        series_with_strings.append(
            {
                "date": current_date.isoformat(),
                "value1": val1,
                "value2": val2,
                "value3": val3,
                "note": f"Generated for {current_date.isoformat()}",
            }
        )

    return series_only, series_with_strings
