from View.views import View
from Models.actionDB import ActionDB
from Controller.bruteforce import findallcombinations, combinationranking


def main():
    view = View()
    path = "OC_P07_actionDB.csv"

    action_db = ActionDB(path)
    actions_list = action_db.extractdatacsv()

    combinations_list = findallcombinations(actions_list)
    best_option = combinationranking(combinations_list)[0]

    view.displaybestcombination(best_option)


if __name__ == '__main__':
    main()