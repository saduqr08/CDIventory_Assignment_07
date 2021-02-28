# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 12:30:02 2021

@author: saduq
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 07:39:14 2021
"""

#--------------------------------------#
# Title: CDIventory
# Desc: Script will ask for user input either to save data load data or add new information
# Update to the CDInventory using pickling to savve data and user validation checks
# Saduq Rahman, 2021 Febuary 28, created file
#---------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object

import pickle

# -- PROCESSING -- #
class DataProcessor:
    @staticmethod
    def append_table(table,stID, strTitle,stArtist):
        """ Function to manage data ingestion and append data to the table
            passed the parameters listed below.
        

        Parameters
        ----------
        strID : TYPE
            DESCRIPTION.
        strTitle : TYPE
            DESCRIPTION.
        strArtist : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
   
   
        intID = int(stID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
        lstTbl.append(dicRow)
        return lstTbl
         
        
       
   
    @staticmethod
    def delete_inventory(lstTbl, id_to_remove):
        """Function to manage data ingestion and delete user input
        
        Takes user input from memory and writes to CDInventory.txt in a 2D table
        each line represents ID,Title, and Artist
        
        Args:
            file_name (string) name of file to save user data too.
            table (list of dict): 2d Data structure (list of dict) that holds the saved user input
        

        Returns:
        None.

        """
        
        
       
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == id_to_remove:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
            print()# update to create space 
            return lstTbl
        



class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        with open(file_name, "rb+") as objFile:# using pickle to read file 
         table = pickle.load(objFile)
         return table

       
             
         
                

             

    @staticmethod
    def write_file(strFileName, table):
        """Function to manage data ingestion from user to a txt file
        
        Takes user input from memory and display CDInventory in a 2D table
        each line represents ID,Title, and Artist
        
        Args:
            file_name (string) name of file to save user data too.
            table (list of dict): 2d Data structure (list of dict) that holds the saved user input
        
        
        Returns:
            None.
        """
        
         #Save the data to a text file CDInventory.dat if the user chooses so
        with open(strFileName, 'wb+') as ObjFile:#writes/creates dat file.
           pickle.dump(lstTbl, ObjFile) 
           
            
    
    


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu choice\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
    @staticmethod   
    def get_input():
         """Function to manage data ingestion from user.
        
        Takes user input put it in a 2D table
        each line represents ID,Title, and Artist
        
        Args:
            file_name (string) name of file to save user data too.
            table (list of dict): 2d Data structure (list of dict) that holds the saved user input
        

        Returns:
            strID, strTitle, stArtist
        

        """
         strID = input('Enter ID: ').strip()
         strTitle = input('What is the CD\'s title? ').strip()
         stArtist = input('What is the Artist\'s name? ').strip()
         return strID, strTitle, stArtist
        
       

    @staticmethod
    def load_inventory(file_name,table):
         """Function to manage data ingestion from user to a txt file
        
        Takes user input from memory and writes to CDInventory.dat in a 2D table
        each line represents ID,Title, and Artist
        
        Args:
            file_name (string) name of file to save user data too.
            table (list of dict): 2d Data structure (list of dict) that holds the saved user input
        

        Returns:
        None.

        """
        
         
         

# 1. When program starts, read in the currently saved Inventory
    try:
        lstTbl = FileProcessor.read_file(strFileName, lstTbl)
    except:   
                print('\n\n\n', '=' * 6 ,'CDInventory.dat file is missing please create file','=' * 6)
                print()


# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled:')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstTbl = FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # Add a try statement here due to circumvent errors
        while True:
            try: 
                strID, stArtist, strTitle = IO.get_input()
                lstTbl = DataProcessor.append_table(lstTbl, strID, strTitle, stArtist)
                IO.show_inventory(lstTbl)
                break
            except ValueError:
                                print('\n\n\n','=' * 6, 'Invalid entry. ID must be an integer', '=' * 6) 
        # 3.3.2 Add item to the table
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        try: # try statment add to combat invalid entry
            intIDDel = int(input('Which ID would you like to delete? ').strip())
        except:
               print('\n\n\n','=' * 6, 'Invalid CD ID selection: Please make a valid selection:', '=' * 6)
        IO.show_inventory(lstTbl)
        lstTbl = DataProcessor.delete_inventory(lstTbl,intIDDel)
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to use
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo.lower() in ['yes', 'y']:
             FileProcessor.write_file(strFileName, lstTbl) ## Calls for to save inventory to target dat file 
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')







