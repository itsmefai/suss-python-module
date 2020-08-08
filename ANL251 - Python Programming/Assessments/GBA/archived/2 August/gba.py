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
        
        keys = list(self.data.keys())

        for i in keys:
            for k, v in self.data[i].items():
                if k != 'Information':
                    print(f"{k}: {v}")
                else:
                    print(f"{k}:")
                    count = 1
                    for info in v:
                        print(f"({count}) {info}")
                        count += 1
            print()
    
    def add_plant(self, name):

        plants = list(self.data.keys())

        # check if plant already exist
        if name in plants:
            print('Plant name already exist.')

        # If plant does not exist
        else: 
            # datetime object containing current date and time
            now = datetime.now()

            # YY-mm-dd H:M:S
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

            plant_info = []

            # Counter for when adding information for the flower
            count = 1

            print()
            print("INSTRUCTIONS:") 
            print("Enter --> to add plant information")
            print("0     --> stop adding plant information")
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
        
        plants = list(self.data.keys())
        
        # Prints out all the plant information
        if name in plants:
            # if name is found
            for k, v in self.data[name].items():
                if k != 'Information':
                    print(f"{k}: {v}")
                else:
                    print(f"{k}:")
                    count = 1
                    for info in v:
                        print(f"({count}) {info}")
                        count += 1

            # promt user if they would like to add in additional information
            while True:
                print()
                choice = input("Would you like to add in additional information? (Y or N): ")
                if choice.lower() == 'y':
                    self.edit_information(name)
                    break
                elif choice.lower() == 'n':
                    break
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

    def edit_information(self, name):

        # accessing the plant information list
        plant_info = self.data[name]['Information']

        # get the current count of information and adding 1
        count = len(self.data[name]['Information']) + 1

        print()
        print("INSTRUCTIONS:") 
        print("Enter --> to add plant information")
        print("0     --> stop adding plant information")
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

                # Before exiting, let's update the plant's last updated time data
                # datetime object containing current date and time
                now = datetime.now()

                # dd-mm-YY H:M:S
                dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                
                self.data[name]['Last Updated'] = dt_string

                print()
                print("Stop Editing ...")
                break

    def save_output(self):
        # open the file with write access. If file do not exist, it will create a new one
        f = open("myplants.txt", "w")

        keys = list(self.data.keys())

        for i in keys:
            for k, v in self.data[i].items():
                if k != 'Information':
                    f.write(f"{v}\n")
                else:
                    for info in v:
                        f.write(f"{info}\n")
                        
            # add an additional line of space between each flower data            
            f.write("\n")
        
        f.close()
        print('Saved')


start = Plant()

def main():

    # Main menue
    print('What would you like to do?')
    print('''
    (1) View All Plants
    (2) Add Plant
    (3) Search Plant
    (4) Exit
    ''')

    while True:
        choice = input('Please enter 1, 2, 3 or 4: ')
        print()

        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                print(start.view_all())
                print()

                # go back to the main menu
                main()
            elif choice == '2':
                plant_name = input('Please enter the plant name: ')
                start.add_plant(plant_name)
                print()

                # go back to the main menu
                main()
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