from pandas_ods_reader import read_ods


class ActionDB:
    def __init__(self, path, sheet_index):
        self.path = path
        self.sheet_index = sheet_index

    def extractactiondata(self, path, sheet_index):
        df = read_ods(path, sheet_index)
        return df
