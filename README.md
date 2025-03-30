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
from groq_summarizer import summarize_webpage

# Example usage
url = "https://groq.com"
summary = summarize_webpage(url)
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

## Error Handling

The module includes error handling for common issues:
- Invalid URLs
- API authentication errors
- Rate limiting
- Network connectivity issues

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

## Acknowledgments

- Groq for providing the high-performance inference API
- The open-source community for model availability

## Support

For questions and support:
- Check the [Groq Documentation](https://console.groq.com/docs/overview)

## Command Line Usage

### Basic Usage

1. Open your terminal and navigate to the project directory:
```bash
cd groq_playground/website_summarizer
```

2. Run the summarizer script:
```bash
python groq_summarizer.py
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
python groq_summarizer.py --url https://groq.com
```

Additional options:
```bash
python groq_summarizer.py --url https://groq.com --max-length 500 --temperature 0.7
```

Available arguments:
- `--url`: The webpage URL to summarize
- `--max-length`: Maximum length of the summary (default: 500)
- `--temperature`: Controls creativity of the response (default: 0.7)
- `--model`: Specify the Groq model to use (default: mixtral-8x7b-32768)

### Example Output

When you run the summarizer, you'll see the following output:

# Groq Web Content Summarizer
---

### Configuration
- **Model:** deepseek-r1-distill-llama-70b
- **Max Length:** 600
- **Temperature:** 0.8

> 🌐 *Fetching content from https://groq.com...*  
> 🤖 *Generating summary...*

### Summary Results
---

#### 📝 Summary

*Model's Thought Process:*

First, I need to read through the text carefully. It looks like the text is from a website or a promotional material for Groq, highlighting their products, services, and recent news. The user wants the main points extracted without the fluff.

I notice that Groq is focused on AI inference, specifically with their GroqCloud platform. They have a self-serve developer tier available now, which is a key point. There's mention of a new TTS model called PlayAI Dialog, which makes voice AI sound more human. That seems important.

Looking further, there are specific models like Mistral Saba 24B for the Middle East and South Asia, and Qwen QwQ-32B running on their cloud. These are specialized models, so they should be included.

The text also talks about how easy it is to switch from OpenAI by changing just three lines of code. That's a big selling point for developers, so that's definitely worth noting.

Financial aspects are mentioned too, with Groq raising $640 million and being valued at $2.8 billion. This indicates their growth and position in the market, competing with major players like Nvidia.

There are endorsements from Yann LeCun, which adds credibility. Also, the availability of benchmarks and the emphasis on speed from independent analyses should be highlighted.

I should structure the summary to include all these points in a logical flow: start with what Groq is known for, their new products and services, ease of integration, financial status, endorsements, and performance benchmarks.

I need to make sure the summary is concise, so I'll avoid redundant information and focus on the most impactful details. The user probably needs this for a quick overview or to share key updates, so clarity is essential.

*Final Summary:*

Groq specializes in fast AI inference, offering solutions like GroqCloud™, a platform for running openly available models such as Llama, Whisper, and Qwen. The company recently launched PlayAI Dialog, a text-to-speech (TTS) model designed to produce more human-like voice AI. GroqCloud™ now has a self-serve developer tier, making it easier for developers to access and integrate AI models. The platform is compatible with OpenAI, requiring only minimal code changes to migrate. Groq has raised significant funding, with a valuation of $2.8 billion, and is recognized for its high-speed inference capabilities, as validated by independent benchmarks. The company also offers specialized models like Mistral Saba 24B for the Middle East and South Asia. Groq is endorsed by AI leaders like Yann LeCun and is positioned as a key challenger to Nvidia in the AI chip market.

### Statistics
- **Processing Time:** 3.02 seconds
- **Summary Length:** 2,868 characters

---