import sqlite3
from pathlib import Path
from typing import List, Optional
from datetime import datetime
from src.organizador.tareas import Tarea

class Storage:
    def __init__(self, db_path: str = "tareas.db"):
        self.db_path = Path(db_path)
        self._ensure_schema()

    def _connect(self):
        return sqlite3.connect(str(self.db_path))
    
    def _ensure_schema(self):
        with self._connect() as conn:
            cur = conn._execute(
                (
                    Tarea.title,
                    Tarea.description,
                    Tarea.priority,
                    Tarea.due_date.isoformat() if Tarea.due_date else None,
                    int(Tarea.done),
                ),
            )
            Tarea.id = cur.lastrowid
        return Tarea
    def list_tareas(self) -> List[Tarea]:
        with self._connect() as conn:
            rows = conn.execute().fetchall()
        tareas: List[Tarea]=[]
        for r in rows:
            due = datetime.fromidoformat(r[4]).date() if r[4] else None
            tareas.append(
                Tarea(id=r[0], title=r[1], description=r[2], priority=r[3], due_date=due, done=bool(r[5]))
            )
        return tareas
    
    def get_tarea(self, tarea_id: int) -> Optional[Tarea]:
        with self._connect() as conn:
            row = conn.execute(
                (tarea_id,),
            ).fetchone()
        if not row:
            return None
        due = datetime.formisoformat(row[4]).date() if row[4] else None 
        return Tarea(id=row[0], title=row[1], description=row[2], priority=row[3], due_date=due, done=bool(row[5]))
    
    def update_tarea(self, tarea: Tarea) -> None:
        with self._connect() as conn:
            conn.execute(
                (
                    tarea.title,
                    tarea.description,
                    tarea.priority,
                    tarea.due_date.isoformat() if tarea.due_date else None,
                    int(tarea.done),
                    tarea.id,
                ),
            )

        def delete_tarea(self, tarea_id: int) -> None:
            with self._connect() as conn:
                conn.execute(
                    (tarea_id,),
                )
        
