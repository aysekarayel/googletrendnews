import streamlit as st
import xml.etree.ElementTree as et
import sqlitecloud
import sqlite3
import requests
from datetime import date
from google import genai
from pydantic import BaseModel

conn = sqlitecloud.connect('sqlitecloud://cx3hxeobnk.g6.sqlite.cloud:8860/chinook.sqlite?apikey=TcI4Cyl57LO9xl5mDfAuySGlzAGSJ5iKbPO1dSyUBSw')
c = conn.cursor()

c.execute("SELECT * FROM haberler ORDER BY trend_id DESC LIMIT 99")
haberler=c.fetchall()

for i in range(haberler):
    st.image(haberler[i][3])
    st.write(haberler[i][1])
    st.link_button("Habere Git",haberler[i][2])
