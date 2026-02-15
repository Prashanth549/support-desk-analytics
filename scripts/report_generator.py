"""
Report Generator - Creates visual analytics reports
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

class ReportGenerator:
    def __init__(self):
        db_path = Path(__file__).parent.parent / 'database' / 'support_desk.db'
        self.conn = sqlite3.connect(db_path)
        
        # Create reports directory if it doesn't exist
        self.reports_dir = Path(__file__).parent.parent / 'reports'
        self.reports_dir.mkdir(exist_ok=True)
        
        print(f"Connected to database")
        print(f"Reports will be saved to: {self.reports_dir}\n")
    
    def generate_status_chart(self):
        """Generate pie chart of ticket status distribution"""
        query = """
        SELECT status, COUNT(*) as count
        FROM tickets
        GROUP BY status
        """
        df = pd.read_sql_query(query, self.conn)
        
        # Create pie chart
        plt.figure(figsize=(8, 6))
        colors = ['#2ecc71', '#f39c12', '#e74c3c']
        plt.pie(df['count'], labels=df['status'], autopct='%1.1f%%', 
                colors=colors, startangle=90)
        plt.title('Ticket Status Distribution', fontsize=16, fontweight='bold')
        
        # Save chart
        output_path = self.reports_dir / 'status_distribution.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Status distribution chart saved: {output_path.name}")
        plt.close()
    
    def generate_category_chart(self):
        """Generate bar chart of tickets by category"""
        query = """
        SELECT 
            c.category_name,
            COUNT(t.ticket_id) as total,
            COUNT(CASE WHEN t.status = 'Resolved' THEN 1 END) as resolved
        FROM categories c
        LEFT JOIN tickets t ON c.category_id = t.category_id
        GROUP BY c.category_name
        HAVING total > 0
        ORDER BY total DESC
        """
        df = pd.read_sql_query(query, self.conn)
        
        # Create bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        
        x = range(len(df))
        width = 0.35
        
        ax.bar([i - width/2 for i in x], df['total'], width, 
               label='Total', color='#3498db')
        ax.bar([i + width/2 for i in x], df['resolved'], width, 
               label='Resolved', color='#2ecc71')
        
        ax.set_xlabel('Category', fontsize=12, fontweight='bold')
        ax.set_ylabel('Number of Tickets', fontsize=12, fontweight='bold')
        ax.set_title('Tickets by Category', fontsize=16, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(df['category_name'], rotation=45, ha='right')
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        
        # Save chart
        output_path = self.reports_dir / 'category_breakdown.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Category breakdown chart saved: {output_path.name}")
        plt.close()
    
    def generate_priority_chart(self):
        """Generate bar chart of priority distribution"""
        query = """
        SELECT priority, COUNT(*) as count
        FROM tickets
        GROUP BY priority
        ORDER BY 
            CASE priority
                WHEN 'Critical' THEN 1
                WHEN 'High' THEN 2
                WHEN 'Medium' THEN 3
                WHEN 'Low' THEN 4
            END
        """
        df = pd.read_sql_query(query, self.conn)
        
        # Create horizontal bar chart
        fig, ax = plt.subplots(figsize=(8, 5))
        
        colors = {'Critical': '#e74c3c', 'High': '#f39c12', 
                  'Medium': '#3498db', 'Low': '#95a5a6'}
        bar_colors = [colors.get(p, '#95a5a6') for p in df['priority']]
        
        ax.barh(df['priority'], df['count'], color=bar_colors)
        ax.set_xlabel('Number of Tickets', fontsize=12, fontweight='bold')
        ax.set_ylabel('Priority Level', fontsize=12, fontweight='bold')
        ax.set_title('Ticket Priority Distribution', fontsize=16, fontweight='bold')
        ax.grid(axis='x', alpha=0.3)
        
        # Add count labels on bars
        for i, (priority, count) in enumerate(zip(df['priority'], df['count'])):
            ax.text(count + 0.1, i, str(count), va='center')
        
        plt.tight_layout()
        
        # Save chart
        output_path = self.reports_dir / 'priority_distribution.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Priority distribution chart saved: {output_path.name}")
        plt.close()
    
    def generate_agent_performance_chart(self):
        """Generate agent performance comparison"""
        query = """
        SELECT 
            a.name as agent_name,
            COUNT(t.ticket_id) as total_tickets,
            COUNT(CASE WHEN t.status = 'Resolved' THEN 1 END) as resolved_tickets
        FROM agents a
        LEFT JOIN tickets t ON a.agent_id = t.agent_id
        GROUP BY a.name
        HAVING total_tickets > 0
        ORDER BY total_tickets DESC
        """
        df = pd.read_sql_query(query, self.conn)
        
        # Create grouped bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        
        x = range(len(df))
        width = 0.35
        
        ax.bar([i - width/2 for i in x], df['total_tickets'], width, 
               label='Total Handled', color='#3498db')
        ax.bar([i + width/2 for i in x], df['resolved_tickets'], width, 
               label='Resolved', color='#2ecc71')
        
        ax.set_xlabel('Agent', fontsize=12, fontweight='bold')
        ax.set_ylabel('Number of Tickets', fontsize=12, fontweight='bold')
        ax.set_title('Agent Performance Comparison', fontsize=16, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(df['agent_name'], rotation=45, ha='right')
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        
        # Save chart
        output_path = self.reports_dir / 'agent_performance.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Agent performance chart saved: {output_path.name}")
        plt.close()
    
    def generate_all_reports(self):
        """Generate all visualization reports"""
        print("=" * 70)
        print("GENERATING VISUAL REPORTS")
        print("=" * 70)
        print()
        
        self.generate_status_chart()
        self.generate_category_chart()
        self.generate_priority_chart()
        self.generate_agent_performance_chart()
        
        print()
        print("=" * 70)
        print("✓ All reports generated successfully!")
        print(f"Location: {self.reports_dir.absolute()}")
        print("=" * 70)
    
    def close(self):
        self.conn.close()

def main():
    generator = ReportGenerator()
    generator.generate_all_reports()
    generator.close()

if __name__ == "__main__":
    main()