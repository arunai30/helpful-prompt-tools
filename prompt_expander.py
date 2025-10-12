#!/usr/bin/env python3
"""
Prompt Expander Demo Script

A tool that helps expand prompts based on general guidelines through an iterative
conversation process with OpenAI models.
"""

import os
from typing import List, Dict, Optional
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class PromptExpander:
    def __init__(self):
        """Initialize the PromptExpander with OpenAI client and configuration."""
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.primary_model = "gpt-4o"
        self.guidance_model = "gpt-5"
        self.max_iterations = 3
        self.conversation_history = []
        self.guidelines = ""
        
    def send_to_model(self, messages: List[Dict[str, str]], model: str) -> str:
        """
        Send messages to specified OpenAI model and return response.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model name to use for the API call
            
        Returns:
            Response content from the model
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            return f"Error: Unable to get response from {model}"
    
    def has_clarifying_questions(self, response: str) -> bool:
        """
        Detect if the response contains clarifying questions using simple heuristics.
        
        Args:
            response: The model's response text
            
        Returns:
            True if clarifying questions are detected, False otherwise
        """
        # Simple heuristics to detect questions
        question_indicators = [
            "Can you clarify these questions"
        ]
        
        response_lower = response.lower()
        
        # Check for question marks
        if "?" in response:
            return True
            
        # Check for question indicators
        for indicator in question_indicators:
            if indicator in response_lower:
                return True
                
        return False
    
    def generate_answers(self, clarifying_questions: str) -> Optional[str]:
        """
        Use secondary model to answer clarifying questions based on guidelines.
        
        Args:
            clarifying_questions: The clarifying questions from the primary model
            
        Returns:
            Answers to the questions or None if guidelines are missing
        """

        check_messages = [
            {
                "role": "system",
                "content": f"""You are helping to answer clarifying questions for a task based on guidelines.
                    You may have guidlines from the start or you can ask the user for guidelines as conversation progresses.
                    Existing guidelines: {self.guidelines.strip()}
                    Determine if you can provide meaningful answers to the questions below without specific guidelines, or if guidelines are needed.
                    If guidelines are needed, ask the user for them with the question "Can you provide some guidelines for the task?"
                    """
            },
            {
                "role": "user",
                "content": f"Questions to answer: {clarifying_questions}\n\nCan you provide meaningful answers to these questions based on the existing guidelines? If not, explain what kind of additional guidelines would be needed."
            }
        ]
        
        answers = self.send_to_model(check_messages, self.guidance_model)
        if "Can you provide some guidelines for the task" in answers.lower():
            print(f"\n🤖 {self.guidance_model} says: {answers}")
            return None
        else:
            return answers
    
    def get_guidelines_from_user(self) -> str:
        """
        Prompt user to provide guidelines for the task.
        
        Returns:
            Guidelines provided by the user
        """
        print("\n📝 Guidelines are needed to answer the clarifying questions effectively.")
        print("Please provide some general guidelines for the task:")
        print("(You can describe the context, goals, constraints, or preferences)")
        print("Guidelines: ", end="")
        
        guidelines = input().strip()
        return guidelines
    
    def update_guidelines(self, new_info: str):
        """
        Update guidelines with new information.
        
        Args:
            new_info: New information to add to guidelines
        """
        if self.guidelines:
            self.guidelines += f"\n\n {new_info}"
        else:
            self.guidelines = new_info
    
    def log_conversation(self, speaker: str, message: str):
        """
        Log conversation entry.
        
        Args:
            speaker: Who is speaking (User, GPT-4o, GPT-5, etc.)
            message: The message content
        """
        self.conversation_history.append({
            "speaker": speaker,
            "message": message
        })
    
    def print_conversation_history(self):
        """Print the complete conversation history."""
        print("\n" + "="*80)
        print("📝 COMPLETE CONVERSATION HISTORY")
        print("="*80)
        
        for i, entry in enumerate(self.conversation_history, 1):
            speaker = entry["speaker"]
            message = entry["message"]
            
            # Use emojis for different speakers
            if speaker == "User":
                icon = "👤"
            elif "gpt-4o" in speaker.lower():
                icon = "🤖"
            elif "gpt-5" in speaker.lower():
                icon = "🧠"
            else:
                icon = "💬"
                
            print(f"\n{i}. {icon} {speaker}:")
            print("-" * 40)
            print(message)
    
    def print_final_guidelines(self):
        """Print the final updated guidelines."""
        print("\n" + "="*80)
        print("📋 FINAL GUIDELINES")
        print("="*80)
        
        if self.guidelines.strip():
            print(self.guidelines)
        else:
            print("No guidelines were provided or updated during this session.")
    
    def run(self):
        """Main execution loop for the prompt expander."""
        print("🚀 Welcome to the Prompt Expander Demo!")
        print("This tool helps expand and improve prompts through iterative clarification.\n")
        
        # Get initial user prompt
        print("Please enter your initial prompt:")
        print("Prompt: ", end="")
        user_prompt = input().strip()
        
        if not user_prompt:
            print("❌ No prompt provided. Exiting.")
            return
        
        self.log_conversation("User", user_prompt)
        
        # Start the conversation loop
        current_messages = [
            {
                "role": "user",
                "content": f"{user_prompt}\n\nAsk clarifying questions so you can perform better."
            }
        ]
        
        iteration = 0
        
        while iteration < self.max_iterations:
            iteration += 1
            print(f"\n🔄 Iteration {iteration}/{self.max_iterations}")
            print("-" * 40)
            
            # Send to primary model
            print(f"📤 Sending to {self.primary_model}...")
            response = self.send_to_model(current_messages, self.primary_model)
            print(f"📥 Response from {self.primary_model}:")
            print(response)
            
            self.log_conversation(f"{self.primary_model}", response)
            
            # Check for clarifying questions
            if not self.has_clarifying_questions(response):
                print(f"\n✅ No clarifying questions detected. Task completed by {self.primary_model}!")
                break
            
            print(f"\n❓ Clarifying questions detected. Using {self.guidance_model} to answer...")
            
            # Generate answers using secondary model
            answers = self.generate_answers(response)
            
            # If guidelines are missing, get them from user
            if answers is None:
                guidelines = self.get_guidelines_from_user()
                if guidelines:
                    self.update_guidelines(guidelines)
                    print(f"\n📝 Guidelines updated. Trying {self.guidance_model} again...")
                    answers = self.generate_answers(response)
                else:
                    print("⚠️ No guidelines provided. Continuing without specific guidance...")
                    answers = "I'll do my best to answer based on general knowledge."
            
            if answers:
                print(f"\n📥 Answers from {self.guidance_model}:")
                print(answers)
                self.log_conversation(f"{self.guidance_model} (Answering Questions)", answers)
                
                # Continue the conversation with the answers
                current_messages.append({"role": "assistant", "content": response})
                current_messages.append({"role": "user", "content": f"Here are the answers to your questions: {answers}\n\nNow please proceed with the task."})
            else:
                print("⚠️ Could not generate answers. Ending conversation.")
                break
        
        if iteration >= self.max_iterations:
            print(f"\n⏰ Maximum iterations ({self.max_iterations}) reached.")
        
        # Print final results
        self.print_conversation_history()
        self.print_final_guidelines()
        
        print(f"\n🎉 Prompt expansion session completed!")
        print(f"Total iterations: {iteration}")
        print(f"Total conversation entries: {len(self.conversation_history)}")

def main():
    """Main entry point for the script."""
    # Check for OpenAI API key
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY environment variable not set.")
        print("Please set your OpenAI API key:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        return
    
    try:
        expander = PromptExpander()
        expander.run()
    except KeyboardInterrupt:
        print("\n\n👋 Session interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
