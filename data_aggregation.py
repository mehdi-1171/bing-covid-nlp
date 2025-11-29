"""
Author: m.habibina1171@gmail.com
Description:
    This File for Aggregation file from:
                https://github.com/microsoft/BingCoronavirusQuerySet/tree/master/data
"""

from pandas import read_csv, concat, DataFrame
from utility import BASE_DIR
import calendar


class DataAggregation:
    BASE_URL = "https://raw.githubusercontent.com/microsoft/BingCoronavirusQuerySet/master/data/"
    def __init__(self, year):
        self.year = year
        self.file_name_list =[]
        self.dfs = []
        self.dfs = DataFrame()
    def create_file_list(self):
        for month in range(1, 13):
            last_day = calendar.monthrange(self.year, month)[1]
            filename = f"QueriesByCountry_{self.year}-{month:02d}-01_{self.year}-{month:02d}-{last_day:02d}.tsv"
            self.file_name_list.append(filename)

    def aggregate_files(self):
        for file_name in self.file_name_list:
            print(file_name)
            df_month = read_csv(self.BASE_URL + str(self.year) + '/' + file_name, sep="\t")
            self.dfs.append(df_month)
    def export_file(self):
        self.df = concat(self.dfs, ignore_index=True)
        self.df.to_csv(BASE_DIR + '/data/input/Bing_Covid_Queries_Country_' + str(self.year) + '.csv', index=False)

    def process_handler(self):
        self.create_file_list()
        self.aggregate_files()
        self.export_file()

# Runner

if __name__ == "__main__":
    agg_instance = DataAggregation(year=2020)
    agg_instance.process_handler()
