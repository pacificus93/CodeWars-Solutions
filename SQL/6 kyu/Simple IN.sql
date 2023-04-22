/*
DESCRIPTION:
For this challenge you need to create a SELECT statement, this SELECT statement will use an IN 
to check whether a department has had a sale with a price over 98.00 dollars.

departments table schema
 - id
 - name

sales table schema
 - id
 - department_id (department foreign key)
 - name
 - price
 - card_name
 - card_number
 - transaction_date

resultant table schema
 - id
 - name

*/

SELECT D.*
FROM DEPARTMENTS D

WHERE D.ID IN (
                SELECT DEPARTMENT_ID 
                FROM SALES 
                WHERE PRICE >98.00)