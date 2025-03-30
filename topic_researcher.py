"""
Topic Researcher Module

This module uses web search and the GroqSummarizer to research specific topics,
gathering and summarizing information from multiple relevant sources.
"""

import os
import json
from typing import List, Dict, Optional
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from dotenv import load_dotenv
from webpage_summarizer import GroqSummarizer

# Initialize console
console = Console()

class TopicResearcher:
    def __init__(
        self,
        api_key: Optional[str] = None,
        search_api_key: Optional[str] = None,
        max_sources: int = 5,
        summarizer_config: Dict = None
    ):
        # Load environment variables
        load_dotenv()
        
        # Initialize API keys
        self.search_api_key = os.getenv("GROQ_GOOGLE_SEARCH_API_KEY")
        self.search_engine_id = os.getenv("GROQ_GOOGLE_SEARCH_ENGINE_ID")
        
        if not (self.search_api_key and self.search_engine_id):
            raise ValueError("Google Search API key and Engine ID are required")
        
        # Initialize summarizer
        self.summarizer = GroqSummarizer(**(summarizer_config or {}))
        self.max_sources = max_sources

    def search_topic(self, topic: str) -> List[Dict]:
        """
        Search for relevant URLs about the topic using Google Custom Search API.
        """
        search_url = "https://www.googleapis.com/customsearch/v1"
        
        try:
            params = {
                'key': self.search_api_key,
                'cx': self.search_engine_id,
                'q': topic,
                'num': self.max_sources
            }
            
            console.print(f"\nSearching for: {topic}")
            response = requests.get(search_url, params=params)
            response.raise_for_status()
            
            results = response.json()
            
            if 'items' not in results:
                console.print("[yellow]No results found for this topic[/yellow]")
                return []
            
            # Extract relevant information from search results
            sources = []
            for item in results.get('items', []):
                sources.append({
                    'title': item.get('title', ''),
                    'url': item.get('link', ''),
                    'snippet': item.get('snippet', ''),
                    'source': item.get('displayLink', '')
                })
                console.print(f"[green]Found:[/green] {item.get('title', '')}")
            
            return sources
            
        except Exception as e:
            console.print(f"[red]Error during search: {str(e)}[/red]")
            return []

    def research_topic(self, topic: str) -> Dict:
        """
        Research a topic by searching, fetching, and summarizing content from multiple sources.
        """
        research_results = {
            'topic': topic,
            'timestamp': datetime.now().isoformat(),
            'sources': [],
            'consolidated_summary': ''
        }
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            # Search for sources
            search_task = progress.add_task(f"🔍 Searching for information about '{topic}'...", total=None)
            sources = self.search_topic(topic)
            progress.update(search_task, completed=True)
            
            if not sources:
                raise Exception(f"No sources found for topic: {topic}")
            
            # Process each source
            for idx, source in enumerate(sources, 1):
                try:
                    progress.add_task(
                        f"📚 Processing source {idx}/{len(sources)}: {source['source']}...",
                        total=None
                    )
                    
                    # Summarize content
                    summary = self.summarizer.summarize_webpage(source['url'])
                    
                    # Store results
                    research_results['sources'].append({
                        'title': source['title'],
                        'url': source['url'],
                        'source': source['source'],
                        'summary': summary
                    })
                    
                except Exception as e:
                    console.print(f"[yellow]Warning: Could not process {source['url']}: {str(e)}[/yellow]")
            
            # Generate consolidated summary
            if research_results['sources']:
                consolidate_task = progress.add_task("🤖 Generating consolidated summary...", total=None)
                consolidated_summary = self.generate_consolidated_summary(
                    topic,
                    research_results['sources']
                )
                research_results['consolidated_summary'] = consolidated_summary
                progress.update(consolidate_task, completed=True)
        
        return research_results

    def generate_consolidated_summary(self, topic: str, sources: List[Dict]) -> str:
        """
        Generate a consolidated summary from all sources.
        """
        combined_content = f"Topic: {topic}\n\nSource Summaries:\n\n"
        for source in sources:
            combined_content += f"Source: {source['title']}\n{source['summary']}\n\n"
        
        prompt = f"""Please create a comprehensive summary of the following research about '{topic}'.
        Combine information from all sources, avoid redundancy, and highlight key findings.
        Include any conflicting information or different perspectives if present.
        
        {combined_content}
        
        Please structure the summary with:
        1. Overview
        2. Key Findings
        3. Different Perspectives (if any)
        4. Conclusions
        """
        
        try:
            completion = self.summarizer.client.chat.completions.create(
                model=self.summarizer.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1500
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error generating consolidated summary: {str(e)}"

def display_research_results(results: Dict):
    """
    Display research results in a formatted way.
    """
    # Display header
    console.print(f"\n[bold blue]Research Results: {results['topic']}[/bold blue]")
    console.print("=" * 50, "\n")
    
    # Display consolidated summary
    console.print(Panel(
        Markdown(results['consolidated_summary']),
        title="📚 Consolidated Summary",
        border_style="blue",
        padding=(1, 2)
    ))
    
    # Display sources table
    console.print("\n[bold]Sources and Individual Summaries[/bold]")
    for idx, source in enumerate(results['sources'], 1):
        console.print(f"\n[bold cyan]Source {idx}:[/bold cyan] {source['title']}")
        console.print(f"[link]{source['url']}[/link]")
        console.print(Panel(
            Markdown(source['summary']),
            title="Summary",
            border_style="green",
            padding=(1, 1)
        ))

def main():
    """
    Main function to handle command-line research requests.
    """
    try:
        console.print("\n[bold blue]Topic Research Tool[/bold blue]")
        console.print("=" * 50, "\n")
        
        # Get topic from user
        topic = console.input("[yellow]Enter the topic to research:[/yellow] ").strip()
        
        # Initialize researcher
        researcher = TopicResearcher(
            max_sources=5,
            summarizer_config={
                'max_length': 1000,
                'temperature': 0.7
            }
        )
        
        # Conduct research
        start_time = datetime.now()
        results = researcher.research_topic(topic)
        end_time = datetime.now()
        
        # Display results
        display_research_results(results)
        
        # Show statistics
        processing_time = (end_time - start_time).total_seconds()
        console.print("\n[bold]Research Statistics:[/bold]")
        console.print(f"• Processing Time: [cyan]{processing_time:.2f}[/cyan] seconds")
        console.print(f"• Sources Processed: [cyan]{len(results['sources'])}/{researcher.max_sources}[/cyan]")
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"research_{topic.replace(' ', '_')}_{timestamp}.json"
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        console.print(f"\nResults saved to: [green]{filename}[/green]")
        
    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {str(e)}", style="red")
        console.print("\n[yellow]Tip: Make sure you have valid API keys set in your environment.[/yellow]")

if __name__ == "__main__":
    main() 