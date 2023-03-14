-- script that creates the MySQL server user user_0d_1

-- If the user user_0d_1 already exists, the script should not fail
CREATE USER IF NOT EXISTS user_0d_1@localhost
-- The user_0d_1 password should be set to user_0d_1_pwd
IDENTIFIED BY 'user_0d_1_pwd';
-- user_0d_1 should have all privileges on the MySQL server
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
FLUSH PRIVILEGES;
