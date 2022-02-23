from Models.constants import max_spend_per_customer


def sortactionslist(actions_list):
    """
    This function helps to created a sorted actions list based on a mere actions objects list
    :param actions_list: contains action objects
    :return: list of tuple (action object, action benefit %, action final value) sorted by descending action benefit%
    """
    actions_list_valuated = []  # Initialize the output list
    for action in actions_list:
        # For each action create a tuple (action object, action benefit %)
        actions_list_valuated.append((action, action.benefit))

    # Sort the list by descending action benefit percentage
    actions_list_valuated = sorted(actions_list_valuated, key=lambda x: -x[1])

    return actions_list_valuated


def optimizedalgo(actions_list_sorted, first_value_rank):
    """
    Within a list of actions sorted and for a given first value index, this function will find the combination with
    the greater profit
    :param actions_list_sorted: list of tuple (action object, action benefit %) sorted by
    descending action benefit%
    :param first_value_rank: integer
    :return: tuple (actions list, sum of actions costs, sum of actions final values)
    """
    best_combination = (0, 0, 0)  # Initialize the output tuple

    """
    For a given starting point, the code will try all the combination for different second points and return the
    combination that gives the higher profit
    """
    for j in range(first_value_rank + 1, len(actions_list_sorted)):
        # Initialize the combination variables with the starting point
        best_option = [actions_list_sorted[first_value_rank]]
        profit_counter = actions_list_sorted[first_value_rank][0].finalvalue()
        spend_counter = actions_list_sorted[first_value_rank][0].value

        k = j  # k will be used to iterate through the actions_list_sorted from the second starting point j

        # The "while" loop will help check we don't go over the maximum spend and that k index doesn't get out of range
        while actions_list_sorted[k][0].value + spend_counter <= max_spend_per_customer and \
                k < len(actions_list_sorted) - 1:

            # The "if" controls that the iteration is still within the constraints of max spend
            if actions_list_sorted[k][0].finalvalue() + profit_counter > profit_counter and \
                    actions_list_sorted[k][0].value + spend_counter <= max_spend_per_customer:
                best_option.append(actions_list_sorted[k])  # Add the action to the list of the combination
                profit_counter += actions_list_sorted[k][0].finalvalue()  # Increment profit with the current iteration
                spend_counter += actions_list_sorted[k][0].value  # Increment the spend counter

            k += 1

        # Check if the new combination is better than the current best and replaces it if so
        if best_combination[2] < profit_counter:
            best_combination = (best_option, spend_counter, profit_counter)

    return best_combination


def optimizatorloop(actions_list):
    """
    This function will help in finding the most profitable actions combination
    :param actions_list: contains action objects
    :return: tuple (actions list, sum of actions costs, sum of actions final values)
    """
    # Sort the actions_list depending on each action benefit percentage
    actions_list_sorted = sortactionslist(actions_list)

    best_combination = (0, 0, 0)  # Initialize the output tuple

    # The loop below will test the combinations for different starting points in the actions list and return the best
    for i in range(0, 50):
        if optimizedalgo(actions_list_sorted, i)[2] > best_combination[2]:
            best_combination = optimizedalgo(actions_list_sorted, i)

    return best_combination
