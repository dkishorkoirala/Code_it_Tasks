d = {"ram": 40, "shyam": 50, "hari": 30}

passed = {key: value for key, value in d.items() if value >= 40}

print(passed)
