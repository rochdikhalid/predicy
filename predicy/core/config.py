import json 



# Get number of bathrooms
def getNumOfBathrooms():
    num = []
    for i in range(1, 8):
        num.append(i)
    return num

# Get number of bedrooms
def getNumOfBedrooms():
    num = []
    for i in range(1, 11):
        num.append(i)
    return num 
    
# Get location name
def getLocations():
    with open("../data/localities.json", "r") as file:
        localities_data = json.load(file)['localities_data']
    return localities_data


