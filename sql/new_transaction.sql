INSERT INTO Transactions(transaction_id, emp_id, res_id, dated, amount, payment_mode, type, status)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s);