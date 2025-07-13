# OceanBase Multi-Model Database Demo Setup Guide

This guide provides detailed instructions for setting up and running the OceanBase Multi-Model Database Demo for GenAI Agents.

## Prerequisites

- Python 3.7 or higher
- OceanBase database server (version 4.0 or higher)
- OceanBase MCP server (optional, for MCP integration)

## Installation

### Option 1: Using the Setup Script

1. Clone or download the demo repository
2. Navigate to the demo directory
3. Run the setup script:

```bash
./setup.sh
```

The setup script will:
- Create a Python virtual environment
- Install required dependencies
- Create a `.env` file if it doesn't exist
- Check if the OceanBase MCP server is running

### Option 2: Manual Setup

1. Clone or download the demo repository
2. Navigate to the demo directory
3. Create a Python virtual environment:

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

```bash
# On Linux/macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

5. Install required dependencies:

```bash
pip install -r requirements.txt
```

6. Create a `.env` file:

```bash
cp .env.example .env
```

7. Edit the `.env` file with your OceanBase connection details and AWS credentials

## Configuration

Edit the `.env` file to configure the demo:

```
# OceanBase Database Connection Settings
OB_HOST=<YOUR_OB_HOST>
OB_PORT=<YOUR_OB_PORT>
OB_USER=<YOUR_OB_USER>
OB_PASSWORD=<YOUR_OB_PASSWORD>
OB_DATABASE=<YOUR_OB_DATABASE>

# AWS Bedrock Configuration
AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY>
AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_KEY>
AWS_REGION=us-east-1
```

## Running the Demo

### Interactive Mode

Run the demo in interactive mode:

```bash
python run_demo.py
```

This will present a menu with the following options:

1. Setup Database (create tables and sample data)
2. Run Multi-Model Queries Demo
3. Run Real Estate Agent Demo
4. Run All Demos
5. Exit

### Batch Mode

Run the demo in batch mode:

```bash
python run_demo.py --batch --component all
```

Available components:
- `setup`: Run database setup only
- `queries`: Run multi-model queries demo only
- `agent`: Run real estate agent demo only
- `all`: Run all demos (default)

## MCP Integration

To run the MCP-specific demo:

```bash
python mcp_demo.py
```

This demo showcases how to use OceanBase MCP for multi-model queries in GenAI agents.

### Setting Up OceanBase MCP

1. Install the OceanBase MCP server
2. Start the OceanBase MCP server:

```bash
# Example command (adjust based on your MCP server installation)
npx -y @modelcontextprotocol/server-oceanbase
```

3. Configure the MCP server to connect to your OceanBase database

## Demo Components

### 1. Database Setup

The `setup_database.py` script creates and populates the database with sample data:

```bash
python setup_database.py
```

### 2. Multi-Model Queries Demo

The `multi_model_queries.py` script demonstrates various multi-model queries:

```bash
python multi_model_queries.py
```

### 3. Real Estate Agent Demo

The `real_estate_agent.py` script implements a GenAI agent for real estate recommendations:

```bash
python real_estate_agent.py
```

### 4. MCP Demo

The `mcp_demo.py` script demonstrates how to use OceanBase MCP:

```bash
python mcp_demo.py
```

## Troubleshooting

### Database Connection Issues

If you encounter database connection issues:

1. Verify that your OceanBase server is running
2. Check the connection details in the `.env` file
3. Ensure that the database user has appropriate permissions
4. Check if the database exists and is accessible

### MCP Integration Issues

If you encounter MCP integration issues:

1. Verify that the OceanBase MCP server is running
2. Check if the `mcp_tools` module is installed and accessible
3. Ensure that the MCP server is configured to connect to your OceanBase database

## Additional Resources

- [OceanBase Documentation](https://www.oceanbase.com/docs)
- [OceanBase GitHub Repository](https://github.com/oceanbase/oceanbase)
- [Model Context Protocol (MCP) Documentation](https://modelcontextprotocol.github.io/docs/)