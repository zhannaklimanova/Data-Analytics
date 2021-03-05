import pandas as pd
import matplotlib.pyplot as plt


def removeSpecialChars(data):
    a_string = data
    alphanumeric = ""
    for character in a_string:
      if character == '.':
        break
      if character.isalnum():
          alphanumeric += character
    return alphanumeric
    
pd.set_option("max_columns", None)
pd.set_option("max_rows", None)

#Movies_Data
dataFrame = pd.read_csv('https://raw.githubusercontent.com/williamykzhang/MAIS_CE/master/movies_data.csv')

#Genre_Data
dataFrame2 = pd.read_csv('https://raw.githubusercontent.com/williamykzhang/MAIS_CE/master/genre_data.csv')


col = dataFrame['worldwide_gross']
col2 = dataFrame2['Main_Genre']
dataFrame.insert(8, "Main_Genre", col2, False) # Inserting a new column containing the main movie genres into the dataFrame

main_Genres_dictionary = dict() # Dictionary which is used to calculate the number of times each movie genre appears
for Main_Genre in col2:
    if Main_Genre in main_Genres_dictionary:
        main_Genres_dictionary[Main_Genre] += 1
    else:
        main_Genres_dictionary[Main_Genre] = 1

main_Genres_dictionary2_sum = dict() # Dictionary which is used to calculate the worldwide_gross sum of each movie genre
for index, row in dataFrame.iterrows():
    if row["Main_Genre"] in main_Genres_dictionary2_sum:
        main_Genres_dictionary2_sum[row["Main_Genre"]] += int(removeSpecialChars(row["worldwide_gross"]))
    else:
        main_Genres_dictionary2_sum[row["Main_Genre"]] = int(removeSpecialChars(row["worldwide_gross"]))

main_Genres_dictionary3_average = dict() # Dictionary which is used to calculate the average worldwide gross for each of the genres
for key in main_Genres_dictionary2_sum:
    if key in main_Genres_dictionary:
        main_Genres_dictionary3_average[key] = "{:e}".format(main_Genres_dictionary2_sum[key]/main_Genres_dictionary[key])
    else:
        pass
 
# print(main_Genres_dictionary3_average)
# print(main_Genres_dictionary2_sum)
# print(main_Genres_dictionary)

# Sorting the dictionary in descending order such that the highest grossing movie genre will be at the beginning and the lowest will be at the end
main_Genres_dictionary3_average = sorted(main_Genres_dictionary3_average.items(), key=lambda x: float(x[1]), reverse = True)
# for el in main_Genres_dictionary3_average: # TESTER
#   print(el)


main_Genres_dictionary3_average_graph = sorted(main_Genres_dictionary3_average, key=lambda x: float(x[1]), reverse = False) # ordering for graph
# for el in main_Genres_dictionary3_average_graph: # TESTER
#   print(el)


# Create a new pandas DataFrame that includes the Main_Genre and worldwide_gross columns - this data frame will be used to display movie genres and their gross revenue
combinedDataFrame2 = pd.DataFrame(list(main_Genres_dictionary3_average), columns = ['Main_Genre', 'worldwide_gross'])
print(combinedDataFrame2)

# Create a new pandas DataFrame that includes the Main_Genre and worldwide_gross columns - this data frame will be used to plot the graph
combinedDataFrame = pd.DataFrame(list(main_Genres_dictionary3_average_graph), columns = ['Main_Genre', 'worldwide_gross'])

# Plot DataFrame data into a graph
x_axis_genres = combinedDataFrame['Main_Genre']
y_axis_data = combinedDataFrame['worldwide_gross']
%matplotlib inline
plt.rcParams['figure.figsize'] = (20, 10)
plt.bar(x_axis_genres, y_axis_data);
plt.title('Average worldwide gross')
plt.xlabel('Main_Genre')
plt.ylabel('worldwide_gross')
plt.show()

