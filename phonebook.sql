CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    phone VARCHAR(20)
);



COPY phonebook(first_name, phone)
FROM '/contacts.csv'
DELIMITER ','
CSV HEADER;

UPDATE phonebook
SET first_name = 'Nursultan'
WHERE first_name = 'dias';


SELECT * FROM phonebook
WHERE first_name = 'Nursultan';


SELECT * FROM phonebook
WHERE phone LIKE '8700%';

DELETE FROM phonebook
WHERE first_name = 'Nursultan';

DELETE FROM phonebook
WHERE phone = '87001234567';