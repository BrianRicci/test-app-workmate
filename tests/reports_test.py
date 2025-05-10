from src.reports import PayoutReport

    
def test_calculate_max_length_of_fields():
    input_headers = ['email', 'name', 'department', 'hours_worked', 'salary', 'id']
    input_data = [
        {
            'email': 'karen@example.com',
            'name': 'Karen White',
            'department': 'Sales',
            'hours_worked': '165',
            'salary': '50',
            'id': '201'
        },
        {
            'email': 'liam@example.com',
            'name': 'Liam Harris',
            'department': 'HR',
            'hours_worked': '155',
            'salary': '42',
            'id': '202'
        },
        {
            'email': 'mia@example.com',
            'name': 'Mia Young',
            'department': 'Sales',
            'hours_worked': '160',
            'salary': '37',
            'id': '203'
        }
    ]

    report = PayoutReport(input_headers, input_data)

    correct_headers = ['id                ', 'name              ', 'email             ', 'department        ', 'hours             ', 'rate              ', 'payout            ']
    correct_data = [{'id': '201               ', 'name': 'Karen White       ', 'email': 'karen@example.com ', 'department': 'Sales             ', 'hours': '165               ', 'rate': '50                ', 'payout': '8250$             '}, {'id': '202               ', 'name': 'Liam Harris       ', 'email': 'liam@example.com  ', 'department': 'HR                ', 'hours': '155               ', 'rate': '42                ', 'payout': '6510$             '}, {'id': '203               ', 'name': 'Mia Young         ', 'email': 'mia@example.com   ', 'department': 'Sales             ', 'hours': '160               ', 'rate': '37                ', 'payout': '5920$             '}]
    
    result_headers, result_data = report.generate_report()

    assert result_headers == correct_headers
    assert result_data == correct_data
