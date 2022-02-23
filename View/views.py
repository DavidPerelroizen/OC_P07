from Models.constants import main_menu_list
from Models.action import Action


class View:

    def displaybestcombination(self, best_combination):
        """
        This view is used to display the result of the brute force algorithm
        :param best_combination: tuple made of a list of actions, the sum of the costs of the actions in the list,
        and the sum of the final.value() of each action in the list
        :return: print below
        """
        print(f"""
------------------------------------------------------
            FINAL RECOMMENDATION BRUTE
------------------------------------------------------
Actions to purchase: {best_combination[0]}
Initial investment: {best_combination[1]} euros
Benefit after two years: {best_combination[2]} euros
------------------------------------------------------
""")

    def displaymainmenu(self):
        """
        Displays the main menu option and enables the user to make a choice for which algorithm he wishes to execute
        :return: the user_choice variable
        """
        print("""
        ------------------------------------------------------
                        MAIN MENU
        ------------------------------------------------------
        Trigger bruteforce --> press B
        Trigger optimized --> press O
        Exit program --> press X
        ------------------------------------------------------
        """)
        user_choice = ''
        while user_choice not in main_menu_list:
            user_choice = input('        Press the appropriate key + ENTER : ').upper()

        return user_choice

    def displaybestcombinationoptimized(self, best_option):
        """
        This view is used to display the result of the optimized algorithm
        :param best_option: tuple containing an action list, the sum of the cost of each action in the list, and the
        sum of the final values of each action in the list
        :return: print displaying the information about the best option
        """
        print(f"""
        ------------------------------------------------------
                    FINAL RECOMMENDATION OPTIMIZED
        ------------------------------------------------------
        Actions to purchase: """)
        for action in best_option[0]:
            action[0].displayaction()
        print(f"""
        Initial investment: {best_option[1]} euros
        Benefit after two years: {best_option[2]} euros
        ------------------------------------------------------
        """)
