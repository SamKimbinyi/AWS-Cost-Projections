from currency_converter import CurrencyConverter
import sys
# https://pypi.org/project/CurrencyConverter/
c = CurrencyConverter()

def gigabytes_to_bytes(quantity):
    """Takes a quantity in GB and returns it's equivalent number of Bytes."""
    return quantity * pow(1024,3)

def bytes_to_gigabytes(quantity):
    """Takes a quantity in Bytes and returns it's equivalent number of GB."""
    return quantity / pow(1024,3)

def gb_months_to_cost(gb_months):
    """Takes an amount of GB Months and returns the AWS cost."""
    # see https://aws.amazon.com/s3/pricing/
    cost = 0
    accounted_for = 0
    while(gb_months):
        if accounted_for < 50 * 1000:
            quantity = min(50*1000,gb_months)
            price = 0.023
        elif accounted_for < 500 * 1000:
            quantity = min(450*1000,gb_months)
            price = 0.022
        else:
            quantity = gb_months
            price = 0.021
        accounted_for += quantity
        cost += quantity * price
        gb_months -= quantity
    return c.convert(cost, 'USD', 'GBP')


def run_simulation(initial_bucket_size=0, average_daily_input=0, days_to_run=0):
    """Run a simulation to determine S3 bucket costs.

    Keyword arguments:
    initial_bucket_size -- initial volume of data in bucket. (GB)
    average_daily_input -- data to be added to S3 bucket per day (GB)
    days_to_run -- number of days to simulate costs for.
    """
    # see https://github.com/awsdocs/amazon-s3-developer-guide/blob/master/doc_source/aws-usage-report-understand.md
    cumulative_byte_hours = 0
    current_capacity = initial_bucket_size

    for day in range(days_to_run):
        cumulative_byte_hours += gigabytes_to_bytes(current_capacity) * 24
        current_capacity += average_daily_input

    gb_months = bytes_to_gigabytes(cumulative_byte_hours) / 24
    total_cost = gb_months_to_cost(gb_months)
    print("Bucket storage size after {} days: {} GB\nTotal GB-Months: {}\nTotal Cost: £{}".format(
        days_to_run,
        int(current_capacity),
        gb_months,total_cost
    ))

if __name__ == "__main__":
    [initial_bucket_size,daily_input,days_to_run] = [int(arg) for arg in sys.argv[1:]]
    run_simulation(initial_bucket_size, daily_input, days_to_run)
