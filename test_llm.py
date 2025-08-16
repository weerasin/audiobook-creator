"""
Audiobook Creator
Copyright (C) 2025 Prakhar Sharma

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from utils.llm_utils import check_if_llm_is_up

load_dotenv()

OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL", "http://localhost:11434/v1")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "not-needed")
OPENAI_MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME", "qwen3:14b")

# Handle empty API key case
if not OPENAI_API_KEY:
    OPENAI_API_KEY = "not-needed"

async_openai_client = AsyncOpenAI(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY)
model_name = OPENAI_MODEL_NAME

async def main():
    print("Testing LLM API endpoint accessibility...")
    is_llm_up, message = await check_if_llm_is_up(async_openai_client, model_name)
    
    if is_llm_up:
        print("✅ LLM API is accessible!")
        print(f"Response: {message}")
    else:
        print("❌ LLM API is not accessible.")
        print(f"Error: {message}")

if __name__ == "__main__":
    asyncio.run(main())