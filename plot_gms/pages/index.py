import pynecone as pc
from plot_gms.components.navbar import navbar


def container(*children, **kwargs):
    kwargs = {'max_width': '1440px', 'padding_x': ['1em', '2em', '3em'], **kwargs}
    return pc.container(
        *children,
        **kwargs,
    )


def intro():
    return pc.box(
        container(
            pc.flex(
                pc.box(
                    pc.text(
                        'Plot and visualize your numerical data with simple procedure.',
                        font_style='normal',
                        font_weight=800,
                        font_size='2em',
                        padding_bottom='0.5em',
                    ),
                    pc.text(
                        'Visualize your data quickly without'
                        + 'writing any additional code using PlotGMS.',
                        color='#666',
                        margin_bottom='1.5em',
                    ),
                    pc.hstack(
                        pc.text('Accepted data', font_weight='600'),
                        margin_bottom='0.5em',
                    ),
                    pc.text(
                        'This app now can accept .txt file only',
                        color='#666',
                    ),
                    flex=1,
                    margin_right=[0, 0, '1em'],
                    margin_bottom=['2em', '2em', 0],
                ),
                flex_direction=['column', 'column', 'column', 'row', 'row'],
            ),
        ),
        background='linear-gradient(200deg, #FFFFFF 10%, #F8F8F8 140%)',
        padding_top='30px',
        padding_bottom='80px',
    )


def index() -> pc.Component:
    return pc.center(
        navbar(),
        pc.vstack(
            pc.heading('Welcome to PlotGMS!', font_size='2.5em', padding_bottom='5%'),
            intro(),
            pc.button(
                'Get started',
                font_size='1.5em',
                width='15em',
                color='white',
                background_color='rgb(36, 90, 162)',
                border_radius='1em',
                padding='1em',
            ),
        ),
    )
