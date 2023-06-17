import pm4py
import pandas as pd

if __name__ == "__main__":
    log = pm4py.read_xes('/Users/frederikschubert/PycharmProjects/Process_loan/BPI Challenge 2017.xes')
    dataframe = pm4py.convert_to_dataframe(log)
    dataframe.to_csv('Loan_Process.csv')
    print(dataframe)
    print(dataframe.columns)
    print(dataframe['concept:name'])





