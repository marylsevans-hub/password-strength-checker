# password-strength-checker
## About the Project 
The Password Strength Checker is a beginner-friendly Python cybersecurity project that evaluates the strength of a password based on five security requirements. 
I created this project to strengthen my understanding of Python while applying programming concepts to cybersecurity. As a Cybersecurity Management Policy student with professional experience in QA automation, I wanted to create a practical tool that demonstrates how basic programming can be used to encourage stronger password practices. 

## Features

The program checks whether a password:

- Contains at least 12 characters
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one number
- Contains at least one special character

The program assigns one point for each requirement that is met and provides an overall strength rating:

- 0–2 points: Weak
- 3–4 points: Moderate
- 5 points: Strong

The program also provides recommendations when a password does not meet all five requirements.

## Security Feature

The program uses Python's `getpass` module so the password is not displayed on the screen while the user types it.

## What I Learned

Building this project helped me practice Python concepts including variables, conditional statements, `if`, `elif`, and `else` logic, character validation, scoring logic, and importing a Python module.

Most importantly, this project allowed me to connect programming with my interest in cybersecurity and better understand how code can be used to solve practical security problems.

My QA automation background influenced how I approached this project. As I built each feature, I tested individual requirements, performed positive and negative testing with different password combinations, and completed an end-to-end test of the finished program. The project helped me see the connection between software development, quality assurance, and cybersecurity while giving me hands-on experience with Python.

## How to Run the Program

1. Install Python 3.
2. Download `password_checker.py`.
3. Open Command Prompt or a terminal in the folder containing the file.
4. Run:

   `python password_checker.py`

5. Enter a test password when prompted.
6. Review the password strength score and recommendations.

**Security reminder:** Use a test password rather than an actual password when experimenting with this project.
