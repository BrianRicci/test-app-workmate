from csv_reader import CSVReader
import argparse


class Report:

    def generate_report():
        pass


class PaymentReport(Report):
    def __init__(self, headers: list, data: dict):
        self.data = data
        self.headers = headers

    def generate_report(self):
        rows = list()
        
        for row in self.data:
            row_str = ' '.join(row.values())
            rows.append(row_str)

        return rows


def main():
    reader = CSVReader()

    headers, data = reader.get_data_from_csv('./test_data/data1.csv')
    
    pr = PaymentReport(headers, data)

    print(pr.generate_report())


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--report", help="Введите название отчета", required=True)
    # args = parser.parse_args()

    # print(args)

    main()