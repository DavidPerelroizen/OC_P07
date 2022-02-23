from View.views import View
from Models.actionDB import ActionDB
from Controller.bruteforce2 import findbestcombination
from Controller.optimized import optimizatorloop


def main():
    view = View()
    path = "csv_db/dataset1_Python+P7.csv"  # To be updated depending on the targeted dataset

    # Transforms the CSV file into an ActionDB object and extracts the data
    action_db = ActionDB(path)
    actions_list = action_db.extractdatacsv()

    # Main menu display
    user_choice = view.displaymainmenu()

    # Bruteforce execution
    if user_choice == 'B':
        best_option = findbestcombination(actions_list)
        view.displaybestcombination(best_option)

    # Optimized algorithm execution
    elif user_choice == 'O':
        best_combination = optimizatorloop(actions_list)
        view.displaybestcombinationoptimized(best_combination)

    else:
        exit()


if __name__ == '__main__':
    main()
