"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc
from plot_gms.pages.index import index
from plot_gms.pages.general import general
from plot_gms.pages.markov import markov
from plot_gms.pages.semivar import semivar
from plot_gms.state import State

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, route='/')
app.add_page(general, route='/general')
app.add_page(markov, route='/markov')
app.add_page(semivar, route='/semivar')

app.compile()
