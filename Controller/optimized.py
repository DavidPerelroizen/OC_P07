from Models.action import Action
from Models.constants import max_spend_per_customer


def sortactionslist(actions_list):
    """
    Step1: This function calculates the final profit in euros based on the action cost and % profit.
    Step2: The tuple composed by the action object and the action final profit will be stored in a new list.
    Step3: This new list is then sorted in descending order based on the action final value
    Step4: The function returns the sorted list
    """
    actions_list_valuated = []
    for action in actions_list:
        actions_list_valuated.append((action, action.finalvalue()))  # Step1 + Step2
    actions_list_valuated = sorted(actions_list_valuated, key=lambda x: -x[1])  # Step3
    return actions_list_valuated  # Step4


def optimizedalgo(actions_list_sorted, first_value_rank):
    best_combination = (0, 0, 0)

    for j in range(first_value_rank + 1, len(actions_list_sorted)):
        best_option = [actions_list_sorted[first_value_rank]]
        profit_counter = actions_list_sorted[first_value_rank][1]
        spend_counter = actions_list_sorted[first_value_rank][0].value
        k = j
        while actions_list_sorted[k][0].value + spend_counter <= max_spend_per_customer and \
                k < len(actions_list_sorted) - 1:
            if actions_list_sorted[k][1] + profit_counter > profit_counter and \
                    actions_list_sorted[k][0].value + spend_counter <= max_spend_per_customer:
                best_option.append(actions_list_sorted[k])
                profit_counter += actions_list_sorted[k][1]
                spend_counter += actions_list_sorted[k][0].value
            k += 1
        if best_combination[2] < profit_counter:
            best_combination = (best_option, spend_counter, profit_counter)

    return best_combination


def optimizatorloop(actions_list):
    # Step 1: sort the actions_list depending on each action valuated benefit
    actions_list_sorted = sortactionslist(actions_list)

    best_combination = (0, 0, 0)
    for i in range(0, 50):
        if optimizedalgo(actions_list_sorted, i)[2] > best_combination[2]:
            best_combination = optimizedalgo(actions_list_sorted, i)

    return best_combination
