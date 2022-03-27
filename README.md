## Eurostat-Visualizer
### This repo hosts a python script which downloads, visualizes and stores the table data, between two countries of your choice, for any given [Eurostat's Database](https://ec.europa.eu/eurostat/web/main/data/database) URL


## How to use
### After cloning locally and executing main.py ...
#### To download any given data table:
  - Choose "Download data"
  - Give the URL and filename of your choice to store the data locally   
✔️ **More than one files can be downloaded and processed at once, by giving sequentially the URLS of your choice**    
#### To plot them:
- Choose "Plot data"
- Give the two countries of your choice  
⚠️ **The one is hardcoded in the script, and the other is asked from the user as an input. In my case, hardcoded is Greece, so you can either change it manually or parameterize it.** 

#### To store them:
- Choose "store data"
- Pick the format of your choice (.csv, .xlsx, .sql, .tsv)    
‼️ **In the case of .sql format, change to your account username/password and db name. The associated DB table will be created automatically**   
  
## Class methods worth mentioning
### :large_orange_diamond: dfi.get_data(self)  
This method, at first, checks if the given filename is already locally downloaded. If not, the inner method *download_file(url, filename)* is executed and with the help of *urlretrieve()* function downloads the associated file. Then, user is asked to give the two countries of his choice, processes the data (according to the above) and loads them to a *pandas DataFrame*.

### :large_orange_diamond: dfi.get_title(self)  
This method automatically scrapes and returns the associated title of the dataset, once every *dfi* isntance is a file proccess

### :large_orange_diamond: dfi.plot_data(self)  
This method, for every downloaded-proccessed file, creates a histogram which y-axis label is autocompoleted by dfi.get_title(self)

### :large_orange_diamond: dfi.export_data(self, file_format)
This method stores locally a file of the proccessed data with the format of our choice (.csv, .xlsl, .tsv, .json, .sql). In *.sql* case, it auto creates a DB table. In each case, the exported file/DB table, is named after the get_title() automatically.

## Limitations
:no_entry: **The initial downloadable URL must be in excel format**

## Execution Examples
1. photo1
2. photo2
3. photo3
