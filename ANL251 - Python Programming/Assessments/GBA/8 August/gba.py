# Updated as of 2 Aug 2020

from datetime import datetime
import os

class Plant:
    def __init__(self, filepath = 'myplants.txt'):
        self.filepath = filepath
        self.data = self.load_data()
    
    def load_data(self):
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
            plant_dict[info[0]] = {'Name': info[0],
                                    'Last Updated': info[1],
                                    'Information': info[2:]}
        
        return plant_dict
        
        # closing the text file
        f.close()
        
    def view_all(self):

        print("How would you like to view it?")
        print("""
        (1) Alphabetical Order
        (2) Latest Revision Time
        """)

        # Implement a while loop to ensure that user enters a valid input. Else, prompt the user to enter again.
        while True:
            choice = input('Choice (1 or 2): ')
            print("\033c")
            print('-------------------------------------------------------')
            print('|                 Plant Information                   |')
            print('-------------------------------------------------------')


            if choice in ['1', '2']:
                if choice == '1':
                    # sorting the values by their names
                    # returns a list of tuples
                    sort_by_name = sorted(self.data.items(), key=lambda plant: plant[0])

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

                # break out of the while loop
                break

            else:
                print('Invalid input! Please try again.')
                continue

    def add_plant(self, name):

        plants = list(self.data.keys())

        # check if plant already exist
        if name in plants:
            print()
            print('Plant name already exist.')
            print('Returning back to main menu...')

        # If plant does not exist
        else: 
            # datetime object containing current date and time
            now = datetime.now()

            # YY-mm-dd H:M:S
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

            plant_info = []

            # Counter for when adding information for the flower
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
                    #we're happy with the value given.
                    #we're ready to exit the loop.
                    print()
                    print("Stop Editing ...")
                    break

            self.data[name] = {'Name': name,
                            'Last Updated': dt_string,
                            'Information': plant_info}

            print('Plant added.')
        
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
        plant_information = [] # variable to hold all the plant's information for easy retrieval later
        
        # If searched name in database, prints out all the plant's information
        if name in plants:

            print('-------------------------------------------------------')
            print('|                 Plant Information                   |')
            print('-------------------------------------------------------')
            # if name is found
            for k, v in self.data[name].items():
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
            print('------------------------------------------------------')

            # Then, promt user if they would like to perform any of the 3 actions to add new information, delete information or delete the entire record
            while True:
                print()
                print("There are 3 options for you to choose from: ")
                print('     (1) Add new information')
                print('     (2) Delete plant information')
                print('     (3) Delete plant record')
                print('     (4) Go back to main menu')
                print()
                
                choice = input("What would you like to do? Enter 1, 2, 3 or 4: ")

                # if user decides to add new information
                if choice == '1':
                    self.add_information(name)
                    break
            
                # if user chooses to delete information
                elif choice == '2':
                    print()
                    print('Deleting any information')
                    print()

                    print('Which information would you like to delete?')
                    print()

                    # printing out the list of information from plant_information list
                    for info in plant_information:
                        print(info)

                    print()
                    avail_options = [i for i in range(1, len(plant_information) + 1)] # getting the index values

                    while True:
                        
                        number = input(f"Please enter your choice ({str(avail_options).strip('[]')[:-1]}or {str(avail_options).strip('[]')[-1]}): ") # printing the options as a string

                        if number in str(avail_options):
                            number = int(number) # convert string into int

                            # passing the plant name and information index to be deleted to the edit_information records
                            self.edit_information(name, number-1) # minus 1 as index always starts at 0
                            break

                        else:
                            print('Invalid input! Please try again.')
                            continue                    
                    
                    break

                # if user chooses to delete the entire record
                elif choice == '3':
                    print()
                    print('Deleting entire record')
                    print()

                    # passing the plant name to the delete_records function
                    self.delete_record(name)
                    break

                # if user chooses to return to main menu
                elif choice == '4':
                    print()
                    print("Returning to main menu...")
                    print()
                    break

                # if user enters an invalid input
                else:
                    print('Invalid input. Try again.')
                    continue

        else:
            print('Flower not found!')
            print()
            while True:
                # convert the string input to lowercase 
                choice = input('Would you like to add the flower? (Y/N): ').lower()
                if choice == 'y':
                    self.add_plant(name)
                    print('Plant Added.')
                    break
                elif choice == 'n':
                    print('Exiting...')
                    break
                else:
                    print('Invalid input. Try again.')
                    continue

    def add_information(self, name):

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
                        
            # add an additional line of space between each flower data            
            f.write("\n")
        
        f.close()
        print('Saved')

    def delete_record(self, name):
        # a function to delete plant records
        
        # removing a key from dictionary based on the plant name provided 
        del self.data[name]
        
        print(f"Plant {name} has been deleted.")

    def edit_information(self, name, number):
        # takes in the plant name and the information ID to be deleted

        # deleting the chosen informtion from the plant data
        del self.data[name]['Information'][number]

        print("Information deleted.")

start = Plant()
print("\033c") # clear the terminal console before starting the program

def main():

    # Main menu
    print('What would you like to do?')
    print('''
    (1) View All Plants
    (2) Add Plant
    (3) Search Plant
    (4) Exit
    ''')

    while True:
        choice = input('Please enter 1, 2, 3 or 4: ')
        print("\033c")
        print()

        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                print(start.view_all())
                print()

                # go back to the main menu
                main()

            # if user decides to add a plant
            elif choice == '2':
                plant_name = input('Please enter the name of the plant you would like to add: ')
                start.add_plant(plant_name)
                print()

                # go back to the main menu
                main()

            # if user decides to search for a plant
            elif choice == '3':
                plant_name = input('Please enter the plant name: ')
                print()
                start.search(plant_name)
                print()

                # go back to the main menu
                main()

            elif choice == '4':
                start.save_output()
                print('Exiting program...')
                break

            # Break out of the while Loop
            break
        else:
            print('Invalid input! Please try again.')
            continue


if __name__ == "__main__":
    main()



# d = start.data



# # sorting the values by their last updated date by descending order 
# sort_rev_date = sorted(d.items(), key=lambda plant: plant[1]['Last Updated'], reverse= True)

