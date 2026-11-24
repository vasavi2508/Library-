# Library-
# Library Borrowing and Fine Reconciliation System

## 1. Project Overview

The **Library Borrowing and Fine Reconciliation System** is a Python-based application designed to analyse library book borrowing records using tuples.

The system stores book identifiers, borrower names, borrowing periods, return delays, and return statuses. It calculates fines for overdue books, identifies overdue records, and determines whether books are available or currently borrowed.

It also generates a summary of total fines, overdue records, available books, and borrowed books.

## 2. Objectives

- To store library borrowing records using tuples.
- To analyse book identifiers and borrowing periods.
- To calculate fines for delayed book returns.
- To identify overdue borrowing records.
- To determine book availability.
- To calculate the total fine amount.
- To reconcile available and borrowed books.
- To generate a library borrowing summary.

## 3. Assumptions

1. Each book has a unique book ID.
2. Each book has one current borrowing record at a time.
3. The fine rate is ₹5 per overdue day.
4. No fine is charged when the return delay is zero.
5. The return delay is entered in days.
6. A returned book is marked as available.
7. A book that has not been returned is marked as borrowed.
8. Books without borrowing records are considered available.
9. Borrowing records are stored as tuples.

## 4. Tuple Structure

Each borrowing record contains five elements:

```python
(book_id, borrower_name, borrowing_period,
 return_delay, returned_status)
```

Example:

```python
("B102", "Rahul", 17, 3, True)
```

| Element | Description |
|---|---|
| B102 | Book identifier |
| Rahul | Borrower name |
| 17 | Borrowing period in days |
| 3 | Return delay in days |
| True | Book has been returned |

## 5. Formula Used

### Fine Calculation

Fine = Return Delay × Fine Per Day

Example:

Fine = 3 × 5 = ₹15

### Total Fine

Total Fine = Sum of Fines of All Borrowing Records

### Book Availability

- If returned status is True: Available.
- If returned status is False: Borrowed.
- If no borrowing record exists: Available.

## 6. Algorithm

1. Start the program.
2. Define the library book inventory.
3. Define the fine rate per overdue day.
4. Enter the number of borrowing records.
5. Read the book ID and borrower name.
6. Enter the borrowing period.
7. Enter the return delay.
8. Enter the book return status.
9. Store the borrowing details in a tuple.
10. Calculate the fine for each record.
11. Identify overdue borrowing records.
12. Determine whether each book is available or borrowed.
13. Calculate the total fine amount.
14. Identify books without borrowing records.
15. Display overdue records.
16. Display book availability.
17. Display the final library summary.
18. Stop the program.

## 7. Pseudocode

```text
START

DEFINE library book inventory
SET fine per day = 5

INPUT number of borrowing records

FOR each borrowing record:

    INPUT book ID
    INPUT borrower name
    INPUT borrowing period
    INPUT return delay
    INPUT returned status

    STORE details as a tuple

INITIALIZE total fine = 0

FOR each borrowing record:

    EXTRACT tuple elements

    fine = return delay * fine per day

    IF return delay > 0:
        IDENTIFY as overdue

    IF returned status is TRUE:
        SET availability = AVAILABLE

    ELSE:
        SET availability = BORROWED

    ADD fine to total fine

IDENTIFY books without borrowing records
MARK them as AVAILABLE

DISPLAY overdue records
DISPLAY book availability
DISPLAY total fine
DISPLAY available books
DISPLAY borrowed books

STOP
```

## 8. Test Cases

| Test Case | Book ID | Borrowing Period | Return Delay | Expected Fine |
|---|---|---:|---:|---:|
| 1 | B101 | 14 days | 0 | ₹0 |
| 2 | B102 | 17 days | 3 | ₹15 |
| 3 | B103 | 20 days | 6 | ₹30 |
| 4 | B104 | 10 days | 0 | ₹0 |
| 5 | B105 | 16 days | 2 | ₹10 |

### Expected Results

- Total borrowing records: 5
- Overdue records: 3
- Total fine: ₹55
- Available books: 4
- Borrowed books: 1

## 9. Sample Output

```text
==========================================
          LIBRARY REPORT
==========================================

Book ID | Borrower | Delay | Fine | Status

B101 | Anu | 0 | Rs. 0 | Available
B102 | Rahul | 3 | Rs. 15 | Available
B103 | Priya | 6 | Rs. 30 | Borrowed
B104 | Kiran | 0 | Rs. 0 | Available
B105 | Sneha | 2 | Rs. 10 | Available

==========================================
           OVERDUE RECORDS
==========================================

Book ID: B102
Borrower: Rahul
Delay: 3 days
Fine: Rs. 15

Book ID: B103
Borrower: Priya
Delay: 6 days
Fine: Rs. 30

Book ID: B105
Borrower: Sneha
Delay: 2 days
Fine: Rs. 10

==========================================
        BOOK AVAILABILITY
==========================================

B101 : Available
B102 : Available
B103 : Borrowed
B104 : Available
B105 : Available

==========================================
          FINAL SUMMARY
==========================================

Total Library Books : 5
Total Records       : 5
Overdue Records     : 3
Total Fine          : Rs. 55
Available Books     : 4
Borrowed Books      : 1

==========================================
Library analysis completed successfully.
```

## 10. Python Concepts Used

- Variables and data types
- Input and output statements
- Tuples
- Lists
- Conditional statements (if and else)
- For loops
- Functions
- Arithmetic operators
- Tuple indexing
- Boolean values
- List operations

## 11. Conclusion

The Library Borrowing and Fine Reconciliation System successfully analyses book borrowing records using Python tuples.

It calculates overdue fines, identifies delayed returns, determines book availability, and generates a summary of library records.

This project demonstrates the practical application of Python concepts such as tuples, lists, functions, loops, and conditional statements in solving real-world library management problems.

## 12. Project Structure

```text
Library-Fine-Reconciliation/
│
├── library_fine_reconciliation.py
├── README.md
│
└── screenshots/
    └── output.png
```

## 13. Execution Instructions

1. Install Python on your computer.
2. Open the project folder in Visual Studio Code.
3. Open `library_fine_reconciliation.py`.
4. Run the program using:

```bash
python library_fine_reconciliation.py
```

5. Enter the borrowing record details.
6. View the overdue records and fine calculations.
7. Check the book availability report.
8. Capture the actual program output screenshot.
9. Upload the Python file, README, and screenshot to GitHub.

## 14. Author Details

- **Name:** v.v.s.s.gayathri
- **Roll Number:** N26V01A0388
- **Branch:** CSE
- **Section:** Section-5
- **Subject:** Python Programming
- **Project:** Library borrowing
