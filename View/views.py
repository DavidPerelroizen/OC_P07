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

