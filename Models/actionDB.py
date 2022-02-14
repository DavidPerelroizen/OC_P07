from Models.action import Action
import csv


class ActionDB:
    def __init__(self, path, sheet_index):
        self.path = path
        self.sheet_index = sheet_index

    def extractdatacsv(self, path):
        """This method enables to extract the data from a csv file and save it as a list of Actions"""
        actions_list = []
        with open(path, 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                action = Action(row[0], row[1], row[2])
                actions_list.append(action)
        actions_list.pop(0)
        return actions_list
