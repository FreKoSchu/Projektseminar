import pm4py
from pm4py.algo import decision_mining
from pm4py.visualization.petri_net import visualizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import pydotplus


if __name__ == "__main__":
    log = pm4py.read_xes('/Users/frederikschubert/PycharmProjects/Process_loan/BPI Challenge 2017.xes')
    net, im, fm = pm4py.discover_petri_net_inductive(log)
    gviz = visualizer.apply(net, im, fm, parameters={visualizer.Variants.WO_DECORATION.value.Parameters.DEBUG: True})
    visualizer.view(gviz)
    X, y, class_names = decision_mining.apply(log, net, im, fm, decision_point="p_4")

    # Perform decision tree classification
    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    # Export decision tree visualization
    dot_data = export_graphviz(clf, out_file=None, feature_names=class_names, class_names=class_names)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_png('decision_tree.png')


