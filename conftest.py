def pytest_addoption (passer):
    passer.addption('--type', default='Chrome')
    passer.addption('--env', default='Local')
