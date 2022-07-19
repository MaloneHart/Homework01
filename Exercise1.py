# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

name = "Michael"
age = 23
Difference = age - 18

if Difference == 1:
    Translate = "год"
elif 1 < Difference < 5:
    Translate = "года"
else:
    Translate = "лет"

if Difference >= 0:
    print(name, "на", Difference, Translate, "больше 18")
else:
    print(name, "младше 18")



