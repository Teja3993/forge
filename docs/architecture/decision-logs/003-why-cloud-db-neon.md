**Decision:** Hosting database on Neon.tech rather than running a local PostgreSQL Docker container.

**Why:**

1.  **Serverless Architecture:** Neon separates compute from storage. It automatically spins down to zero when not in use and spins up instantly when traffic hits.
    
2.  **Environment Parity:** By putting the DB in the cloud on Day 1, the local development environment matches the eventual production environment. There will be no database configuration bugs later.


**Tradeoffs:**    

*   **Network Latency:** Every query during local development has to travel over the internet to Neon's servers and back, making local testing slightly slower than a localhost database.