from Models.constants import main_menu_list

class View:

    def displaybestcombination(self, best_combination):
        print(f"""
------------------------------------------------------
                FINAL RECOMMENDATION
------------------------------------------------------
Actions to purchase: {best_combination[0]}
Initial investment: {best_combination[1]} euros
Benefit after two years: {best_combination[2]} euros
------------------------------------------------------
""")

    def displaymainmenu(self):
        print(f"""
        ------------------------------------------------------
                        MAIN MENU
        ------------------------------------------------------
        Trigger bruteforce --> press B
        Trigger optimized --> press O
        ------------------------------------------------------
        """)
        user_choice = ''
        while user_choice not in main_menu_list:
            user_choice = input('        Press the appropriate key + ENTER : ').upper()
