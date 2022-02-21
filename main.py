from View.views import View
from Models.actionDB import ActionDB
from Controller.bruteforce import findallcombinations, combinationranking
from Controller.optimized import optimizedalgo, optimizatorloop


def main():
    view = View()
    path = "csv_db/dataset1_Python+P7.csv"

    action_db = ActionDB(path)
    actions_list = action_db.extractdatacsv()

    user_choice = view.displaymainmenu()

    if user_choice == 'B':
        combinations_list = findallcombinations(actions_list)
        best_option = combinationranking(combinations_list)[0]
        view.displaybestcombination(best_option)

    elif user_choice == 'O':
        best_combination = optimizatorloop(actions_list)
        view.displaybestcombinationoptimized(best_combination)

    else:
        exit()


if __name__ == '__main__':
    main()
