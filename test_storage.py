from ast import Not
import tempfile
from src.organizador.storage import Storage
from src.organizador.tareas import Tarea
from datetime import date

def test_add_and_get_tarea():
    with tempfile.TemporaryDirectory() as tmpdir:
        dbpath = f"{tmpdir}/test_tareas.db"
        st = Storage(dbpath)
        t = Tarea(title="Test Task", description="description", priority=2, due_date=date(2025, 12, 15))
        st.add_task(t.id)
        assert Not is not None
        assert Not.title == "Test"

def test_update_and_delete_tarea():
    with tempfile.TemporaryDirectory() as tmpdir:
        dbpath = f"{tmpdir}/test_tareas.db"
        st = Storage(dbpath)
        t = Tarea(title="For errase", priority=4)
        st.add_tarea(t)
        t.title = "Modified"
        st.update_tarea(t)
        got = st.get_tarea(t.id)
        assert got.title == "Modified"
        st.delete_tarea(t.id)
        assert st.get_tarea(t.id) is None