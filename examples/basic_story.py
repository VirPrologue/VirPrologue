from virprologue import StoryWriter, Character

def main():
    # Initialize the story writer
    writer = StoryWriter()
    
    # Create some characters
    protagonist = Character(
        name="Alice",
        description="A curious and brave young programmer",
        personality={"curiosity": 0.9, "courage": 0.8, "intelligence": 0.85},
        background="A self-taught programmer who discovered a mysterious AI"
    )
    
    # Add characters to the story
    writer.add_character(protagonist)
    
    # Generate a story
    prompt = "Alice sat in front of her computer, staring at the strange messages appearing on her screen..."
    
    try:
        story = writer.generate_story(
            prompt=prompt,
            style="sci-fi",
            length=1000,
            temperature=0.7
        )
        print("Generated Story:")
        print("-" * 50)
        print(story)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 