from src.organizador.tareas import Tarea

def test_mark_done():
    t = Tarea(title="t", priority=3)
    assert not t.done
    t.mark_done()
    assert t.done
    t.mark_undone()
    assert not t.done