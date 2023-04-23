from pymongo import MongoClient
class DataBase:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')

        self.db = self.client.gazprom
        self.collection = self.db.gazprom


    def get_documents(self,fg,domen,tech,method):
            print("Get all users")
            data = self.collection.find({"Технология":tech,"Домен":domen,'Функциональная группа':fg,'Метод использования':method})

            res = [i for i in data]
            return res



Data = DataBase()

print(Data.get_documents("Добыча на шельфе","AR/VR и естественные интерфейсы","AR","Визуализация информации для поддержки процессов"))