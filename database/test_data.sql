-- Sample test data for support desk

-- Add agents
INSERT INTO agents (name, email, role) VALUES 
('Sarah Johnson', 'sarah@support.com', 'Support Analyst'),
('Mike Chen', 'mike@support.com', 'Support Analyst'),
('Priya Sharma', 'priya@support.com', 'Senior Analyst');

-- Add customers
INSERT INTO customers (name, email, phone) VALUES
('John Doe', 'john@email.com', '555-0101'),
('Jane Smith', 'jane@email.com', '555-0102'),
('Bob Wilson', 'bob@email.com', '555-0103'),
('Alice Brown', 'alice@email.com', '555-0104'),
('Charlie Davis', 'charlie@email.com', '555-0105');

-- Add categories
INSERT INTO categories (category_name, description) VALUES
('Network Issue', 'Connectivity and network problems'),
('Device Activation', 'New device setup and activation'),
('Billing', 'Billing inquiries and disputes'),
('5G Home Internet', '5G home internet setup and issues'),
('Account Management', 'Account updates and changes');

-- Add realistic tickets
INSERT INTO tickets (customer_id, agent_id, category_id, subject, description, priority, status, created_at, resolved_at)
VALUES 
-- Ticket 1: Resolved
(1, 1, 1, 'No 5G connection', 'Customer cannot connect to 5G network in downtown area', 'High', 'Resolved', 
 datetime('now', '-5 days'), datetime('now', '-5 days', '+2 hours')),

-- Ticket 2: Resolved
(2, 2, 2, 'iPhone activation failed', 'New iPhone 15 activation showing error code 404', 'High', 'Resolved',
 datetime('now', '-4 days'), datetime('now', '-4 days', '+1 hour')),

-- Ticket 3: Resolved
(3, 1, 3, 'Unexpected charges on bill', 'Customer sees $50 roaming charge, claims to be in coverage', 'Medium', 'Resolved',
 datetime('now', '-3 days'), datetime('now', '-3 days', '+3 hours')),

-- Ticket 4: In Progress
(4, 3, 4, '5G gateway not powering on', 'Home internet gateway received yesterday will not turn on', 'Critical', 'In Progress',
 datetime('now', '-2 days'), NULL),

-- Ticket 5: New
(5, NULL, 1, 'Dropped calls in specific area', 'Calls dropping consistently at work address', 'High', 'New',
 datetime('now', '-1 day'), NULL),

-- Ticket 6: Resolved
(1, 2, 5, 'Need to update payment method', 'Credit card expired, need to update before next bill', 'Low', 'Resolved',
 datetime('now', '-6 days'), datetime('now', '-6 days', '+30 minutes')),

-- Ticket 7: Resolved  
(3, 1, 2, 'SIM card not detected', 'New SIM card not being recognized by device', 'High', 'Resolved',
 datetime('now', '-7 days'), datetime('now', '-7 days', '+1 hour')),

-- Ticket 8: In Progress
(2, 3, 1, 'Slow data speeds', '5G showing but speeds under 10 Mbps', 'Medium', 'In Progress',
 datetime('now', '-1 day'), NULL);