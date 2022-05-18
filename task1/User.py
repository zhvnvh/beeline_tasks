import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_json(self):
        return json.dump({
            "name" : self.name,
            "age" : self.age
        })

# if __name__ == "__main__":


