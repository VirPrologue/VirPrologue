# VirPrologue

<p align="center">
An AI-powered story writing assistant that helps create engaging narratives with context awareness and character development.
</p>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#basic-usage">Basic Usage</a> •
  <a href="#features">Features</a> •
  <a href="#examples">Examples</a>
</p>

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/virprologue.git
cd virprologue
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key'
```

## Basic Usage

```python
from virprologue import StoryWriter, Character

# Initialize the writer
writer = StoryWriter()

# Create a story
story = writer.generate_story(
    prompt="The mysterious package arrived at midnight...",
    style="mystery",
    length=1000
)

print(story)
```

## Features

### 1. Character Management

Create and manage characters with personalities and relationships:

```python
# Create a character
protagonist = Character(
    name="Emma",
    description="A brilliant detective with a troubled past",
    personality={
        "intelligence": 0.9,
        "determination": 0.8,
        "skepticism": 0.7
    },
    background="Former FBI profiler turned private investigator"
)

# Add to story
writer.add_character(protagonist)
```

### 2. Writing Styles

Support for multiple genres:
- modern
- fantasy
- sci-fi
- mystery
- romance
- historical
- horror
- children

```python
# Generate fantasy story
fantasy_story = writer.generate_story(
    prompt="The ancient spell book glowed with an eerie light...",
    style="fantasy"
)
```

### 3. Context Awareness

VirPrologue maintains story context for coherent narratives:

```python
# First part
part1 = writer.generate_story(
    prompt="The detective found footprints leading to the garden..."
)

# Continues with context awareness
part2 = writer.generate_story(
    prompt="Following the trail, she discovered..."
)
```

## Examples

### Character Interaction Example

```python
# Create characters
detective = Character(
    name="Inspector Chen",
    description="Methodical detective",
    personality={"analytical": 0.9},
    background="20 years on the force"
)

witness = Character(
    name="Dr. Smith",
    description="Nervous scientist",
    personality={"anxious": 0.7},
    background="Quantum physics researcher"
)

# Set relationships
detective.add_relationship("Dr. Smith", "suspicious of his story")
witness.add_relationship("Inspector Chen", "fears being blamed")

# Add to story
writer.add_character(detective)
writer.add_character(witness)

# Generate scene
scene = writer.generate_story(
    prompt="Inspector Chen watched Dr. Smith's hands tremble as he explained..."
)
```

### Configuration Example

```python
from virprologue import WritingConfig

config = WritingConfig(
    model_name="gpt-4",
    max_tokens=1000,
    temperature=0.7,  # Creativity level (0.0-1.0)
    context_memory_size=5  # Number of previous segments to remember
)
```

## API Reference

### StoryWriter

```python
class StoryWriter:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize with optional API key"""
    
    def generate_story(
        self,
        prompt: str,
        style: str = "modern",
        length: int = 1000
    ) -> str:
        """Generate story content"""
    
    def add_character(self, character: Character) -> None:
        """Add character to story"""
    
    def reset_context(self) -> None:
        """Clear context history"""
```

### Character

```python
@dataclass
class Character:
    name: str
    description: str
    personality: Dict[str, float]
    background: str
    relationships: Dict[str, str] = None
```

## Requirements

- Python 3.8+
- OpenAI API key
- Required packages:
  ```text
  openai>=0.27.0
  python-dotenv>=0.19.0
  typing-extensions>=4.0.0
  ```

## License

MIT License

---

<p align="center">
Created for storytellers and creative writers 📚✨
</p>
