-- Create the server user_0d_1

-- Have a privileges on mysql server
-- Passowred should be set to usser

CREATE USER IF NOT 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password By 'user_0d_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user-0d_1'@'localhost'WITH GRANT OPTION;
