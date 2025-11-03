import re
from typing import Callable

def generator_numbers(text: str):

    # Finding mumbers that are separated with spaces
    reg_ex = r'\b\d+(?:\.\d+)?\b'
    numbers = re.findall(reg_ex, text)
    for num in numbers:
        yield float(num)


def sum_profit(text: str, my_function: Callable):
    return sum(my_function(text))


# Check time
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, " \
    "доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

text2 = "Our income is $1200.50, but our expenses are $300.25 so it gives us pure $900.25. plus my aunt's comission in $25.19" \
    " but function is just summing it up altogather"
result = sum_profit(text2, generator_numbers)

print(result)
