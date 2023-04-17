import pynecone as pc
from plot_gms.visualize import MarkovPlot
from plot_gms.components.navbar import navbar


def plot_title() -> pc.Component:
    return pc.vstack(
        pc.hstack(
            pc.box(
                pc.text('Fig title', font_size='0.5em'),
                width='100%',
                align_items='center',
            ),
        ),
        pc.hstack(
            pc.input(
                placeholder='Fig title',
                on_change=MarkovPlot.set_mk_fig_title,
                width='100%',
            ),
        ),
        pc.hstack(
            pc.box(
                pc.text('Title font size', font_size='0.5em'),
            ),
        ),
        pc.hstack(
            pc.input(
                placeholder='Title font size',
                on_change=MarkovPlot.set_mk_fig_title_font_size,
            ),
        ),
        pc.hstack(
            pc.box(
                pc.text('Fig height', font_size='0.5em'),
                width='100%',
            ),
            pc.box(
                pc.text('Fig width', font_size='0.5em'),
                width='100%',
            ),
        ),
        pc.hstack(
            pc.input(
                placeholder='Fig height (default: 600)',
                on_change=MarkovPlot.set_mk_fig_heigth,
            ),
            pc.input(
                placeholder='Fig width (default: 1200)',
                on_change=MarkovPlot.set_mk_fig_width,
            ),
        ),
        pc.hstack(
            pc.box(
                pc.text('X scale', font_size='0.5em'),
                width='100%',
            ),
            pc.box(
                pc.text('X limit', font_size='0.5em'),
                width='100%',
            ),
        ),
        pc.hstack(
            pc.input(
                placeholder='X scale (default: 1)',
                on_change=MarkovPlot.set_mk_x_scale,
            ),
            pc.input(
                placeholder='X limit (default: 100)',
                on_change=MarkovPlot.set_mk_x_lim,
            ),
        ),
        align_items='left',
    )


def plot_options() -> pc.Component:
    return pc.accordion(
        pc.accordion_item(
            pc.accordion_button(
                pc.text('Figure Options', font_weight='bold'),
                pc.accordion_icon(),
            ),
            pc.accordion_panel(
                plot_title(),
            ),
        ),
        width='100%',
    )


def markov() -> pc.Component:
    return pc.center(
        navbar(),
        pc.box(
            pc.vstack(
                pc.heading('Markov Chain', font_size='1em'),
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
                plot_options(),
                pc.button(
                    pc.cond(
                        MarkovPlot.is_progressing,
                        pc.circular_progress(is_indeterminate=True),
                        pc.text('Plot'),
                    ),
                    font_size='0.75em',
                    width='10em',
                    color='white',
                    background_color='rgb(36, 90, 162)',
                    border_radius='1em',
                    padding='1em',
                    on_click=lambda: MarkovPlot.markov_handle_upload(
                        pc.upload_files(),
                    ),
                ),
                pc.cond(
                    MarkovPlot.has_fig,
                    pc.plotly(data=MarkovPlot.fig, layout=MarkovPlot.fig_layout),
                ),
                spacing='1.5em',
                font_size='2em',
            ),
        ),
        padding_top='10%',
    )
