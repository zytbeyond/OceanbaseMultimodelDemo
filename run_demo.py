#!/usr/bin/env python3
"""
OceanBase Multi-Model Demo Runner

This script runs the complete OceanBase multi-model demo from start to finish.
It sets up the database, loads sample data, and runs the demo queries.
"""

import os
import sys
import time
import argparse
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def print_header():
    """Print the demo header."""
    print("""
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║   OceanBase Multi-Model Demo Runner                                  ║
║                                                                       ║
║   This script runs the complete OceanBase multi-model demo from       ║
║   start to finish.                                                    ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
    """)

def print_section_header(title):
    """Print a section header."""
    print(f"\n{'=' * 80}")
    print(f"  {title}")
    print(f"{'=' * 80}\n")

def run_script(script_name, description):
    """Run a Python script and return its exit code."""
    print_section_header(description)
    
    print(f"Running {script_name}...\n")
    
    try:
        # Run the script as a subprocess
        result = subprocess.run([sys.executable, script_name], check=True)
        print(f"\n✅ {description} completed successfully")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"\n❌ {description} failed with exit code {e.returncode}")
        return e.returncode
    except Exception as e:
        print(f"\n❌ {description} failed: {e}")
        return 1

def check_mcp_server():
    """Check if the OceanBase MCP server is running."""
    print_section_header("Checking OceanBase MCP Server")
    
    try:
        # Import the MCP tools module
        from mcp_tools import use_mcp_tool
        
        # Try to execute a simple query
        result = use_mcp_tool(
            server_name="oceanbase",
            tool_name="execute_sql",
            arguments={
                "query": "SELECT 1"
            }
        )
        
        print("✅ OceanBase MCP server is running")
        return True
    except ImportError:
        print("❌ Failed to import mcp_tools module")
        print("This demo requires the OceanBase MCP server to be running.")
        print("Please make sure the MCP server is running and the mcp_tools module is installed.")
        return False
    except Exception as e:
        print(f"❌ Error connecting to OceanBase MCP server: {e}")
        print("Please make sure the OceanBase MCP server is running.")
        return False

def show_menu():
    """Show the interactive menu."""
    print("\n" + "-" * 50)
    print("OceanBase Multi-Model Demo Menu")
    print("-" * 50)
    print("1. Setup Database (create tables and sample data)")
    print("2. Run Vector Similarity Demo")
    print("3. Run MCP Demo")
    print("4. Run All Demos")
    print("5. Exit")
    print("-" * 50)
    
    choice = input("Enter your choice (1-5): ")
    return choice

def run_interactive_mode():
    """Run the demo in interactive mode."""
    print_header()
    
    print("\n🚀 Welcome to the OceanBase Multi-Model Demo!")
    print("This demo showcases how OceanBase enables GenAI agents to efficiently answer complex")
    print("questions that require different data types, making it an attractive solution for")
    print("AWS Solution Architects looking to simplify their data architecture.\n")
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            # Setup database
            run_script("setup_database.py", "Setting up the database")
        elif choice == "2":
            # Run vector similarity demo
            run_script("bedrock_vector_demo.py", "Running vector similarity demo")
        elif choice == "3":
            # Run MCP demo
            if check_mcp_server():
                run_script("setup_database_mcp.py", "Setting up the database with MCP")
            else:
                print("\n❌ MCP demo cannot run without the OceanBase MCP server.")
        elif choice == "4":
            # Run all demos
            run_all_demos()
        elif choice == "5":
            # Exit
            print("\nThank you for exploring the OceanBase Multi-Model Demo!")
            return 0
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 5.")

def run_all_demos():
    """Run all demos in sequence."""
    # Check if the OceanBase MCP server is running
    mcp_available = check_mcp_server()
    
    # Step 1: Set up the database
    if run_script("setup_database.py", "Setting up the database") != 0:
        print("\n⚠️ Database setup failed. Continuing anyway.")
    
    # Step 2: Run the vector similarity demo
    if run_script("bedrock_vector_demo.py", "Running vector similarity demo") != 0:
        print("\n⚠️ Vector similarity demo failed. Continuing anyway.")
    
    # Step 3: Run the MCP demo if available
    if mcp_available:
        if run_script("setup_database_mcp.py", "Setting up the database with MCP") != 0:
            print("\n⚠️ MCP database setup failed. Continuing anyway.")
    
    print_section_header("Demo Complete")
    
    print("✅ The OceanBase Multi-Model Demo has completed successfully.")
    print("\nYou can now explore the individual demo scripts:")
    print("  - bedrock_vector_demo.py: Demo for vector similarity search")
    print("  - setup_database_mcp.py: Demo for using the OceanBase MCP server")
    
    print("\nFor more information, please refer to the README.md file.")

def run_batch_mode(component):
    """Run the demo in batch mode."""
    print_header()
    
    print(f"\n🚀 Running OceanBase Multi-Model Demo in batch mode (component: {component})")
    
    if component == "setup":
        return run_script("setup_database.py", "Setting up the database")
    elif component == "vector":
        return run_script("bedrock_vector_demo.py", "Running vector similarity demo")
    elif component == "mcp":
        if check_mcp_server():
            return run_script("setup_database_mcp.py", "Setting up the database with MCP")
        else:
            print("\n❌ MCP demo cannot run without the OceanBase MCP server.")
            return 1
    elif component == "all":
        run_all_demos()
        return 0
    else:
        print(f"\n❌ Unknown component: {component}")
        return 1

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="OceanBase Multi-Model Demo Runner")
    parser.add_argument("--batch", action="store_true", help="Run in batch mode")
    parser.add_argument("--component", choices=["setup", "vector", "mcp", "all"], 
                        default="all", help="Component to run in batch mode")
    
    args = parser.parse_args()
    
    if args.batch:
        return run_batch_mode(args.component)
    else:
        return run_interactive_mode()

if __name__ == "__main__":
    sys.exit(main())