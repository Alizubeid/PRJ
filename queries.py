CREATE_TABLE_USERS = """
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(200)
)"""

CREATE_TABLE_ACCOUNTS = """
CREATE TABLE IF NOT EXISTS accounts (
    account_id SERIAL PRIMARY KEY,
    title VARCHAR(20) UNIQUE,
    user_id INT,
    balance NUMERIC(10,2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
"""

CREATE_TABLE_TRANSACTION = """
CREATE TABLE IF NOT EXISTS transaction (
    transaction_id SERIAL PRIMARY KEY,
    account_id INT,
    transaction_type VARCHAR(10) CHECK(transaction_type='deposit' OR transaction_type='withdrawal' OR transaction_type='transfer'),
    amount NUMERIC(10,2),
    timestamp TIMESTAMP
)
"""

CREATE_TABLE_ETC = """
CREATE TABLE IF NOT EXISTS etc (
    id SERIAL PRIMARY KEY,
    user_id INT UNIQUE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
"""

CREATE_ALL_TABLE = (CREATE_TABLE_USERS, CREATE_TABLE_ACCOUNTS,
                    CREATE_TABLE_TRANSACTION, CREATE_TABLE_ETC)

INSERT_INTO_USERS = "INSERT INTO users(username,password) values (%s,%s)"
INSERT_INTO_ACCOUNTS = "INSERT INTO accounts(user_id,balance) values (%s,%s)"
INSERT_INTO_TRANSACTION = "INSERT INTO transaction(account_id,transaction_type,amount,timestamp) values (%s,%s,%s,NOW())"
