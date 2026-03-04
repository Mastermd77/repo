import re

with open('raw.txt', 'r', encoding='utf-8') as f:
    raw = f.read()


items = re.findall(r'\d+\.\n(.*?)\n[\d,]+ x ([\d\s,]+)', raw, re.S)

print("--- ТОВАРЫ И ЦЕНЫ ---")
for name, price in items:
    name = name.replace('\n', ' ').strip()
    price = price.replace(' ', '').replace(',', '.')
    print(f"- {name}: {price} тг")


total = re.search(r'ИТОГО:\s+([\d\s,]+)', raw).group(1).replace(' ', '').replace(',', '.')
payment = re.search(r'(Банковская карта|Наличные)', raw).group(1)
date_time = re.search(r'Время: (.*)', raw).group(1)

print(f"\nСПОСОБ ОПЛАТЫ: {payment}")
print(f"ДАТА И ВРЕМЯ: {date_time}")
print(f"ИТОГО К ОПЛАТЕ: {total} тг")