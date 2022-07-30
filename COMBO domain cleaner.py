def dom1(lines,good,save):
        for line in lines:
           if line.find("@mail.ru") != -1 or line.find("@ya.ru") != -1 or line.find("@bk.ru") != -1 or line.find("@list.ru") != -1 or line.find("@inbox.ru") != -1 or line.find("@rambler.ru") != -1 or line.find("@mail.ua") != -1 or line.find("@ro.ru") != -1 or line.find("@yandex.ru") != -1 or line.find("@yandex.ua") != -1 or line.find("@yandex.com") != -1 or line.find("@yandex.by") != -1 or line.find("@yandex.kz") != -1 or line.find("@myrambler.ru") != -1 or line.find("@internet.ru") != -1 or line.find("@autorambler.ru") != -1 or line.find("@lenta.ru") != -1 or line.find("@vk.com") != -1:
              save.writelines(line)
              good += 1
        return good

def dom2(lines,good,save):
        for line in lines:
            if line.find(".ru") != -1 or line.find(".ua") != -1 or line.find(".uz") != -1 or line.find(".тм") != -1 or line.find(".tj") != -1 or line.find(".md") != -1 or line.find(".kg") != -1 or line.find(".kz") != -1 or line.find(".by") != -1 or line.find(".am") != -1 or line.find(".az") != -1 or line.find(".рус") != -1 or line.find(".su") != -1:
                save.writelines(line)
                good += 1
        return good

answer = input("выберите вариант поиска, 1/2: ")
base = open(input("Перекинь базу сюда.\n").replace('"', ''), "r", encoding='utf-8')
save = open(input("название файла результатов: ") + ".txt", "w+", encoding='utf-8')
lines = base.readlines()
good = 0
if answer == "1":
    t_d = dom1(lines,good,save)
    print("Было найдено:" + str(t_d) + " почт")
    save.close()
elif answer == "2":
    t_d = dom1(lines,good,save)
    print("Было найдено:" + str(t_d) + " почт")
    save.close()
base.close()
input()
