import numpy as np
import matplotlib.pyplot as plt

# تعریف تابع
def f(x):
    return 2 * x**2 + 3 * x + 1

# پیاده‌سازی روش سیمپسون
def simpson_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n باید یک عدد زوج باشد")
    
    h = (b - a) / n  # عرض هر زیر بازه
    x = np.linspace(a, b, n + 1)  # نقاط تقسیم بازه
    y = f(x)  # مقادیر تابع در نقاط
    #اندیس [-1] در واقع به آخرین عنصر یک لیست یا آرایه اشاره دارد.
    # محاسبه انتگرال با فرمول سیمپسون
    integral =h/3 *( y[0] + y[-1] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]))# b joz zoj avali akhari
    #integral *= h / 3 # zarb meghdar bala dar h/3
    
    return integral, x, y# yek tuple darim
# تابع اصلی
def main():
    # تنظیمات اولیه
    a, b = -4, 2  # بازه انتگرال‌گیری
    n = 20       # تعداد زیر بازه‌ها (باید زوج باشد)

    # محاسبه انتگرال با روش سیمپسون
    result, x, y = simpson_rule(f, a, b, n)

    # چاپ نتیجه
    print("انتگرال با روش سیمپسون:", result)
# رسم نمودار
x_plot = np.linspace(a, b, 1000)  # نقاط برای رسم نمودار تابع
y_plot = f(x_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, label="f(x) = 3x^2 + 2x + 1", color='blue')
plt.fill_between(x, 0, y, color='skyblue', alpha=0.4, label=f"Approx. Integral = {result:.2f}")
plt.scatter(x, y, color='red', label="Sample Points (Simpson's Rule)")  # تمامی نقاط
plt.title("Approximation of Integral using Simpson's Rule")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
