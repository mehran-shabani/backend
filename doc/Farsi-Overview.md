# معرفی مخزن

این مخزن شامل کدهای «Health Care Worker @Home» است که یک سیستم متن‌باز برای انجام مشاوره‌‌های پزشکی از راه دور محسوب می‌شود. این سامانه امکانات زیر را فراهم می‌کند:

- برقراری تماس صوتی و تصویری با استفاده از WebRTC
- گفت‌وگوی امن (چت)
- دعوت از بیمار از طریق پیامک یا ایمیل
- ارسال فایل یا تصویر
- تولید گزارش به صورت فایل PDF
- امکان اتصال به سامانه‌های خارجی مانند OpenEMR
- ورود مهمان یا همکار
- احراز هویت از طریق OpenID

پروژه با فریم‌ورک **Sails.js** روی پلتفرم **Node.js** نوشته شده است و تحت مجوز GPLv3 منتشر شده است.

## ساختار کلی

کدها در پوشه‌ی `api/` دسته‌بندی شده‌اند که شامل کنترلرها، مدل‌ها، سرویس‌ها و ... است. برای مدیریت تماس‌های ویدیویی از سرویس MediaSoup استفاده می‌شود و برای پیامک و ایمیل از سرویس‌های خارجی نظیر Twilio کمک گرفته شده است. همچنین برای سازگاری با استانداردهای پرونده الکترونیک سلامت، سرویس `FhirService` در پروژه موجود است.

## پیشنهاد برای لایه‌ی ایجنت

برای افزودن قابلیت‌های هوشمند (مانند خودکارسازی هماهنگی ملاقات‌ها یا بررسی سوابق بیمار) می‌توان لایه‌ای از ایجنت‌ها را به پروژه اضافه کرد. مناسب‌ترین محل برای این کار پوشه‌ی `api/services/` است که سرویس‌های کمکی در آن قرار دارند. هر ایجنت می‌تواند به صورت یک سرویس مجزا پیاده‌سازی شود و از طریق کنترلرها فراخوانی شود. به عنوان نمونه، ایجنت می‌تواند وضعیت نوبت‌های هر بیمار را بررسی کرده و در زمان مقرر، به صورت خودکار پیام یادآوری ارسال کند.

## پیاده‌سازی مشابه در Django

در صورتی که بخواهید این لایه را در جنگو توسعه دهید، می‌توانید مراحل زیر را دنبال کنید:

1. ایجاد یک اپلیکیشن جدید در جنگو برای ایجنت‌ها (مثلاً `agents`).
2. تعریف مدل‌های مورد نیاز برای نگهداری تنظیمات یا صف کارها.
3. پیاده‌سازی منطق ایجنت‌ها در قالب تسک‌های Celery تا امکان اجرای دوره‌ای یا زمان‌بندی‌شده وجود داشته باشد.
4. در صورت نیاز به ارتباط بلادرنگ با کاربر، می‌توان از Django Channels برای WebSocket استفاده کرد.
5. در نهایت، از طریق APIهای REST یا GraphQL، ارتباط بین جنگو و این سامانه‌ی Node.js برقرار می‌شود.

با این روش می‌توانید یک لایه‌ی هوشمند مستقل در جنگو داشته باشید که عملیات خودکارسازی را انجام داده و از طریق API با سامانه‌ی اصلی در ارتباط باشد.

