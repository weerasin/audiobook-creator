"""
Simple script to test if the Kokoro TTS API is accessible.
This uses the same approach as generate_audiobook.py to check the TTS service.
"""

import os
import asyncio
import sys

# Add the current directory to the path so we can import the utility
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Get TTS configuration from environment variables
TTS_BASE_URL = os.environ.get("TTS_BASE_URL", "http://localhost:8880/v1")
TTS_API_KEY = os.environ.get("TTS_API_KEY", "not-needed")
TTS_MODEL = os.environ.get("TTS_MODEL", "kokoro")

async def test_api_accessibility():
    """Test if the TTS API is accessible."""
    print(f"Testing TTS API accessibility...")
    print(f"TTS Base URL: {TTS_BASE_URL}")
    print(f"TTS Model: {TTS_MODEL}")
    
    try:
        # Load environment variables if dotenv is available
        try:
            from dotenv import load_dotenv
            load_dotenv()
        except ImportError:
            print("Note: dotenv not available, using system environment variables only.")
        
        # Import here to avoid issues if openai is not installed
        from openai import AsyncOpenAI
        
        # Create the async OpenAI client
        async_openai_client = AsyncOpenAI(
            base_url=TTS_BASE_URL, api_key=TTS_API_KEY
        )
        
        # Import the utility function
        from utils.check_if_audio_generator_api_is_up import check_if_audio_generator_api_is_up
        
        # Use the same function as generate_audiobook.py to check if the API is up
        is_audio_generator_api_up, message = await check_if_audio_generator_api_is_up(async_openai_client)
        
        if is_audio_generator_api_up:
            print("✅ TTS API is accessible!")
            print(f"Message: {message}")
        else:
            print("❌ TTS API is not accessible.")
            print(f"Error: {message}")
            
    except ImportError as e:
        print(f"❌ ImportError: {str(e)}")
        print("Please make sure the required packages are installed.")
    except Exception as e:
        print(f"❌ Error testing TTS API: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_api_accessibility())