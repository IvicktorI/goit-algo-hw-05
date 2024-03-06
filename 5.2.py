import re

text = '''Загальний дохід працівника складається з декількох частин:
        1000.01 як основний дохід,
        доповнений додатковими надходженнями
        27.45 і 324.00 доларів.'''

def generator_numbers(text: str):
    reg = re.compile(r'\b\d+(\.\d+)?\b')
    curent_position = 0
    while(curent_position != len(text)):
        curent_text = text[curent_position::]

        match_ = reg.search(curent_text)
        if match_:
            curent_position += match_.end()
            yield float(match_.group())
        else:
            return 0

def sum_profit(text, generator_numbers):
    sum=0
    for i in generator_numbers(text):
        sum += i
    
    return sum

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")