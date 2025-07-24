# Import libraries
import pandas as pd

# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python
# Build api
import fastapi
app = fastapi.FastAPI(title="Social Media Engagement API")

# Load the csv
df = pd.read_csv("social_media_engagement.csv")


