## Support API Backend

Python version 3.12

- Install requitements `pip3 install -r requirements.txt`
- Run api `uvicorn main:app --reload`

### Database

```-- Create User Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create support_ticket Table
CREATE TABLE support_ticket (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    database_name VARCHAR(255),
    schema_name VARCHAR(255),
    sql_query TEXT,
    created_by VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id)
);

-- Insert test users
INSERT INTO
    users (username, password)
VALUES
    ('alice', 'password123'),
    ('bob', 'password456'),
    ('charlie', 'password789');

-- Insert test support tickets
INSERT INTO
    support_ticket (
        description,
        database_name,
        schema_name,
        sql_query,
        created_by
    )
VALUES
    (
        'Authentication error when trying to connect to the database.',
        'auth_db',
        'public',
        'SELECT * FROM auth_errors;',
        4
    ),
    (
        'Performance issue with the monthly reports query.',
        'reports_db',
        'monthly',
        'SELECT * FROM monthly_reports WHERE status = ''pending'';',
        5
    ),
    (
        'Failure in data synchronization between databases.',
        'sync_db',
        'sync_schema',
        'SELECT * FROM data_sync WHERE status = ''failed'';',
        6
    ),
    (
        'Review of indexes in the users table for optimization.',
        'main_db',
        'users',
        'EXPLAIN ANALYZE SELECT * FROM users;',
        1
    ),
    (
        'Incorrect query in the inventory module.',
        'inventory_db',
        'public',
        'SELECT SUM(quantity) FROM inventory;',
        2
    ),
    (
        'Pending update in the products table.',
        'products_db',
        'update_schema',
        'UPDATE products SET price = price * 1.1 WHERE updated_at < NOW() - INTERVAL ''1 year'';',
        3
    ),
    (
        'Problem with the error log file.',
        'logs_db',
        'errors',
        'SELECT * FROM error_logs WHERE severity = ''critical'';',
        4
    ),
    (
        'Query to clean old data from the audit table.',
        'audit_db',
        'audit_schema',
        'DELETE FROM audit_logs WHERE timestamp < NOW() - INTERVAL ''30 days'';',
        5
    ),
    (
        'Failure in generating quarterly reports.',
        'reports_db',
        'quarterly',
        'SELECT * FROM quarterly_reports WHERE status = ''failed'';',
        6
    ),
    (
        'Problem with automatic database maintenance.',
        'maintenance_db',
        'auto_maintenance',
        'SELECT * FROM maintenance_tasks WHERE status = ''pending'';',
        1
    );
```
