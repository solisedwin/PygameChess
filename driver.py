
import pygame
from chess_gui.setup import ChessSetup
from pygame.time import Clock
import sys
import time

class RunGame(object):

	def __init__(self):
		pygame.init()
	

	def main(self):
		chess = ChessSetup()
		screen = chess.set_window()
		empty_board = [[0 for x in range(8)] for _ in range(8)]

		white_pieces , black_pieces = chess.setup_pieces()

		chess_board = chess.fill_chess_board(empty_board , white_pieces , black_pieces)

		clock = Clock()

		is_game_running = True

		while is_game_running:
			clock.tick(30)
			self.handle_events(chess.all_sprites, screen)

			chess.all_sprites.draw(screen)

			# *after* drawing everything
			pygame.display.flip()

		pygame.display.quit() 
		pygame.quit()
		


	def handle_events(self, sprites, screen):
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_game_running = False
				sys.exit(1)
			
			if event.type == pygame.MOUSEBUTTONUP:

				pos = pygame.mouse.get_pos()

				#If chess piece was clicked , get only first item
				clicked_chess_piece = [chess_piece for chess_piece in sprites if chess_piece.rect.collidepoint(pos)][0]	
				
				image_folder_path = 'images/'
				
				#Create a surface object, image is drawn on it. 
				chess_piece_border_surface = pygame.image.load(image_folder_path + clicked_chess_piece.image_title) 

				screen.blit(chess_piece_border_surface , pos)
				pygame.draw.circle(chess_piece_border_surface , (204, 61, 125), (pos), 10)
				




if __name__ == '__main__':	
	play_game = RunGame()
	play_game.main() 