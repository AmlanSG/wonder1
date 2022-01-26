# Importing pandas
import pandas as pd

# The webpage URL whose table we want to extract
url = "http://trenovision.com/design-and-analysis-of-algorithms-questions-and-answers-daa-mcq-2/"
table1 = pd.read_html(url)[0]
table2 = pd.read_html(url)[1]
result = table1.append(table2)
# Assign the table data to a Pandas dataframe
for i in range (2,19):
        print (i)
        table2 = pd.read_html(url)[i]
        result = result.append(table2)

# Print the dataframe
print(result)
result.to_excel("E:\\Annex\\data.xlsx")