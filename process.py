import pm4py
if __name__ == "__main__":
    log = pm4py.read_xes('/Users/frederikschubert/PycharmProjects/Process_loan/BPI Challenge 2017.xes')
    process_model = pm4py.discover_bpmn_inductive(log)
    pm4py.view_bpmn(process_model)

