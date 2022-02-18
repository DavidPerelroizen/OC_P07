from Models.actionDB import ActionDB
from Models.action import Action
from Controller.bruteforce import findallcombinations, combinationranking
from View.views import View

path = "C:/Users/david/Documents/Openclassrooms/Python/projects/P07/OC_P07_actionDB_test.csv"
actionDB_1 = ActionDB(path)

df = actionDB_1.extractdatacsv()

combination_list = findallcombinations(df)

view = View()

combinations_ranking = combinationranking(combination_list)

for item in combinations_ranking:
    print(item)




