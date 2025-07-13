# OceanBase Multi-Model Database Demo - Hands-On Lab Guide

This hands-on lab guide provides a step-by-step walkthrough of the OceanBase Multi-Model Database Demo for GenAI Agents. It is designed for AWS Solution Architects to explore and understand the capabilities of OceanBase's multi-model database features.

## Lab Overview

In this lab, you will:

1. Set up the OceanBase multi-model database
2. Explore different data types and query capabilities
3. See how GenAI agents can leverage OceanBase's multi-model capabilities
4. Understand the benefits of using a unified database for diverse data types

## Prerequisites

Before starting this lab, ensure you have:

- Completed the setup steps in the [Setup Guide](./setup_guide.md)
- Basic understanding of SQL and database concepts
- Familiarity with Python (optional)

## Lab 1: Database Setup and Exploration

### Step 1: Set Up the Database

1. Run the database setup script:

```bash
python setup_database.py
```

This script creates a `unified_properties` table with multiple data models:
- Relational data (property details)
- JSON data (property features)
- Geospatial data (property locations)
- Full-text search data (property descriptions)
- Vector data (property embeddings)

### Step 2: Explore the Database Schema

1. Connect to your OceanBase database using a SQL client
2. Examine the `unified_properties` table structure:

```sql
DESCRIBE unified_properties;
```

Notice the different data types used in the table:
- Standard SQL types (INT, VARCHAR, DECIMAL)
- JSON type for flexible schema
- POINT type for geospatial data
- TEXT with FULLTEXT index for full-text search
- VARBINARY for vector embeddings

### Step 3: Explore the Sample Data

1. Query the sample data:

```sql
SELECT * FROM unified_properties LIMIT 5;
```

2. Examine the JSON data:

```sql
SELECT 
    property_id, 
    address, 
    JSON_EXTRACT(features, '$.amenities') AS amenities
FROM 
    unified_properties
LIMIT 5;
```

## Lab 2: Multi-Model Queries

### Step 1: Run the Multi-Model Queries Demo

1. Run the multi-model queries demo:

```bash
python multi_model_queries.py
```

2. Observe the different types of queries demonstrated:
   - Basic relational queries
   - JSON data queries
   - Geospatial queries
   - Full-text search queries
   - Combined multi-model queries

### Step 2: Try Your Own Queries

1. Open `multi_model_queries.py` in a text editor
2. Modify one of the demo queries or create your own
3. Run the script again to see your results

### Step 3: Understand the Query Patterns

For each query type, understand the key SQL functions and operators used:

- **JSON Data**: `JSON_EXTRACT()`, `JSON_CONTAINS()`, `->>`
- **Geospatial Data**: `ST_Distance()`, `ST_Contains()`, `ST_Buffer()`, `ST_GeomFromText()`
- **Full-Text Search**: `MATCH() AGAINST()`
- **Combined Queries**: Using multiple conditions and custom scoring

## Lab 3: Real Estate Agent Demo

### Step 1: Run the Real Estate Agent Demo

1. Run the real estate agent demo:

```bash
python real_estate_agent.py
```

2. Observe how the agent processes natural language queries and translates them into multi-model database queries

### Step 2: Understand the Agent Architecture

1. Open `real_estate_agent.py` in a text editor
2. Examine the `RealEstateAgent` class and its methods:
   - `process_user_query()`: Entry point for natural language queries
   - `_analyze_query()`: Parses user intent and extracts parameters
   - `find_properties_by_location()`: Uses geospatial queries
   - `find_properties_by_features()`: Uses JSON and relational queries
   - `find_similar_properties()`: Uses combined multi-model queries

### Step 3: Try Different Queries

The demo includes three sample queries:
1. "Show me properties near downtown San Francisco"
2. "I'm looking for a house with at least 3 bedrooms and a pool"
3. "Find properties similar to property ID 1"

Modify the `demo_queries` list in the `demo_agent()` function to try different queries.

## Lab 4: MCP Integration

### Step 1: Run the MCP Demo

1. Ensure the OceanBase MCP server is running
2. Run the MCP demo:

```bash
python mcp_demo.py
```

3. Observe how OceanBase MCP enables GenAI agents to access diverse data types through a single unified interface

### Step 2: Understand the MCP Integration

1. Open `mcp_demo.py` in a text editor
2. Examine the different demo functions:
   - `demo_mcp_connection()`: Basic connection test
   - `demo_mcp_relational_query()`: Relational queries using MCP
   - `demo_mcp_json_query()`: JSON queries using MCP
   - `demo_mcp_geospatial_query()`: Geospatial queries using MCP
   - `demo_mcp_fulltext_query()`: Full-text search queries using MCP
   - `demo_mcp_combined_query()`: Combined multi-model queries using MCP
   - `demo_mcp_agent_integration()`: How GenAI agents use MCP

### Step 3: Integrate with Your Own Agent

The pattern for integrating OceanBase MCP with a GenAI agent is:

1. Parse user intent and extract parameters
2. Generate appropriate SQL based on intent
3. Execute query through OceanBase MCP
4. Format results for user

## Lab 5: Performance and Scalability

### Step 1: Understand the Benefits

Discuss the benefits of using OceanBase's multi-model capabilities:

1. **Simplified Architecture**: Eliminate the need for multiple specialized databases
2. **Reduced Operational Overhead**: Manage a single database system
3. **Enhanced Performance**: Avoid network latency from cross-database queries
4. **Cost Efficiency**: Consolidate database licenses and infrastructure
5. **Improved Developer Experience**: Use a unified SQL interface for all data types
6. **AI-Ready Infrastructure**: Provide GenAI agents with a comprehensive data foundation
7. **Scalability**: OceanBase's distributed architecture scales horizontally

### Step 2: Benchmark Queries

1. Use the `time` module to measure query execution time:

```python
import time

start_time = time.time()
results = execute_query(connection, query)
end_time = time.time()

print(f"Query executed in {end_time - start_time:.4f} seconds")
```

2. Compare the performance of different query types and combinations

## Conclusion

In this lab, you've explored OceanBase's multi-model capabilities and how they can be leveraged by GenAI agents. You've seen how a single database can handle diverse data types and provide a unified interface for complex queries.

This approach dramatically simplifies architecture, improves performance, and enhances the capabilities of AI applications.

## Next Steps

1. Explore more complex query patterns
2. Integrate with your own GenAI agents
3. Benchmark performance against traditional multi-database architectures
4. Explore OceanBase's other enterprise features (high availability, scalability, etc.)