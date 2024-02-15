print ("Ну здравствуй! Ты пришел сюда чтобы замерить скорость свой лошадки, верно? :))))")
output = input('Yes / No: ')

driver = False
if output == "No":
    print("выали тогда")

else:
    s = input("Расстояние в метрах: ") # расстояние пройденное
    t = input("Время в секундах: ") # время пройденное
    u = (float(s) / 1000) // (float(t) / 3600)
    sec = float(s) // float(t)
    if u > 1:
        print(u, 'Км/ч.')
        print(sec, "Метров/сек.")
    elif u < 1:
        print("да ты мурио, ты на столько медленный что мне смешно")
    if u > 210:
        driver = True
if driver == True:
    print("тру драйвер сан франциско")

input()
