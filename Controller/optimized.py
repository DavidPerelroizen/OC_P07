from Models.action import Action
from Models.constants import max_spend_per_customer


def sortactionslist(actions_list):
    actions_list_valuated = []
    for action in actions_list:
        actions_list_valuated.append((action, action.finalvalue()))
    actions_list_valuated = sorted(actions_list_valuated, key=lambda x: -x[1])
    return actions_list_valuated


def optimizedalgo(actions_list, first_value_rank):
    best_option = []
    # Step 1: sort the actions_list depending on each action valuated benefit
    actions_list_sorted = sortactionslist(actions_list)

    # Step 2: find the best combination by adding the most profitable actions from top to bottom
    profit_counter = 0
    spend_counter = 0
    i = first_value_rank
    while spend_counter <= max_spend_per_customer and i < len(actions_list):
        if actions_list_sorted[i][1] + profit_counter > profit_counter and \
                actions_list_sorted[i][0].value + spend_counter <= max_spend_per_customer:
            best_option.append(actions_list_sorted[i])
            profit_counter += actions_list_sorted[i][1]
            spend_counter += actions_list_sorted[i][0].value
        i += 1
    best_combination = (best_option, spend_counter, profit_counter)
    return best_combination


def optimizatorloop(actions_list):
    best_combination = (0, 0, 0)
    for i in range(0, len(actions_list)):
        if optimizedalgo(actions_list, i)[2] > best_combination[2]:
            best_combination = optimizedalgo(actions_list, i)

    return best_combination
