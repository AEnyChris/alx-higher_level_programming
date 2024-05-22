-- creates user if it does not exist and grant all privileges

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
