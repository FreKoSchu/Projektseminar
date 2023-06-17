import pm4py
import pandas as pd

# check datframe dtypes and return array of dtypes
def check_dtypes(df):
    return df.dtypes

#main method
if __name__ == "__main__":
    df = pd.read_csv('Loan_Process_update_time.csv')

    # change timestamp to datetime
    df['time:timestamp'] = pd.to_datetime(df['time:timestamp'], format='ISO8601', utc=True)
    print(check_dtypes(df))
    log = pm4py.convert_to_event_log(df)
    #export the event log to xes
    pm4py.write_xes(log, 'Loan_Process_update_time.xes')
