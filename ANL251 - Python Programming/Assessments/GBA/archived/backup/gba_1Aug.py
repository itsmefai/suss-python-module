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

        for i in contents.split('\n\n'):
            plant_info = i.split('\n')
            plant_name = plant_info[0]

            plant_dict[plant_name] = {'Name': plant_name,
                                      'Last Updated': plant_info[1],
                                      'Information': plant_info[2:-1]}
        
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

            # dd-mm-YY H:M:S
            dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
            
            plant_info = []
            
            while True:
                info = input(f"Please enter the information for plant name: {name}. Key in 0 to exit: ")
                if info != '0':
                    print("Information added")
                    plant_info.append(info)
                    continue
                else:
                    #we're happy with the value given.
                    #we're ready to exit the loop.
                    print("Stop Editing ...")
                    break

            self.data[name] = {'Name': name,
                            'Last Updated': dt_string,
                            'Information': plant_info}
            print('Plant added.')
        
    def search(self, name):
        
        plants = list(self.data.keys())
        
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
            
        else:
            print('Flower not found!')
            print('Would you like to add the flower? Yes = 1, No = 0')
            while True:
                choice = input()
                if choice == '1':
                    self.add_plant(name)
                    print('Plant Added.')
                    break
                elif choice == '0':
                    print('Exiting...')
                    break
                else:
                    print('Invalid input. Try again.')
                    continue

start = Plant()

def main():

    print('What would you like to do?')
    print('''
    (1) View All Plants
    (2) Add Plant
    (3) Search Plant
    (4) Exit
    ''')

    choice = input()

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
        print('Exiting program...')


if __name__ == "__main__":
    main()