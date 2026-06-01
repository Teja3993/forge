**What I learned today?**
I learned how to bridge a local GUI (DBeaver) to a remote cloud server (Neon.tech) using a connection string. I also learned that defining a database schema is about setting strict rules—using constraints like UNIQUE, NOT NULL, and DEFAULT CURRENT\_TIMESTAMP to force the database to reject bad data before it can corrupt the system.

**What confused me?**
The syntax for executing functions directly inside the SQL DEFAULT parameter. For example, DEFAULT gen\_random\_uuid() means the database engine itself handles generating the ID at the exact moment of insertion, rather than relying on Python to generate and send the ID.

**What surprised me?**
How unforgiving raw SQL is. If a single comma is missed or if tried to insert a Foreign Key that doesn't exist in the parent table, the entire transaction is  rejected. The database acts as a shield, not just a storage drive.

**What next?**
Writing raw SQL strings is powerful, but doing it inside a Python application leads to messy code and security vulnerabilities like SQL Injection. Next it is implementation of an Object-Relational Mapper (SQLAlchemy) so this cloud database can be controlled using pure Python classes.