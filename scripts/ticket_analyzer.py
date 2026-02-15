"""
Ticket Analyzer - Generates support metrics
"""

import sqlite3
import pandas as pd
from pathlib import Path
from datetime import datetime

class TicketAnalyzer:
    def __init__(self):
        db_path = Path(__file__).parent.parent / 'database' / 'support_desk.db'
        self.conn = sqlite3.connect(db_path)
        print(f"Connected to database\n")
    
    def get_summary_metrics(self):
        """Get overall ticket metrics"""
        query = """
        SELECT 
            COUNT(*) as total_tickets,
            COUNT(CASE WHEN status = 'Resolved' THEN 1 END) as resolved,
            COUNT(CASE WHEN status = 'In Progress' THEN 1 END) as in_progress,
            COUNT(CASE WHEN status = 'New' THEN 1 END) as new_tickets,
            COUNT(CASE WHEN priority = 'Critical' THEN 1 END) as critical,
            COUNT(CASE WHEN priority = 'High' THEN 1 END) as high_priority
        FROM tickets
        """
        df = pd.read_sql_query(query, self.conn)
        return df
    
    def get_tickets_by_category(self):
        """Breakdown tickets by category"""
        query = """
        SELECT 
            c.category_name,
            COUNT(t.ticket_id) as ticket_count,
            COUNT(CASE WHEN t.status = 'Resolved' THEN 1 END) as resolved
        FROM categories c
        LEFT JOIN tickets t ON c.category_id = t.category_id
        GROUP BY c.category_name
        HAVING ticket_count > 0
        ORDER BY ticket_count DESC
        """
        df = pd.read_sql_query(query, self.conn)
        return df
    
    def get_agent_performance(self):
        """Agent-level metrics"""
        query = """
        SELECT 
            a.name as agent_name,
            a.role,
            COUNT(t.ticket_id) as tickets_handled,
            COUNT(CASE WHEN t.status = 'Resolved' THEN 1 END) as resolved
        FROM agents a
        LEFT JOIN tickets t ON a.agent_id = t.agent_id
        GROUP BY a.name, a.role
        HAVING tickets_handled > 0
        ORDER BY tickets_handled DESC
        """
        df = pd.read_sql_query(query, self.conn)
        return df
    
    def print_report(self):
        """Generate and print the full report"""
        print("=" * 70)
        print("SUPPORT DESK ANALYTICS REPORT")
        print("=" * 70)
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Summary metrics
        print("SUMMARY METRICS")
        print("-" * 70)
        summary = self.get_summary_metrics()
        print(summary.to_string(index=False))
        
        total = summary['total_tickets'].values[0]
        resolved = summary['resolved'].values[0]
        resolution_rate = (resolved / total * 100) if total > 0 else 0
        print(f"\nResolution Rate: {resolution_rate:.1f}%")
        
        # Category breakdown
        print("\n" + "=" * 70)
        print("TICKETS BY CATEGORY")
        print("-" * 70)
        categories = self.get_tickets_by_category()
        print(categories.to_string(index=False))
        
        # Agent performance
        print("\n" + "=" * 70)
        print("AGENT PERFORMANCE")
        print("-" * 70)
        agents = self.get_agent_performance()
        print(agents.to_string(index=False))
        
        print("\n" + "=" * 70)
    
    def close(self):
        self.conn.close()

def main():
    analyzer = TicketAnalyzer()
    analyzer.print_report()
    analyzer.close()

if __name__ == "__main__":
    main()