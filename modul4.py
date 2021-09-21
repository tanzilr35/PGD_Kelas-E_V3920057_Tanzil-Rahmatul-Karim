# Part E
import pygame, sys
from pygame import rect
from pygame.locals import *
import time

# Ukuran lebar dan tinggi window pygame
WIDTH, HEIGHT = 400, 400

# Variabel judul
TITLE = "Smooth Movement"

# Instalasi
pygame.init()

# Mengatur ukuran layar window pygame
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Memberi judul caption window pygame
pygame.display.set_caption(TITLE)

# Untuk mengontrol seberapa cepat layar dapat mengupdate
clock = pygame.time.Clock()

# Pilihan variabel warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POWDERBLUE = (176, 224, 230)
ROSYBROWN = (188, 143, 142)

# Part D = Membuat class dengan object Player
class Player:
  #Membuat fungsi init dengan variabel self, x, dan  y
  def __init__(self, x, y):
      self.x = int(x)
      self.y = int(y)
      self.rect = pygame.Rect(self.x, self.y, 32, 32)
      self.color = (BLACK) 
      self.velX = 0 #kecepatan/speed sumbu X
      self.velY = 0 #kecepatan sumbu Y
      self.left_pressed = False
      self.right_pressed = False
      self.up_pressed = False
      self.down_pressed = False
      self.speed = 4

  # Part F = Fungsi draw untuk menggambar kotak
  def draw(self, win):
    pygame.draw.rect(win, self.color, self.rect)

  # Part A = Fungsi update untuk saat kotak digerakkan
  def update(self):
    self.velX = 0
    self.velY = 0
    if self.left_pressed and not self.right_pressed:
      self.velX = -self.speed
    if self.right_pressed and not self.left_pressed:
      self.velX = self.speed
    if self.up_pressed and not self.up_pressed:
      self.velY = -self.speed
    if self.down_pressed and not self.down_pressed:
      self.velY = self.speed
    
    # Speed player bertambah
    self.x += self.velX
    self.y += self.velY

    self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

# Part B
# Ukuran kotak objek player
player = Player(WIDTH/2, HEIGHT/2)

# Menambahkan nama/teks di layar window pygame
font_color = (BLACK)
font_obj = pygame.font.Font("Outwrite.ttf",20)
text = "Tanzil Rahmatul Karim"
img = font_obj.render(text, True, (BLACK))

rect = img.get_rect()
rect.topleft = (20,20)
cursor = Rect(rect.topright, (3, rect.height))

# Mulai loop
while True:
  # Gamenya dimulai
  for event in pygame.event.get():
    # Loop berhenti
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    # Kondisi tombol kanan,kiri,atas,bawah saat ditekan
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player.left_pressed = True
      if event.key == pygame.K_RIGHT:
        player.right_pressed = True
      if event.key == pygame.K_UP:
        player.up_pressed = True
      if event.key == pygame.K_DOWN:
        player.down_pressed = True
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        player.left_pressed = False
      if event.key == pygame.K_RIGHT:
        player.right_pressed = False
      if event.key == pygame.K_UP:
        player.up_pressed = False
      if event.key == pygame.K_DOWN:
        player.down_pressed = False

      if event.type == KEYDOWN:
        if event.key == K_BACKSPACE:
          if len(text)>0:
            text = text[:-1]

        else:
          text += event.unicode
          img = font_obj.render(text, True, ROSYBROWN)
          rect.size = img.get_size()
          cursor.topleft = rect.topright

  # Part C
  win.fill((POWDERBLUE))
  player.draw(win)

  win.blit(img,rect)
  if time.time() % 1 > 0.5:
    pygame.draw.rect(win, POWDERBLUE, cursor)
  pygame.display.update()

  player.update()

  # Memperbarui isi dari layar permainan
  pygame.display.flip()

  # Batasi fps 
  clock.tick(120)

  # Jika kodingan di ubah, maka tampilan dalam pygame langsung di update
  pygame.display.update()

# Quit aplikasi pygame ketika exit
pygame.quit()