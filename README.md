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


## Acknowledgments

- Groq for providing the high-performance inference API
- The open-source community for model availability

## Support

For questions and support:
- Join the [Groq Discord community](https://discord.gg/groq)
- Check the [Groq Documentation](https://docs.groq.com)
