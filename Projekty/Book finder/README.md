Book finder APP.

This program helps to find books from database, according to entered criteria from user.

Database file "bestsellers_list.txt" contains a list of more than 1000 bestsellers to demonstrate the example of use.
After start, the program displays a menu of options and allows the user to search for books by certain criteria. The menu items are:

-   Extract all books from any years range: Prompts for two years (start and end year), then lists all books that are listed between those two years (inclusive).
    For example, if a user enters "1970" and "1973", all books that were bestsellers in 1970, 1971, 1972, or 1973 are displayed.
-   List all books from a particular month and year: You'll be prompted for the month and year, then list all the books that were best sellers during that month.
    For example, if a user enters "7" and "1985", all books that were bestsellers during the month of July in 1985 would be displayed.
-   Search for books by an author: You'll be prompted to enter a string, then list all books whose author contains that string (regardless of case).
    For example, if the user enters "ST", all books whose author name contains "ST", "St", "sT" or "st" are listed.
-   Title search: You are prompted for a string, then it lists all books whose title contains that string (regardless of the case).
    For example, if the user enters "secret", there are three books: "The Secret of Santa Vittoria" by Robert Crichton, "The Secret Pilgrim" by John le Carré and "Harry Potter and the Chamber of Secrets".

**************
Sample output:
**************

What do you want to do?
 1: Search books by years
 2: Search books by month and year
 3: Search books by author
 4: Search books by title
 E: Exit
> 1
Enter the start year: 1960
Enter end year: 1962

All titles between 1960 and 1962:
 A Shade of Difference by Allen Drury (10/28/1962)
 Franny and Zooey, by JD Sallinger (10/29/1961)
 Hawaii by James Michener (1/17/1960)
 Seven Days in May by Fletcher Knebel (11/18/1962)
 Ship of Fools by Katherine Anne Porter (4/29/1962)
 The Agony and the Ecstasy by Irving Stone (4/23/1961)
 The Last of the Just, by Andre Schwarz-Bart (3/26/1961)
 Born Free, by Joy Adamson (8/7/1960)
 Calories Don't Count by Herman Taller (3/25/1962)
 May This House Be Safe From Tigers by Alexander King (3/13/1960)
 Silent Spring by Rachel Carson (10/28/1962)
 Making The President - 1960, by Theodore H. White (9/10/1961)
 The New English Bible, by Oxford University Press (5/28/1961)
 Rise and Fall of the Third Reich by William Shirer (12/4/1960)
 The Rothchilds, by Frederic Morton (6/24/1962)
 The Waste Makers by Vance Packard (11/6/1960)
 John Steinbeck Travels with Charley (10/21/1962)

Number of books found = 17

What do you want to do?
 1: Search books by years
 2: Search books by month and year
 3: Search books by author
 4: Search books by title
 E: Exit
> 2
Enter month (as number 1-12): 9
Enter year: 1990

All titles in 9. 1990:
 Stephen King - Four Past Midnight (9/16/1990)
 Memories of Midnight by Sidney Sheldon (9/2/1990)
 Darkness Visible by William Styron (9/16/1990)
 Millie's Book by Barbara Bush (9/30/1990)
 Trump: Surviving At The Top, by Donald Trump (9/9/1990)

Number of books found = 5

What do you want to do?
 1: Search books by years
 2: Search books by month and year
 3: Search books by author
 4: Search books by title
 E: Exit
> 3
Enter author name (or part of name): tolkein
  Silmarillion, by JRR Tolkein (10/2/1977)
  The Children of the Hurin, by J.R.R. Tolkein (5/6/2007)

Number of books found = 2

What do you want to do?
  1: Search by years
  2: Search by month and year
  3: Search by author
  4: Search by title
  K: Exit
> 4
Enter title (or part of title): secret
  Harry Potter and the Chamber of Secrets by J.K. Rowling (6/20/1999)
  The Secret of Santa Vittoria by Robert Crichton (11/20/1966)
  The Secret Pilgrim, by John Le Carre (1/20/1991)

Number of books found = 3
