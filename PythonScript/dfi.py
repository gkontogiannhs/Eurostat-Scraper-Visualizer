import warnings
from urllib.request import urlretrieve
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine


class DataFromInternet:
    def __init__(self, url, local_filename):
        self.url = url
        self.local_filename = local_filename
        self.df = pd.DataFrame()
        self.title = ''

    # this method downloads, process and returns the data as a Pandas DataFrame.
    def get_data(self):

        # inner function for downloading the required file
        def download_file(url, filename):
            try:
                urlretrieve(url, filename)
            except Exception as e:
                print(e)
                return None

        # if file is already downloaded, process data. Else download the file and then process
        while True:
            try:
                # catching a read file warning
                with warnings.catch_warnings(record=True):
                    warnings.simplefilter("always")

                    # keeping the desired excel data sheet
                    self.df = pd.read_excel(self.local_filename, sheet_name='Sheet 1', engine='openpyxl')

                    # finding the title of the data sheet for future use
                    self.title = self.df.iloc[0, 1]

                # telling to pandas not to abbreviate the columns
                pd.set_option('display.max_columns', self.df.shape[1])

                # number of columns
                col_length = len(self.df.columns)

                # keeping the measurements for the last 4 years per country
                self.df = self.df.iloc[:, [0, col_length - 8, col_length - 6, col_length - 4, col_length - 2]]

                # get the first column and convert to list
                times = list(self.df[self.df.columns.values[0]].array)
                # in column 0, there is a row named 'TIME' which contains the dates of the measurements
                # finding it's position (as a row)
                times_row = times.index('TIME')
                # get the dates of the measurements
                times = list(self.df.iloc[times_row, 1:])

                # creating new columns by the dates of the measurements
                # and checking for non str dates
                new_columns = ['Country']
                for time in times:
                    new_columns.append(str(time).strip('.0'))

                # renaming the columns
                self.df.columns = new_columns[:]

                # choosing an additional country for analysis
                my_country = input("Select an additional country to check tourism stats:").title()

                # filtering the data
                data_filter = (self.df[self.df.columns[0]] == 'Greece') | (self.df[self.df.columns[0]] == my_country)

                # applying the filter
                self.df = self.df.loc[data_filter]

                # Removing blank measurements
                self.df.replace([':'], 0, inplace=True)

                # return data
                return self.df
            # if filename not found locally, download it my url class member
            except FileNotFoundError:
                download_file(self.url, self.local_filename)

    # method for data plotting
    def plot_data(self):
        # check if data frame is not calculated
        if self.df.empty:
            self.get_data()

        # plot data and name y-axis
        self.df.set_index(self.df.columns[0]).plot(kind='bar', ylabel='# Of ' + self.get_title())
        plt.show()

    # method for data export
    def export_data(self, file_format):
        # check if data frame is not calculated
        if self.df.empty:
            self.get_data()

        # exporting data
        try:
            # get the title name, crop if too long and replace every blank with underscore
            db_name = self.get_title().split(' 2')[0].replace(' ', '_').casefold()

            # remove blanks and un-capitalize
            ff = file_format.strip().casefold()
            # concatenate filename & format
            of = db_name + f'.{file_format}'.title()

            if ff == 'csv':
                self.df.set_index(self.df.columns[0]).to_csv(of)
            elif ff == 'xlsx':
                self.df.set_index(self.df.columns[0]).to_excel(of)
            elif ff == 'tsv':
                self.df.set_index(self.df.columns[0]).to_csv(of, sep='\t')
            elif ff == 'json':
                self.df.set_index(self.df.columns[0]).to_json(of)
            elif ff == 'sql':
                engine = create_engine('mysql+pymysql://root:root@localhost:3306/pythondb')
                self.df.to_sql(name=db_name, con=engine, index=False, if_exists='append')
            else:
                print('Not valid file format!')

        except Exception  as e:
            print(e)

    # dunder method for object iteration
    def __getitem__(self, item):
        return self.df[item]

    # method which determines the data title depending on the excel sheet
    def get_title(self):
        if self.df.empty:
            self.get_data()
        return self.title.rsplit(' [')[0]
