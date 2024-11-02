import pymongo
import random
import time
from datetime import datetime

# MongoDB connection string (replace <password> and <cluster-url> with your actual values)
MONGO_URI = "mongodb+srv://your-username:<password>@your-cluster-url.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client['sample_database']
collection = db['data_collection']

# Function to generate and insert data
def generate_and_insert_data():
    data = {
        "temperature": round(random.uniform(20.0, 25.0), 2),
        "humidity": round(random.uniform(30.0, 50.0), 2),
        "timestamp": datetime.utcnow()
    }
    collection.insert_one(data)
    print("Data inserted:", data)

# Run the data generation in a loop
if __name__ == "__main__":
    for _ in range(10):  # Generate 10 sample records
        generate_and_insert_data()
        time.sleep(1)  # Pause for a second between inserts
