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

# Research Results: new nike running shoes
---

### 📚 Consolidated Summary

*Model's Thought Process:*

First, I need to read through each source summary carefully to gather all the information. Source 1 is from Nike's official website, which lists various shoe models, their prices, categories like road and trail running, and mentions of best sellers and new arrivals. Source 2 is from Reddit, introducing a community for running shoe enthusiasts discussing Nike's new lineup categorized into Pegasus, Structure, and Vomero. Source 3 is another Nike.com page, detailing men's running shoes with specific models and their features.

I'll start with the Overview. It should give a broad picture of the research, mentioning that the summary combines information from multiple sources, avoids redundancy, and highlights key findings while noting any differing perspectives.

Next, Key Findings. I'll list the main points from all sources. The new lineup is categorized into three cushioning types, specific models like Vomero 18 and Pegasus 41 are highlighted, and the website offers customization options. There's a focus on sustainability and advanced cushioning technologies.

For Different Perspectives, I need to check if there are any conflicting views. The Reddit community seems supportive, but there might be a mention of simplification making the lineup less diverse. I'll note that as a potential differing perspective.

Finally, the Conclusions will tie everything together, emphasizing Nike's focus on innovation, customization, and sustainability, catering to a broad audience.

*Final Research Summary:*

## Comprehensive Summary of Research on New Nike Running Shoes

### 1. Overview

This summary combines information from multiple sources to provide a comprehensive overview of Nike's new running shoes. The research covers various aspects, including product features, pricing, availability, and customer perspectives. The goal is to highlight key findings while avoiding redundancy and noting any conflicting information or different perspectives.

### 2. Key Findings

- **New Nike Running Shoes Lineup:** Nike has introduced a new lineup of running shoes, categorized into three main franchises: Pegasus (responsive cushioning), Structure (supportive cushioning), and Vomero (maximum cushioning). These categories are designed to meet the specific needs of runners, offering a clear distinction between cushioning types.

- **Key Models:** The Pegasus 41 and Pegasus Plus are currently available, while the Pegasus Premium will launch in late January 2025. The Vomero 18 will be available starting February 27, 2025, with additional Vomero and Structure models launching later in 2025.

- **Customization and Options:** Nike offers a wide range of options for runners, including road running, trail running, and track & field shoes. Customers can filter by cushioning type, gender, age, price, color, and width, making it easier to find the right shoe for their needs.

- **Promotions and Discounts:** Nike provides promotions and discounts for specific groups, such as students and military personnel, offering savings on select models.

- **Sustainability and Technology:** The new lineup incorporates advanced cushioning technologies and sustainable materials, reflecting Nike's commitment to innovation and environmental responsibility.

### 3. Different Perspectives

- **Community Feedback:** The running shoe community, as seen on platforms like Reddit, has expressed enthusiasm for the new lineup. However, some users have noted that the streamlined product line may limit options for runners who prefer more niche or specialized shoes.

- **Price Points:** While some models are competitively priced (e.g., the Pegasus 41 at $140), others, such as the Vaporfly 4 at $260, are on the higher end of the spectrum. This pricing strategy may appeal to serious athletes but could be a barrier for casual runners.

### 4. Conclusions

Nike's new running shoes lineup demonstrates the brand's focus on innovation, customization, and sustainability. By categorizing its products into three distinct cushioning types—Pegasus, Structure, and Vomero—Nike aims to simplify the shopping experience for runners. The inclusion of advanced technologies and eco-friendly materials underscores Nike's commitment to meeting the evolving needs of athletes and environmentally conscious consumers. However, the streamlined product line and higher price points for certain models may not appeal to all runners, particularly those seeking more affordable or specialized options.

---

This example shows how the Topic Researcher:
- Processes multiple sources
- Structures information clearly
- Provides comprehensive analysis
- Includes different perspectives
- Draws meaningful conclusions

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