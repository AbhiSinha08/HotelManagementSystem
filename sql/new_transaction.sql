INSERT INTO Transactions(transaction_id, emp_id, res_id, dated, amount, payment_mode, type, status)
    VALUES
    (%s, NULL, %s, %s, %s, %s, 1, %s);