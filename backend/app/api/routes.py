from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import os, uuid, json, re
import qrcode
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = os.getenv("DATA_DIR", "data")
METADATA_FILE = os.getenv("METADATA_FILE", "metadata.json")


# Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)

