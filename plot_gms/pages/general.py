import pynecone as pc
from plot_gms.visualize import GeneralUpload
from plot_gms.components.navbar import navbar
from plot_gms.components.modal import alert_modal


def general_subplot_options() -> pc.Component:
    return pc.cond(
        GeneralUpload.plot_option == GeneralUpload.plot_options_list[1],
        pc.vstack(
            pc.hstack(
                pc.box(
                    pc.text('Row number', font_size='0.5em'),
                    width='50%',
                ),
                pc.box(
                    pc.text('Col number', font_size='0.5em'),
                ),
            ),
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
            align_items='left',
        ),
    )


def general_options() -> pc.Component:
    return pc.accordion(
        pc.accordion_item(
            pc.accordion_button(
                pc.text('Figure Options'),
                pc.accordion_icon(),
            ),
            pc.accordion_panel(
                pc.vstack(
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
                            on_change=GeneralUpload.set_fig_title,
                        ),
                    ),
                    pc.hstack(
                        pc.box(
                            pc.text('Fig height', font_size='0.5em'),
                            width='50%',
                        ),
                        pc.box(
                            pc.text('Fig width', font_size='0.5em'),
                        ),
                    ),
                    pc.hstack(
                        pc.input(
                            placeholder='Fig height',
                            on_change=GeneralUpload.set_fig_height,
                        ),
                        pc.input(
                            placeholder='Fig width',
                            on_change=GeneralUpload.set_fig_width,
                        ),
                    ),
                    align_items='left',
                ),
            ),
        ),
        width='100%',
    )


def general() -> pc.Component:
    return pc.center(
        navbar(),
        pc.box(
            pc.vstack(
                pc.heading('General', font_size='1em'),
                pc.box('Upload txt file and plot'),
                pc.upload(
                    pc.text(
                        GeneralUpload.uploaded,
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
                general_subplot_options(),
                general_options(),
                pc.button(
                    pc.cond(
                        GeneralUpload.plot_state,
                        pc.circular_progress(is_indeterminate=True),
                        pc.text('Plot'),
                    ),
                    font_size='0.75em',
                    width='10em',
                    color='white',
                    background_color='rgb(36, 90, 162)',
                    border_radius='1em',
                    padding='1em',
                    on_click=lambda: GeneralUpload.handle_upload_check(
                        pc.upload_files(),
                    ),
                ),
                alert_modal(),
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
