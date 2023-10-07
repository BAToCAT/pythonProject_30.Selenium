Работа с ресурсом https://petfriends.skillfactory.ru/my_pets

1. Создаем виртуапльное окружение командой:
    python -m venv venv
2. Активируем виртуальное окружение командой (MacOS/Linux):
    source venv/bin/activate
   для Windows другая команда:
    \env\Scripts\activate.bat
3. Установка зависимостей:
    pip install -r requirements.txt
4. Настроить в IDE(Pycharm) текущий интерпритатор, выбрав текущее виртуальное окружение

Нажмите на зеленую стрелочку слева от названия теста, если она вдруг не появилась,
значит вы не установили библиотеку pytest. Установите командой: pip install pytest.

Тесты проводятся через GoogleChrome и используют Chrome Driver
Для корректной работы необходимо быть зарегистрированным пользователем и передать в функции валидные email и password.
Для удобства и безопасности эти данные хранятся в файле .env и импортируются в conftest.py.
В тестах: test_names, test_all_pets_get_photo, test_show_my_pets используется явное ожидание.
В тесте test_name_descr_age, неявное.
Все зависимости на время составления теста собраны в requirements.txt.
Команда для установки pip install -r requirements.txt