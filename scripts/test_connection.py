"""
Simple script to test database connection and query data
"""

import sqlite3
from pathlib import Path

def test_database():
    # Connect to database
    db_path = Path(__file__).parent.parent / 'database' / 'support_desk.db'
    
    print(f"Connecting to: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Test 1: Count tickets
    cursor.execute("SELECT COUNT(*) FROM tickets")
    ticket_count = cursor.fetchone()[0]
    print(f"\n✓ Total tickets: {ticket_count}")
    
    # Test 2: Show all tickets
    cursor.execute("""
        SELECT 
            t.ticket_id,
            c.name as customer,
            a.name as agent,
            t.subject,
            t.priority,
            t.status
        FROM tickets t
        JOIN customers c ON t.customer_id = c.customer_id
        LEFT JOIN agents a ON t.agent_id = a.agent_id
    """)
    
    print("\nTickets in database:")
    print("-" * 80)
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Customer: {row[1]} | Agent: {row[2]}")
        print(f"  Subject: {row[3]} | Priority: {row[4]} | Status: {row[5]}")
        print()
    
    conn.close()
    print("✓ Database connection test successful!")

if __name__ == "__main__":
    test_database()