def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 0:
        print("\nВсе тесты прошли успешно!")
    else:
        print("\nНекоторые тесты не прошли.")
