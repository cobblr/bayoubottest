import logging
for logger_name in ['streamlit', 'streamlit.runtime', 'streamlit.runtime.scriptrunner_utils']:
    logging.getLogger(logger_name).setLevel(logging.ERROR)

import asyncio
import time
from datetime import datetime
import nest_asyncio
import os
from dotenv import load_dotenv

from xrpl.asyncio.clients import AsyncWebsocketClient
from xrpl.models import BookOffers, IssuedCurrency, XRP
from xrpl.utils import drops_to_xrp
from openai import AsyncOpenAI
from decimal import Decimal

import streamlit as st
import pandas as pd
import plotly.express as px
from threading import Thread

# Load environment variables
load_dotenv()
XAI_API_KEY = os.getenv("XAI_API_KEY")
if not XAI_API_KEY:
    st.error("XAI_API_KEY not found in .env file. Please add it.")
    st.stop()

# ... rest of your config, functions (get_current_price, get_grok_sentiment, check_signal, background_updater), session_state setup, Thread start, and the entire Streamlit UI code ...

# No ! commands, no tunnel code at the bottom