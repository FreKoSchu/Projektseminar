import pm4py
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('Loan_Process_update_time.csv')
    log = pm4py.convert_to_event_log(df)
    #export the event log to xes
    pm4py.write_xes(log, 'Loan_Process_update_time.xes')