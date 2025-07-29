#!/usr/bin/env python3
"""
AI Concierge Run Script
=======================

This script starts the AI Concierge application.
"""

import os
import sys
import uvicorn
from pathlib import Path

def check_requirements():
    """Check required files"""
    print("🔍 Checking required files...")
    
    # .env file check
    if not os.path.exists(".env"):
        print("⚠️  .env file not found!")
        print("📝 Copy env.example to .env and add OPENAI_API_KEY")
        return False
    
    # Static files check
    if not os.path.exists("static/chat.html"):
        print("⚠️  static/chat.html file not found!")
        return False
    
    print("✅ All files present")
    return True

def check_dependencies():
    """Check dependencies"""
    print("📦 Checking dependencies...")
    
    try:
        import fastapi
        import uvicorn
        import langchain
        import openai
        print("✅ All dependencies installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("💡 Run pip install -r requirements.txt")
        return False

def main():
    """Main function"""
    print("🏨 Starting AI Concierge...")
    print("=" * 40)
    
    # Checks
    if not check_requirements():
        print("\n❌ Required files missing!")
        return 1
    
    if not check_dependencies():
        print("\n❌ Dependencies missing!")
        return 1
    
    print("\n🚀 Starting application...")
    print("📱 Open http://localhost:8000 in your browser")
    print("🛑 Press Ctrl+C to stop")
    print("=" * 40)
    
    try:
        # Start application
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 Application stopped")
        return 0
    except Exception as e:
        print(f"\n❌ Could not start application: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 