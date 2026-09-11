from pathlib import Path
from file_manager import obtener_facturas


def test_obtener_facturas(tmp_path):
    (tmp_path / "factura1.pdf").write_text("test")
    (tmp_path / "factura_cliente.pdf").write_text("test")
    (tmp_path / "documento.pdf").write_text("test")
    (tmp_path / "factura.txt").write_text("test")

    resultado = obtener_facturas(tmp_path)

    nombres = [Path(archivo).name for archivo in resultado]

    assert "factura1.pdf" in nombres
    assert "factura_cliente.pdf" in nombres
    assert "documento.pdf" not in nombres
    assert "factura.txt" not in nombres