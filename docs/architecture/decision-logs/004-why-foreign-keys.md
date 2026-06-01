**Decision:** Enforce relational integrity using Foreign Keys with ON DELETE CASCADE.


**Why:**

*   A database is not just a storage bucket; it is the final line of defense for data integrity. By explicitly linking code\_snippets.user\_id to users.id, mathematically it becomes impossible for the application to accidentally save a snippet for a non-existent user. ON DELETE CASCADE acts as an automated garbage collector, instantly destroying a user's snippets if their account is deleted, preventing database bloat.