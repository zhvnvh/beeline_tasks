import json
import os

class FileStorage:
    def __init__(self, filepath):
        # if not exists create a file
        self.filepath = filepath
    
    def is_file_empty(self):
        return os.stat(self.filepath).st_size == 0

    def get_all(self):
        if self.is_file_empty():
            return None

        with open(self.filepath, "r") as file:
            return json.load(file)
        return None

    def write(self, content):
        with open(self.filepath, "w") as file:
            json.dump(content, file)

    def save(self, data):   
        content = list()  
        if self.is_file_empty():
            content.append(data)
        else:
            with open(self.filepath, "r") as file:
                content = json.load(file)
                if content is not None:
                    content.append(data)
        self.write(content)

    def delete(self, id):
        content = self.get_all()

        if content is None: return

        index = -1

        for i in range(0, len(content)):
            if id == content[i]['id']:
                index = i
                break
        
        if index == -1: return
        
        content.pop(index)
        self.write(content)

    def update(self, id, new_data):
        content = self.get_all()

        if content is None: return 

        index = -1

        for i in range(0, len(content)):
            if id == content[i]['id']:
                index = i
                break
        
        if index == -1: return
        
        for key in new_data:
            content[index][key] = new_data[key]
        
        self.write(content)
