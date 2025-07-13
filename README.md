# OceanBase Multi-Model Demo for GenAI Agents

This project demonstrates OceanBase's multi-model capabilities for GenAI agents. It showcases how OceanBase can handle different data types (relational, vector, geospatial, JSON, full-text) in a single database, making it an ideal solution for GenAI applications that need to query diverse data sources.

## Key Features

- **Vector Similarity Search**: Store and query vector embeddings for semantic search
- **Geospatial Data**: Perform location-based queries with spatial functions
- **JSON Data**: Store and query semi-structured data with JSON functions
- **Full-Text Search**: Perform keyword-based searches with relevance ranking
- **Relational Data**: Use traditional SQL for structured data
- **Combined Multi-Model Queries**: Mix all data types in a single query

## Why This Matters for GenAI Agents

GenAI agents often need to access and combine data from multiple sources and formats. OceanBase's multi-model capabilities allow agents to:

1. **Simplify Architecture**: Use a single database instead of multiple specialized databases
2. **Reduce Latency**: Avoid network hops between different databases
3. **Improve Performance**: Execute complex queries efficiently in a single operation
4. **Enhance Capabilities**: Combine different query types for more powerful results
5. **Streamline Development**: Use a single SQL interface for all data access

## Demo Contents

- `bedrock_vector_demo.py`: Main demo script showcasing OceanBase's multi-model capabilities
- `multi_model_queries.py`: Demonstrates various multi-model queries
- `real_estate_agent.py`: Implements a GenAI agent for real estate recommendations
- `mcp_demo.py`: Demonstrates integration with Model Context Protocol
- `setup_database.py`: Sets up the database schema and sample data
- `docs/hands_on_lab_guide.md`: Step-by-step guide for the hands-on lab
- `docs/setup_guide.md`: Instructions for setting up the demo environment

## Prerequisites

- Python 3.8+
- OceanBase database with MCP server running
- AWS account with Bedrock access

## Setup Instructions

1. Clone this repository:
   ```
   git clone <repository-url>
   cd OceanbaseMultimodelDemo-GitHub
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables in `.env` file:
   ```
   # AWS Bedrock credentials
   AWS_ACCESS_KEY=<YOUR_AWS_ACCESS_KEY>  <!-- PLACEHOLDER: Replace with your AWS access key -->
   AWS_SECRET_KEY=<YOUR_AWS_SECRET_KEY>  <!-- PLACEHOLDER: Replace with your AWS secret key -->
   AWS_REGION=us-east-1
   
   # OceanBase connection details (if not using MCP)
   OB_HOST=<YOUR_OB_HOST>  <!-- PLACEHOLDER: Replace with your OceanBase host -->
   OB_PORT=<YOUR_OB_PORT>  <!-- PLACEHOLDER: Replace with your OceanBase port -->
   OB_USER=<YOUR_OB_USER>  <!-- PLACEHOLDER: Replace with your OceanBase username -->
   OB_PASSWORD=<YOUR_OB_PASSWORD>  <!-- PLACEHOLDER: Replace with your OceanBase password -->
   OB_DATABASE=<YOUR_OB_DATABASE>  <!-- PLACEHOLDER: Replace with your OceanBase database name -->
   ```

4. Run the setup script:
   ```
   ./setup.sh
   ```

5. Run the demo:
   ```
   python run_demo.py
   ```

## Running the Demo with MCP

This demo is designed to work with the Model Context Protocol (MCP) for seamless integration with AI assistants. To run the demo with MCP:

1. Make sure the OceanBase MCP server is running
2. Use the `mcp_tools` module to execute queries through MCP
3. Run the MCP-specific demo:
   ```
   python mcp_demo.py
   ```

## Demo Walkthrough

The demo showcases the following capabilities:

1. **Setup**: Creates a properties table with various data types
2. **Sample Data**: Loads sample property data with embeddings from AWS Bedrock
3. **Relational Queries**: Demonstrates basic SQL queries and aggregations
4. **Vector Similarity Search**: Shows semantic search using vector embeddings
5. **Geospatial Queries**: Performs location-based searches
6. **JSON Queries**: Queries nested JSON structures and arrays
7. **Full-Text Search**: Performs keyword-based searches with relevance ranking
8. **Combined Queries**: Demonstrates complex queries using multiple data models

## Example Query

This example shows a combined multi-model query that uses all data types:

```sql
SELECT 
    id, 
    address, 
    city, 
    price,
    JSON_EXTRACT(features, '$.bedrooms') as bedrooms,
    JSON_EXTRACT(features, '$.property_type') as property_type,
    SUBSTRING(description, 1, 100) as description_excerpt,
    VECTOR_COSINE_SIMILARITY(embedding, '[...]') as semantic_similarity,
    ST_Distance_Sphere(location, ST_GeomFromText('POINT(-122.3321 47.6062)')) / 1609.34 as distance_miles,
    MATCH(description) AGAINST('modern energy efficient') as keyword_relevance
FROM 
    properties
WHERE 
    -- Geospatial condition
    ST_Distance_Sphere(location, ST_GeomFromText('POINT(-122.3321 47.6062)')) / 1609.34 < 100
    
    -- JSON condition
    AND JSON_EXTRACT(features, '$.bedrooms') >= 3
    
    -- Full-text condition
    AND MATCH(description) AGAINST('modern energy efficient')
    
    -- Relational condition
    AND price < 1500000
ORDER BY 
    -- Combined ranking
    (semantic_similarity * 0.7 + keyword_relevance * 0.3) DESC
```

## Troubleshooting

If you encounter issues with vector operations, try the following:

1. Check that your OceanBase version supports vector operations
2. Verify that the AWS Bedrock credentials are correct
3. Ensure that the MCP server is properly configured
4. Check the logs for any error messages

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OceanBase for providing the multi-model database capabilities
- AWS for providing the Bedrock API for embeddings generation