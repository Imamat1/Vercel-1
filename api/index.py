# Vercel serverless function entry point
import sys
import os

# Add the backend directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Import the FastAPI app
from server import app

# Export the app for Vercel
app = app