from typing import Dict, Optional
from dataclasses import dataclass

@dataclass
class Character:
    """Class for managing story characters"""
    
    name: str
    description: str
    personality: Dict[str, float]
    background: str
    relationships: Dict[str, str] = None
    
    def __post_init__(self):
        if self.relationships is None:
            self.relationships = {}

    def add_relationship(self, other_character: str, relationship: str) -> None:
        """Add or update a relationship with another character"""
        self.relationships[other_character] = relationship

    def get_relationship(self, other_character: str) -> Optional[str]:
        """Get the relationship with another character"""
        return self.relationships.get(other_character) 