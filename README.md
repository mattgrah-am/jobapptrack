# Job Application Tracker

GA-SEI - Project 2 - [Live Version](https://floating-forest-21500.herokuapp.com/)

## Summary

This full stack web app is a job application tracker that can be used to track jobs that the user has applied to, and has the ability to addfurther information or edit existing information to track the progress of the application process.

## Technology Used

- HTML
- CSS
- Javascript
- Python
- Flask
- Postgres
- Heroku

## Technical Requirements

- [x] Must Have at least 2 tables (more if they make sense) – one of them should represent the people using the application (users).
- [x] Include sign up/log in functionality (if it makes sense), with encrypted passwords & an authorization flow
- [x] Modify data in the database. There should be ways for users to add/change some data in the database (it's ok if only admins can make changes).
- [x] Have semantically clean HTML and CSS
- [x] Be deployed online and accessible to the public

## Necessary Deliverables

- [x] A working full-stack application, hosted somewhere on the internet
- [x] A link the hosted working app in the URL section of your GitHub repo
- [x] A git repository hosted on GitHub, with a link to the hosted project, and frequent commits dating back to the very beginning of the project. Commit early, commit often.
- [x] A README.md file with explanations of the technologies used, the approach taken, installation instructions, unsolved problems, etc.

## Optional extras

- [x] Use JavaScript to make a smooth UI, e.g. validating forms before submitting.
- [ ] ~~Interact with an external JSON API (check the weather, get book/movie info, space pictures, send SMSs, etc.)~~
- [ ] ~~Upload and store images or files using AWS S3~~

## Planning

### WebApp Wireframes

### Desktop

<img src="https://github.com/mattgrah-am/jobapptrack/blob/main/static/assets/readme/mockup.png" width="400px">

### Mobile

<img src="https://github.com/mattgrah-am/jobapptrack/blob/main/static/assets/readme/mobile.png" width="400px">

### HTML Design and Layout

- Standard semantic HTML

### CSS styles

- **Font Family:**

  - Poppins (https://fonts.google.com/specimen/Poppins)

- **Colours:**

  - Font (light): #000000
  - Font (dark): #ffffff
  - Accents: #21D4FD, #B721FF, #ff8b8b
  - Alert: #f8d7da, #842029
  - Success: #d1e7dd, #0f5132

- **Responsiveness**
  - Media queries at 800px and 1000px
  - Flexblox: Mobile layout
  - Grid: About section layout

### Javascript

- Form validation
- Modal windows

### Python / Flask

- **Flask**
  - HTML Templates using Jinja wiht index.html being the central file calling all temaplates
  - Models for job and user commands
  - Controllers for job and user commands
  - Password encryption and validation using bcrypt
  -

### Database

Database is using Postgres with Python Module: psycopg2.

<img src="https://github.com/mattgrah-am/jobapptrack/blob/main/static/assets/readme/database.png" width="250px">
