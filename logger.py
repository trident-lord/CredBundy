import sqlite3

def log_transaction(transaction_id, transaction_details, result):
    conn = sqlite3.connect('database/transactions.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO logs (transaction_id, transaction_details, result)
    VALUES (?, ?, ?)
    ''', (transaction_id, transaction_details, result))

    conn.commit()
    conn.close()
