from csv_reader import CSVReader
from reports import PayoutReport
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='+')
    parser.add_argument('--report', '-r', help="Название отчета", required=True)

    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    reader = CSVReader()

    for filename in namespace.filenames:
        headers, data = reader.get_staff_data_with_csv(filename)

        match namespace.report:
            case 'payout':
                report = PayoutReport(headers, data)

                report.generate_report()
            
            case _:
                raise Exception('Такого вида отчета нет')

# python main.py ../test_data/data3.csv ../test_data/data1.csv ../test_data/data2.csv -r payout