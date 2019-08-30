import configparser

print("Welcome to acServerConfigurator!")
print("--------------------------------")
print("Press enter to change setup. Enter exit to exit.")
# startConfig = input()
# if startConfig == "exit":
#     SystemExit

# start reading config files
configServer = configparser.ConfigParser()
configServer.optionxform = str 
configServer.read('test_server_cfg.ini')
configCar = configparser.ConfigParser()
configCar.optionxform = str 
configCar.read('test_entry_list.ini')

firstCar = input("Enter the name of cars. One at a time: ")
cars = firstCar
firstColor = input("Specify color: ")
carNumber = 0
configCar["CAR_"+str(carNumber)] = {'MODEL': firstCar,'SKIN': firstColor, 'SPECTATOR_MODE': 0, 'DRIVERNAME': "", 'TEAM': "", 'GUID': "", 'BALLAST': ""}
'''
configCar["CAR_"+str(carNumber)]['MODEL'] = cars
configCar["CAR_"+str(carNumber)]['SKIN'] = color
configCar["CAR_"+str(carNumber)]['SPECTATOR_MODE'] = 0
configCar["CAR_"+str(carNumber)]['DRIVERNAME'] = ""
configCar["CAR_"+str(carNumber)]['TEAM'] = ""
configCar["CAR_"+str(carNumber)]['GUID'] = ""
configCar["CAR_"+str(carNumber)]['BALLAST'] = ""
'''
while True:
    carNumber += 1
    nextCar = ";"
    nextCar += input("Next car: ")
    if nextCar == ";":
        break
    else:
        color = input("Specify color: ")
        configCar["CAR_"+str(carNumber)] = {'MODEL': nextCar[1:],'SKIN': color, 'SPECTATOR_MODE': 0, 'DRIVERNAME': "", 'TEAM': "", 'GUID': "", 'BALLAST': ""}
        '''
        configCar["CAR_"+str(carNumber)]['MODEL'] = nextCar[1:]
        configCar["CAR_"+str(carNumber)]['SKIN'] = color
        configCar["CAR_"+str(carNumber)]['SPECTATOR_MODE'] = 0
        configCar["CAR_"+str(carNumber)]['DRIVERNAME'] = ""
        configCar["CAR_"+str(carNumber)]['TEAM'] = ""
        configCar["CAR_"+str(carNumber)]['GUID'] = ""
        configCar["CAR_"+str(carNumber)]['BALLAST'] = ""
        '''
        cars += nextCar
configServer['SERVER']['CARS'] = cars

track = input("Enter the name of track: ")
configServer['SERVER']['TRACK'] = track

track_layout = input("Enter the layout of track, if any: ")
configServer['SERVER']['CONFIG_TRACK'] = track_layout

# serverName = "XiaoJinServer"
# newServerName = input("server name: ")
# if len(newServerName) != 0:
#     serverName = newServerName
# config['SERVER']['NAME'] = serverName


with open('test_server_cfg.ini', 'w') as configfileServer:
    configServer.write(configfileServer)

with open('test_entry_list.ini', 'w') as configfileCars:
    configCar.write(configfileCars)
