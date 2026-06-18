import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import app
from dash import html, dcc


def test_header_present():
    header_found = False

    for component in app.layout.children:
        if isinstance(component, html.H1):
            header_found = True

    assert header_found


def test_visualisation_present():
    graph_found = False

    for component in app.layout.children:
        if isinstance(component, dcc.Graph):
            graph_found = True

    assert graph_found


def test_region_picker_present():
    picker_found = False

    for component in app.layout.children:
        if hasattr(component, "children"):
            children = component.children

            if isinstance(children, list):
                for child in children:
                    if isinstance(child, dcc.RadioItems):
                        picker_found = True

    assert picker_found
