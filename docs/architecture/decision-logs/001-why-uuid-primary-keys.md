**Decision:** Use UUIDv4 (Universally Unique Identifier) for all primary keys instead of auto-incrementing integers (1, 2, 3...).


**Why:**

1.  **Security (IDOR Prevention):** If a user's snippet is at /snippets/5, a malicious actor can easily guess /snippets/6 and scrape the entire database. UUIDs (e4b7...) are cryptographically unguessable.
    
2.  **Distributed Scaling:** When scaling to multiple database servers, auto-incrementing integers will collide (Server A creates ID 1, Server B creates ID 1). UUIDs can be generated anywhere without risk of collision.


**Tradeoffs:**    

*   **Storage Cost:** UUIDs take up 16 bytes, whereas standard integers take 4 bytes.
    
*   **Performance:** B-Tree indexes (the default database sorting mechanism) are slightly slower when sorting random strings compared to sequential numbers, causing minor index bloat. For this platform's scale, the security benefits vastly outweigh the microsecond performance hit.