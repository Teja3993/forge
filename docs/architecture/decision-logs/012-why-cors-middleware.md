# ADR 012: CORS Middleware Configuration


## Context
This architecture uses a decoupled frontend and backend. The React application will run on `localhost:3000` while the FastAPI server runs on `localhost:8000`. By default, modern browsers enforce the Same-Origin Policy, blocking HTTP requests between different ports or domains to prevent Cross-Site Request Forgery (CSRF) and unauthorized data reading.

## Decision
Implemented `CORSMiddleware` in FastAPI to explicitly whitelist `http://localhost:3000`. Configured `allow_methods=["*"]` to ensure standard CRUD operations and preflight `OPTIONS` requests are accepted.

## Consequences
1. The browser will now allow React application to fetch and display data.
2. Deliberately did NOT use `allow_origins=["*"]`. While wildcard origins make development easier, they are a critical security flaw in production. Strict origin whitelists must be maintained.
3. CORS does not protect the server from direct API access via tools like cURL or Postman; it exclusively protects browser-based interactions.