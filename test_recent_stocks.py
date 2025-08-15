#!/usr/bin/env python3
"""
Test script to verify recent stocks functionality
"""

import sys
import os
import django

# Add the project directory to the Python path
sys.path.append('/f%3A/project/new/-Stock-market-Prediction-with-Machine-Learning-Django')

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app.views import index
from django.test import RequestFactory
import json

def test_recent_stocks():
    """Test the recent stocks functionality"""
    print("Testing recent stocks functionality...")
    
    # Create a mock request
    factory = RequestFactory()
    request = factory.get('/')
    
    try:
        # Call the index view
        response = index(request)
        
        # Check if response is successful
        if response.status_code == 200:
            print("✓ Index view returned successfully")
            
            # Get the context data
            context = response.context_data if hasattr(response, 'context_data') else {}
            
            # Check if recent_stocks is in context
            if 'recent_stocks' in context:
                recent_stocks = context['recent_stocks']
                print(f"✓ Found {len(recent_stocks)} recent stocks")
                
                # Display the recent stocks data
                for i, stock in enumerate(recent_stocks[:3]):  # Show first 3
                    print(f"  {i+1}. {stock.get('Ticker', 'N/A')}: ${stock.get('Close', 'N/A')}")
                
                if len(recent_stocks) > 3:
                    print(f"  ... and {len(recent_stocks) - 3} more stocks")
                
                return True
            else:
                print("✗ No recent_stocks found in context")
                return False
        else:
            print(f"✗ Index view failed with status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"✗ Error testing recent stocks: {e}")
        return False

if __name__ == "__main__":
    success = test_recent_stocks()
    if success:
        print("\n✓ Recent stocks functionality is working correctly!")
    else:
        print("\n✗ Recent stocks functionality has issues!")
        sys.exit(1)
