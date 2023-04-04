"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc
from plot_gms.pages.index import index
from plot_gms.state import State

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)

app.compile()
