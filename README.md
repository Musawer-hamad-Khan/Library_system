<strong>Library Management System</strong>
<br>
This Python script is designed to manage a library's book database. It allows for book searches and administrative functions like adding and removing books.

Prerequisites
<br>
Before running the script, you need to ensure the following:

Python: Make sure you have Python installed on your system. You may need to install the mysql-connector package if it's not already installed.

MySQL: Ensure you have a MySQL server up and running with a database named library_mngmnt_sys. You should have the appropriate access rights and credentials.

Database Structure: You need to create the necessary tables and schema in your MySQL database to match the data structure used in the code. The schema includes tables for book, author, bk_athr_info, publisher, and bk_pblshr_info.
<br>

Usage
<br>
Student Functions: The student class provides a search_book function to search for books in the library database based on the book name.

To use this function, create an instance of the student class, and then call the search_book method. The script will prompt you to enter the name of the book you want to search for.

Admin Functions: <br>The admin class provides several administrative functions:

add_book: <br>This function allows an administrator to add a new book to the library database.

remove_book: <br>This function lets an administrator remove a book from the database.

To use these functions, create an instance of the admin class, and then call the desired method. Follow the prompts to provide the necessary information.

<br>Important Note<br>
Remember to uncomment the function calls (s.search_book(), a.add_book(), and a.remove_book()) if you want to execute specific actions when using the script.

Ensure that your MySQL server is properly configured with the required tables and schema, as per the code's expectations.

Always exercise caution when working with a live database, especially when using functions like remove_book, as they involve data deletion.
