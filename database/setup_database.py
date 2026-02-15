"""
Setup script to create the support desk database
"""

import sqlite3
from pathlib import Path

def create_database():
    # Define paths
    db_path = Path(__file__).parent / 'support_desk.db'
    schema_path = Path(__file__).parent / 'schema.sql'
    test_data_path = Path(__file__).parent / 'test_data.sql'
    
    # Remove old database if exists
    if db_path.exists():
        db_path.unlink()
        print("Removed old database")
    
    # Create new database
    print(f"Creating database: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Read and execute schema
    print("Creating tables...")
    with open(schema_path, 'r') as f:
        schema_sql = f.read()
        cursor.executescript(schema_sql)
    print("✓ Tables created")
    
    # Load test data
    print("Loading test data...")
    with open(test_data_path, 'r') as f:
        test_sql = f.read()
        cursor.executescript(test_sql)
    print("✓ Test data loaded")
    
    conn.commit()
    conn.close()
    
    print("\n✓ Database setup complete!")
    print(f"Location: {db_path.absolute()}")

if __name__ == "__main__":
    create_database()