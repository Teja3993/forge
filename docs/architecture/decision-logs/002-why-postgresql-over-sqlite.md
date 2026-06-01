**Decision:** Use PostgreSQL as the primary relational database instead of SQLite.


**Why:**

1.  **Concurrency:** This is a real-time collaborative workspace. SQLite locks the entire database file during a write operation. If two users save code at the exact same millisecond, one request will fail. PostgreSQL uses row-level locking, handling massive concurrent traffic effortlessly.
    
2.  **Advanced Data Types:** PostgreSQL natively supports UUIDs and JSONB (critical when saving nested AI evaluation logs).


**Tradeoffs:** 

*   **Complexity:** SQLite is just a file on a computer. PostgreSQL requires managing a server, configuring connection pools, and handling network latency.