from pymongo import MongoClient
from jarowinkler import *

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


    def get_documents_by_fg(self,func):
            print("Get all users")
            data = self.collection.find({"Функциональная группа":func},{'_id':0})

            res = [i for i in data]
            return res

    def get_documents_by_fg_and_domen(self,func,domen):
        print("Get all users")
        data = self.collection.find({"Функциональная группа": func,'Домен':domen}, {'_id': 0})

        res = [i for i in data]
        return res

    def get_documents_by_fg_and_domen_and_tech(self,func,domen,tech):
        print("Get all users")
        data = self.collection.find({"Функциональная группа": func, 'Домен': domen,'Технология':tech}, {'_id': 0})

        res = [i for i in data]
        return res

    def get_correlation(self,s1):
        res=[]
        maxx = 0.0
        object=5
        objects = []
        count=0
        data = self.collection.find({},{'_id':0})
        for i in data:
            res.append(i)
        for i in res:
            count+=1
            if jarowinkler_similarity(s1,i['Описание']) > maxx:
                maxx = jarowinkler_similarity(s1,i['Описание'])
                objects.append(i)
        return objects[-1:-5:-1]




Data = DataBase()