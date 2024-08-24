# ใช้ base image ของ Python
FROM python:3.9-slim

# กำหนด working directory ภายใน container
WORKDIR /app

# คัดลอกไฟล์ requirements.txt ไปยัง container
COPY requirements.txt .

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมดไปยัง container
COPY . .

# ระบุคำสั่งที่ให้รันเมื่อ container เริ่มทำงาน
CMD ["python", "app.py"]
