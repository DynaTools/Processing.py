def setup():
    size(800, 800)  # Tamanho da janela
    background(255)  # Fundo branco

def draw():
    # arc
    fill(255, 0, 0)  # Cor de preenchimento vermelha
    arc(100, 100, 80, 80, 0, PI + QUARTER_PI)  # Desenha um arco
    
    # circle
    fill(0, 255, 0)  # Cor de preenchimento verde
    circle(250, 100, 80)  # Desenha um círculo
    
    # ellipse
    fill(0, 0, 255)  # Cor de preenchimento azul
    ellipse(400, 100, 80, 120)  # Desenha uma elipse
    
    # line
    stroke(0)  # Cor da linha preta
    line(500, 60, 580, 140)  # Desenha uma linha
    
    # point
    stroke(0)  # Cor do ponto preta
    point(650, 100)  # Desenha um ponto
    
    # quad
    fill(255, 255, 0)  # Cor de preenchimento amarela
    quad(100, 200, 150, 150, 200, 200, 150, 250)  # Desenha um quadrilátero
    
    # rect
    fill(0, 255, 255)  # Cor de preenchimento ciano
    rect(250, 150, 100, 50)  # Desenha um retângulo
    
    # square
    fill(255, 0, 255)  # Cor de preenchimento magenta
    square(400, 150, 80)  # Desenha um quadrado
    
    # triangle
    fill(128, 128, 128)  # Cor de preenchimento cinza
    triangle(550, 200, 600, 150, 650, 200)  # Desenha um triângulo
    
    noLoop()  # Para o loop draw
