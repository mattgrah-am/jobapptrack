-- Delete table if it exists
DROP TABLE IF EXISTS users;

-- Create table
CREATE TABLE users (
  id SERIAL PRIMARY KEY NOT null,
  first_name VARCHAR(20),
  last_name VARCHAR(20),
  email TEXT UNIQUE,
  password VARCHAR(64),
  admin BOOLEON,
);

-- Insert Dummy Data
INSERT INTO users (first_name, last_name, email, password, admin) VALUES ("Matt", "Graham", "iam@mattgrah.am", "1234", TRUE );
INSERT INTO users (first_name, last_name, email, password, admin) VALUES ("Jim", "Beam", "jim@beam.com", "0000", FALSE );
INSERT INTO users (first_name, last_name, email, password, admin) VALUES ("Jack", "Daniels", "jack@daniels.com", "0000", FALSE );
INSERT INTO users (first_name, last_name, email, password, admin) VALUES ("Glen", "fiddich", "glen@fiddich.com", "0000", FALSE );
INSERT INTO users (first_name, last_name, email, password, admin) VALUES ("Johnny", "Walker", "johnny@walker.com", "0000", FALSE );