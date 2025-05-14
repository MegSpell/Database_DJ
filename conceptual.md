### Conceptual Exercise

Answer the following questions below:


- What is PostgreSQL?

PostgreSQL (often just called Postgres) is a database system, a program that stores, organizes, and lets you retrieve data efficiently.

Think of it like a digital filing cabinet where you can:

Store information (like names, emails, and passwords for a website)

Search and filter through that data quickly

Keep data safe and consistent, even when multiple people are using it at once

It’s widely used in web applications, is free and open-source, and is known for being powerful, reliable, and secure. Unlike simpler tools like spreadsheets, PostgreSQL can handle complex data relationships, huge amounts of information, and multiple users at the same time.

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

- What is the difference between SQL and PostgreSQL?

SQL (Structured Query Language)
SQL is a language, not a program.

It's the standard language used to interact with relational databases.

With SQL, you can do things like: Create tables, Add or remove data, Search or filter data, Update records

PostgreSQL is a database management system (DBMS).

It's one of the many programs that uses SQL to manage and query data.

Think of it as the tool that stores your data and understands the SQL commands you give it.

SQL is like English (a language).

PostgreSQL is like a person who speaks English and uses it to do tasks (like organize and find information in a big library).

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

- In `psql`, how do you connect to a database?

In your terminal:
First make sure you are in postgresql with the command:     psql
then connect to the database using command:     \c database_name

You can also connect from outside psql by using command: psql -d database_name

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

- What is the difference between `HAVING` and `WHERE`?

WHERE — filters rows before grouping
Used to filter data before any GROUP BY or aggregation happens.

Works on individual rows.

Use WHERE when you're filtering raw data.

Example:

SELECT *
FROM users
WHERE age > 18;

HAVING — filters groups after aggregation
Used after data has been grouped using GROUP BY.

Works on aggregate functions like COUNT(), SUM(), AVG().

Use HAVING when you're filtering aggregated results.

Example:

SELECT city, COUNT(*) 
FROM users
GROUP BY city
HAVING COUNT(*) > 5;
#This finds cities that have more than 5 users.

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

- What is the difference between an `INNER` and `OUTER` join?

INNER JOIN: Only matching rows from both tables
Returns only the rows that have matches in both tables.

If there’s no match, the row is excluded.

OUTER JOIN: Includes non-matching rows too
There are 3 types of outer joins: LEFT OUTER JOIN, RIGHT OUTER JOIN & FULL OUTER JOIN

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

LEFT OUTER JOIN	
--Shows everything from the left table
--Adds matching rows from the right table
--If there’s no match, fills in NULL from the right side


RIGHT OUTER JOIN
--Shows everything from the right table
--Adds matching rows from the left table
--If there’s no match, fills in NULL from the left side

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

- What is an ORM? What do they do?

What is an ORM?
ORM stands for Object-Relational Mapper.

It’s a tool that connects your code (objects) to your database (tables) so you can work with the database using your programming language instead of writing SQL directly.

What does an ORM do?
An ORM lets you:

Create, read, update, and delete data in a database using code objects (like classes)

Avoid writing raw SQL—you use familiar programming syntax instead

Map database tables to classes, and rows to objects

An ORM saves time, makes your code cleaner, and lets you think in Python instead of SQL.

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

AJAX:
Where the Request Happens:
--Location: Runs in the browser (client-side)
--Who makes request: The user’s browser
Common Uses:
--Dynamically update a web page without reloading (e.g., like/dislike buttons)
--Submit forms or load content asynchronously
Visibility:
--Visible in browser dev tools (Network tab)
Security & API Keys:
--Not ideal for secret keys (they can be exposed in browser)
Languages/Libraries:
-- AJAX often uses fetch() or axios in JavaScript.

requests:
Where the Request Happens:
--Location: Runs on the server-side
--Who makes request: The web server (e.g., Flask)
Common Uses:
--Fetch data from an external API on the backend
--Integrate third-party services like weather APIs, Petfinder, etc.
Visibility:
--Hidden from user—runs on the server
Security & API Keys:
--Good for using private API keys securely
Languages/Libraries:
--requests is a Python library, commonly used with Flask/Django.


---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

- What is CSRF? What is the purpose of the CSRF token?

CSRF stands for Cross-Site Request Forgery.

It’s a type of attack where a malicious website tricks a user's browser into submitting an unwanted action to another site where the user is already logged in—without their permission.

Example: If you’re logged into your bank, a bad site could secretly try to send a request to transfer money, using your login session.

A CSRF token is a unique, secret value that a website generates and includes with sensitive forms or requests.

The purpose is to:

Prove the request came from your site, not a malicious one

Block fake or forged requests, because the attacker’s site won’t have the valid token

In short:
CSRF = sneaky attack using your session

CSRF token = secret code that protects against it

---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

- What is the purpose of `form.hidden_tag()`?

In Flask-WTF, form.hidden_tag() is used in your HTML form template to render hidden fields—most importantly, the CSRF token.

The main reason you use form.hidden_tag() is to include the CSRF protection token automatically. This helps Flask-WTF verify that form submissions came from your own site, not from a malicious third party.

