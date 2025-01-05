class VirPrologueError(Exception):
    """Base exception for VirPrologue"""
    pass

class APIKeyNotFoundError(VirPrologueError):
    """Raised when OpenAI API key is not found"""
    pass

class StoryGenerationError(VirPrologueError):
    """Raised when story generation fails"""
    pass 