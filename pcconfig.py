import pynecone as pc

config = pc.Config(
    app_name='plot_gms',
    db_url='sqlite:///pynecone.db',
    env=pc.Env.DEV,
)
