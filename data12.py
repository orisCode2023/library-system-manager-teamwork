import csv, json, pandas as pd


class Data:
    @staticmethod
    def load_from_json(file_name):
        with open(file_name, 'r') as f:
            books_data = json.loads(f.read())
            return books_data
        
    @staticmethod  
    def add_to_data(books_data: dict, data: dict):
        books_data["books"].append(data)
        return books_data

    @staticmethod
    def write_to_json(file_name, file_data: dict):
        with open(file_name, "w") as f:
            json.dump(file_data, f, indent=4)
     
    @staticmethod
    def write_to_csv(file_name, data):
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            column = 0
            for book in data["books"]:
                if column == 0:
                    header = book.keys()
                    writer.writerow(header)
                    column += 1
                writer.writerow(book.values())
                print(book.values())
            
            file.close()


    @staticmethod
    def read_from_csv(file_name):
        df = pd.read_csv(file_name)
        return df





