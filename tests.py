import re

def task_1(text):
    return bool(re.fullmatch(r'ab*', text))

def task_2(text):
    return bool(re.fullmatch(r'ab{2,3}', text))

def task_3(text):
    return re.findall(r'[a-z]+_[a-z]+', text)

def task_4(text):
    return re.findall(r'[A-Z][a-z]+', text)

def task_5(text):
    return bool(re.fullmatch(r'a.*b', text))

def task_6(text):
    return re.sub(r'[ ,.]', ':', text)

def task_7(text):
    parts = text.split('_')
    return parts[0] + ''.join(x.title() for x in parts[1:])

def task_8(text):
    return re.split(r'(?=[A-Z])', text)

def task_9(text):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', text)

def task_10(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

test_str = "snake_case_example"
camel_str = "CamelCaseExample"

print(task_1("abbb"))
print(task_2("abb"))
print(task_3("hello_world test_case"))
print(task_4("Python Exercises"))
print(task_5("a123b"))
print(task_6("Python, Exercises. Test"))
print(task_7(test_str))
print(task_8(camel_str))
print(task_9(camel_str))
print(task_10(camel_str))