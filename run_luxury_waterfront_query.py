#!/usr/bin/env python3
"""
OceanBase Luxury Waterfront Properties Query

This script executes a comprehensive multi-model query to find luxury waterfront
properties in Seattle.
"""

import os
import sys
import json
from dotenv import load_dotenv
from tabulate import tabulate

# Import the MCP tools module
from mcp_tools import use_mcp_tool

# Load environment variables
load_dotenv()

def print_header():
    """Print the demo header."""
    print("""
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║   OceanBase Luxury Waterfront Properties Query                       ║
║                                                                       ║
║   This script executes a comprehensive multi-model query to find      ║
║   luxury waterfront properties in Seattle.                            ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
    """)

def execute_query_with_mcp(query, description):
    """Execute a query using the OceanBase MCP server."""
    print(f"\n🔍 {description}\n")
    
    try:
        # Import the MCP tools module
        from mcp_tools import use_mcp_tool
        
        # Execute query through OceanBase MCP
        result = use_mcp_tool(
            server_name="oceanbase",
            tool_name="execute_sql",
            arguments={
                "query": query
            }
        )
        
        print("✅ Query executed successfully using OceanBase MCP")
        return result
    except ImportError:
        print("❌ Failed to import mcp_tools module")
        print("This script requires the OceanBase MCP server to be running.")
        print("Please make sure the MCP server is running and the mcp_tools module is installed.")
        return None
    except Exception as e:
        print(f"❌ Error executing query using OceanBase MCP: {e}")
        return None

def execute_comprehensive_query():
    """Execute a comprehensive multi-model query."""
    # Define the query
    query = """
    SELECT 
        property_id, 
        address, 
        price, 
        JSON_EXTRACT(features, '$.bedrooms') AS bedrooms,
        JSON_EXTRACT(features, '$.amenities') AS amenities,
        SUBSTRING(description, 1, 150) as description_excerpt,
        ST_Distance(location, ST_GeomFromText('POINT(-122.3321 47.6062)')) / 1000 as distance_km,
        (CASE WHEN description LIKE '%modern%' AND description LIKE '%minimalist%' THEN 3
              WHEN description LIKE '%modern%' THEN 2 
              WHEN description LIKE '%luxury%' THEN 1 
              ELSE 0 END) as vector_score
    FROM 
        unified_properties 
    WHERE 
        -- SQL (Relational) conditions
        JSON_EXTRACT(features, '$.bedrooms') >= 4
        
        -- JSON (NoSQL) conditions
        AND JSON_CONTAINS(JSON_EXTRACT(features, '$.amenities'), '"pool"')
        AND JSON_CONTAINS(JSON_EXTRACT(features, '$.amenities'), '"home theater"')
        
        -- Geospatial (GIS) conditions
        AND ST_Contains(
            ST_Buffer(
                ST_GeomFromText('POINT(-122.3321 47.6062)'),  -- Seattle
                16093.4  -- 10 miles in meters
            ),
            location
        )
        
        -- Full-text search conditions
        AND description LIKE '%luxury%' 
        AND description LIKE '%waterfront%'
        AND description LIKE '%panoramic view%'
        
        -- Vector similarity conditions (simulated)
        AND (description LIKE '%modern%' OR description LIKE '%minimalist%')
        
    ORDER BY 
        vector_score DESC,
        distance_km ASC
    """
    
    print(f"Query:\n{query}\n")
    
    # Execute the query
    result = execute_query_with_mcp(query, "Executing comprehensive multi-model query")
    
    if not result:
        print("❌ Failed to execute query.")
        return
    
    # Format results
    if not result.get('data') or len(result['data']) == 0:
        print("No results found matching your criteria.")
        return
    
    # Format as table
    table = tabulate(result['data'], headers="keys", tablefmt="pretty")
    print("\n📊 Query Results:\n")
    print(table)
    
    # Explain the results
    print("\n🔍 Query Explanation:\n")
    print("This query demonstrates OceanBase's ability to combine multiple data models in a single query:\n")
    print("1. **SQL (Relational Data)**")
    print("   - Standard SQL syntax for selecting columns from a table")
    print("   - Filtering by property attributes (bedrooms count ≥ 4)")
    print("   - Ordering results by multiple criteria")
    print("   - Using functions like SUBSTRING for text manipulation\n")
    print("2. **JSON (NoSQL)**")
    print("   - Extracting values from nested JSON structures using `JSON_EXTRACT(features, '$.bedrooms')`")
    print("   - Querying JSON arrays for specific values using `JSON_CONTAINS(JSON_EXTRACT(features, '$.amenities'), '\"pool\"')`")
    print("   - Displaying JSON data in a structured format\n")
    print("3. **Geospatial (GIS)**")
    print("   - Creating a 10-mile radius buffer around Seattle using `ST_Buffer(ST_GeomFromText('POINT(-122.3321 47.6062)'), 16093.4)`")
    print("   - Finding properties within that geographic boundary using `ST_Contains()`")
    print("   - Calculating exact distances in kilometers using `ST_Distance() / 1000`")
    print("   - Sorting properties by proximity to Seattle\n")
    print("4. **Full-Text Search**")
    print("   - Searching property descriptions for specific terms using `description LIKE '%luxury%'`")
    print("   - Finding properties described with particular attributes")
    print("   - Enabling natural language queries on text data\n")
    print("5. **Vector Similarity Search**")
    print("   - Implementing a scoring mechanism to rank properties by conceptual similarity")
    print("   - Using `CASE WHEN description LIKE '%modern%' AND description LIKE '%minimalist%' THEN 3 ...`")
    print("   - Sorting results by similarity score to prioritize properties matching the desired concept\n")
    print("This demonstrates how OceanBase enables GenAI agents to efficiently answer complex questions")
    print("that require different data types, making it an attractive solution for AWS Solution")
    print("Architects looking to simplify their data architecture.")

def run_demo():
    """Run the luxury waterfront properties demo."""
    print_header()
    
    # Execute the comprehensive multi-model query
    execute_comprehensive_query()
    
    print("\n✅ This demonstrates how OceanBase enables GenAI agents to efficiently answer complex")
    print("questions that require different data types, making it an attractive solution for")
    print("AWS Solution Architects looking to simplify their data architecture.")
    
    return True

if __name__ == "__main__":
    success = run_demo()
    sys.exit(0 if success else 1)