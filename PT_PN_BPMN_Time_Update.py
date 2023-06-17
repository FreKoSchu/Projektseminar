import pm4py
from pm4py.visualization.petri_net import visualizer
import pandas as pd


if __name__ == "__main__":
    log=pm4py.read_xes('/Users/frederikschubert/PycharmProjects/Process_loan/Loan_Process_update_time.xes')
    # bpmn=pm4py.discover_bpmn_inductive(log)
    # process_tree=pm4py.discover_process_tree_inductive(log)
    net, im, fm = pm4py.discover_petri_net_inductive(log)
    gviz = visualizer.apply(net, im, fm, parameters={visualizer.Variants.WO_DECORATION.value.Parameters.DEBUG: True})
    visualizer.view(gviz)
    # pm4py.view_bpmn(bpmn)
    # pm4py.view_process_tree(process_tree)
    pm4py.view_petri_net(petri)
