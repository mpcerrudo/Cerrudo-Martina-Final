import click # type: ignore
from datetime import date
from tabulate import tabulate # type: ignore
from .storage import Storage
from .tareas import Task
from .utils import parse_iso_date




@click.group()
def main():
    pass

@main.command("init-db")
@click.option("--db", default="tareas.db", help="Path to the database file.")
def init_db(db: str) -> None:
    click.echo("Initializing the database...")
    Storage(db)
    click.echo(f"Based initialized at {db}.")

@main.command("add")
@click.argument("title")
@click.option("--description", "-d", default="", help="Task description.")
@click.option("--priority", "-p", default=3, type=int, help="Task priority (1-5).")
@click.option("--due", "-D", default=None, help="Due date in ISO format (YYYY-MM-DD).")
@click.option("--db", default="tareas.db", help="Path db")

def add(title: str, description: str, priority: int, due: str, db: str) -> None:
    due_date = parse_iso_date(due)
    tarea = Task(titulo=title, descripcion=description, priority=priority, due_date=due_date)
    storage = Storage(db)
    storage.add_tarea(tarea)
    click.echo(f"Tarea made with ID {tarea.id}")

@main.command("list")
@click.option("--db", default="tareas.db", help="Path DB")
def list_tareas(db: str) -> None:
    storage = Storage(db)
    tareas = storage.list_tareas()
    rows = []
    for t in tareas:
        rows.append([t.id, t.titulo, t.descripcion, t.priority, t.due_date.isoformat() if t.due_date else"", "X" if t.done else ""])
    click.echo(tabulate(rows, headers=["id", "title", "priority", "due", "done"]))

@main.command("done")
@click.argument("tarea_id", type=int)
@click.option("--db", default="tareas.db", help="Path DB")
def mark_done(task_id: int, db: str) -> None:
    storage = Storage(db)
    tarea = storage.get_tarea(task_id)
    if not tarea:
        click.echo("Task not found.")
        return
    tarea.mark_done()
    storage.update_task(tarea)
    click.echo(f"Task {task_id} marked as done.")

@main.command("delete")
@click.argument("tarea_id", type=int)
@click.option("--db", default="tareas.db", help="Path DB")
def delete(task_id: int, db: str) -> None:
    storage = Storage(db)
    storage.delete_tarea(task_id)
    click.echo(f"Task {task_id} deleted.")

if __name__ == "__main__":
    main()