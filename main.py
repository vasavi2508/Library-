
# Library Borrowing and Fine Reconciliation System

FINE_PER_DAY = 5
STANDARD_BORROWING_DAYS = 14


# Function to calculate fine
def calculate_fine(return_delay):

    fine = return_delay * FINE_PER_DAY

    return fine


# Function to identify overdue records
def check_overdue(return_delay):

    if return_delay > 0:
        return True

    return False


# Function to determine book availability
def check_availability(returned_status):

    if returned_status:
        return "Available"

    return "Borrowed"


# Main program
print("==========================================")
print(" LIBRARY BORROWING AND FINE RECONCILIATION")
print("==========================================")

# Library book inventory
library_books = ["B101", "B102", "B103", "B104", "B105"]

# Store borrowing records as tuples
borrowing_records = []

n = int(input("Enter number of borrowing records: "))

# Collect borrowing details
for i in range(n):

    print("\nEnter details for Record", i + 1)

    book_id = input("Enter Book ID: ")

    if book_id not in library_books:
        print("Book ID not found in library inventory.")
        continue

    borrower = input("Enter borrower name: ")

    borrowing_period = int(
        input("Enter borrowing period in days: ")
    )

    return_delay = int(
        input("Enter return delay in days (0 if on time): ")
    )

    returned_input = input(
        "Has the book been returned? (yes/no): "
    ).lower()

    if borrowing_period < 0 or return_delay < 0:
        print("Invalid borrowing details.")
        continue

    if returned_input not in ["yes", "no"]:
        print("Invalid return status.")
        continue

    if returned_input == "yes":
        returned_status = True
    else:
        returned_status = False

    # Create tuple
    record = (
        book_id,
        borrower,
        borrowing_period,
        return_delay,
        returned_status
    )

    borrowing_records.append(record)


# Initialize totals
total_fine = 0
overdue_count = 0
available_count = 0
borrowed_count = 0

recorded_books = []

print("\n==========================================")
print("          LIBRARY REPORT")
print("==========================================")

print("Book ID | Borrower | Delay | Fine | Status")

# Process each tuple
for record in borrowing_records:

    book_id = record[0]
    borrower = record[1]
    borrowing_period = record[2]
    return_delay = record[3]
    returned_status = record[4]

    # Calculate fine
    fine = calculate_fine(return_delay)

    # Check overdue status
    overdue = check_overdue(return_delay)

    # Check availability
    availability = check_availability(returned_status)

    total_fine += fine

    if overdue:
        overdue_count += 1

    if availability == "Available":
        available_count += 1
    else:
        borrowed_count += 1

    recorded_books.append(book_id)

    print(
        book_id, "|",
        borrower, "|",
        return_delay, "|",
        "Rs.", fine, "|",
        availability
    )


# Find books without borrowing records
unrecorded_books = []

for book in library_books:

    if book not in recorded_books:
        unrecorded_books.append(book)
        available_count += 1


# Display overdue records
print("\n==========================================")
print("           OVERDUE RECORDS")
print("==========================================")

found = False

for record in borrowing_records:

    if check_overdue(record[3]):

        found = True

        print("Book ID:", record[0])
        print("Borrower:", record[1])
        print("Delay:", record[3], "days")
        print("Fine: Rs.", calculate_fine(record[3]))

if not found:
    print("No overdue records found.")


# Display availability details
print("\n==========================================")
print("        BOOK AVAILABILITY")
print("==========================================")

for book in library_books:

    status = "Available"

    for record in borrowing_records:

        if record[0] == book:

            status = check_availability(record[4])
            break

    print(book, ":", status)


# Display final summary
print("\n==========================================")
print("          FINAL SUMMARY")
print("==========================================")

print("Total Library Books :", len(library_books))
print("Total Records       :", len(borrowing_records))
print("Overdue Records     :", overdue_count)
print("Total Fine          : Rs.", total_fine)
print("Available Books     :", available_count)
print("Borrowed Books      :", borrowed_count)

print("==========================================")
print("Library analysis completed successfully.")
