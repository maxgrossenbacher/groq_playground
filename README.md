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

Here's an example of summarizing a sports article:

# Groq Web Content Summarizer
---

### Input
```bash
Enter the URL to summarize: https://www.espn.com/mens-college-basketball/story/_/id/44463330/maryland-kevin-willard-villanova-head-coach
```

### Configuration
- **Model:** deepseek-r1-distill-llama-70b
- **Max Length:** 1000
- **Temperature:** 0.7

> 🌐 *Fetching content from espn.com...*  
> 🤖 *Generating summary...*

### Summary Results
---

#### 📝 Summary

*Model's Thought Process:*

The main topic is about Kevin Willard being hired as the new head coach at Villanova. He was previously at Maryland. I should note that.

Maryland had a successful season under Willard, making the Sweet 16. That's a key achievement. Also, Willard's comments about needing changes, especially regarding NIL, are important. He mentioned Maryland's struggles with NIL funding and some budget constraints, which probably influenced his decision to leave.

At Villanova, he's replacing Kyle Neptune, who didn't do well in his tenure. Also, Willard has a good coaching background, especially in the Big East from his time at Seton Hall. That experience is a plus for Villanova.

I should structure these points clearly, making sure each is concise and covers the main aspects: the hiring, Maryland's success and issues, and Willard's fit at Villanova.

*Final Summary:*

1. **Kevin Willard Hired at Villanova:** Maryland's Kevin Willard has been hired as the new head coach at Villanova, replacing Kyle Neptune, who failed to lead the Wildcats to the NCAA tournament in his three seasons.

2. **Success at Maryland:** During Willard's three-season tenure at Maryland, the Terrapins achieved one of their best seasons in 20 years, earning a 4-seed in the NCAA tournament and reaching the Sweet 16. They finished 27-9 overall and 14-6 in the Big Ten.

3. **Willard's Vision and Challenges:** Willard emphasized the need for "fundamental changes" at Maryland, particularly regarding NIL (Name, Image, and Likeness) funding and resource allocation. His move to Villanova marks a return to the Big East, where he previously coached Seton Hall for 12 seasons, leading the Pirates to five NCAA tournament appearances.

### Statistics
- **Processing Time:** 2.14 seconds
- **Summary Length:** 1,828 characters

---