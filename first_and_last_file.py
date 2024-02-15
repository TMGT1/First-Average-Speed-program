print ("Ну здравствуй! Ты пришел сюда чтобы замерить скорость свой лошадки, верно? :))))")
output = input('Yes / No: ')

driver = False
if output == "No": # if No, take a hike far away
    print("выали тогда")

else:
    s = input("Расстояние в метрах: ") # расстояние пройденное -- distance 
    t = input("Время в секундах: ") # время пройденное -- time
    u = (float(s) / 1000) // (float(t) / 3600)
    sec = float(s) // float(t)
    if u > 1:
        print(u, 'Км/ч.') # km / hour
        print(sec, "Метров/сек.") # meters / second
    elif u < 1:
        print("да ты мурио, ты на столько медленный что мне смешно")
    if u > 210:
        driver = True
if driver == True:
    print("тру драйвер сан франциско") # true driver san francisco 

input()
