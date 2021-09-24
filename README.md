# ETL Challenge: Wine Pricing Standards 

### Team Name: 
Rosé All Day

### Team Members: 
Erin Kinney, Scott Seely, Kacee Kira Chien


## Proposal

### Outline:
Use an API to pull data from wine-searcher.com on a specific wine (Duckhorn Vineyards Napa Valley Merlot) with all its vintages, transform the data, and store it in a SQL database. Time permitting, do preliminary exploration and analysis to  compare the retail price from different merchants across the United States.

### Tools/Methods to be used:
+ SQL database
+ Wine Searcher API
+ GitHub Repo
+ Python
+ Pandas
+ SQLAlchemy
+ Geopandas

### Deliverables:
+ GitHub repo
+ PowerPoint deck
+ Live presentation


## Process

### ETL
+ Recieved a sample of data from calls to the wine-searcher API. 
+ Performed transformations to:
    + Break out street address and city from the full address returned by the API 
    + Separate bottle format and volume into distinct columns
+ Loaded the transformed data into a SQL database
+ Output database table to CSV

### Analysis & Visualization
+ Performed statistical analysis to determine mean and median price per state
+ Created a cholopleth map showing three bins of pricing

## Results & Next Steps:

### Results
Delivered proof of concept that pricing data can be aggregated and mapped to show areas of pricing ranges. Could be used by suppliers to track SRP compliance.

### Next Steps & What we'd do if we had more time!
+ Build  out the price aggregation tool with a larger dataset
    + State level view
    + City level view
+ Create a scores map
+ Expand price comparison tool out to different liquor categories


__Cheers!__
