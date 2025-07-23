from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseTool(ABC):
    """Temel Tool sınıfı"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    @abstractmethod
    async def execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Tool'u çalıştır"""
        pass
