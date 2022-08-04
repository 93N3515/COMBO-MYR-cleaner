def dom1(base,good,save):
        lines = base.readlines()
        for line in lines:
           if line.find("@mail.ru") != -1 or line.find("@ya.ru") != -1 or line.find("@bk.ru") != -1 or line.find("@list.ru") != -1 or line.find("@inbox.ru") != -1 or line.find("@rambler.ru") != -1 or line.find("@mail.ua") != -1 or line.find("@ro.ru") != -1 or line.find("@yandex.ru") != -1 or line.find("@yandex.ua") != -1 or line.find("@yandex.com") != -1 or line.find("@yandex.by") != -1 or line.find("@yandex.kz") != -1 or line.find("@myrambler.ru") != -1 or line.find("@internet.ru") != -1 or line.find("@autorambler.ru") != -1 or line.find("@lenta.ru") != -1 or line.find("@vk.com") != -1:
               save.writelines(line)
               good += 1
        return good

def dom2(base,good,save):
        lines = base.readlines()
        for line in lines:
            if line.find(".ru") != -1 or line.find(".ua") != -1 or line.find(".uz") != -1 or line.find(".тм") != -1 or line.find(".tj") != -1 or line.find(".md") != -1 or line.find(".kg") != -1 or line.find(".kz") != -1 or line.find(".by") != -1 or line.find(".am") != -1 or line.find(".az") != -1 or line.find(".рус") != -1 or line.find(".su") != -1:
                save.writelines(line)
                good += 1
        return good

answer = input("выберите вариант поиска, 1/2: ")
base = open(input("Название базы/путь. ex(base1.txt | C:/base.txt):\n").replace('"', ''), "r", encoding='utf-8')
save = open(input("название файла результатов ex(result): ") + ".txt", "w+", encoding='utf-8')
good = 0
if answer == "1":
    t_d = dom1(base,good,save)
    save.close()
    print("Было найдено:" + str(t_d) + " почт")
    base.close()

elif answer == "2":
    t_d = dom2(base,good,save)
    save.close()
    print("Было найдено:" + str(t_d) + " почт")
    base.close()

input()
