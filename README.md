# Тестовое задания для Workmate

## Описание
Суть приложения заключается в чтении csv файлов с данными о выплатах и выводе в консоль отчета на их основе.  

Пример вывода отчета:  
![output](https://github.com/user-attachments/assets/a97c1f55-c9b0-4593-bbf7-afe85b78c7a2)

## Зависимости
Использованы только стандартные библиотеки и `pytest` для тестов. Разработка велась на `Python 3.12.8`.

## Команды для запуска  
**Windows:**
```
python main.py {названия файлов через пробел} -r(--report) {тип отчета(доступен только payout)}
```

**Linux/MacOS:**
```
python3 main.py {названия файлов через пробел} -r(--report) {тип отчета(доступен только payout)}
```

**Пример**
```
python main.py ../test_data/data3.csv ../test_data/data1.csv ../test_data/data2.csv -r payout
```

## Команды для тестов  
Для начала нужно создать виртуальное окружение и установить туда `pytest`.  
Для этого пошагово выполняем команды:  
**Windows:**  
`python -m venv .venv`  
`venv\Scripts\activate.bat`  
`pip install -r requirements.txt`  

**Linux/MacOS:**  
`python3 -m venv .venv`  
`source venv/bin/activate`  
`pip3 install -r requirements.txt`  

Далее тест запускается командой `pytest`.

## Масштабирование
Для добавления новых видов отчетов, следует наследоваться от класса `Report` из файла `reports.py`. После добавить новый вид отчета в конструкцию `match-case`.

Вносить изменения в класс `CSVReader` нет необходимости.
