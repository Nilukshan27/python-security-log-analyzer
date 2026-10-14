Python Security Log Analyzer

A beginner-friendly Python project that analyzes security logs to detect failed login attempts and count failures by IP address.

Features

- Detects failed login attempts.
- Counts the total number of failed logins.
- Groups failed login attempts by IP address.
- Reads log entries from a text file.

Technologies Used

- Python
- Text-based security logs

Project Files

- "main.py" — The security log analyzer.
- "sample_security.log" — Sample security events used for testing.

Sample Results

Using the included sample data, the expected results are:

- Total failed login attempts: 4
- "192.168.1.10": 3 failed attempts
- "10.0.0.5": 1 failed attempt

How It Works

The program reads the log file line by line, identifies entries containing "event=login_failed", extracts the associated IP address, and counts the failures.

Purpose

This project demonstrates basic Python programming, file handling, string processing, dictionaries, and introductory security log analysis.

Disclaimer

The included log entries are fictional and intended for educational purposes only.
