import pynecone as pc
from plot_gms.state import State


class ModalState(State):
    show: bool = False
    title: str = 'Error'
    content: str = 'Interal Server Error'

    def change(self, title: str, content: str):
        self.content = content[1:-1]
        self.title = title[1:-1]
        self.show = not (self.show)

    def close(self):
        self.show = not (self.show)


def alert_modal():
    return pc.box(
        pc.modal(
            pc.modal_overlay(
                pc.modal_content(
                    pc.center(
                        pc.vstack(
                            pc.modal_header(
                                ModalState.title,
                                font_size='2em',
                                font_weight='bold',
                                color='red',
                            ),
                            pc.image(src='/warning.png', width='50px', height='auto'),
                            pc.modal_body(
                                ModalState.content,
                                text_align='center',
                            ),
                            pc.modal_footer(
                                pc.button(
                                    'Close',
                                    on_click=ModalState.close,
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            is_open=ModalState.show,
        ),
    )
