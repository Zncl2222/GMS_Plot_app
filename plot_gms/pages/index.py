import pynecone as pc
from plot_gms.markov import MarkovPlot


def index() -> pc.Component:
    return pc.center(
        pc.box(
            pc.vstack(
                pc.heading('Welcome to PlotGMS!', font_size='1em'),
                pc.box('Upload txt file and plot'),
                pc.upload(
                    pc.text(
                        'Drag and drop files here or click to select files',
                        font_size='0.75em',
                    ),
                    border='2px dotted rgb(0, 0, 0)',
                    background_color='rgb(222, 222, 222)',
                    padding='2em',
                    multiple_files=True,
                ),
                pc.button(
                    'Plot',
                    font_size='0.75em',
                    width='100%',
                    color='white',
                    background_color='rgb(36, 90, 162)',
                    border_radius='1em',
                    padding='1em',
                    on_click=lambda: MarkovPlot.handle_upload(
                        pc.upload_files(),
                    ),
                ),
                spacing='1.5em',
                font_size='2em',
            ),
        ),
        padding_top='10%',
    )
