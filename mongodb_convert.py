from pymongo import MongoClient
import pandas as pd

dataset_posts = pd.read_csv("dataset-posts.csv")
dataset_words = pd.read_csv("dataset-pasangankata.csv")
client = MongoClient("mongodb://localhost:27017/") 
db = client['data_instagram']
collection1 = db['posts']
collection2 = db['pairofwords']
insert_posts = collection1.insert_many(dataset_posts.to_dict('records'))
insert_words = collection2.insert_many(dataset_words.to_dict('records'))
print("sukses")
