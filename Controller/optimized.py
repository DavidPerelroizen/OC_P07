from Models.action import Action
from Models.constants import max_spend_per_customer

def sortactionslist(actions_list):
    actions_list_valuated = []
    for action in actions_list:
        actions_list_valuated.append((action, action.finalvalue()))
    actions_list_valuated = sorted(actions_list_valuated, key=lambda x: -x[1])
    return actions_list_valuated


def optimizedalgo(actions_list):
    best_option = []
    # Step 1: sort the actions_list depending on each action valuated benefit
    actions_list_sorted = sortactionslist(actions_list)

    # Step 2: find the best non-optimal combination by adding the most profitable actions from top to bottom
    profit_counter = 0
    spend_counter = 0
    i = 0
    while spend_counter <= max_spend_per_customer and i < len(actions_list):
        if actions_list_sorted[i][1] + profit_counter > profit_counter and \
                actions_list_sorted[i][0].value + spend_counter <= max_spend_per_customer:
            best_option.append(actions_list_sorted[i])
            profit_counter += actions_list_sorted[i][1]
            spend_counter += actions_list_sorted[i][0].value
        i += 1
    print(best_option)
    print(spend_counter)
    print(profit_counter)

    return best_option
