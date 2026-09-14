def add(*nums):
    total = 0
    for arg in nums:
        total += arg
    return total

def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

address(Country="Indonesia", city="Yogyakarta")
