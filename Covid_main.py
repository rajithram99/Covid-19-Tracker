import requests
import matplotlib.pyplot as plt

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "af8414c813mshfa68b005eced6a6p1d6a6fjsn16bfa57b4c34"
    }

response = requests.request("GET", url, headers=headers).json()

def view_world_data():
    for each in response['world_total']:
        print(each)


def search_by_country(c_name):
    flag=0
    print('#####################################################')
    print('#####################################################')
    for each in response['countries_stat']:
        if each['country_name'].lower() == c_name.lower():
            del each['region']
            for key in each:
                print(key.upper(), ' : ', each[key])
                flag=1
            plt.title(each['country_name'] + "'s Statistics")
            del each['country_name']

            plt.barh(range(len(each)), list(each.values()), color='magenta', align='center')
            plt.yticks(range(len(each)), list(each.keys()))
            plt.show()
    if flag == 0:
        print(' Sorry !! The Data For this country is unavailable ')
    print('#####################################################')
    print('#####################################################')

def display_all():

    for each in response['countries_stat']:
        del each['region']
        for key in each:
            print(key.upper(), ' : ', each[key])
        print('#####################################################')
        print('#####################################################')


def main():
        choice = 0

        while choice != -1:
            print(' ####$$$$%^ WELCOME TO THE COVID-19 TRACKER ^%$$$$#### ')
            print('1. Print the Data of all available countries ')
            print('2. Print the data of a country of your choice ')
            print('3. Print the World Data ')
            print('4. Exit ')
            choice = int(input('   Please Enter your choice (1-4) = '))

            if choice == 1:
                display_all()
            elif choice == 2:
                c_name = str(input(" Enter the Country's Name = "))
                search_by_country(c_name)
            elif choice == 3:
                view_world_data()
            elif choice == 4:
                print(' Thank you and bye!!!')
                choice = - 1
            else:
                print(" Invalid Choice")
                choice = 0
main()







