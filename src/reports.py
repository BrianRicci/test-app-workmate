import services


class Report:
    """ Родительский класс для отчетов """
    
    def __init__(self, headers: list, data: list):
        self.headers = headers
        self.data = data

    def __prepare_headers(self, headers: list) -> list:
        pass

    def __prepare_staff_data(self) -> list:
        pass

    def generate_report():
        pass


class PayoutReport(Report):
    """ Класс отчета о выплатах """

    def __prepare_headers(self, headers: list) -> list:
        """ Метод для подготовки заголовков перед выводом в отчете """
        required_length = services.calculate_max_length_of_fields(self.data)
        output_headers = list()

        for header in headers:
            how_many_spaces_needed = ' ' * (required_length - len(header) + 1)
            output_headers.append(header + how_many_spaces_needed)

        return output_headers

    def __prepare_staff_data(self) -> list:
        """ Метод для подготовки данных перед выводом в отчете """
        hourly_rate_fieldname = services.detect_hourly_rate_column(self.headers)

        required_length = services.calculate_max_length_of_fields(self.data)

        output_data = list()

        for row in self.data:
            output_row = dict(row)
            output_row['payout'] = f'{int(row.get('hours_worked')) * int(row.get(hourly_rate_fieldname))}$'

            for key, value in output_row.items():
                how_many_spaces_needed = ' ' * (required_length - len(value) + 1)
                output_row[key] += how_many_spaces_needed

            output_data.append(output_row)

        return output_data

    def __sort_columns(self, data: list) -> list:
        """ Метод для сортировки данных в требуемом порядке """
        hourly_rate_fieldname = services.detect_hourly_rate_column(self.headers)

        for index, row in enumerate(data):
            data[index] = {
                'id': row.get('id'),
                'name': row.get('name'),
                'email': row.get('email'),
                'department': row.get('department'),
                'hours': row.get('hours_worked'),
                'rate': row.get(hourly_rate_fieldname),
                'payout': row.get('payout'),
            }

        return data

    def generate_report(self) -> list | list:
        """ Метод для вывода отчета """
        prepared_data = self.__prepare_staff_data()
        output_data = self.__sort_columns(prepared_data)

        output_headers = self.__prepare_headers(output_data[0].keys())

        return output_headers, output_data
