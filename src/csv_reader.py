class CSVReader:
    def __get_headers(self, first_line: str) -> list:
        headers = first_line.replace('\n', '').split(',')

        return headers

    def __read_staff_data_with_csv(self, csv_file_path) -> dict:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            headers: list = self.__get_headers(file.readline())

            staff_salaries = list()
            for line in file:
                staff_salaries.append(line.replace('\n', '').split(','))

        return {'headers': headers,
                'staff_salaries': staff_salaries}

    def get_data_from_csv(self, csv_file_path) -> list:
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