CREATE TABLE Customer(
    cust_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    cust_fname VARCHAR(255),
    cust_lname VARCHAR(255),
    cust_address VARCHAR(255),
    cust_ph_no CHAR(10),
    status BOOLEAN);

CREATE TABLE Reservation(
    res_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    cust_id INT,
    room_id INT,
    transaction_id VARCHAR(12),
    in_date DATETIME,
    out_date DATETIME,
    days INT);

CREATE TABLE Room(
    room_id INT PRIMARY KEY NOT NULL,
    type_id CHAR(3),
    description TEXT,
    price INT,
    occupancy_status BOOLEAN);

CREATE TABLE Room_Type(
    type_id CHAR(3) PRIMARY KEY NOT NULL,
    name VARCHAR(255),
    capacity INT);

CREATE TABLE Transactions(
    transaction_id VARCHAR(12) PRIMARY KEY NOT NULL,
    emp_id INT,
    res_id INT,
    dated DATETIME,
    amount INT,
    payment_mode VARCHAR(255),
    type BOOLEAN,
    status TINYINT(1));

CREATE TABLE Employees(
    emp_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    job_id INT,
    emp_fname VARCHAR(255),
    emp_lname VARCHAR(255),
    emp_address VARCHAR(255),
    emp_ph_no CHAR(10));

CREATE TABLE Job(
    job_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    job_title VARCHAR(255),
    salary INT);


ALTER TABLE Reservation ADD FOREIGN KEY
   (cust_id) REFERENCES Customer(cust_id);

ALTER TABLE Reservation ADD FOREIGN KEY
   (room_id) REFERENCES Room(room_id);

ALTER TABLE Room ADD FOREIGN KEY
   (type_id) REFERENCES Room_Type(type_id);

ALTER TABLE Transactions ADD FOREIGN KEY
   (emp_id) REFERENCES Employees(emp_id);

ALTER TABLE Transactions ADD FOREIGN KEY
   (res_id) REFERENCES Reservation(res_id);

ALTER TABLE Employees ADD FOREIGN KEY
   (job_id) REFERENCES Job(job_id);
