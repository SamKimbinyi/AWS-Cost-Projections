import sys

from currency_converter import CurrencyConverter

c = CurrencyConverter()


def gigabytes_to_bytes(quantity: float) -> float:
    """
    :param quantity: GB quantity
    :returns: The byte conversion of the GB input
    """
    return quantity * pow(1024, 3)


def bytes_to_gigabytes(quantity: float) -> float:
    """

    :param quantity: Byte quantity:
    :return: The GB conversion of the Byte input
    """
    return quantity / pow(1024, 3)


def gb_months_to_cost(gb_months: float) -> float:
    """
    see https://aws.amazon.com/s3/pricing/

    :param gb_months: The timeframe in months to cost for
    :return: The total cost for the timeframe
    """
    cost = 0
    accounted_for = 0
    while gb_months:
        if accounted_for < 50 * 1000:
            quantity = min(50 * 1000, gb_months)
            price = 0.023
        elif accounted_for < 500 * 1000:
            quantity = min(450 * 1000, gb_months)
            price = 0.022
        else:
            quantity = gb_months
            price = 0.021
        accounted_for += quantity
        cost += quantity * price
        gb_months -= quantity
    return c.convert(cost, 'USD', 'GBP')


def run_simulation(initial_bucket_size=0, average_daily_input=0, average_daily_output=0, days_to_run=0):
    """Run a simulation to determine S3 bucket costs.


    :param  initial_bucket_size: initial volume of data in bucket. (GB)
    :param average_daily_input: data to be added to S3 bucket per day (GB)
    :param  days_to_run: number of days to simulate costs for.
    """
    # see https://github.com/awsdocs/amazon-s3-developer-guide/blob/master/doc_source/aws-usage-report-understand.md
    cumulative_byte_hours = 0
    current_capacity = initial_bucket_size

    for day in range(days_to_run):
        cumulative_byte_hours += gigabytes_to_bytes(current_capacity) * 24
        current_capacity += average_daily_input - average_daily_output

    gb_months = bytes_to_gigabytes(cumulative_byte_hours) / 24
    total_cost = gb_months_to_cost(gb_months)
    print(f"Bucket storage size after {days_to_run} days: {int(current_capacity)} GB\n"
          f"Total GB-Months: {gb_months}\nTotal Cost: £{total_cost}")


if __name__ == "__main__":
    [initial_bucket_size, daily_input, daily_output, days_to_run] = [int(arg) for arg in sys.argv[1:]]
    run_simulation(initial_bucket_size, daily_input, daily_output, days_to_run)
