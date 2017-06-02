import pytest
import time

target = "C:\\Users\\BrykMV\\PycharmProjects\\eisuks\\test_suite_closed_circuit.py::TestSuite::"

tests = [
    'test_rules_list',
    'test_users_management',
    'test_commissions'
]

pytest_args = '-n 4'

running = []
for i in tests:
    running.append(pytest_args)
    running.append(target+i)
running.append('--html=report.html')

print(running)

pytest.main(running)
