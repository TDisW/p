print("название блока")

q = str(input())
if q == "A"
    print("Подключение к роботу через роутер")
    w = str(input())
    if w == "описание":
        print("Подключись к роботу\n что за вопрос")
    if w == "решение":
        print("найдите папку boot и в ней создайте файл wpa_supplicant.conf\n В файле напишите \n ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n update_config=1\n country=US\nnetwork={\n  ssid=WIFI_NAME\n  psk=WIFI_PASSWORD\n }")
if q == "B":
    print("Выберите задание: 1, 2 или 3")
    e = float(input())
        if e == 1: 
            print("Командой git clone создайте папку ws_serv_b\n Затем в самой папке наберите команду git log найдите версию noetic и спомощью команды git checkout")
            print("Запустите launch файл и продемонстрируйте экспертам configurationchecksum")
        if e == 2:
            print("Скачайте папку ws_serv_c\n Продемонстрировать список доступных веток командой git branch\nЗатем с помощью git fetch origin new:new создайте ветку new\n Перейдите в ветку и с помощью git log и git checkout переключитесь на версию указанную в задании")
            print("Запустите launch файл и продемонстрируйте экспертам configurationchecksum")
        if e == 3:
            print("Скачайте папку ws_serv_a из собственной репрезитории на GitHub(Загрузить папку из чужого репризетория можно с помощью кнопки fork)\n измените файл Изменение скрипта service_configuration.py:nrange:")
            print("Также изменение версии в файле package.xml\n Загрузите изменения в свой репризеторий с помощью git push\n Выведите список репризеториев командой git remote\n Затем поменяйте репризеторий на свой командой git remote set-url origin<новый url>")
            print("Выгрузите изменения из своего репризетория git pull")
            print("Запустите launch файл и продемонстрируйте экспертам configurationchecksum")
        