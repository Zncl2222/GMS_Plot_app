import pynecone as pc
from plot_gms.constants import GITHUB_URL


def navbar():
    return pc.box(
        pc.hstack(
            pc.link(
                pc.hstack(pc.image(src='favicon.ico'), pc.heading('PlotGMS')),
                href='/',
            ),
            pc.desktop_only(
                pc.hstack(
                    pc.menu(
                        pc.hstack(
                            pc.menu_button(
                                'Start',
                                pc.icon(tag='chevron_down'),
                                font_size='1.1em',
                            ),
                        ),
                        pc.menu_list(
                            pc.link(
                                pc.menu_item(
                                    'General',
                                    _hover={'background_color': 'white'},
                                    _focus={},
                                ),
                            ),
                            pc.link(
                                pc.menu_item(
                                    'MarkovChain(GMS)',
                                    _hover={'background_color': 'white'},
                                    _focus={},
                                ),
                            ),
                            pc.link(
                                pc.menu_item(
                                    'SemiVariance(GMS)',
                                    _hover={'background_color': 'white'},
                                    _focus={},
                                ),
                            ),
                        ),
                    ),
                    pc.link(
                        pc.image(src='/github.png', height='1.75em', width='1.75em'),
                        href=GITHUB_URL,
                        padding_x='2em',
                    ),
                ),
            ),
            justify='space-between',
            # border_bottom='0.2em solid #F0F0F0',
            padding_x='2em',
            padding_y='1em',
            bg='rgba(255,255,255, 0.90)',
        ),
        position='fixed',
        width='100%',
        top='0px',
        z_index='500',
        bg='linear-gradient(271.68deg, #EE756A 10%, #756AEE 95%)',
    )
