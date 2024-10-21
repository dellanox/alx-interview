# 0x03. Log Parsing

This project involves creating a Python script that reads log data from standard input and computes metrics based on the log entries. The project focuses on real-time data stream parsing, processing, and calculating statistics from logs. Below is a detailed description of the project and its requirements.

## Project Details

**Weight**: 1  
**Project Start**: Oct 21, 2024, 6:00 AM  
**Project End**: Oct 25, 2024, 6:00 AM  
**Auto Review**: An automatic review will be launched at the deadline.  

### Concepts Covered:

- **File I/O in Python**:  
  Learn to read from `sys.stdin` line by line.
  
- **Signal Handling**:  
  Handle keyboard interruptions (CTRL + C) to print statistics.

- **Data Processing**:  
  Parse strings and aggregate data to compute summaries.

- **Regular Expressions**:  
  Use regular expressions to validate log entry formats.

- **Dictionaries in Python**:  
  Use dictionaries to count occurrences of HTTP status codes and accumulate file sizes.

- **Exception Handling**:  
  Handle potential exceptions during file reading and data processing.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files must end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder is mandatory
- Code must follow the PEP 8 style (version 1.7.x)
- All files must be executable
- File length will be tested using `wc`

## Tasks

### 0. Log Parsing

Write a Python script that reads from standard input and computes metrics:

- **Input format**:  
  `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`

- **Statistics** (output after every 10 lines or when interrupted with CTRL + C):
  - Total file size
  - Number of lines per HTTP status code (200, 301, 400, 401, 403, 404, 405, 500)

