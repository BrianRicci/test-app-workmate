# def detect_hourly_rate_column(csv_file_path):
#     # Возможные варианты названий столбца
#     possible_names = ['salary', 'rate', 'hourly_rate']
    
#     with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
#         # Читаем первую строку (заголовки)
#         reader = csv.reader(file)
#         headers = next(reader)
        
#         # Проверяем каждый возможный вариант
#         for name in possible_names:
#             if name in headers:
#                 return name
    
#     # Если ни один вариант не подошел
#     return None
