from dataclasses import dataclass
from typing import Dict

@dataclass
class WritingConfig:
    """Configuration settings for the story generator"""
    
    model_name: str = "gpt-4"
    max_tokens: int = 1000
    temperature: float = 0.7
    top_p: float = 1.0
    frequency_penalty: float = 0.5
    presence_penalty: float = 0.3
    context_memory_size: int = 5
    
    writing_styles: Dict[str, str] = None
    
    def __post_init__(self):
        if self.writing_styles is None:
            self.writing_styles = {
                "modern": "Contemporary and realistic style",
                "fantasy": "Magical and imaginative style",
                "sci-fi": "Scientific and futuristic style",
                "mystery": "Suspenseful and intriguing style",
                "romance": "Emotional and romantic style",
                "historical": "Period-accurate and detailed style",
                "horror": "Dark and atmospheric style",
                "children": "Simple and engaging style"
            } 