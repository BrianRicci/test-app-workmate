from src.services import detect_hourly_rate_column, calculate_max_length_of_fields
    

def test_detect_hourly_rate_column():
    current_headers = ['department', 'id', 'email', 'name', 'hours_worked', 'rate']
    result = detect_hourly_rate_column(current_headers)
    
    assert result == 'rate'

def test_calculate_max_length_of_fields():
    current_headers = [
        {
            'id': '1',
            'name': 'Alice Johnson',
            'email': 'alice@example.com',
            'department': 'Marketing',
            'hours': '160',
            'rate': '50',
            'payout': '8000',
        },
        {
            'id': '2',
            'name': 'Bob Smith',
            'email': 'bob@example.com',
            'department': 'Design',
            'hours': '150',
            'rate': '40',
            'payout': '6000',
        }
    ]
    result = calculate_max_length_of_fields(current_headers)

    assert result == 17