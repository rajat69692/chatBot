import sqlite3

# Connect to sqlite
connection = sqlite3.connect("sales.db")

# Create a cursor object
cursor = connection.cursor()

# Drop existing tables if they exist
cursor.execute('DROP TABLE IF EXISTS COMMISSIONS')
cursor.execute('DROP TABLE IF EXISTS AGENTS')
cursor.execute('DROP TABLE IF EXISTS SALES')

# Create COMMISSIONS table
cursor.execute('''CREATE TABLE COMMISSIONS (
    TRANSACTION_TYPE VARCHAR(20),
    CHARGEBACK_CODE VARCHAR(10),
    POLICY_NUMBER INT PRIMARY KEY,
    COMM_AMOUNT DECIMAL(10,2),
    COMM_PERCENT DECIMAL(5,2),
    COMM_GENERATED_DATE DATE
);''')

# Create AGENTS table
cursor.execute('''CREATE TABLE AGENTS (
    AGENT_ID INT PRIMARY KEY,
    AGENT_NAME VARCHAR(255),
    POLICY_ISSUING_STATE VARCHAR(2),
    POLICY_NUMBER INT,
    FOREIGN KEY (POLICY_NUMBER) REFERENCES COMMISSIONS(POLICY_NUMBER)
);''')

# Create SALES table
cursor.execute('''CREATE TABLE SALES (
    BILLING_FREQUENCY VARCHAR(20),
    BILLING_OPTION VARCHAR(20),
    POLICY_NUMBER INT,
    POLICY_ISSUE_DATE DATE,
    PRODUCT VARCHAR(50),
    EXPECTED_PREMIUM_AMOUNT DECIMAL(10,2),
    FOREIGN KEY (POLICY_NUMBER) REFERENCES COMMISSIONS(POLICY_NUMBER)

);''')

# COMMISSIONS table details
Commissions_Details = [
    ("New Business", "", 1001, 500.00, 10.00, "2024-01-15"),
    ("Renewal", "", 1002, 250.00, 5.00, "2024-04-01"),
    ("Chargeback", "CB123", 1003, -100.00, 0.00, "2024-06-10"),
    ("New Business", "", 1004, 750.00, 12.00, "2024-02-28"),
    ("Renewal", "", 1005, 300.00, 6.00, "2024-05-15"),
    ("New Business", "", 1006, 450.00, 9.00, "2024-03-05"),
    ("Chargeback", "CB456", 1007, -150.00, 0.00, "2024-07-12"),
    ("Renewal", "", 1008, 200.00, 4.00, "2024-01-25"),
    ("New Business", "", 1009, 600.00, 11.00, "2024-06-20"),
    ("Renewal", "", 1010, 350.00, 7.00, "2024-03-18"),
    ("Chargeback", "CB789", 1011, -200.00, 0.00, "2024-04-05"),
    ("New Business", "", 1012, 800.00, 13.00, "2024-07-01"),
    ("Renewal", "", 1013, 400.00, 8.00, "2024-02-12"),
    ("Chargeback", "CB101", 1014, -120.00, 0.00, "2024-05-25"),
    ("New Business", "", 1015, 900.00, 14.00, "2024-01-30"),
    ("Renewal", "", 1016, 450.00, 9.00, "2024-04-10"),
    ("Chargeback", "CB112", 1017, -180.00, 0.00, "2024-06-15"),
    ("New Business", "", 1018, 1000.00, 15.00, "2024-02-15"),
    ("Renewal", "", 1019, 500.00, 10.00, "2024-05-01"),
    ("Chargeback", "CB123", 1020, -250.00, 0.00, "2024-07-20")
]

# Insert the rows into the COMMISSIONS table
cursor.executemany("INSERT INTO COMMISSIONS (TRANSACTION_TYPE, CHARGEBACK_CODE, POLICY_NUMBER, COMM_AMOUNT, COMM_PERCENT, COMM_GENERATED_DATE) VALUES (?, ?, ?, ?, ?, ?)", Commissions_Details)

# Define the Agent_Details to be inserted
Agent_Details = [
    (101, "John Doe", "CA", 1001),
    (102, "Jane Smith", "NY", 1002),
    (103, "Alex Brown", "TX", 1003),
    (104, "Emily Davis", "FL", 1004),
    (105, "Michael Johnson", "CA", 1005),
    (106, "Sarah Miller", "NY", 1006),
    (107, "David Wilson", "TX", 1007),
    (108, "Olivia Carter", "FL", 1008),
    (109, "William Anderson", "CA", 1009),
    (110, "Jennifer Lopez", "NY", 1010),
    (111, "Matthew Lee", "TX", 1011),
    (112, "Ava Miller", "FL", 1012),
    (113, "Christopher Evans", "CA", 1013),
    (114, "Sophia Rodriguez", "NY", 1014),
    (115, "Daniel Brown", "TX", 1015),
    (116, "Isabella Johnson", "FL", 1016),
    (117, "Ethan Davis", "CA", 1017),
    (118, "Mia Miller", "NY", 1018),
    (119, "Jacob Wilson", "TX", 1019),
    (120, "Charlotte Carter", "FL", 1020)
]

# Insert the rows into the AGENTS table
cursor.executemany("INSERT INTO AGENTS (AGENT_ID, AGENT_NAME, POLICY_ISSUING_STATE, POLICY_NUMBER) VALUES (?, ?, ?, ?)", Agent_Details)

# Define the Sales_Details to be inserted
Sales_Details = [
    ("Monthly", "Credit Card", 1001, "2024-01-01", "Term Life Insurance", 100.00),
    ("Annual", "Bank Draft", 1002, "2024-03-15", "Whole Life Insurance", 2000.00),
    ("Quarterly", "Direct Bill", 1003, "2024-05-05", "Universal Life Insurance", 350.00),
    ("Semi-Annually", "Credit Card", 1004, "2024-02-10", "Variable Universal Life", 1500.00),
    ("Monthly", "Bank Draft", 1005, "2024-04-15", "Simplified Issue Life", 280.00),
    ("Annual", "Direct Bill", 1006, "2024-01-25", "Term Life Insurance", 120.00),
    ("Quarterly", "Credit Card", 1007, "2024-06-10", "Whole Life Insurance", 2200.00),
    ("Semi-Annually", "Bank Draft", 1008, "2024-03-05", "Universal Life Insurance", 380.00),
    ("Monthly", "Direct Bill", 1009, "2024-05-20", "Variable Universal Life", 1600.00),
    ("Annual", "Credit Card", 1010, "2024-02-18", "Simplified Issue Life", 300.00),
    ("Quarterly", "Bank Draft", 1011, "2024-04-05", "Term Life Insurance", 140.00),
    ("Semi-Annually", "Direct Bill", 1012, "2024-01-01", "Whole Life Insurance", 2400.00),
    ("Monthly", "Credit Card", 1013, "2024-06-15", "Universal Life Insurance", 410.00),
    ("Annual", "Bank Draft", 1014, "2024-03-20", "Variable Universal Life", 1700.00),
    ("Quarterly", "Direct Bill", 1015, "2024-05-10", "Simplified Issue Life", 320.00),
    ("Semi-Annually", "Credit Card", 1016, "2024-02-25", "Term Life Insurance", 160.00),
    ("Monthly", "Bank Draft", 1017, "2024-04-18", "Whole Life Insurance", 2600.00),
    ("Annual", "Direct Bill", 1018, "2024-01-12", "Universal Life Insurance", 440.00),
    ("Quarterly", "Credit Card", 1019, "2024-06-05", "Variable Universal Life", 1800.00),
    ("Semi-Annually", "Bank Draft", 1020, "2024-03-08", "Simplified Issue Life", 340.00)
]

# Insert the rows into the SALES table
cursor.executemany("INSERT INTO SALES (BILLING_FREQUENCY, BILLING_OPTION, POLICY_NUMBER, POLICY_ISSUE_DATE, PRODUCT, EXPECTED_PREMIUM_AMOUNT) VALUES (?, ?, ?, ?, ?, ?)", Sales_Details)

print("Database schema created successfully!")

# # Save changes and close connection
connection.commit()
connection.close()
