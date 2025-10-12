# Prompt Expander Demo

A simple Python tool that demonstrates iterative prompt expansion through clarifying questions using OpenAI's API.

## How It Works

1. **User Input**: You provide an initial prompt
2. **Clarification**: The script sends your prompt to GPT-4o with instructions to ask clarifying questions
3. **Answer Generation**: If questions are detected, GPT-5 answers them based on guidelines
4. **Iteration**: This process repeats up to 3 times until the task is clear
5. **Output**: Complete conversation history and final guidelines are displayed

## Quick Start

### Prerequisites
- Python 3.7+
- OpenAI API key

### Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

### Usage

Run the script:
```bash
python prompt_expander.py
```

Follow the interactive prompts:
- Enter your initial prompt
- Provide guidelines when requested
- Watch the iterative expansion process

## Example Flow

```
🚀 Welcome to the Prompt Expander Demo!

Please enter your initial prompt:
Prompt: Write a blog post about AI

🔄 Iteration 1/3
📤 Sending to gpt-4o...
📥 Response: I'd be happy to help you write a blog post about AI! 
Could you clarify: What specific aspect of AI interests you most?

❓ Clarifying questions detected. Using gpt-5 to answer...
📝 Guidelines are needed to answer the clarifying questions effectively.
Guidelines: Focus on practical AI applications for small businesses

📥 Answers from gpt-5: Based on the guidelines, focus on practical 
AI applications that small businesses can implement...
```

## Features

- **Two-Model Architecture**: Uses GPT-4o for conversation and GPT-5 for guidance
- **Smart Guidelines**: Automatically detects when guidelines are needed
- **Question Detection**: Uses heuristics to identify clarifying questions
- **Conversation Logging**: Complete history with emojis for easy reading
- **Error Handling**: Graceful handling of API failures

## Files

- `prompt_expander.py` - Main script
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore rules
- `README.md` - This file

## Configuration

The script uses these models by default:
- **Primary Model**: `gpt-4o` (main conversation)
- **Guidance Model**: `gpt-5` (answering clarifying questions)

Maximum iterations: 3

## License

This is a demo script for educational purposes.
