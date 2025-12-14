from dataclasses import dataclass
from datetime import date 
from typing import Optional

@dataclass
class Tarea:
    id: Optional[int] = None
    titulo: str = ""
    descripcion: str = ""
    priority: int = 3
    due_date: Optional[date] = None
    completed: bool = False

    def mark_completed(self):
        self.completed = True

        def mark_undone(self):
            self.completed = False
        
