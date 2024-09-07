#!/usr/bin/env python3
""" scribt for database"""


import os
import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file

MONGODB_URI = os.getenv("MONGODB_URI")
if not MONGODB_URI:
    print("Error: MONGODB_URI is not set in the env.", file=sys.stderr)
    sys.exit(1)
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")

if not MONGODB_DATABASE:
    print("Error: db must be set in the environment.", file=sys.stderr)
    sys.exit(1)


try:
    # Connect to MongoDB using the URI from environment variables
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    # Trigger a server selection to verify connection
    client.admin.command('ping')
    db = client[MONGODB_DATABASE]
    print("Connected to MongoDB successfully.")
except ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}", file=sys.stderr)
    sys.exit(1)
