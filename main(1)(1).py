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
            print("Затем замените удалённый репризеторий разработчика на свой командой git remote ste-url origin <новый url> ")
            print("Запустите launch файл и продемонстрируйте экспертам configurationchecksum")
if q =="C":
    print("Модификация робота")
    print("Загрузиет пришивку turtlebro_overheat_sensor из репризетории turtlebro_extre, находящеся  GitHub\n Затем проверьте работу лампы с тепловизором\n После проверок зайдите в launch файл turtlebro_overheat_sensor и измените температуру на которую будет реагировать робот ")
if q =="D":
    print("Запустите пакет навигации командой roslaunch turtlebro_navigtion turtlebro_slem_navigation\nЗатем с помощью команды export ROS_MASTER_URL= и команды ROS_HOSTNAME= указатьадрес по которому находится ROS_MASTER и ROS_HOST")
    print("Затем запустите Rviz и создайте карту\n Сохраните карту в папку map\n Задать точки роботу можно в файле goals.toml в папк turtlebro_patrol/data")

        