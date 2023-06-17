import pm4py
import pandas as pd

# Method time_to_datetime() converts the time in the dataframe to datetime format
def time_to_datetime(df):
    df['time:timestamp'] = pd.to_datetime(df['time:timestamp'], format='ISO8601', utc=True)
    return df

def check_time_format(df):
    non_iso_count = 0
    for timestamp in df['time:timestamp']:
        try:
            pd.to_datetime(timestamp, format='ISO8601')
        except ValueError:
            non_iso_count += 1
    return non_iso_count

if __name__ == "__main__":
    df = pd.read_csv('Loan_Process_update_time.csv')
    non_iso_count = check_time_format(df)
    iteration_count = len(df['time:timestamp'])
    print(f"Number of non-ISO8601 timestamps: {non_iso_count}")
    print(f"Number of iterations: {iteration_count}")






