import openai
import os
from typing import List, Dict, Optional
from .config import WritingConfig
from .character import Character
from .exceptions import APIKeyNotFoundError, StoryGenerationError

class StoryWriter:
    """Main class for generating stories using OpenAI's API"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise APIKeyNotFoundError("OpenAI API key not found")
            
        openai.api_key = self.api_key
        self.config = WritingConfig()
        self.context_history = []
        self.characters = {}

    def add_character(self, character: Character) -> None:
        """Add a character to the story"""
        self.characters[character.name] = character

    def _build_prompt(self, base_prompt: str) -> str:
        """Build a complete prompt including context and characters"""
        character_descriptions = "\n".join([
            f"{name}: {char.description}"
            for name, char in self.characters.items()
        ])
        
        context = "\n".join(self.context_history[-self.config.context_memory_size:])
        
        return f"""
Characters:
{character_descriptions}

Previous Context:
{context}

Continue the story:
{base_prompt}
"""

    def generate_story(
        self,
        prompt: str,
        style: str = "modern",
        length: int = 1000,
        temperature: float = 0.7
    ) -> str:
        """
        Generate story content based on prompt and parameters
        
        Args:
            prompt: Initial story prompt or continuation point
            style: Writing style to use
            length: Desired length in tokens
            temperature: Creativity level (0.0-1.0)
            
        Returns:
            Generated story text
        """
        try:
            full_prompt = self._build_prompt(prompt)
            
            response = openai.ChatCompletion.create(
                model=self.config.model_name,
                messages=[
                    {
                        "role": "system",
                        "content": f"You are a professional writer specialized in {style} style. "
                                 f"Write in a coherent and engaging manner."
                    },
                    {"role": "user", "content": full_prompt}
                ],
                max_tokens=length,
                temperature=temperature,
                top_p=self.config.top_p,
                frequency_penalty=self.config.frequency_penalty,
                presence_penalty=self.config.presence_penalty
            )
            
            generated_text = response.choices[0].message.content
            self.context_history.append(generated_text)
            return generated_text

        except Exception as e:
            raise StoryGenerationError(f"Error generating story: {str(e)}")

    def reset_context(self) -> None:
        """Clear the context history"""
        self.context_history = [] 