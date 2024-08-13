import tkinter as tk

# تابعی برای نمایش نام و نام خانوادگی کاربر
def show_name():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    label_result.config(text=f"Hello, {first_name} {last_name}!")

# ایجاد پنجره اصلی
root = tk.Tk()
# تغییر سایز پنجره به عرض 400 و ارتفاع 300 پیکسل
root.geometry("400x300")
root.title("فرم تست")

# برچسب‌ها و فیلدهای ورودی
label_first_name = tk.Label(root, text="نام: ")
label_first_name.grid(row=0, column=0, padx=10, pady=5)

entry_first_name = tk.Entry(root, width=30)
entry_first_name.grid(row=1, column=0, padx=10, pady=5)

label_last_name = tk.Label(root, text="نام خانوادگی: ")
label_last_name.grid(row=0, column=1, padx=10, pady=5)

entry_last_name = tk.Entry(root, width=30)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

# دکمه برای نمایش نام کامل کاربر
button_show = tk.Button(root, text="باتن نمایش اسم", command=show_name)
button_show.grid(row=2, column=0, columnspan=2, pady=10)

# برچسب برای نمایش نتیجه
label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# نمایش پنجره
root.mainloop()
