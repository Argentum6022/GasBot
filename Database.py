from pymongo import MongoClient
class DataBase:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')

        self.db = self.client.gazprom
        self.collection = self.db.gazprom


    def get_documents(self,fg,domen,tech,method):
            print("Get all users")
            data = self.collection.find({"Технология":tech,"Домен":domen,'Функциональная группа':fg,'Метод использования':method},{'_id':0})

            res = [i for i in data]
            return res

    def get_technology(self,domen,func):
        data = self.collection.find({'Домен':domen,'Функциональная группа':func},{'Технология':1,'_id':0})
        res = [i for i in data]
        res_new = []
        for i in res:
            res_new.append(i['Технология'])
        return set(res_new)


    def get_domen(self,func):
        data = self.collection.find({'Функциональная группа':func}, {'Домен': 1, '_id': 0})
        res = [i for i in data]
        res_new = []
        for i in res:
            res_new.append(i['Домен'])
        return set(res_new)

    def get_func_group(self):
        data = self.collection.find({}, {'Функциональная группа': 1, '_id': 0})
        res = [i for i in data]
        res_new = []
        for i in res:
            res_new.append(i['Функциональная группа'])
        return set(res_new)


    def get_method(self,domen,func,tech):
        data = self.collection.find({'Домен':domen,'Функциональная группа':func,'Технология':tech}, {'Метод использования': 1, '_id': 0})
        res = [i for i in data]
        res_new = []
        for i in res:
            res_new.append(i['Метод использования'])
        return set(res_new)




Data = DataBase()

Data.db.updateMany({'Домен' : "Искусственный интеллект и цифровые двойники "}, {'$set': {'Домен' : 'Искусственный интеллект и цифровые двойники'}})