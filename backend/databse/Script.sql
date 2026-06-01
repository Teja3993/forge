-- 1. Enable the UUID extension (Built into modern Postgres, but good practice to ensure it's active)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. Create the Users Table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL, -- We will hash passwords later in Python
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Create the Code Snippets Table
CREATE TABLE code_snippets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    title VARCHAR(100) NOT NULL,
    language VARCHAR(30) NOT NULL,
    code TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- This Foreign Key connects the snippet to the user.
    -- ON DELETE CASCADE means if a user deletes their account, all their snippets are instantly deleted too.
    CONSTRAINT fk_user
      FOREIGN KEY(user_id) 
      REFERENCES users(id)
      ON DELETE CASCADE
);

-- 4. Insert Fake Data (Replace with your own variations)
INSERT INTO users (username, email, password_hash) 
VALUES ('teja_dev', 'teja@example.com', 'fake_hash_123');
--
-- 5. Retrieve the generated UUID to use in the next insert
SELECT * FROM users;
-- (Run a quick SELECT * FROM users; to copy the UUID, then paste it below)
--
INSERT INTO code_snippets (user_id, title, language, code)
VALUES ('8db81971-dcae-40ef-9e04-77f5c5547c2d', 'Hello World C++', 'cpp', '#include <iostream> ...');

SELECT * FROM code_snippets;