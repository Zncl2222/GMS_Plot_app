class VisualizeVar:
    __symbol_buttons = [
        dict(
            args=['mode', 'markers'],
            label='Markers',
            method='restyle',
        ),
        dict(
            args=['mode', 'line'],
            label='Lines',
            method='restyle',
        ),
        dict(
            args=['mode', 'lines+markers'],
            label='Markers and Lines',
            method='restyle',
        ),
    ]

    __marker_buttons = [
        dict(
            label='Circle',
            method='update',
            args=[{'marker.symbol': 'circle'}],
        ),
        dict(
            label='Square',
            method='update',
            args=[{'marker.symbol': 'square'}],
        ),
        dict(
            label='Diamond',
            method='update',
            args=[{'marker.symbol': 'diamond'}],
        ),
        dict(
            label='X',
            method='update',
            args=[{'marker.symbol': 'x'}],
        ),
        dict(
            label='Triangle-Up',
            method='update',
            args=[{'marker.symbol': 'triangle-up'}],
        ),
        dict(
            label='Star',
            method='update',
            args=[{'marker.symbol': 'star'}],
        ),
        dict(
            label='Hexagon',
            method='update',
            args=[{'marker.symbol': 'hexagon'}],
        ),
        dict(
            label='Hexagon2',
            method='update',
            args=[{'marker.symbol': 'hexagon2'}],
        ),
    ]

    @classmethod
    def get_slider(cls) -> dict:
        steps = []
        for i in range(30):
            step = dict(
                method='restyle',
                args=['marker.size', [(i + 1)]],
                label=f'Size {i + 1}',
            )
            steps.append(step)

        sliders = [
            dict(
                active=10,
                currentvalue={'prefix': 'Marker size: '},
                pad={'t': 50},
                steps=steps,
            ),
        ]
        return dict(sliders=sliders)

    @classmethod
    def get_update_menu(cls) -> list[dict]:
        update_menu = [
            dict(
                buttons=cls.__symbol_buttons,
                direction='down',
                showactive=True,
                x=0,
                xanchor='left',
                y=1.2,
                yanchor='top',
            ),
            dict(
                buttons=cls.__marker_buttons,
                direction='down',
                showactive=True,
                x=0.2,
                xanchor='left',
                y=1.2,
                yanchor='top',
            ),
        ]
        return update_menu

    @classmethod
    def get_annotations(cls) -> list[dict]:
        annotations = [
            dict(
                text='Scatter style',
                x=0,
                xref='paper',
                y=1.27,
                yref='paper',
                showarrow=False,
            ),
            dict(
                text='marker symbol',
                x=0.2,
                xref='paper',
                y=1.27,
                yref='paper',
                showarrow=False,
            ),
        ]
        return annotations