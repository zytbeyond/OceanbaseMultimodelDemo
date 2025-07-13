#!/bin/bash
# OceanBase Multi-Model Demo Setup Script

# Print header
echo "╔═══════════════════════════════════════════════════════════════════════╗"
echo "║                                                                       ║"
echo "║   OceanBase Multi-Model Demo Setup                                   ║"
echo "║                                                                       ║"
echo "║   This script sets up the environment for the OceanBase Multi-Model   ║"
echo "║   Demo for AWS Solution Architects.                                   ║"
echo "║                                                                       ║"
echo "╚═══════════════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

echo "✅ Python 3 is installed."

# Create a virtual environment
echo "🔧 Creating a virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "❌ Failed to create virtual environment. Please install the venv module and try again."
    exit 1
fi

# Activate the virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "❌ Failed to activate virtual environment."
    exit 1
fi

# Install required packages
echo "🔧 Installing required packages..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Failed to install required packages."
    exit 1
fi

# Check if .env file exists, if not create it from .env.example
if [ ! -f .env ]; then
    echo "🔧 Creating .env file from .env.example..."
    cp .env.example .env
    echo "⚠️ Please update the .env file with your OceanBase connection details and AWS credentials."
fi

# Check if MCP server is running
echo "🔧 Checking if OceanBase MCP server is running..."
if ! command -v npx &> /dev/null; then
    echo "⚠️ npx is not installed. Cannot check if MCP server is running."
    echo "⚠️ If you want to use MCP features, please install Node.js and npx."
else
    # This is a simple check and might need to be adjusted based on how the MCP server is actually detected
    if npx -y @modelcontextprotocol/server-oceanbase --version &> /dev/null; then
        echo "✅ OceanBase MCP server is available."
    else
        echo "⚠️ OceanBase MCP server might not be running or installed."
        echo "⚠️ To use MCP features, please install and run the OceanBase MCP server."
    fi
fi

echo ""
echo "✅ Setup completed successfully!"
echo ""
echo "To run the demo:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the setup script: python setup_database.py"
echo "3. Run the demo: python run_demo.py"
echo ""
echo "For more information, please refer to the README.md file."