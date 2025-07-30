--- database name Library
create database Library;
use Library;

--- signup page
create table signup(
First varchar(20),
last varchar(20),
class1 varchar(20),
Roll_no int primary key,
phone varchar(20) unique
);

---- book table to add the book details


CREATE TABLE books (
    Roll_no INT,
    Serial INT UNIQUE,  
    Writer VARCHAR(100),
    Title VARCHAR(100),
    FOREIGN KEY (Roll_no) REFERENCES signup(Roll_no)
);

--- To access all value of table
select * from signup;
select * from books;







