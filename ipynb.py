# Save the code to a Jupyter notebook file
import nbformat as nbf

nb = nbf.v4.new_notebook()

code = """
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

# Raw CSV data
csv_data = '''"State","Type of Index Crime","Index Offense","Year","Number Actual Offenses","Number Offenses Cleared","Percent Cleared"
"NC","Violent Crime","Murder","2018","575","422","73.4%"
"NC","Violent Crime","Murder","2019","621","350","56.4%"
"NC","Violent Crime","Murder","2020","830","428","51.6%"
"NC","Violent Crime","Murder","2021","964","462","47.9%"
"NC","Violent Crime","Murder","2022","848","394","46.5%"
"NC","Violent Crime","Rape","2018","2,434","1,031","42.4%"
"NC","Violent Crime","Rape","2019","3,199","917","28.7%"
"NC","Violent Crime","Rape","2020","3,029","774","25.6%"
"NC","Violent Crime","Rape","2021","3,277","770","23.5%"
"NC","Violent Crime","Rape","2022","3,216","682","21.2%"
"NC","Violent Crime","Robbery","2018","7,625","3,008","39.4%"
"NC","Violent Crime","Robbery","2019","7,409","2,206","29.8%"
"NC","Violent Crime","Robbery","2020","7,049","2,095","29.7%"
"NC","Violent Crime","Robbery","2021","5,903","1,615","27.4%"
"NC","Violent Crime","Robbery","2022","5,788","1,495","25.8%"
"NC","Violent Crime","Aggravated Assault","2018","24,679","12,419","50.3%"
"NC","Violent Crime","Aggravated Assault","2019","26,277","8,541","32.5%"
"NC","Violent Crime","Aggravated Assault","2020","33,676","9,283","27.6%"
"NC","Violent Crime","Aggravated Assault","2021","33,284","9,238","27.8%"
"NC","Violent Crime","Aggravated Assault","2022","32,255","8,330","25.8%"
"NC","Violent Crime","Subtotal","2018","35,313","16,880","47.8%"
"NC","Violent Crime","Subtotal","2019","37,506","12,014","32.0%"
"NC","Violent Crime","Subtotal","2020","44,584","12,580","28.2%"
"NC","Violent Crime","Subtotal","2021","43,428","12,085","27.8%"
"NC","Violent Crime","Subtotal","2022","42,107","10,901","25.9%"
"NC","Property Crime","Burglary","2018","57,373","11,537","20.1%"
"NC","Property Crime","Burglary","2019","48,783","7,082","14.5%"
"NC","Property Crime","Burglary","2020","47,812","7,331","15.3%"
"NC","Property Crime","Burglary","2021","41,914","6,393","15.3%"
"NC","Property Crime","Burglary","2022","39,079","5,719","14.6%"
"NC","Property Crime","Larceny","2018","165,243","42,066","25.5%"
"NC","Property Crime","Larceny","2019","165,290","29,706","18.0%"
"NC","Property Crime","Larceny","2020","163,322","26,288","16.1%"
"NC","Property Crime","Larceny","2021","156,540","20,543","13.1%"
"NC","Property Crime","Larceny","2022","158,200","19,472","12.3%"
"NC","Property Crime","Motor Vehicle Theft","2018","16,111","3,812","23.7%"
"NC","Property Crime","Motor Vehicle Theft","2019","15,600","2,272","14.6%"
"NC","Property Crime","Motor Vehicle Theft","2020","17,812","2,335","13.1%"
"NC","Property Crime","Motor Vehicle Theft","2021","17,379","2,186","12.6%"
"NC","Property Crime","Motor Vehicle Theft","2022","18,672","1,940","10.4%"'''

# Read the data into a DataFrame
data = pd.read_csv(StringIO(csv_data), quotechar='"')

# Data cleaning
data['Number Actual Offenses'] = data['Number Actual Offenses'].str.replace(',', '').astype(int)
data['Number Offenses Cleared'] = data['Number Offenses Cleared'].str.replace(',', '').astype(int)
data['Percent Cleared'] = data['Percent Cleared'].str.replace('%', '').astype(float)

# Basic statistics
basic_stats = data.describe()

# Group by Year and Type of Index Crime
grouped_by_year = data.groupby(['Year', 'Type of Index Crime']).sum().reset_index()

# Trends over time for Number Actual Offenses
trends_over_time = data.pivot(index='Year', columns='Index Offense', values='Number Actual Offenses')

# Crime type analysis (average values)
crime_type_analysis = data.groupby('Index Offense').mean().reset_index()

# Plotting Trends over time for Number Actual Offenses
trends_over_time.plot(kind='line', figsize=(14, 7))
plt.title('Trends Over Time for Number of Actual Offenses')
plt.ylabel('Number of Actual Offenses')
plt.xlabel('Year')
plt.legend(title='Index Offense')
plt.grid(True)
plt.show()

# Plotting Number of Actual Offenses by Type of Index Crime
plt.figure(figsize=(14, 7))
for crime_type in data['Type of Index Crime'].unique():
    subset = data[data['Type of Index Crime'] == crime_type]
    plt.plot(subset['Year'], subset['Number Actual Offenses'], marker='o', label=crime_type)

plt.title('Number of Actual Offenses by Type of Index Crime')
plt.ylabel('Number of Actual Offenses')
plt.xlabel('Year')
plt.legend(title='Type of Index Crime')
plt.grid(True)
plt.show()

# Plotting Average Percent Cleared by Index Offense
plt.figure(figsize=(14, 7))
plt.bar(crime_type_analysis['Index Offense'], crime_type_analysis['Percent Cleared'])
plt.title('Average Percent Cleared by Index Offense')
plt.ylabel('Percent Cleared')
plt.xlabel('Index Offense')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()
"""

nb['cells'].append(nbf.v4.new_code_cell(code))

# Save to a .ipynb file
with open('/mnt/data/Crime_Data_Analysis.ipynb', 'w') as f:
    nbf.write(nb, f)
