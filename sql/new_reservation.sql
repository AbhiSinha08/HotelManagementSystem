INSERT INTO Reservation(cust_id, room_id, transaction_id, in_date, out_date, days)
    VALUES
    (%s, %s, %s, %s, %s, %s);