-- Delete table if it exists
DROP TABLE IF EXISTS jobs;

-- Create table
CREATE TABLE jobs (
  id SERIAL PRIMARY KEY NOT null,
  user_id INTEGER,
  company VARCHAR(50),
  role VARCHAR(50),
  pay INTEGER,
  link TEXT,
  app_date DATE,
  contact_name VARCHAR(50),
  contact_details VARCHAR(50),
  app_response VARCHAR(20), -- dropdown menu form
  interview_stage VARCHAR(20), -- dropdown menu form
  interview_details VARCHAR(50)
  offer BOOLEON,
  CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(id)
);

-- Insert Dummy Data
INSERT INTO jobs (user_id, company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer) VALUES (1, "Google", "Junior WebDev", "65000", "www.google.com", 2022-01-10, "Sundar Pichai", "sundar@google.com", "no response", "", "", FALSE );
INSERT INTO jobs (user_id, company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer) VALUES (1, "Facebook", "Junior WebDev", "75000", "www.facebook.com", 2022-01-14, "Mark Zuckerberg", "mark@facebook.com", "Positive email", "1st Face to Face", "2022-01-20", FALSE );
INSERT INTO jobs (user_id, company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer) VALUES (1, "Amazon", "Junior WebDev", "88000", "www.amazon.com", 2022-01-11, "Jeff Bezos", "jeff@amazon.com", "Positive phonecall", "2nd Face to Face", 2022-01-20, FALSE );
INSERT INTO jobs (user_id, company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer) VALUES (1, "Netflix", "Junior WebDev", "55000", "www.netflix.com", 2022-01-05, "Reed Hastings", "reed@netflix.com", "no response", "", "", FALSE );
INSERT INTO jobs (user_id, company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer) VALUES (1, "Apple", "Junior WebDev", "75000", "www.apple.com", 2022-01-6, "Tim Cook", "tim@apple.com", "Positive Email", "3rd Face to Face", "2022-01-15", TRUE );
