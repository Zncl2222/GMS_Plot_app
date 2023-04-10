import pynecone as pc
from plot_gms.visualize import GeneralUpload
from plot_gms.components.navbar import navbar


def general() -> pc.Component:
    return pc.center(
        navbar(),
        pc.box(
            pc.vstack(
                pc.heading('General', font_size='1em'),
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
                pc.select(
                    GeneralUpload.plot_options_list,
                    on_change=GeneralUpload.set_plot_option,
                ),
                pc.cond(
                    GeneralUpload.plot_option == GeneralUpload.plot_options_list[1],
                    pc.hstack(
                        pc.input(
                            placeholder='Row number',
                            value=GeneralUpload.rows_number,
                            on_change=GeneralUpload.set_rows_number,
                        ),
                        pc.input(
                            placeholder='Col number',
                            value=GeneralUpload.cols_number,
                            on_change=GeneralUpload.set_cols_number,
                        ),
                    ),
                ),
                pc.button(
                    'Plot',
                    font_size='0.75em',
                    width='10em',
                    color='white',
                    background_color='rgb(36, 90, 162)',
                    border_radius='1em',
                    padding='1em',
                    on_click=lambda: GeneralUpload.handle_upload(
                        pc.upload_files(),
                    ),
                ),
                pc.cond(
                    GeneralUpload.has_fig,
                    pc.plotly(data=GeneralUpload.fig, layout=GeneralUpload.fig_layout),
                ),
                spacing='1.5em',
                font_size='2em',
            ),
        ),
        padding_top='10%',
    )
