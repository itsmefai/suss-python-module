# Updated as of 9 Aug 2020
# Team members:
# 1. MUHAMMAD AL-FAIRUZ BIN MOHD BASER J2010990
# 2.
# 3.
# 4. 
# 5. 

from datetime import datetime
import os

class Plant:
    def __init__(self, filepath = 'myplants.txt'):
        self.filepath = filepath
        self.data = self.load_data()
    
    def load_data(self):
        """
        reads the txt file and converts it to dictionary
        """

        f = open(self.filepath, "r")
        contents = f.read()

        # Creating a dictionary to store the plant's information
        plant_dict = {}
        plant_list = []

        for i in contents.split('\n\n'):
            plant_info = i.split('\n')
            plant_name = plant_info[0]

            plant_list.append(plant_info)

        for info in plant_list[:-1]:
            plant_dict[info[0].lower()] = {'Name': info[0], # save plant key as lowercase
                                    'Last Updated': info[1],
                                    'Information': info[2:]}
        
        return plant_dict
        
        # closing the text file
        f.close()
        
    def view_all(self):

        # Implement a while loop to ensure that user enters a valid input. Else, prompt the user to enter again.
        while True:
            
            # display view all menu
            print("How would you like to view it?")
            print()
            print(' (1) Alphabetical Order')
            print(' (2) Latest Revision Time')
            print()
            print(' (0) Return to Main Menu')
            print()

            choice = input('Please enter 1, 2 or 0: ')
            print("\033c")
            print('-------------------------------------------------------')
            print('|                 Plant Informations                  |')
            print('-------------------------------------------------------')


            if choice in ['1', '2', '0']:
                if choice == '1':
                    # sorting the values by their names uppercased. This will handle plant names with lowercases.
                    # returns a list of tuples
                    sort_by_name = sorted(self.data.items(), key=lambda plant: plant[0].upper())

                    # converting list into a dictionary using python build in dict() function
                    sort_by_name = dict(sort_by_name)
                
                    keys = list(sort_by_name.keys())

                    print()
                    for i in keys:
                        for k, v in self.data[i].items():
                            if k != 'Information':
                                print(f"{k}: {v}")
                            else:
                                print()
                                print(f"{k}(s):")
                                count = 1
                                for info in v:
                                    print(f"({count}) {info}")
                                    count += 1
                        print()
                        print('-------------------------------------------------------')
                        print()

                elif choice == '2':
                    # sorting the values by their names 
                    # returns a list of tuples
                    # sorting the values by their last updated date by descending order 
                    sort_by_date = sorted(self.data.items(), key=lambda plant: plant[1]['Last Updated'], reverse= True)    

                    # converting list into a dictionary using python build in dict() function
                    sort_by_date = dict(sort_by_date)
                
                    keys = list(sort_by_date.keys())

                    for i in keys:
                        for k, v in self.data[i].items():
                            if k != 'Information':
                                print(f"{k}: {v}")
                            else:
                                print()
                                print(f"{k}(s):")
                                count = 1
                                for info in v:
                                    print(f"({count}) {info}")
                                    count += 1
                        print()
                        print('-------------------------------------------------------')
                        print()

                elif choice == '0':
                    print("\033c") # clear the terminal console
                    break

                # print out the total number of records
                print(f"There are {len(keys)} records in total.")
                print()
                print('-------------------------------------------------------')
                
                # break out of the while loop
                break
            
            else:
                print()
                print('Invalid input! Please try again.')
                print()
                continue

    def add_plant(self, name):

        name_lower = name.lower()
        plants = list(self.data.keys())
        #  plants_lower = [i.lower() for i in plants]

        # check if plant already exist
        if name_lower in plants:
            print()
            print('----------------------------------------------------------------------')
            print('|                 Message: Plant name already exist!                 |')
            print('----------------------------------------------------------------------')
            print()
            print('Returning to Main Menu...')

        # If plant does not exist
        else: 
            # datetime object containing current date and time
            now = datetime.now()

            # YY-mm-dd H:M:S
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

            plant_info = []

            # Counter for when adding information for the plant
            count = 1

            # printing out the information instruction menu
            print()
            print('----------------------------------------------------------------------')
            print('|                            INSTRUCTIONS                            |')
            print('----------------------------------------------------------------------')
            print('|                                                                    |')
            print("| Press 'Enter' --> to add the plant information                     |")
            print("| Enter '0' and Press 'Enter' --> to stop adding plant information   |")
            print('|                                                                    |')
            print('----------------------------------------------------------------------')
            print()

            while True:
                info = input(f"Information ({count}): ")
                if info != '0':
                    # print("Information added")
                    plant_info.append(info)

                    # increment by 1 everytime it loops
                    count +=1 
                    continue
                else:
                    #we're happy with the value given and ready to exit the loop.
                    print("\033c") # clear terminal console
                    break
            
            # store key as a lowercase and name as per user input
            self.data[name_lower] = {'Name': name,
                            'Last Updated': dt_string,
                            'Information': plant_info}

            print(f"Plant '{name}' has been added.")
        
    def search(self, name):
        """
        If plant exist:

        (1) option for the user to add new information
        (2) option for the user to delete any information
        (3) option for the user to delete the whole record about the houseplant
        
        If plant does not exist:
        (1) option for the user to add new plant
        """

        plants = list(self.data.keys())
        # plants_lower = [i.lower() for i in plants]
        plant_information = [] # variable to hold all the plant's information for easy retrieval later
        
        # convert input into lowercase
        name_lower = name.lower()

        # If searched name in database, prints out all the plant's information
        if name_lower in plants:
            # name = name.title()

            print('-------------------------------------------------------')
            print('|                 Plant Information                   |')
            print('-------------------------------------------------------')
            print()

            # if name is found
            for k, v in self.data[name_lower].items():
                if k != 'Information':
                    print(f"{k}: {v}")
                else:
                    print('')
                    print(f"{k}: ")
                    count = 1
                    for info in v:
                        print(f"({count}) {info} ")
                        plant_information.append(f'({count}) {info}') # appending each information into the plant_information list
                        count += 1
            print()
            print('------------------------------------------------------')

            print()
            print("There are 3 options for you to choose from: ")
            print()
            print(' (1) Add new information')
            print(' (2) Delete plant information')
            print(' (3) Delete plant record')
            print()
            print(' (0) Return to Main Menu')
            print()

            # Then, promt user if they would like to perform any of the 3 actions to add new information, delete information or delete the entire record
            while True:
                
                choice = input("What would you like to do? Please enter 1, 2, 3 or 0: ")

                # if user decides to add new information
                if choice == '1':
                    self.add_information(name_lower)
                    break
                
                # if user chooses to delete information
                elif choice == '2':
                    print()
                    print('-------------------------------------------------------')
                    print()
                    print('Which information would you like to delete?')
                    print()

                    # printing out the list of information from plant_information list
                    for info in plant_information:
                        print(info)

                    # Option for user to go back to Main Menu
                    print()
                    print(" (0) Return to Main Menu")
                    print()
                    avail_options = [i for i in range(1, len(plant_information) + 1)] # getting the index values

                    while True:
                        
                        number = input(f"Please enter your choice ({str(avail_options).strip('[]')} or 0): ") # printing the options as a string

                        if number in str(avail_options):
                            number = int(number) # convert string into int

                            # passing the plant name and information index to be deleted to the edit_information records
                            self.edit_information(name, number-1) # minus 1 as index always starts at 0
                            break

                        elif number == '0':
                            break

                        else:
                            print()
                            print('Invalid input! Please try again.')
                            continue                    
                    
                    break

                # if user chooses to delete the entire record
                elif choice == '3':
                    print()
                    print('Deleting entire record...')

                    # passing the plant name to the delete_records function
                    self.delete_record(name_lower)
                    break

                # if user chooses to return to Main Menu
                elif choice == '0':
                    print("\033c")
                    break

                # if user enters an invalid input
                else:
                    print()
                    print('Invalid input. Try again.')
                    print()
                    continue

        else:
            print('----------------------------------------------------------------------')
            print('|                     Message: Plant not found!                     |')
            print('----------------------------------------------------------------------')
            print()
            
            while True:
                choice = input("Would you like to add the Plant? (1 = Yes, 2 = No)")
                if choice == '1':
                    self.add_plant(name)
                    break
                elif choice == '2':
                    print('Exiting...')
                    break
                else:
                    print()
                    print('Invalid input. Try again.')
                    continue

    def add_information(self, name):

        name = name.lower()
        
        # accessing the plant information list
        plant_info = self.data[name]['Information']

        # get the current count of information and adding 1
        count = len(self.data[name]['Information']) + 1

        # printing out the instruction menu 
        print()
        print('----------------------------------------------------------------------')
        print('|                            INSTRUCTIONS                            |')
        print('----------------------------------------------------------------------')
        print('|                                                                    |')
        print("| Press 'Enter' --> to add the plant information                     |")
        print("| Enter '0' and Press 'Enter' --> to stop adding plant information   |")
        print('|                                                                    |')
        print('----------------------------------------------------------------------')
        print()

        while True:
            info = input(f"Information ({count}): ")
            if info != '0':
                # appending the new information into the existing list
                plant_info.append(info)

                # increment by 1 everytime it loops
                count +=1 
                continue

            else:
                #we're happy with the value given.
                #we're ready to exit the loop.

                # Before exiting, let's update the plant's last updated time 
                # datetime object containing current date and time
                now = datetime.now()

                # dd-mm-YY H:M:S
                dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                
                # updating the last updated date
                self.data[name]['Last Updated'] = dt_string

                print()
                print("Stop Editing ...")
                break

    def save_output(self):

        # open the file with write access. If file do not exist, it will create a new one
        f = open("myplants.txt", "w")

        keys = list(self.data.keys())

        # For every dictionary key, we will retrieve the key and value from it.
        for i in keys:
            for k, v in self.data[i].items():
                if k != 'Information':
                    f.write(f"{v}\n")
                
                # If the key is "information", we will prin them out separately in a single line
                else:
                    for info in v:
                        f.write(f"{info}\n")
                        
            # add an additional line of space between each Plant data            
            f.write("\n")
        
        f.close()
        print('Saved')

    def delete_record(self, name):
        """ 
        A function to delete plant records
        """
        
        # removing a key from dictionary based on the plant name provided 
        del self.data[name]
        print("\033c") # clear teminal output
        print(f'Plant "{name}"" has been deleted.')

    def edit_information(self, name, number):
        # takes in the plant name and the information ID to be deleted

        # deleting the chosen information from the plant data
        del self.data[name]['Information'][number]
        print()
        print('----------------------------------------------------------------------')
        print(f'|                   Message: Information deleted.                   |')
        print('----------------------------------------------------------------------')


def main():

    # Main menu
    print('What would you like to do?')

    print()
    print(' (1) View All Plants')
    print(' (2) Add Plant')
    print(' (3) Search Plant')
    print()
    print(' (4) Exit')
    print()

    while True:
        choice = input('Please enter 1, 2, 3 or 4: ')
        print("\033c") # clear terminal console
        print()

        if choice in ['1', '2', '3', '4']:
            if choice == '1':

                # run view_all() function
                start.view_all()
                print()

                # Once the view all function has successfully been executed, go back to the Main Menu
                main()

            # if user decides to add a plant
            elif choice == '2':
                plant_name = input('Please enter the name of the plant you would like to add: ')
                start.add_plant(plant_name)
                print()

                # go back to the Main Menu
                main()

            # if user decides to search for a plant
            elif choice == '3':
                plant_name = input('Please enter the plant name: ')
                print()
                start.search(plant_name)
                print()

                # go back to the Main Menu
                main()

            elif choice == '4':
                start.save_output()
                print('Exiting program...')
                break

            # Break out of the while Loop
            break
        else:
            print('Invalid input! Please try again.')
            print()

            main()

start = Plant()
print("\033c") # clear the terminal console before starting the program

if __name__ == "__main__":
    main()

