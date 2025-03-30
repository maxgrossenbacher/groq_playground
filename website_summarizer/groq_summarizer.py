"""
Groq Summarizer Module

This module provides functionality to summarize web content using the Groq API.
It fetches webpage content and generates concise summaries using Groq's language models.

Example:
    Basic usage:
        >>> summarizer = GroqSummarizer()
        >>> summary = summarizer.summarize_webpage("https://groq.com")
        >>> print(summary)

    Command line usage:
        $ python groq_summarizer.py --url https://groq.com
        $ python groq_summarizer.py --url https://groq.com --max-length 600 --temperature 0.8

"""

import os
import argparse
from typing import Optional
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
import groq

# Load environment variables
load_dotenv()

# Initialize console globally at the top level
console = Console()

class GroqSummarizer:
    """
    A class to handle web content summarization using the Groq API.

    This class provides methods to fetch webpage content and generate summaries
    using Groq's language models. It handles API authentication, content fetching,
    and text summarization.

    Attributes:
        api_key (str): Groq API key for authentication
        client (groq.Client): Initialized Groq client
        model (str): Name of the Groq model to use
        max_length (int): Maximum length of generated summary
        temperature (float): Temperature setting for text generation

    Args:
        api_key (Optional[str]): Groq API key. If not provided, will look for GROQ_API_KEY in environment
        model (str): Name of the Groq model to use (default: "deepseek-r1-distill-llama-70b")
        max_length (int): Maximum length of generated summary (default: 1000)
        temperature (float): Temperature setting for text generation (default: 0.7)

    Raises:
        ValueError: If no API key is found
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "deepseek-r1-distill-llama-70b",
        max_length: int = 1000,
        temperature: float = 0.7
    ):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("Groq API key not found. Please set GROQ_API_KEY environment variable.")
        
        self.client = groq.Client(api_key=self.api_key)
        self.model = model
        self.max_length = max_length
        self.temperature = temperature

    def fetch_webpage_content(self, url: str) -> str:
        """
        Fetch and parse content from a webpage.

        Args:
            url (str): The URL of the webpage to fetch

        Returns:
            str: The extracted text content from the webpage

        Raises:
            Exception: If there's an error fetching or parsing the webpage
        """
        # Add user agent and other headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            return soup.get_text()
        except requests.RequestException as e:
            raise Exception(f"Error fetching webpage: {str(e)}")

    def summarize_text(self, text: str) -> str:
        """
        Generate a summary of the provided text using Groq API.

        This method sends the text to Groq's API for summarization, using
        the configured model and parameters.

        Args:
            text (str): The text to summarize

        Returns:
            str: The generated summary

        Raises:
            Exception: If there's an error generating the summary
        """
        prompt = f"""Please summarize the following text concisely into 3 main points:

        {text[:10000]}  # Limit input text to prevent token overflow

        Key points to include:
        - Main topics and themes
        - Important facts and figures
        - Key announcements or updates
        """

        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=self.max_length
            )
            return completion.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error generating summary: {str(e)}")

    def summarize_webpage(self, url: str) -> str:
        """
        Main method to fetch and summarize webpage content.

        This method combines webpage fetching and text summarization into
        a single operation.

        Args:
            url (str): The URL of the webpage to summarize

        Returns:
            str: The generated summary of the webpage content

        Raises:
            Exception: If there's an error in fetching or summarizing
        """
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console  # Use the global console
        ) as progress:
            # Show fetching progress
            fetch_task = progress.add_task(f"🌐 Fetching content from {url}...", total=None)
            content = self.fetch_webpage_content(url)
            progress.update(fetch_task, completed=True)
            
            # Show summarization progress
            summary_task = progress.add_task("🤖 Generating summary...", total=None)
            summary = self.summarize_text(content)
            progress.update(summary_task, completed=True)
            
        return summary

def main():
    """
    Main function to handle command-line interface.

    This function sets up argument parsing and handles the main execution
    flow when the script is run from the command line.

    Command-line Arguments:
        --url: URL to summarize
        --max-length: Maximum length of summary (default: 500)
        --temperature: Temperature for text generation (default: 0.7)
        --model: Groq model to use (default: deepseek-r1-distill-llama-70b)
    """
    parser = argparse.ArgumentParser(description="Summarize web content using Groq API")
    parser.add_argument("--url", type=str, help="URL to summarize")
    parser.add_argument("--max-length", type=int, default=1000, help="Maximum length of summary")
    parser.add_argument("--temperature", type=float, default=0.7, help="Temperature for text generation")
    parser.add_argument("--model", type=str, default="deepseek-r1-distill-llama-70b", help="Groq model to use")
    
    args = parser.parse_args()
    
    try:
        # Create header
        console.print("\n[bold blue]Groq Web Content Summarizer[/bold blue]")
        console.print("=" * 50, "\n")
        
        # Get URL (remove duplicate URL prompt)
        url = args.url or console.input("[yellow]Enter the URL to summarize:[/yellow] ").strip()
        
        # Show configuration
        console.print("\n[bold]Configuration:[/bold]")
        console.print(f"• Model: [cyan]{args.model}[/cyan]")
        console.print(f"• Max Length: [cyan]{args.max_length}[/cyan]")
        console.print(f"• Temperature: [cyan]{args.temperature}[/cyan]\n")
        
        # Initialize summarizer
        summarizer = GroqSummarizer(
            model=args.model,
            max_length=args.max_length,
            temperature=args.temperature
        )
        
        # Get summary with timing
        start_time = datetime.now()
        summary = summarizer.summarize_webpage(url)
        end_time = datetime.now()
        
        # Calculate processing time
        processing_time = (end_time - start_time).total_seconds()
        
        # Display results
        console.print("\n[bold green]Summary Results[/bold green]")
        console.print("=" * 50)
        
        # Display summary in a nice panel
        console.print(Panel(
            Markdown(summary),
            title="📝 Summary",
            border_style="blue",
            padding=(1, 2)
        ))
        
        # Show footer with stats
        console.print("\n[bold]Statistics:[/bold]")
        console.print(f"• Processing Time: [cyan]{processing_time:.2f}[/cyan] seconds")
        console.print(f"• Summary Length: [cyan]{len(summary)}[/cyan] characters")
        console.print("\n" + "=" * 50 + "\n")
        
    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {str(e)}", style="red")
        console.print("\n[yellow]Tip: Make sure you have a valid URL and your API key is set correctly.[/yellow]")

if __name__ == "__main__":
    main() 