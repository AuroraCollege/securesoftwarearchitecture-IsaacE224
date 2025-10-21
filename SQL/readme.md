# SQLite Recap

Start sqlite by typing `sqlite3`, quit it by typing `.quit`. 

To open the *chinook.db* database, use `sqlite3 chinook.db`.

(Note that if you are still in the root directory, that command will create a *new* file called *chinook.db* in root - be sure to `cd SQL` or else use `sqlite3 SQL/chinook.db`). 

To see what **tables** are in the file, use `.tables`. 

Information about this file can be found at https://www.sqlitetutorial.net/sqlite-sample-database/

## SQL Excercises

_Complete the excercises using sqlite, then add your solutions here between `backticks` (eg  ` ).

### SELECT Basics 
- Show all columns and all data from the Artist table.
_Hint: Use SELECT *._


- List only the FirstName and LastName of all employees from the Employee table.

### LIMIT 
- Display the first 5 rows from the Customer table.

- Retrieve the first 10 tracks (TrackId and Name) from the Track table.

### WHERE Clauses
- Find all customers who live in the country 'USA'.

- Show all tracks with a duration (in milliseconds) longer than 5 minutes (300,000 ms).

- List all invoices where the total (Total column) is greater than $10.

### ORDER BY
- Show all albums sorted by Title in alphabetical order.

- List the top 5 most expensive tracks (show Name and UnitPrice), ordered by price descending.

### JOINs
- List all tracks (Name) and their corresponding album titles.
_Hint: JOIN Track and Album on AlbumId._

- Show each customer's first name, last name, and the total amount of their invoices.
_Hint: JOIN Customer and Invoice, group by customer._

### Aggregation (COUNT, SUM, AVG, GROUP BY)
- How many tracks are in the Track table?

- What is the average unit price of a track?

- List the number of albums per artist (show artist name and count).

### DISTINCT
- List all the unique countries where customers live.

- Show all distinct genres in the Genre table.

### LIKE and Pattern Matching
- Find all customers whose email ends with '.com'.

- List all tracks whose name starts with 'Love'.

### IN and BETWEEN
- Show all employees whose title is either 'Sales Support Agent' or 'Sales Manager'.

- List all invoices where the total is between $5 and $15.

### INNER and OUTER JOIN (Advanced)
- Show all tracks (name), the album title, and the artist name.

- List all customers and any invoice Total they have (customers without invoices should still appear, showing NULL for total).
_Hint: Try a LEFT JOIN._


## More Challenging Excercises
|Challenge|SQL Query|
|---------|------|
|Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.|`SELECT FirstName, LastName, CustomerID, Country FROM Customers WHERE NOT Country='USA';`
|Provide a query only showing the Customers from Brazil.|
|Provide a query showing the Invoices of customers who are from Brazil. The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.|
Provide a query showing only the Employees who are Sales Agents.|
Provide a query showing a unique list of billing countries from the Invoice table.
Provide a query showing the invoices of customers who are from Brazil.
Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.
Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.
How many Invoices were there in 2009 and 2011? What are the respective total sales for each of those years?
Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.
Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: GROUP BY
Provide a query that includes the track name with each invoice line item.
Provide a query that includes the purchased track name AND artist name with each invoice line item.
Provide a query that shows the # of invoices per country. HINT: GROUP BY
Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resultant table.
Provide a query that shows all the Tracks, but displays no IDs. The resultant table should include the Album name, Media type and Genre.
Provide a query that shows all Invoices but includes the # of invoice line items.
Provide a query that shows total sales made by each sales agent.
Which sales agent made the most in sales in 2009?
Which sales agent made the most in sales in 2010?
Which sales agent made the most in sales over all?
Provide a query that shows the # of customers assigned to each sales agent.
Provide a query that shows the total sales per country. Which country's customers spent the most?
Provide a query that shows the most purchased track of 2013.
Provide a query that shows the top 5 most purchased tracks over all.
Provide a query that shows the top 3 best selling artists.
Provide a query that shows the most purchased Media Type.