from Models.constants import max_spend_per_customer
from itertools import combinations


def findcombinations(actions_list):
    """
    This function will help determine all the possible combinations from a list of actions
    :param actions_list: list of actions objects
    :return: list of combinations of actions objects
    """
    combinations_list = []  # Initialize the combinations list

    # For all possible lengths of combinations (max len(actions_list) + 1) the loop will append the combinations
    for r in range(1, len(actions_list) + 1):
        temp_list = combinations(actions_list, r)
        for item in temp_list:
            combinations_list.append(item)

    return combinations_list


def findbestcombination(actions_list):
    """
    This function will determine which actions combination provides the more profit within the maximum spend per
    customer authorized
    :param actions_list: list of actions objects
    :return: tuple (actions list, spend_counter, profit_counter)
    """
    best_option = ([], 0, 0)  # Initialize the best_option tuple

    combinations_list = findcombinations(actions_list)  # Find all the possible combinations

    # The loop below will calculate the spend and the profit for each combination
    for option in combinations_list:
        spend_counter = 0
        profit_counter = 0
        for action in option:
            spend_counter += action.value
            profit_counter += action.finalvalue()

        # The two lines below will control whether the current iteration provides a better option
        if spend_counter <= max_spend_per_customer and profit_counter > best_option[2]:
            best_option = (option, spend_counter, profit_counter)

    return best_option
