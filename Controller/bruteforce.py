from Models.constants import max_spend_per_customer


def findallcombinations(actions_list):
    """
    This function will help to figure out all the possible combinations between all the actions
    (each action can be used only once).
    The function will also check that the spend doesn't go over 500€
    """
    final_combinations_list = []

    for i in range(len(actions_list)):
        final_combinations_list.append([actions_list[i]])  # Every action alone is a combination

        # In the script below we test the different combinations
        # within the limit of 500€ initial investment
        for j in range(len(actions_list)):
            counter = int(actions_list[i].value)  # Will help to respect the max 500€ spend per customer
            combination = [actions_list[i]]

            for k in range(j, len(actions_list)):
                if counter + int(actions_list[k].value) <= max_spend_per_customer and k != i:
                    counter += int(actions_list[k].value)
                    combination.append(actions_list[k])
                else:  # If the ceiling of 500€ is reached or if we already used the action we skip
                    continue

            final_combinations_list.append(sorted(combination, key=lambda x: x.name))

    final_combinations_list_nodupl = []
    # The loop below helps to remove the duplicated combinations
    for item in final_combinations_list:
        if item not in final_combinations_list_nodupl:
            final_combinations_list_nodupl.append(item)
    return final_combinations_list_nodupl


def combinationranking(combinations_list):
    """
    Out of a list of combinations of Action objects, the function will sort them depending on the
    final benefit generated
    :param combinations_list: list of Action objects
    :return: sorted list of Action objects
    """
    combinations_ranking = []
    for combination in combinations_list:
        actions_list = []
        combination_benefit = 0
        initial_investment = 0
        for action in combination:
            actions_list.append(action.name)
            combination_benefit += action.finalvalue()
            initial_investment += float(action.value)
        combinations_ranking.append((actions_list, initial_investment, combination_benefit))
    combinations_ranking_final = sorted(combinations_ranking, key=lambda x: -x[2])
    return combinations_ranking_final


