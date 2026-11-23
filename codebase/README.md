# Bus Pass Management System

A simple console application in Python 3 to issue and manage bus passes.
Passes are saved in a file, so the data is kept even after the program closes.

**Project:** PS No. 54 | B.Tech Computer Science and Engineering, First Semester
**University:** Rungta International Skills University

## Features

- Issue a new bus pass
- Renew an existing pass
- Search a pass by ID
- View all passes
- 25% discount for students
- Input validation for pass type and category
- Passes are saved in `buspass.txt` and loaded when the program starts

## Concepts Used

- Lists
- Dictionaries
- Functions
- File Handling

## How to Run

1. Install Python 3.
2. Save the code as `bus_pass_system.py`.
3. Open the terminal in that folder and run:

```
python bus_pass_system.py
```

The file `buspass.txt` is created automatically when the first pass is issued.

## Menu

```
1. Issue new pass
2. Renew pass
3. Search pass by ID
4. View all passes
5. Exit
```

## Pass Types and Fees

| Pass Type | Validity | Fee (General) |
|-----------|----------|---------------|
| Monthly   | 30 days  | Rs. 500       |
| Quarterly | 90 days  | Rs. 1350      |
| Yearly    | 365 days | Rs. 4800      |

Students get a 25% discount. Example: a Yearly pass for a student costs Rs. 3600.

## Sample Run

```
Menu option: 1
Name: Riya
Route: Route 5
Type: Monthly
Category: General
Pass issued. ID: BP101 | Riya | Route 5 | Monthly | Fee: Rs. 500 | Valid: 30 days
```

Invalid pass type:

```
Type: Weekly
Invalid pass type. Choose Monthly, Quarterly or Yearly. Pass not issued.
```

## Test Cases

| No. | Test | Expected Result |
|-----|------|-----------------|
| 1 | Issue Riya, Route 5, Monthly, General | Pass issued with ID BP101, Fee Rs. 500 |
| 2 | View all with an empty file | No passes issued yet. |
| 3 | Issue a Weekly pass | Invalid pass type. Pass not issued. |
| 4 | Issue Aman, Route 7, Yearly, Student, then search BP101 | ID BP102, Fee Rs. 3600; search shows Riya's pass |

## File Format

Each line in `buspass.txt` is one pass:

```
ID | Name | Route | Type | Category | Fee | Days | Renewals
```

Example:

```
BP101 | Riya | Route 5 | Monthly | General | 500 | 30 | 0
```

## Project Files

```
bus_pass_system.py   # main program
buspass.txt          # saved passes (created automatically)
README.md            # project description
```
