# TODO List API

این پروژه یک API ساده برای مدیریت لیست کارها (TODO List) با استفاده از FastAPI و MongoDB است. این پروژه با هدف تمرین مفاهیم RESTful API، متدهای HTTP و ارتباط با پایگاه‌داده NoSQL طراحی شده است.

## 📌 ویژگی‌ها
- پیاده‌سازی کامل CRUD
- اتصال به دیتابیس MongoDB
- پاسخ‌دهی با فرمت JSON
- دارای Swagger UI برای مستندسازی خودکار

## 📦 تکنولوژی‌ها و ابزارها
- Python 3.10+
- FastAPI
- Uvicorn (برای اجرا)
- Motor (MongoDB Async Driver)
- MongoDB (لوکال)

## 🚀 اجرای پروژه

### 1. کلون کردن پروژه
```bash
git clone https://github.com/your-username/todo-api.git
cd todo-api
```

### 2. نصب وابستگی‌ها
```bash
pip install -r requirements.txt
```

### 3. اجرای سرور
```bash
uvicorn main:app --reload
```

سرور در آدرس زیر در دسترس خواهد بود:
```
http://127.0.0.1:8000
```

### 📄 مستندات API

مستندات Swagger UI به صورت خودکار در این مسیر قابل مشاهده است:
```
http://127.0.0.1:8000/docs
```

---

## 📂 ساختار پروژه
```bash
📁 todo-api
├── main.py              # فایل اصلی اجرای FastAPI
├── database.py          # اتصال به MongoDB با Motor
├── models.py            # مدل‌های پایتونی برای داده‌ها
├── crud.py              # توابع مربوط به CRUD
├── requirements.txt     # لیست کتابخانه‌های مورد نیاز
└── README.md            # توضیحات پروژه (همین فایل)
```

---

## 📬 نقاط پایانی (Endpoints)

- `GET /tasks` — دریافت تمام تسک‌ها
- `GET /tasks/{id}` — دریافت یک تسک خاص
- `POST /tasks` — افزودن تسک جدید
- `PUT /tasks/{id}` — ویرایش تسک موجود
- `DELETE /tasks/{id}` — حذف تسک خاص

---

## 🧪 تست API

می‌توانید از ابزارهایی مانند:
- [Postman](https://www.postman.com/)
- [curl](https://curl.se/)
- مرورگر (فقط برای GET)

استفاده کنید.

---

## 🛠 توسعه‌دهنده

> این پروژه توسط [نام شما] توسعه داده شده به عنوان تمرینی برای یادگیری FastAPI و MongoDB.
