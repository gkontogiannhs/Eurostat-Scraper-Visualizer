## Eurostat-Visualizer
### This repo hosts a python script which downloads, visualizes and stores the table data, between two countries of your choice, for any given [Eurostat's Database](https://ec.europa.eu/eurostat/web/main/data/database) URL


## How to use
### After cloning locally and executing main.py...
#### To download any given data table:
  - Choose "Download data"
  - Give the URL and filename of your choice to store the data locally   
✔️ **More than one files can be downloaded and processed at once, by giving sequentially the URLS of your choice**    
#### To plot them:
- Choose "Plot data"
- Give the two countries of your choice

#### To store them:
- Choose "store data"
- Pick the format of your choice (.csv, .xlsx, .sql, .tsv)  
‼️ **In the case of .sql format, change to your account username/password and db name. The associated DB table will be created automatically**   
  
## Class methods worth mention
### :large_orange_diamond: dfi.get_data(self)  
This method, at first, checks if the given filename is already locally downloaded. If not, the inner method *download_file(url, filename)* is executed and with the help of *urlretrieve()* function downloads the associated file. Then, user is asked to give the two countries of his choice, processes the data (according to the above) and loads them to a *pandas DataFrame*.

### :large_orange_diamond: dfi.get_title(self)  
This method automatically scrapes and returns the associated title of the dataset once every *DFI* isntance is a file proccess

### :large_orange_diamond: dfi.plot_data(self)  
This method, creates
→ Η plot_data() δημιουργεί γραφική τύπου ραβδόγραμμα και με τη βοήθεια της get_title() διαμορφώνει την ετικέτα του y-άξονα.

### :large_orange_diamond: dfi.export_data(self, file_format)
This method takes as argument the format 
παίρνει σαν όρισμα το επιθυμητό format αρχείου με το οποίο θέλει να εξάγει τα επεξεργασμένα δεδομένα (.csv, .xlsl, .tsv, .json, .sql).
Σε κάθε περίπτωση, το όνομα του εξαγώμενου αρχείου διαμορφώνεται και πάλι απο την get_title() αυτόματα.  

## Limitations
:no_entry: **The initial downloadable URL must be in excel format**
