# Debugging Note: Python Import Paths During Refactoring

**Issue:** After restructuring the codebase to move `main.py` and `database/` inside an `app/` module, running `pytest` resulted in `ModuleNotFoundError: No module named 'database'` and `ModuleNotFoundError: No module named 'logger'`.

**Root Cause:**
Python resolves imports based on the execution context. When files were at the root level, `from database.models import...` worked. Once moved into a package, Python could no longer find them at the root level.

**Resolution:**
1. Updated all internal imports to use absolute paths starting from the module root (e.g., `from app.database.models...` and `from app.logger...`).
2. Executed tests using `PYTHONPATH=. pytest tests/ -v` to explicitly tell the Python interpreter to treat the current root directory as the starting point for module resolution.