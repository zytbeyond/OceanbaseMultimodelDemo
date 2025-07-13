#!/usr/bin/env python3
"""
OceanBase MCP Interactive Demo

This script demonstrates how to use the OceanBase MCP to execute multi-model queries
that leverage all data types (SQL, NoSQL, Vector, Full-text search, GIS, JSON).
"""

import json
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Sample data map for reference
DATA_MAP = {
  "database": "real_estate_investments",
  "tables": [
    {
      "name": "property_listings",
      "description": "Comprehensive property information for investment analysis",
      "columns": [
        {"name": "id", "type": "INT", "description": "Unique property identifier"},
        {"name": "address", "type": "VARCHAR(255)", "description": "Property street address"},
        {"name": "city", "type": "VARCHAR(100)", "description": "Property city location"},
        {"name": "state", "type": "VARCHAR(50)", "description": "Property state or province"},
        {"name": "price", "type": "DECIMAL(12, 2)", "description": "Property listing price"},
        {"name": "features", "type": "JSON", "description": "Property features including bedrooms, bathrooms, amenities"},
        {"name": "location", "type": "POINT", "description": "Geospatial coordinates of the property"},
        {"name": "description", "type": "TEXT", "description": "Detailed property description"},
        {"name": "embedding", "type": "VECTOR(4)", "description": "Investment profile vector"}
      ]
    }
  ]
}

class MCPDemo:
    """Demonstrates using OceanBase MCP for multi-model queries."""
    
    def __init__(self):
        """Initialize the demo."""
        self.data_map = DATA_MAP
        print("OceanBase MCP Demo initialized")
        print("Data map loaded with schema information")
    
    def display_menu(self):
        """Display the interactive menu."""
        print("\n=== OceanBase Multi-Model Query Demo ===")
        print("1. Find investment properties (uses all data types)")
        print("2. Find properties by amenities (JSON)")
        print("3. Find properties by description (Full-text)")
        print("4. Find properties by location (Spatial)")
        print("5. Find properties by investment profile (Vector)")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        return choice
    
    def execute_mcp_query(self, query, description):
        """Execute a query using OceanBase MCP."""
        print(f"\n=== Executing {description} ===")
        print(f"Query: {query}")
        
        print("\nConnecting to OceanBase via MCP...")
        print("Executing query...")
        
        # In a real implementation, we would use the MCP to execute the query
        # For this demo, we'll simulate the MCP call
        print("\nMCP Call:")
        print("```python")
        print("from mcp_tools import use_mcp_tool")
        print("")
        print("# Execute query through OceanBase MCP")
        print("result = use_mcp_tool(")
        print("    server_name=\"oceanbase\",")
        print("    tool_name=\"execute_sql\",")
        print("    arguments={")
        print(f"        \"query\": \"{query}\"")
        print("    }")
        print(")")
        print("```")
        
        # Simulate query results
        if "investment" in description.lower():
            results = self.get_sample_investment_results()
        elif "amenities" in description.lower():
            results = self.get_sample_amenities_results()
        elif "description" in description.lower():
            results = self.get_sample_description_results()
        elif "location" in description.lower():
            results = self.get_sample_location_results()
        elif "vector" in description.lower():
            results = self.get_sample_vector_results()
        else:
            results = []
        
        return results
    
    def get_sample_investment_results(self):
        """Get sample results for the investment properties query."""
        return [
            {
                "id": 1,
                "address": "123 Mountain View Cabin",
                "city": "Leavenworth",
                "state": "WA",
                "price": 950000.00,
                "bedrooms": 4,
                "bathrooms": 3,
                "property_type": "Cabin",
                "amenities": ["hot tub", "fireplace", "mountain view", "deck", "game room"],
                "location": "POINT(-120.6615 47.5962)",
                "distance_km": 125.26,
                "description": "Luxury vacation rental property in the picturesque Bavarian-styled town of Leavenworth...",
                "investment_similarity": 0.48
            },
            {
                "id": 2,
                "address": "456 Pine St",
                "city": "Seattle",
                "state": "WA",
                "price": 750000.00,
                "bedrooms": 4,
                "bathrooms": 3,
                "property_type": "House",
                "amenities": ["fireplace", "balcony", "parking", "pool"],
                "location": "POINT(-122.3321 47.6062)",
                "distance_km": 0.0,
                "description": "Experience the epitome of luxury living in this magnificent 4-bedroom home in Seattle...",
                "investment_similarity": 0.98
            }
        ]
    
    def get_sample_amenities_results(self):
        """Get sample results for the amenities query."""
        return [
            {
                "id": 1,
                "address": "123 Mountain View Cabin",
                "city": "Leavenworth",
                "state": "WA",
                "price": 950000.00,
                "amenities": ["hot tub", "fireplace", "mountain view", "deck", "game room"]
            },
            {
                "id": 2,
                "address": "456 Pine St",
                "city": "Seattle",
                "state": "WA",
                "price": 750000.00,
                "amenities": ["fireplace", "balcony", "parking", "pool"]
            }
        ]
    
    def get_sample_description_results(self):
        """Get sample results for the description query."""
        return [
            {
                "id": 1,
                "address": "123 Mountain View Cabin",
                "city": "Leavenworth",
                "state": "WA",
                "price": 950000.00,
                "description": "Luxury vacation rental property in the picturesque Bavarian-styled town of Leavenworth..."
            },
            {
                "id": 2,
                "address": "456 Pine St",
                "city": "Seattle",
                "state": "WA",
                "price": 750000.00,
                "description": "Experience the epitome of luxury living in this magnificent 4-bedroom home in Seattle..."
            }
        ]
    
    def get_sample_location_results(self):
        """Get sample results for the location query."""
        return [
            {
                "id": 2,
                "address": "456 Pine St",
                "city": "Seattle",
                "state": "WA",
                "distance_km": 0.0
            },
            {
                "id": 1,
                "address": "123 Mountain View Cabin",
                "city": "Leavenworth",
                "state": "WA",
                "distance_km": 125.26
            }
        ]
    
    def get_sample_vector_results(self):
        """Get sample results for the vector query."""
        return [
            {
                "id": 1,
                "address": "123 Mountain View Cabin",
                "city": "Leavenworth",
                "state": "WA",
                "price": 950000.00,
                "investment_similarity": 0.48
            },
            {
                "id": 2,
                "address": "456 Pine St",
                "city": "Seattle",
                "state": "WA",
                "price": 750000.00,
                "investment_similarity": 0.98
            }
        ]
    
    def format_results(self, results, query_type):
        """Format query results for display."""
        if not results:
            return "No properties found matching your criteria."
        
        output = f"\n=== {query_type} Results ===\n\n"
        
        for i, prop in enumerate(results, 1):
            output += f"Property {i}: {prop.get('address', 'N/A')}, {prop.get('city', 'N/A')}, {prop.get('state', 'N/A')}\n"
            
            if 'price' in prop:
                output += f"Price: ${float(prop['price']):,.2f}\n"
            
            if 'bedrooms' in prop:
                output += f"Bedrooms: {prop['bedrooms']}\n"
            
            if 'amenities' in prop:
                if isinstance(prop['amenities'], list):
                    output += f"Amenities: {', '.join(prop['amenities'])}\n"
                else:
                    output += f"Amenities: {prop['amenities']}\n"
            
            if 'distance_km' in prop:
                output += f"Distance from Seattle: {prop['distance_km']:.2f} km\n"
            
            if 'investment_similarity' in prop:
                output += f"Investment Similarity: {prop['investment_similarity']:.2f} (lower is better)\n"
            
            if 'description' in prop:
                output += f"Description: {prop['description'][:100]}...\n"
            
            output += "\n"
        
        if query_type == "Investment Properties":
            output += "\nThis search demonstrates OceanBase's multi-model capabilities by combining:\n"
            output += "1. Vector search for investment profile matching\n"
            output += "2. JSON filtering for property features\n"
            output += "3. Full-text search for property descriptions\n"
            output += "4. Spatial search for location-based filtering\n"
            output += "5. Traditional relational data for basic property information\n"
        
        return output
    
    def run_investment_query(self):
        """Run the comprehensive investment properties query."""
        query = """
        SELECT id, address, city, state, price, 
               JSON_EXTRACT(features, '$.bedrooms') AS bedrooms,
               JSON_EXTRACT(features, '$.bathrooms') AS bathrooms,
               JSON_EXTRACT(features, '$.property_type') AS property_type,
               JSON_EXTRACT(features, '$.amenities') AS amenities,
               ST_AsText(location) AS location,
               ST_Distance_Sphere(location, ST_GeomFromText('POINT(-122.3321 47.6062)')) / 1000 AS distance_km,
               description,
               VECTOR_DISTANCE(embedding, '[0.75, 0.85, 0.25, 0.65]') AS investment_similarity
        FROM property_listings
        WHERE 
            -- Vector similarity search (find properties with similar embeddings)
            VECTOR_DISTANCE(embedding, '[0.75, 0.85, 0.25, 0.65]') < 1.0
            -- JSON filtering (properties with at least 3 bedrooms and specific amenities)
            AND JSON_EXTRACT(features, '$.bedrooms') >= 3
            AND JSON_CONTAINS(features, '"fireplace"', '$.amenities')
            -- Full-text search (properties with luxury-related terms in description)
            AND MATCH(description) AGAINST('luxury')
            -- Spatial search (properties within 150km of Seattle)
            AND ST_Distance_Sphere(location, ST_GeomFromText('POINT(-122.3321 47.6062)')) < 150000
        ORDER BY investment_similarity ASC
        LIMIT 10
        """
        
        results = self.execute_mcp_query(query, "Investment Properties Query (All Data Types)")
        formatted_results = self.format_results(results, "Investment Properties")
        print(formatted_results)
    
    def run_amenities_query(self):
        """Run the JSON amenities query."""
        query = """
        SELECT id, address, city, state, price, JSON_EXTRACT(features, '$.amenities') AS amenities
        FROM property_listings
        WHERE JSON_CONTAINS(features, '"fireplace"', '$.amenities')
        """
        
        results = self.execute_mcp_query(query, "JSON Amenities Query")
        formatted_results = self.format_results(results, "Properties with Fireplace")
        print(formatted_results)
    
    def run_description_query(self):
        """Run the full-text description query."""
        query = """
        SELECT id, address, city, state, price, description
        FROM property_listings
        WHERE MATCH(description) AGAINST('luxury view')
        """
        
        results = self.execute_mcp_query(query, "Full-text Description Query")
        formatted_results = self.format_results(results, "Properties with 'luxury view' in Description")
        print(formatted_results)
    
    def run_location_query(self):
        """Run the spatial location query."""
        query = """
        SELECT id, address, city, state, 
               ST_Distance_Sphere(location, ST_GeomFromText('POINT(-122.3321 47.6062)')) / 1000 AS distance_km
        FROM property_listings
        WHERE ST_Distance_Sphere(location, ST_GeomFromText('POINT(-122.3321 47.6062)')) < 150000
        ORDER BY distance_km ASC
        """
        
        results = self.execute_mcp_query(query, "Spatial Location Query")
        formatted_results = self.format_results(results, "Properties within 150km of Seattle")
        print(formatted_results)
    
    def run_vector_query(self):
        """Run the vector similarity query."""
        query = """
        SELECT id, address, city, state, price,
               VECTOR_DISTANCE(embedding, '[0.75, 0.85, 0.25, 0.65]') AS investment_similarity
        FROM property_listings
        WHERE VECTOR_DISTANCE(embedding, '[0.75, 0.85, 0.25, 0.65]') < 1.0
        ORDER BY investment_similarity ASC
        """
        
        results = self.execute_mcp_query(query, "Vector Similarity Query")
        formatted_results = self.format_results(results, "Properties Similar to Premium Investment Profile")
        print(formatted_results)
    
    def run(self):
        """Run the interactive demo."""
        while True:
            choice = self.display_menu()
            
            if choice == '1':
                self.run_investment_query()
            elif choice == '2':
                self.run_amenities_query()
            elif choice == '3':
                self.run_description_query()
            elif choice == '4':
                self.run_location_query()
            elif choice == '5':
                self.run_vector_query()
            elif choice == '6':
                print("\nExiting OceanBase MCP Demo. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
            
            input("\nPress Enter to continue...")

def main():
    """Main function to run the demo."""
    print("=== OceanBase MCP Interactive Demo ===")
    print("This demo shows how to use OceanBase MCP to execute multi-model queries")
    
    demo = MCPDemo()
    demo.run()

if __name__ == "__main__":
    main()