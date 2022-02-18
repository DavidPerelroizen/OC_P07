from Models.action import Action


def sortactionslist(actions_list):
    actions_list_valuated = []
    for action in actions_list:
        actions_list_valuated.append(action, action.finalvalue())
    actions_list_valuated = sorted(actions_list_valuated, key=lambda x: x[1])
    return actions_list_valuated


def optimizedalgo(actions_list):
    best_option = 0
    # Step 1: sort the actions_list depending on each action valuated benefit
    actions_list_sorted = sortactionslist(actions_list)
    return best_option
