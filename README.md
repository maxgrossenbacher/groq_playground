# Groq Playground

A playground project for experimenting with the Groq API, demonstrating web content summarization capabilities.

## Overview

This project provides tools to interact with Groq's LLM API, specifically focused on web content summarization. It uses Groq's high-performance inference platform to process and summarize web content quickly and efficiently.

## Prerequisites

- Python 3.8+
- Groq API key (Get your free API key from [Groq Developer Console](https://console.groq.com))
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

3. Set up your Groq API key:
```bash
export GROQ_API_KEY='your-api-key-here'
```

## Usage Example

Here's an example of how to use the module to summarize the Groq website (https://groq.com):

```python
from groq_summarizer import webpage_summarizer

# Example usage
url = "https://groq.com"
summary = webpage_summarizer.GroqSummarizer(url)
print(summary)
```

Expected output will include key information about Groq, such as:
- Their AI inference platform capabilities
- Available models (Llama, Mixtral, Gemma, Whisper)
- Recent company valuation ($2.8B)
- Developer access through GroqCloud™

## Features

- Web content extraction
- AI-powered summarization using Groq's LLM
- Support for various webpage formats
- Configurable summarization parameters

## Configuration

You can customize the summarization behavior by modifying these parameters:

```python
summarize_webpage(
    url,
    max_length=500,  # Maximum summary length
    temperature=0.7,  # Response creativity (0.0-1.0)
    model="deepseek-r1-distill-llama-70b"  # Choose your preferred Groq model
)
```

## Models Available

Groq supports several open-source models:
- Llama
- DeepSeek
- Gemma
- Whisper
- And more...


## Troubleshooting

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

## Command Line Usage

### Basic Usage

1. Open your terminal and navigate to the project directory:
```bash
cd groq_playground
```

2. Run the summarizer script:
```bash
python webpage_summarizer.py
```

3. When prompted, paste your URL:
```
Enter the URL to summarize: https://groq.com
```

4. The script will then:
   - Fetch the webpage content
   - Process it through Groq's API
   - Display the summary in your terminal

### Command Line Arguments

You can also run the script directly with a URL:
```bash
python webpage_summarizer.py --url https://groq.com
```

Additional options:
```bash
python webpage_summarizer.py --url https://groq.com --max-length 500 --temperature 0.7
```

Available arguments:
- `--url`: The webpage URL to summarize
- `--max-length`: Maximum length of the summary (default: 1000)
- `--temperature`: Controls creativity of the response (default: 0.7)
- `--model`: Specify the Groq model to use (default: deepseek-r1-distill-llama-70b)

### Example Output

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