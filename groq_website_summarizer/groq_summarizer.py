"""
A Python module for summarizing web page content using the Groq API.

This module provides functionality to fetch content from a given URL and generate
a concise summary using Groq's language models. It handles web scraping,
text extraction, and API interaction with proper error handling.

Required environment variables:
    GROQ_API_KEY: Your Groq API authentication key
"""

import os
from groq import Groq
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import textwrap

class GroqURLSummarizer:
    """
    A class to handle web page content extraction and summarization using Groq API.
    
    Attributes:
        client (Groq): An instance of the Groq client for API interactions.
    """

    def __init__(self, api_key):
        """
        Initialize the summarizer with Groq API credentials.

        Args:
            api_key (str): The Groq API authentication key.
        """
        self.client = Groq(api_key=api_key)
        
    def extract_text_from_url(self, url):
        """
        Extract readable text content from a given URL.

        Args:
            url (str): The URL to extract content from.

        Returns:
            str: The extracted text content from the webpage.

        Raises:
            Exception: If there's an error fetching or parsing the URL content.
        """
        try:
            # Add headers to mimic a browser for better compatibility
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            }
            
            # Validate URL format
            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                raise ValueError("Invalid URL")
            
            # Fetch webpage content
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            # Parse HTML and clean up the content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove script and style elements as they don't contain relevant text
            for script in soup(["script", "style"]):
                script.decompose()
                
            # Extract clean text content
            text = soup.get_text(separator=' ', strip=True)
            return text
            
        except Exception as e:
            raise Exception(f"Error extracting text from URL: {str(e)}")

    def summarize_url(self, url):
        """
        Generate a summary of the content from a given URL using Groq API.

        Args:
            url (str): The URL to summarize.

        Returns:
            str: A concise summary of the webpage content.

        Raises:
            Exception: If there's an error in text extraction or API interaction.
        """
        try:
            content = self.extract_text_from_url(url)
            
            # Construct the prompt for the language model
            prompt = f"""Please provide a concise summary of the main points from the following text. 
            Focus on the key ideas and important details:
            
            {content}
            
            Summary of main points:"""
            
            # Generate summary using Groq API
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="deepseek-r1-distill-llama-70b",
                temperature=0.3,
                max_tokens=800
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            raise Exception(f"Error generating summary: {str(e)}")

def pretty_print_summary(url, summary):
    """
    Format and print the URL and its summary in a visually appealing way.

    Args:
        url (str): The URL that was summarized.
        summary (str): The generated summary text.
    """
    width = 80
    border = "=" * width
    
    print(f"\n{border}")
    print(f"URL: {url}".center(width))
    print(f"{border}\n")
    print("SUMMARY:")
    print("-" * width)
    
    # Format paragraphs with proper wrapping and indentation
    paragraphs = summary.split('\n')
    for paragraph in paragraphs:
        wrapped_text = '\n'.join(
            textwrap.fill(line.strip(), width=width-4, initial_indent='  ', subsequent_indent='  ')
            for line in paragraph.split('\n') if line.strip()
        )
        print(wrapped_text)
        print()
    
    print(f"{border}\n")

def main():
    """
    Main function to run the URL summarizer.
    
    Handles user input, API key validation, and program execution flow.
    Uses environment variable GROQ_API_KEY for authentication.
    """
    # Validate API key
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("Please set GROQ_API_KEY environment variable")
    
    summarizer = GroqURLSummarizer(api_key)
    
    # Handle URL input with default option
    default_url = "https://groq.com/"
    url = input(f"Enter the URL you want to summarize (press Enter for {default_url}): ").strip()
    
    if not url:
        url = default_url
    
    try:
        print("\nGenerating summary...")
        summary = summarizer.summarize_url(url)
        pretty_print_summary(url, summary)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()