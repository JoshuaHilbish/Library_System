import pandas as pd
import os
import datetime
import json
import os
from sqlalchemy import create_engine # allows for usage of data base

data_path="data"
dds_path="data\DDS"

class Inventory():
    def __init__(self):
        self.inventory = create_engine('sqlite:///data/inventory.db', echo=False)

    def get_full_db(self):
        return self.inventory

    def get_db_frame(self):
        frame=pd.read_sql("SELECT * FROM  inventory", self.inventory)
        return frame

    def get_tables(self):
        return self.inventory.table_names()

    def query_db(self,question):
        try:
            query=pd.read_sql(question, self.inventory)
        except Exception as ex:
            return ex
        return query 

    def open_dds(self, level = False , inside_key=0):
        inFile1=os.path.join(dds_path,'DewyDecimalSystemKeys.json')
        with open(inFile1) as json_file:
            dds_top = json.load(json_file)

        dds_top_list=[]
        for k in dds_top.keys():
            dds_top_list.append("{}:{}".format(k,dds_top[k]))
            
        inFile2=os.path.join(dds_path,'DewyDecimalSystemValues.json')
        with open(inFile2) as json_file:
            dds_inside = json.load(json_file)

        if level == 0:
            return dds_top_list
        elif level == 1:
            dds_inside_list=[]
            inside_key=(str(inside_key))
            for k in dds_inside[inside_key].keys():
                dds_inside_list.append("{}:{}".format(k,dds_inside[inside_key][k]))
            return dds_inside_list
        else:
            return dds_top,dds_inside

    def gen_call_num(self,num):
        db=self.query_db("select call_number from inventory")
        searchnum=(float("{}.9999".format(num)))
        db=db['Call_Number'].where(db['Call_Number']<=searchnum)
        db = db.sort_values(ascending=False).head(1)
        db="{0:.4f}".format(db.iloc[0]+.0001)
        if str(db).split(".")[0]!=num:
            db=float("{}.0001".format(num))
        return db
    
    def add_media(self,med_list):
        try:
            frame1=self.get_db_frame()
            frame1=frame1.drop(["index"],axis=1)
            frame2=pd.DataFrame([med_list],columns=["Type","Title","Author_First_Name","Author_Last_Name","Publisher","ISBN","Release_Date","Date_Added","Pages","Price","Call_Number","Genre","Status"])
            frame=pd.concat([frame1, frame2], ignore_index=True)
            frame.to_sql('inventory', con=self.inventory, if_exists='replace')
        except Exception as ex:
            print(ex)
            
    def remove_media(self, call_num):
        try:
            query="Select * from inventory where Call_Number is {}".format(call_num)
            idx=self.query_db(query)
            idx=idx["index"][0]
            frame=self.get_db_frame()
            frame=frame.drop(frame.index[idx])
            frame=frame.drop(["index"],axis=1)
            frame.to_sql('inventory', con=self.inventory, if_exists='replace')
            return 1
        except Exception as ex:
            print(ex)
            return 0
    
    def validate_media(self,call_num):
        try:
            query="Select * from inventory where Call_Number is {}".format(call_num)
            test=self.query_db(query)
            rtrn_list=test.values.tolist()
            return rtrn_list[0]
        except Exception as ex:
            print(ex)
            return 0
    
    def check_out(self, call_num, card_num):
        try:
            query="Select * from inventory where Call_Number is {}".format(call_num)
            idx=self.query_db(query)
            frame=self.get_db_frame()
            frame.iloc[idx["index"][0],13]="Check_Out_By:{}".format(card_num)
            frame=frame.drop(["index"],axis=1)
            frame.to_sql('inventory', con=self.inventory, if_exists='replace')
        except Exception as ex:
            print(ex)
            
    def check_in(self,call_num):
        try:
            query="Select * from inventory where Call_Number is {}".format(call_num)
            idx=self.query_db(query)
            frame=self.get_db_frame()
            frame.iloc[idx["index"][0],13]="Available"
            frame=frame.drop(["index"],axis=1)
            frame.to_sql('inventory', con=self.inventory, if_exists='replace')
            return 1
        except Exception as ex:
            print(ex)
            return 0
        
    def reset_all(self):
        try:
            frame_path=os.path.join(data_path,"Book1.xlsx")
            frame= pd.read_excel(frame_path)
            inventory = create_engine('sqlite:///data/inventory.db', echo=False)
            frame.to_sql('inventory', con=inventory, if_exists='replace')
        except Exception as ex:
            print("inventory:",ex)
            
    def hold_media(self,card_num,call_num):
        try:
            query="Select * from inventory where Call_Number is {}".format(call_num)
            idx=self.query_db(query)
            idx=idx["index"][0]
            frame=self.get_db_frame()
            frame.iloc[[idx],13]="Hold for :{}".format(card_num)
            frame=frame.drop(["index"],axis=1)
            frame.to_sql('inventory', con=self.inventory, if_exists='replace')
            return 1
        except Exception as ex:
            print(ex)
            return 0
