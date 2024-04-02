# Flight Reservation Historical Data

This project automates the process of fetching, processing, and storing flight data. It encompasses four Python scripts designed to interact with the Tequila API, manipulate the retrieved data using Pandas, and manage data storage with SQLAlchemy for PostgreSQL integration.

# Structure

Five major components:

1. Data Collection (get_data.py): Includes functions to interact with the Tequila API, fetching flight information based on predefined criteria such as destination, date range, and currency.

2. Data Preparation (prepare_data.py): Processes data to a more manageable form. It flattens nested JSON structures, renames columns for consistency, and prepares the data for database insertion.

3. Data Loading (load_data.py): Deals with the database aspect, creating schemas and tables in PostgreSQL, and loading the prepared data into the database. It also includes functions for modifying table structures to accommodate the processed data.

4. Main (main.py): This script ties together the functionalities provided by the individual modules, integrating the end-to-end data flow.

5. Web Application (streamlit.py): Streamlit application that visualizes some of the data stored in the database. It allows users to select flight destinations and displays statistics related to flight prices and availability.

# Misc

Dependencies can be found in 'requirements.txt', and credentials can be set in the keys.py file. For guidance, check 'keys_template.py'.

This is an ETL solution, from collection to visualization. It's designed to be modular, allowing for easy expansion or modification to suit different requirements or integrate additional data sources.


