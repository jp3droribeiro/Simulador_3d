from ursina import *
from ursina.shaders import lit_with_shadows_shader

app = Ursina(borderless=False, fullscreen=False)

EditorCamera() # classe que permite movimentar a camera pelo mouse em tempo real

# Luz direcional projetada com sombras
DirectionalLight(
    shadows=True,
    rotation=(45, -45, 45)
)

ground = Entity(
    model='plane',
    scale=50, 
    texture='white_cube',
    color=color.gray,
    y=0,
    shader=lit_with_shadows_shader,
    cast_shadows=False
)

# Modelo principal (personagem)
man = Entity(
    model="FinalBaseMesh.obj", # modelo 3d (.obj)
    texture="white_cube",
    scale=(1, 1, 1),
    position=(0, 0.01, 0),
    shader=lit_with_shadows_shader,
    cast_shadows=True
)

wall = Entity(
    model="cube",
    texture="brick", # textura de tijolo , da propria biblioteca
    color=color.red,
    scale=(0.2, 13, 40),  # escalonamento da figura (x,y,z)
    position=(12, 6.5, 0),  
    shader=lit_with_shadows_shader,
    cast_shadows=True
)

app.run()
