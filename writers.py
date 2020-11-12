import csv
file_name = 'D:/PycharmProjects/projects/en_writers.csv'

my_data = [["first_name", "last_name", "date_of_birth", "date_of_death", "country", "gender", "language"],
           ['George', 'Orwell', '25 June 1903', '21 January 1950', 'England', 'male', 'english'],
           ['Joanne', 'Rowling', '31 July 1965', '', 'England', 'female', 'english'],
           ['Douglas', 'Adams', '11 March 1952', '11 May 2001', 'England', 'male', 'english'],
           ['Roald', 'Dahl', '13 September 1916', '23 November 1990', 'England', 'male', 'english'],
           ['Jonathan', 'Stroud', '27 October 1970', '', 'England', 'male', 'english'],
           ['Graham', 'Joyce', '22 October 1954', '9 September 2014', 'England', 'male', 'english'],
           ['Alan', 'Moore', '18 November 1953', '', 'England', 'male', 'english'],
           ['Pamela', 'Travers', '9 August 1899', '23 April 1996', 'England', 'female', 'english'],
           ['Mary', 'Stewart', '17 September 1916', '9 May 2014', 'Scotland', 'female', 'english'],
           ['James', 'Chase', '24 December 1906', '6 February 1985', 'England', 'male', 'english']]

with open(file_name, 'w') as csvfile:
     csvwriter = csv.writer(csvfile)
     csvwriter.writerows(my_data)
