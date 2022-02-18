from Models.actionDB import ActionDB
from Models.action import Action
from Controller.bruteforce import findallcombinations, combinationranking
from View.views import View
from Controller.optimized import optimizedalgo

path = "csv_db/dataset1_Python+P7.csv"
view = View
action_db = ActionDB(path)
actions_list = action_db.extractdatacsv()

best_option = optimizedalgo(actions_list)
print(best_option)








