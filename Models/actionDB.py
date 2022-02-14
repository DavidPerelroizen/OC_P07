from Models.action import Action
import csv


class ActionDB:
    def __init__(self, path):
        self.path = path

    def extractdatacsv(self):
        """This method enables to extract the data from a csv file and save it as a list of Actions"""
        actions_list = []
        with open(self.path, 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                action = Action(row[0], row[1], row[2])  # Instantiate an Action for each row
                actions_list.append(action)
        actions_list.pop(0)  # Remove the database header
        return actions_list
