import os
from groq import Groq
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import textwrap

class GroqURLSummarizer:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        
    def extract_text_from_url(self, url):
        try:
            # Add headers to mimic a browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            }
            
            # Validate URL
            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                raise ValueError("Invalid URL")
            
            # Fetch webpage content with headers
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            # Parse HTML and extract text
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
                
            # Get text content
            text = soup.get_text(separator=' ', strip=True)
            return text
            
        except Exception as e:
            raise Exception(f"Error extracting text from URL: {str(e)}")

    def summarize_url(self, url):
        try:
            # Extract text content from URL
            content = self.extract_text_from_url(url)
            
            # Create prompt for summarization
            prompt = f"""Please provide a concise summary of the main points from the following text. 
            Focus on the key ideas and important details:
            
            {content}
            
            Summary of main points:"""
            
            # Generate summary using Groq
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="deepseek-r1-distill-llama-70b",  # You can also use other models
                temperature=0.3,
                max_tokens=800
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            raise Exception(f"Error generating summary: {str(e)}")

def pretty_print_summary(url, summary):
    width = 80
    border = "=" * width
    
    print(f"\n{border}")
    print(f"URL: {url}".center(width))
    print(f"{border}\n")
    print("SUMMARY:")
    print("-" * width)
    
    # Format the summary with proper line breaks and indentation
    # Split into paragraphs and wrap text
    paragraphs = summary.split('\n')
    for paragraph in paragraphs:
        # Add indentation and wrap long lines
        wrapped_text = '\n'.join(
            textwrap.fill(line.strip(), width=width-4, initial_indent='  ', subsequent_indent='  ')
            for line in paragraph.split('\n') if line.strip()
        )
        print(wrapped_text)
        print()  # Add space between paragraphs
    
    print(f"{border}\n")

def main():
    # Initialize with your Groq API key
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("Please set GROQ_API_KEY environment variable")
    
    summarizer = GroqURLSummarizer(api_key)
    
    # Get URL from user input with default value
    default_url = "https://groq.com/"
    url = input(f"Enter the URL you want to summarize (press Enter for {default_url}): ").strip()
    
    # Use default URL if no input provided
    if not url:
        url = default_url
    
    try:
        print(f"\nGenerating summary...")
        summary = summarizer.summarize_url(url)
        pretty_print_summary(url, summary)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()