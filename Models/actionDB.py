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
                if lines.line_num == 1 or float(row[1]) == 0.0 or float(row[2]) == 0.0:
                    continue
                action = Action(row[0], abs(float(row[1])), float(row[2])/100)  # Instantiate an Action for each row
                actions_list.append(action)

        return actions_list
