# Groq Playground

A playground project for experimenting with the Groq API, demonstrating web content summarization and topic research capabilities.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Modules](#modules)
  - [Web Page Summarizer](#web-page-summarizer)
    - [Basic Usage](#webpage-summarizer-basic-usage)
    - [Command Line Options](#webpage-summarizer-options)
    - [Example Output](#webpage-summarizer-output)
  - [Topic Researcher](#topic-researcher)
    - [Setup](#topic-researcher-setup)
    - [Basic Usage](#topic-researcher-basic-usage)
    - [Example Output](#topic-researcher-output)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Overview

This project provides tools to interact with Groq's LLM API, specifically focused on web content summarization. It uses Groq's high-performance inference platform to process and summarize web content quickly and efficiently.

## Prerequisites

- Python 3.8+
- Groq API key (Get your free API key from [Groq Developer Console](https://console.groq.com))
- Google Search API key (For topic researcher)
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/groq_playground.git
cd groq_playground
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables in `.env`:
```text
GROQ_API_KEY=your-groq-api-key-here
GOOGLE_SEARCH_API_KEY=your-google-api-key-here
GOOGLE_SEARCH_ENGINE_ID=your-search-engine-id-here
```

## Modules

### Web Page Summarizer

The webpage summarizer module (`webpage_summarizer.py`) provides functionality to summarize content from any web page using Groq's AI models.

#### Basic Usage

1. **As a Python Module**:
```python
from webpage_summarizer import GroqSummarizer

# Initialize summarizer
summarizer = GroqSummarizer(
    model="deepseek-r1-distill-llama-70b",
    max_length=500,
    temperature=0.7
)

# Summarize a webpage
url = "https://groq.com"
summary = summarizer.summarize_webpage(url)
print(summary)
```

2. **From Command Line**:
```bash
# Basic usage
python webpage_summarizer.py --url https://groq.com

# Interactive mode
python webpage_summarizer.py
```

#### Command Line Options

```bash
python webpage_summarizer.py [options]

Options:
  --url URL             URL to summarize
  --max-length LENGTH   Maximum length of summary (default: 500)
  --temperature TEMP    Temperature for text generation (default: 0.7)
  --model MODEL         Groq model to use (default: deepseek-r1-distill-llama-70b)
```

#### Example Output

Here's an example of summarizing Groq's website:

# Groq Web Content Summarizer
---

### Configuration
- **Model:** deepseek-r1-distill-llama-70b
- **Max Length:** 1000
- **Temperature:** 0.7

> 🌐 *Fetching content from https://groq.com...*  
> 🤖 *Generating summary...*

### Summary Results
---

#### 📝 Summary

*Model's Thought Process:*

First, I'll scan through the text. I see mentions of GroqCloud™, a self-serve developer tier, which suggests they're expanding access to their platform. There are also specific models like PlayAI Dialog and Mistral Saba 24B, which are probably new releases. Then, there's information about funding rounds and valuations, indicating financial growth.

I should make sure each main point captures these elements. The first point could be about the launch of new models and services. The second point should cover their cloud platform's accessibility and compatibility. The third point would highlight their financial achievements and industry recognition.

I need to ensure the summary is clear and each point is distinct. Also, the user emphasized conciseness, so I'll keep each point brief without losing important details.

*Final Summary:*

1. **Groq Launches New AI Models and Services:** Groq has introduced several new AI models and services, including PlayAI Dialog for more human-like voice AI, Mistral Saba 24B for the Middle East and South Asia, and Qwen QwQ-32B available on GroqCloud™. Additionally, GroqCloud™ now offers a self-serve developer tier.

2. **GroqCloud™ Platform and Compatibility:** GroqCloud™ provides fast AI inference for popular models like Llama, Mixtral, and Whisper. It offers seamless migration from other providers, such as OpenAI, with minimal code changes, and has been benchmarked for speed and efficiency.

3. **Groq's Growth and Recognition:** Groq has raised significant funding, achieving a valuation of $2.8 billion, and is recognized as a major challenger to Nvidia in the AI chip market. Its technology has been praised by industry leaders like Yann LeCun, and the company continues to expand its offerings and user base.

### Statistics
- **Processing Time:** 2.64 seconds
- **Summary Length:** 2,047 characters

---

### Topic Researcher

The Topic Researcher module uses Google Custom Search to find relevant sources about a topic and generates comprehensive summaries using the Groq API.

#### Setup

1. Get a Google Custom Search API key:
   - Visit [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project or select existing
   - Enable Custom Search API
   - Create credentials (API key)

2. Set up a Custom Search Engine:
   - Visit [Programmable Search Engine](https://programmablesearchengine.google.com)
   - Create a new search engine
   - Get your Search Engine ID
   - Configure for searching the entire web

3. Configure environment variables as shown in the Installation section

#### Basic Usage

Run the topic researcher:
```bash
python topic_researcher.py
```

When prompted, enter your research topic:

#### Example Research Output

# Topic Research Tool
---

### Search Results for: "best mens nike running shoes"
- Found: The Best Nike Running Shoes 2025 – The Run Testers
- Found: Men's Running Shoes. Nike.com
- Found: The 8 Best Nike Running Shoes for Men
- Found: Mens Best Sellers Running Shoes. Nike.com
- Found: 7 Best Nike Running Shoes | RunRepeat

### 📚 Consolidated Summary

#### 1. Overview of Best Men's Nike Running Shoes
Nike offers a diverse range of running shoes tailored to different running needs and preferences. The shoes are categorized into lines such as Pegasus, Vomero, and Structure, each designed for specific purposes like daily training, long runs, and racing. Models like the Pegasus 41, Vaporfly 3, and Alphafly 3 are highlighted for their performance in various running scenarios.

#### 2. Key Features and Technologies
- **Cushioning and Comfort:** Models feature advanced cushioning technologies such as ReactX foam and ZoomX foam, providing comfort and energy return. The Pegasus series is noted for its high rocker design, while the Invincible 3 offers plush cushioning for comfort.
- **Weight and Drop:** Shoes vary in weight and heel-to-toe drop, with options like the lightweight Vaporfly 3 for speed and the higher-drop Pegasus Plus for longer runs.
- **Durability and Breathability:** The InfinityRN 4 is praised for its durability, while the Alphafly 3 is commended for its breathability, though it may wear out faster in the heel for some runners.

#### 3. Testers' Opinions and Conclusions
- **Pros and Cons:** The Pegasus 41 is versatile but not ideal for forefoot strikers. The Vaporfly 3 excels in speed but is on the pricier side. The Alphafly 3 is great for marathons but may not be as durable for all runners.
- **Recommendations:** Testers recommend considering factors like running style, surface (road or trail), and personal comfort. The guide emphasizes the importance of fit and purpose in choosing the right shoe.

### Source Summaries

#### Source 1: The Best Nike Running Shoes 2025 – The Run Testers
*URL: https://theruntesters.com/the-best-nike-running-shoes/*

Nike is organizing their 2025 running shoes into three main lines:
1. **Pegasus Line:** Daily trainers
2. **Vomero Line:** Max-cushioned shoes
3. **Structure Line:** Stability-focused models

Top Models and Features:
- Pegasus 41: Balance of comfort and versatility
- Pegasus Plus: Lighter, more responsive
- Zoom Fly 6: Super-trainer with carbon plate
- Alphafly 3: Top-tier racing shoe
- Vomero 18: Maximum cushioning
- Vaporfly 3: Lightweight racer
- Pegasus Premium: High-stack, stylish
- Invincible 3: Soon joining Vomero line

[Additional source summaries follow similar format...]

### Research Statistics
- **Processing Time:** 118.77 seconds
- **Sources Processed:** 5/5

## Error Handling

If you encounter any errors:

1. Check your API key is properly set:
```bash
echo $GROQ_API_KEY
```

2. Verify the URL is accessible:
```bash
curl -I https://groq.com
```

3. Ensure you have all required dependencies:
```bash
pip install -r requirements.txt
```

## Support

For questions and support:
- Check the [Groq Documentation](https://console.groq.com/docs/overview)