import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os
os.system("pip uninstall -y opencv-python") # สั่งลบตัวเจ้าปัญหาทิ้งทันทีที่แอปเริ่มรัน

import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="Eggplant AI", layout="centered")
st.title("🍆 Eggplant Health Detector")

# โหลดโมเดล
@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# ส่วนดึงภาพจากกล้องมือถือ
img_file = st.camera_input("ส่องกล้องไปที่ใบมะเขือเทศ")

if img_file is not None:
    img = Image.open(img_file)
    results = model(img) # ประมวลผล AI
    
    # วาดกล่องคำตอบลงบนภาพ
    res_plotted = results[0].plot()
    st.image(res_plotted, caption="ผลการวิเคราะห์", use_container_width=True)
    
    # แสดงชื่อโรคที่เจอ
    for box in results[0].boxes:
        label = model.names[int(box.cls)]
        st.success(f"ตรวจพบ: {label}")
st.set_page_config(page_title="Eggplant AI", layout="centered")
st.title("🍆 Eggplant Health Detector")

# โหลดโมเดล
@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# ส่วนดึงภาพจากกล้องมือถือ
img_file = st.camera_input("ส่องกล้องไปที่ใบ")

if img_file is not None:
    img = Image.open(img_file)
    results = model(img) # ประมวลผล AI
    
    # วาดกล่องคำตอบลงบนภาพ
    res_plotted = results[0].plot()
    st.image(res_plotted, caption="ผลการวิเคราะห์", use_container_width=True)
    
    # แสดงชื่อโรคที่เจอ
    for box in results[0].boxes:
        label = model.names[int(box.cls)]
        st.success(f"ตรวจพบ: {label}")
