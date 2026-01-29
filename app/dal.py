from typing import List, Dict, Any
from db import get_db_connection


    

def get_customers_by_credit_limit_range():
    sql = """
    SELECT customerName, creditLimit  
    FROM customers 
    WHERE creditLimit < 10000 OR creditLimit > 100000
        """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    table = cursor.fetchall()
    cursor.close()
    connection.close()

    query_result = []
    for column in table:
        query_result.append(
            {
                "customerName": column[0],
                "creditLimit": column[1],
            }
        )

    return query_result

def get_orders_with_null_comments():
    sql = """
    SELECT orderNumber, comments 
    FROM orders 
    WHERE comments IS NULL
    ORDER BY orderDate DESC
        """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    table = cursor.fetchall()
    cursor.close()
    connection.close()

    query_result = []
    for column in table:
        query_result.append(
            {
                "orderNumber": column[0],
                "comments": column[1],
            }
        )

    return query_result

def get_first_5_customers():
    sql = """
    SELECT customerName, contactLastName, contactFirstName
    FROM customers
    ORDER BY contactLastName 
    LIMIT 5;
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    table = cursor.fetchall()
    cursor.close()
    connection.close()

    query_result = []
    for column in table:
        query_result.append(
            {
                "customerName": column[0],
                "contactLastName": column[1],
                "contactFirstName": column[2],
            }
        )

    return query_result

def get_payments_total_and_average():
    sql = """
    SELECT SUM(amount) AS total_amount,
	   AVG(amount) AS avarage_amount,
	   MIN(amount) AS minimal_amount,
	   MAX(amount) AS maximal_amount
	   FROM payments
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    table = cursor.fetchall()
    cursor.close()
    connection.close()

    query_result = []
    for column in table:
        query_result.append(
            {
                "total_amount": column[0],
                "avarage_amount": column[1],
                "minimal_amount": column[2],
                "maximal_amount": column[3],
            }
        )

    return query_result

def get_employees_with_office_phone():
    sql = """
    SELECT e.firstName, e.lastName, o.phone 
    FROM employees e
    JOIN offices o 
    ON e.officeCode  = o.officeCode
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    table = cursor.fetchall()
    cursor.close()
    connection.close()

    query_result = []
    for column in table:
        query_result.append(
            {
                "firstName": column[0],
                "lastName": column[1],
                "phone": column[2],
            }
        )

    return query_result

def get_customers_with_shipping_dates():
    sql = """
    SELECT c.customerName, o.orderDate 
    FROM customers AS c 
    LEFT JOIN orders AS o
    ON c.customerNumber = o.customerNumber;  
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    table = cursor.fetchall()
    cursor.close()
    connection.close()

    query_result = []
    for column in table:
        query_result.append(
            {
                "customerName": column[0],
                "orderDate": column[1],
            }
        )

    return query_result

def get_customer_quantity_per_order():
    sql = """
    SELECT c.customerName, od.quantityOrdered 
    FROM customers c 
    JOIN orders o ON c.customerNumber = o.customerNumber 
    JOIN orderdetails od ON o.orderNumber = od.orderNumber 
    ORDER BY c.customerName;
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    table = cursor.fetchall()
    cursor.close()
    connection.close()

    query_result = []
    for column in table:
        query_result.append(
            {
                "customerName": column[0],
                "quantityOrdered": column[1],
            }
        )

    return query_result

def get_customers_payments_by_lastname_pattern(): # this is working but it returns NULL becouse of the WHERE condition, no one matchaes it...
    sql = """
    SELECT c.customerName, c.salesRepEmployeeNumber, SUM(od.quantityOrdered * od.priceEach ) AS total_amount  
    FROM customers c 
    JOIN orders o ON c.customerNumber = o.customerNumber 
    JOIN orderdetails od ON o.orderNumber = od.orderNumber 
    WHERE c.contactFirstName LIKE '%Mu%' OR c.contactFirstName LIKE '%Iy%' # no contact with that chars :(
    GROUP BY c.customerName, c.salesRepEmployeeNumber
    ORDER BY total_amount DESC
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    table = cursor.fetchall()
    cursor.close()
    connection.close()

    query_result = []
    for column in table:
        query_result.append(
            {
                "customerName": column[0],
                "salesRepEmployeeNumber": column[1],
                "total_amount": column[2],
            }
        )

    return query_result
