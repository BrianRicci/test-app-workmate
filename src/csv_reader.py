class CSVReader:
    def __print_message_about_read(self, file_path: str):
        """ Метод для вывода сообщении о чтении файла """
        slash_index = file_path.rindex('/')
        
        print(f'Прочитан файл: {file_path[slash_index + 1:]}')

    def __get_headers(self, first_line: str) -> list:
        """ Метод для чтения заголовков """
        headers = first_line.replace('\n', '').split(',')

        return headers

    def __read_staff_data_with_csv(self, csv_file_path: str) -> dict:
        """ Метод для чтения данных о сотрудниках из CSV файла """
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            headers: list = self.__get_headers(file.readline())

            staff_salaries = list()
            for line in file:
                staff_salaries.append(line.replace('\n', '').split(','))
        
        self.__print_message_about_read(csv_file_path)
        
        return {'headers': headers,
                'staff_salaries': staff_salaries}

    def get_staff_data_with_csv(self, csv_file_path: str) -> list | list:
        """ Метод, выдающий данных из CSV """
        incoming_data_from_csv: dict = self.__read_staff_data_with_csv(csv_file_path)
        headers: list = incoming_data_from_csv.get('headers')

        data = list()
        for line in incoming_data_from_csv.get('staff_salaries'):
            data.append(
                {
                    headers[i]: line[i] for i in range(len(headers))
                }
            )

        return headers, data