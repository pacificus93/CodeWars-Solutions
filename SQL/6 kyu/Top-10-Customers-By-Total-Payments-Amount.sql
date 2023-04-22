/*Overview

You are working for a company that wants to reward its top 10 customers with a free gift. 
You have been asked to generate a simple report that returns the top 10 customers by total amount spent ordered from highest to lowest. 
Total number of payments has also been requested.

The query should output the following columns:

customer_id [int4]
email [varchar]
payments_count [int]
total_amount [float]
and has the following requirements:

only returns the 10 top customers, ordered by total amount spent from highest to lowest

Database Schema : 

https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/

*/
-- Replace with your query (in pure SQL)

SELECT C.customer_id
       ,cust.email
       ,c.payments_count
       ,c.total_amount 

FROM 
      (SELECT C.CUSTOMER_ID AS customer_id
             ,COUNT(NULLIF(P.AMOUNT,0)) AS payments_count
             ,CAST(SUM(NULLIF(P.AMOUNT,0.0)) AS FLOAT) AS total_amount
       
       FROM CUSTOMER C LEFT JOIN PAYMENT P ON C.CUSTOMER_ID = P.CUSTOMER_ID 
       GROUP BY C.CUSTOMER_ID 
       ORDER BY total_amount desc) c 

JOIN CUSTOMER cust on c.customer_id = cust.customer_id 

LIMIT 10