import json
filename = "cars.json"

class Car:
    def __init__(self, model, size, price):
        self.model = model 
        self.size = size
        self.price = price
    def get_all(self):
        return {
            "model" : self.model, 
            "size" : self.size, 
            "price" : self.price
        }
    
def upload(arr):
    with open(filename, "w") as file:
        json.dump(arr, file)

def download():
    with open(filename, "r") as file:
        return json.load(file)

def show_models(cars):
    for car in cars:
        print(car["model"])

def under_hundred():
    cheap = []
    cars = download()

    for car in cars:
        if car["price"] < 100:
            cheap.append(car)
    return cheap

def medium_cars():
    medium = []
    cars = download()

    for car in cars:
        if car["size"] == "medium":
            medium.append(car)
    return medium

if __name__ == "__main__":
    show_models(under_hundred())
    print("-----")
    show_models(medium_cars())