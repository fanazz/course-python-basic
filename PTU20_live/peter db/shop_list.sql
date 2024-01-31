-- SQLite
--kiekviena sąskaitos eilutė
SELECT bill_line.id, product.product_name, bill_line.quantity AS quantity, product.price,
       bill_line.quantity * product.price AS total, 
       bill.purchase_time, customer.first_name, customer.last_name
FROM bill_line
JOIN product ON bill_line.product_id = product.id
JOIN bill ON bill_line.bill_id = bill.id
JOIN customer ON bill.customer_id = customer.id 
ORDER BY purchase_time;
-- Parduotų produktų kiekis
SELECT product.id, product.product_name, SUM(bill_line.quantity) AS total_sold
FROM product
JOIN bill_line ON product.id = bill_line.product_id
GROUP BY product.id
ORDER BY total_sold DESC
LIMIT 3
--Produktų apyvartos
SELECT product.id, product.product_name, SUM(product.price * bill_line.quantity) AS total_revenue
FROM product
JOIN bill_line ON product.id = bill_line.product_id
GROUP BY product.id
ORDER BY total_revenue DESC
LIMIT 1
--Daugiausiai nupirkę klientai
SELECT customer.id, customer.first_name, customer.last_name, SUM(product.price * bill_line.quantity) AS total_spent
FROM customer
JOIN bill ON customer.id = bill.customer_id
JOIN bill_line ON bill.id = bill_line.bill_id
JOIN product ON bill_line.product_id = product.id
GROUP BY customer.id
ORDER BY total_spent DESC
LIMIT 2
--Didžiausia sąskaita
SELECT bill.id, bill.purchase_time, customer.first_name, customer.last_name,
       SUM(product.price * bill_line.quantity) AS total_amount
FROM bill
JOIN customer ON bill.customer_id = customer.id
JOIN bill_line ON bill.id = bill_line.bill_id
JOIN product ON bill_line.product_id = product.id
GROUP BY bill.id
ORDER BY total_amount DESC
LIMIT 2
--Konkrečios sąskaitos peržiūra
SELECT bill.id, product.product_name, bill_line.quantity AS quantity, product.price,
       bill_line.quantity * product.price AS total_amount,
       bill.purchase_time, customer.first_name, customer.last_name      
FROM bill_line
JOIN product ON bill_line.product_id = product.id
JOIN bill ON bill_line.bill_id = bill.id
JOIN customer ON bill.customer_id = customer.id
WHERE bill.id = 9

