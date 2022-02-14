from Models.constants import max_spend_per_customer


def findallcombinations(actions_list):
    final_combinations_list = []
    final_combinations_names_list = []
    for i in range(len(actions_list)):
        final_combinations_list.append([actions_list[i]])
        final_combinations_names_list.append([actions_list[i].name])
        for j in range(len(actions_list)):
            counter = int(actions_list[i].value)
            combination = [actions_list[i]]
            combination_names = [actions_list[i].name]
            for k in range(j, len(actions_list)):
                if counter + int(actions_list[k].value) <= max_spend_per_customer and k != i:
                    counter += int(actions_list[k].value)
                    combination.append(actions_list[k])
                    combination_names.append(actions_list[k].name)
                else:
                    continue
            final_combinations_list.append(sorted(combination, key=lambda x: x.name))
            final_combinations_names_list.append(sorted(combination_names))
    final_combinations_list_nodupl = []
    for item in final_combinations_list:
        if item not in final_combinations_list_nodupl:
            final_combinations_list_nodupl.append(item)
    return final_combinations_list_nodupl


def combinationranking(combinations_list):
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
    combinations_ranking_final = sorted(combinations_ranking, key=lambda x: -x[1])
    return combinations_ranking_final


