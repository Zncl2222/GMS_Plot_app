import pynecone as pc


def navbar():
    return pc.box(
        pc.hstack(
            pc.link(
                pc.hstack(pc.image(src='favicon.ico'), pc.heading('PlotGMS')),
                href='/',
            ),
            pc.desktop_only(
                pc.link(
                    pc.image(src='/github.png', height='1.25em'),
                    href='/',
                ),
            ),
            justify='space-between',
            border_bottom='0.2em solid #F0F0F0',
            padding_x='2em',
            padding_y='1em',
            bg='rgba(255,255,255, 0.90)',
        ),
        position='fixed',
        width='100%',
        top='0px',
        z_index='500',
    )
