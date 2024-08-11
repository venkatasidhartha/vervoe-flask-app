from flask import current_app
import requests
import math
import json
from app.api.response import response
from app import db
from app.api.models import ProcessData
from multiprocessing import Process
import logging
from app.api.utility import writeTOfile


class DataProcessing:

    def stringConversion(self,string:str):
        arr = []
        for i in string:
            if i.isupper():
                arr.append(i.lower())
            elif i.islower():
                arr.append(i.upper())
            else:
                arr.append(i)
        return ''.join(arr)
    
    def splitINTO_chunks(self,data:list,no_of_chunk:int=5)->list:
            arr = []
            lenOfChunks = math.ceil(len(data) / no_of_chunk)
            startValue = 0
            endValue = no_of_chunk
            for i in range(lenOfChunks):
                arr.append(data[startValue:endValue])
                startValue = endValue
                endValue = endValue + no_of_chunk
            return arr

    def storeProcessedData(self,processed_data:list):
        try:
            for obj in processed_data:
                data_obj = ProcessData(
                    title=obj["title"],
                    price=obj["price"],
                    description=obj["description"],
                    category=obj["category"],
                    rating=obj["rating"],
                )
                db.session.add(data_obj)
                db.session.commit()
        except Exception as e:
            logging.error("Store Processed Data Function Failed",exc_info=e)
            writeTOfile("storeProcessedData.json",data=json.dumps({"processed_data":processed_data,"error":str(e)}))


    def data_processer(self,chunk):
        try:
            arr = []
            for object in chunk:
                arr.append({
                    "title":self.stringConversion(object["title"]),
                    "price":object["price"],
                    "description":self.stringConversion(object["description"]),
                    "category":self.stringConversion(object["category"]),
                    "rating":object["rating"],
                })
            
            self.storeProcessedData(processed_data=arr)
        except Exception as e:
            logging.error("Data Processer Function Failed",exc_info=e)
            writeTOfile("data_processer.json",data=json.dumps({"chunk":chunk,"error":str(e)}))


    def fetch_data_distribute(self):
        try:
            apidata = requests.get(current_app.config['EXTERNAM_SERVICE_URL'])
            if apidata.status_code != 200:
                raise Exception("External service API is down")
            chunks = self.splitINTO_chunks(data=apidata.json())
            for chunk in chunks:
                parallelProcess = Process(target=self.data_processer,args=(chunk,))
                parallelProcess.start()
        except Exception as e:
            logging.error("Fetch Data Distribute Function Failed",exc_info=e)

    def start_process(self):
        parallelProcess = Process(target=self.fetch_data_distribute)
        parallelProcess.start()
        return response(message="Process is started")
    
    
class DataProcessed:

    def get_processedData(self,page_no:int=1,page_length:int=5):
        start_point = (page_no - 1) * page_length
        end_point = page_length
        records = []
        if  page_no == 0 and page_length == 0:
            records = ProcessData.query.all()
        else:
            records = ProcessData.query.offset(start_point).limit(end_point).all()
        responseList = [{
                            "id":r.id,
                            "title":r.title,
                            "price":r.price,
                            "description":r.description,
                            "category":r.category,
                            "rating":r.rating
                        } for r in records]
        message = ""
        if len(responseList) <= 0:
            message = "Data is Empty"
        return response(data=responseList,message=message)
