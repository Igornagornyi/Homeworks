import csv


file_name = 'D:/PycharmProjects/projects/en_writers.csv'
with open(file_name, 'w') as csvfile:
    my_data = [['first name-George'], ['last name-Orwell'], ['date of birth-25 June 1903'],
               ['date of death-21 January 1950'], ['country-England'], ['gender-male'], ['language-english'], [],
               ['first name-Joanne '], ['last name-Rowling'], ['date of birth-31 July 1965'], ['date of death'],
               ['country-England'], ['gender-female'], ['language-english'], [], ['first name-Douglas'],
               ['last name-Adams'], ['date of birth-11 March 1952'], ['date of death-11 May 2001'], ['country-England'],
               ['gender-male'], ['language-english'], [], ['first name-Roald'], ['last name-Dahl'], ['date of birth-13 September 1916'],
               ['date of death-23 November 1990'], ['country-England'], ['gender-male'], ['language-english'], [],
               ['first name-Jonathan'], ['last name-Stroud'], ['date of birth-27 October 1970'], ['date of death'],
               ['country-England'], ['gender-male'], ['language-english'], [], ['first name-Graham'], ['last name-Joyce'],
               ['date of birth-22 October 1954'], ['date of death-9 September 2014'], ['country-England'], ['gender-male'],
               ['language-english'], [], ['first name-Alan'], ['last name-Moore'], ['date of birth-18 November 1953'],
               ['date of death'], ['country-England'], ['gender-male'], ['language-english'], [], ['first name-Pamela'],
               ['last name-Travers'], ['date of birth-9 August 1899'], ['date of death-23 April 1996'], ['country-England'],
               ['gender-female'], ['language-english'], [], ['first name-Mary'], ['last name-Stewart'], ['date of birth-17 September 1916'],
               ['date of death-9 May 2014'], ['country-Scotland'], ['gender-female'], ['language-english'], [], ['first name-James'],
               ['last name-Chase'], ['date of birth-24 December 1906'], ['date of death-6 February 1985'], ['country-England'],
               ['gender-male'], ['language-english']]
    #

    csvwriter = csv.writer(csvfile, lineterminator='\n')
    csvwriter.writerows(my_data)
    # csvwriter.writerows(my_data)