
import os

BASEDIR = os.getcwd()
print(BASEDIR)
text_file = os.path.join(BASEDIR, 'bestsellers_list.txt')

# this function reads all books into list 'book_list' from text file (list items are lists with values: 0=book name, 1=author, 2=editor, 3=date, 4=fiction)
def write_file_into_list(file):
    book_list=[]
    try:
        with open(file) as f:
            row = ' '
            while row != '':
                row = f.readline()
                row = row.strip()
                list_from_row = row.split('\t')
                book_list.append(list_from_row)
        f.close()
        book_list.pop()
        print('Bool list created successfully')
        return book_list
    except FileNotFoundError:
        raise FileNotFoundError('File you are trying to find seems not to be responding')

write_file_into_list(text_file)

# this function gets and validates data from user to print the list of books according to submitted years:
def get_data_for_range_of_years():
    while True:
        try:
            beginning = input('Please enter start year: ')
            end = input('Please enter end year: ')
            return (int(beginning), int(end))
        except ValueError:
            print('*************************************************************')
            print('You must insert proper years to find what you are looking for')
            print('*************************************************************')
            print()


# this function prints all books from file according to submitted years:
def range_of_years():
    years = get_data_for_range_of_years()
    list_of_books = write_file_into_list(text_file)
    print('\nThese are all books from', years[0], ' to ', years[1], ':\n')
    # following cycles pick date from 'list of books' and divide it into list of 3 items ( for examle:
    # dates = ['8/30/2000', '9/24/1978', and so on -- and then dates_divided=[['8','30','2000'],['9','24','1978'], and so on...))
    dates=[]
    dates_divided=[]
    count = 0
    for i in range (len(list_of_books)):
        dates.append(list_of_books[i][3])
    for i in range(len(dates)):
        date_string_divided = dates[i].split('/')
        dates_divided.append(date_string_divided)
    for i in range(len(dates_divided)):
        for j in range(years[0], years[1]+1):
            if str(j) == dates_divided[i][2]:
                printout_of_books = '  ' + list_of_books[i][0] + ',' + ' by ' + list_of_books[i][1] + ',' + ' (' + list_of_books[i][3] + ')'
                print(printout_of_books)
                count += 1
    print()
    print('Number of books found = ', count)
    print()


# this function prints all books from file according to name of author:
def name_of_author():
    name_of_author = input('Enter name of author or a part of name: ').lower()
    # name_of_author = name_of_author.lower()
    list_of_books = write_file_into_list(text_file)
    print('\nThese are all books from this author:', name_of_author, ':\n')
    count = 0
    for i in range(len(list_of_books)):
        name_of_author_string = list_of_books[i][1]
        name_of_author_string = name_of_author_string.lower()
        if name_of_author in name_of_author_string:
            printout_of_books = '  ' + list_of_books[i][0] + ',' + ' by ' + list_of_books[i][1] + ',' + ' (' + list_of_books[i][3] + ')'
            print(printout_of_books)
            count += 1
    print()
    print('Number of books found = ', count)
    print()



# this function gets and validates data from user to print the list of books according to submitted years:
def get_data_for_month_and_year():
    month = 0
    while not int(month) in range(1,27):
        try:
            month = int(input("Enter month (as a number from 1-12): "))
            if month not in range(1,13):
                print('*************************************************************')
                print('You must insert proper month to find what you are looking for')
                print('*************************************************************')
                print()

        except ValueError:
            print('*************************************************************')
            print('You must insert proper month to find what you are looking for')
            print('*************************************************************')
            print()
    while True:
        try:
            year = int(input('Enter year: '))
            return (int(month), int(year))
        except ValueError:
            print('************************************************************')
            print('You must insert proper year to find what you are looking for')
            print('************************************************************')
            print()



#this function prints all books from file according to entered month and year:
def month_year():
    datum = get_data_for_month_and_year()
    list_of_books = write_file_into_list(text_file)
    print('\nThese are all books released in ', datum[0], '. month and ' , datum[1],  'year :\n')
    # following cycles pick date from 'list of books' and divide it into list of 3 items ( for examle:
    # dates = ['8/30/2000', '9/24/1978', and so on -- and then dates_divided=[['8','30','2000'],['9','24','1978'], and so on...))
    dates=[]
    dates_divided=[]
    count = 0
    for i in range (len(list_of_books)):
        dates.append(list_of_books[i][3])
    for i in range(len(dates)):
        date_string_divided = dates[i].split('/')
        dates_divided.append(date_string_divided)
    for i in range(len(dates_divided)):
        if str(datum[0]) == dates_divided[i][0] and str(datum[1]) == dates_divided[i][2]:
            printout_of_books = '  ' + list_of_books[i][0] + ',' + ' by ' + list_of_books[i][1] + ',' + ' (' + list_of_books[i][3] + ')'
            print(printout_of_books)
            count += 1
    print()
    print('Number of books found = ', count)
    print()


#this function prints out all books from file according to entered title (can be entered with lowercase too)
def title():
    title = input('Enter title (or part of title): ')
    title = title.lower()
    list_of_books = write_file_into_list(text_file)
    print('\nThese are all books, that contain "', title, '" in their title:\n')
    count = 0
    for i in range(len(list_of_books)):
        title_string = list_of_books[i][0]
        title_string = title_string.lower()
        if title in title_string:
            printout_of_books = '  ' + list_of_books[i][0] + ',' + ' by ' + list_of_books[i][1] + ',' + ' (' + list_of_books[i][3] + ')'
            print(printout_of_books)
            count += 1
    print()
    print('Number of books found = ', count)
    print()


# this function ask for input from the user
def menu_selection():
    return input('\nWhat do you want to do?\n 1: Search books by years\n 2: Search books by month and year\n 3: Search books by author\n 4: Search books by title\n E: End\n>')


selection = menu_selection()
while selection != 'E':
    if  selection == '1':
        range_of_years()
    elif selection == '2':
        month_year()
    elif selection == '3':
        name_of_author()
    elif selection == '4':
        title()
    elif selection == 'e':
        break
    else:
        print()
        print('**********************************************')
        print('Please enter a valid menu item - 1,2,3,4, or E')
        print('**********************************************')
        print()
    selection = menu_selection()


print()
print('*******************************')
print('Thank you for using our program')
print('*******************************')

input()
