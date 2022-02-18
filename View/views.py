from Models.constants import main_menu_list
from Models.action import Action


class View:

    def displaybestcombination(self, best_combination):
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
