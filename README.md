# Python Starter (Hop Game)

این تمرین برای آشنایی شما با پایتون در نظر گرفته شده است

در این تمرین قصد داریم بازی خاطره‌انگیز هوپ را پیاده‌سازی کنید
بازیکن نخست یک عدد را به عنوان ضریب هوپ انتخاب میکند و سپس کامپیوتر آغاز میکند

بازی نخست توسط کامپیوتر و با یک عدد رندوم که ضریبی از هوپ نیست آغاز میشود و بعد از آن نوبت کاربر است که عدد بعدی یا هوپ را وارد کند و کامپیوتر نیز این اعداد را ادامه داده یا هوپ میگوید

بازی بدین صورت است که هر عددی که کامپیوتر وارد کرد کاربر باید یکی به آن اضافه کند اگر عدد بدست آمده ضریب هوپ بود باید هوپ را چاپ کند و اگر ضریب هوپ نبود باید خود عدد را وارد کند

این بازی بین کاربر و کامپیوتر ادامه میابد تا زمانی که بازیکن عدد یا عبارت هوپ را اشتباه وارد کند

توجه شود تنها عدد آغازین بازی رندوم هستند و بعد از شروع بازی همان عدد افزوده میشود

بعد از پایان هر دور از بازی امتیاز کاربر در یک لیست ذخیره میشود و بیشترین امتیاز و امتیاز این دست به او نمایش داده میشود

سپس از او درمورد بازی مجدد پرسیده میشود و اگر تایید کرد دوباره بازی را انجام میدهد و اگر خواست بازی تمام شود برنامه متوقف میشود
## نمونه خروجی

فرض میکنیم کاربر عدد 5 را به عناون ضریب هوپ انتخاب کرده است 

```bash
game started...
>--------------<
CPU: 27
Player: 28
CPU: 29
Player: hop
CPU: 31
Player: hop
>--------------<
Game Over!
Record: 2
Best Record: 12
---------------

>> wanna play again (y/n): n

> have a nice day
```
