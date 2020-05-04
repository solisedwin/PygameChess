import copy
import sys
import pygame
from gui_setup.setup import ChessSetup
from pygame.time import Clock
from game_play.player import Player
from game_play.game import GamePlay
	

WHITE = (255, 255, 255)
RED = (255, 0, 0)

class RunGame(object):

	def __init__(self):
		pygame.init()


	def handle_events(self, sprites, screen, game_play, chess_board_image):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(1)

			if event.type == pygame.MOUSEBUTTONUP:

				pos = pygame.mouse.get_pos()
				#completed_turn = False

				for chess_piece_sprite in sprites:
					if game_play.get_clicked_choosen_piece(screen, pos, chess_piece_sprite) is not None:

						print("Current player color: " + game_play.current_player.color)
						#First time clicking a piece
						if game_play.current_player.piece_clicked is None:
							game_play.current_player.piece_clicked = chess_piece_sprite
							break
						#Second time player clicked to tell the piece where to move
						elif game_play.validate_piece_move(chess_piece_sprite):
							screen.fill( (106, 168, 176))
							screen.blit(chess_board_image , (90,150) )
							new_empty_space = game_play.move_piece(chess_piece_sprite)

							#new_empty_space.draw_green_border(screen)
							screen.blit(new_empty_space.image,new_empty_space.rect )
							game_play.current_player.piece_clicked = None
							
							#Swap player turn
							game_play.current_player = game_play.player1 if game_play.current_player.color == "black" else game_play.player2 
							print('Switching to player: ' + game_play.current_player.color)
							print('-' * 30)
							break
						else:
							continue


	def main(self):

		chess_settings = ChessSetup()
		screen = chess_settings.set_window()

		empty_board = [[0 for x in range(8)] for _ in range(8)]

		#Set up Chess Piece Sprite Objects by name, color, position, image..etc
		white_pieces , black_pieces = chess_settings.setup_pieces()
		#Fill the chess board with pieces and empty spaces get a value of None
		chess_board = chess_settings.fill_chess_board(empty_board , white_pieces , black_pieces)
		
		all_sprites = chess_settings.all_sprites

		clock = Clock()

		white_player = Player(name='Edwin',color='white',piece_clicked=None, pieces_captured =[],won =  False)
		black_player = Player(name='Kayne',color='black',piece_clicked = None, pieces_captured = [], won = False)
		
		game_play = GamePlay(chess_board = chess_board, chess_sprites = all_sprites, player1 = white_player,player2 = black_player)
		chess_board_image = chess_settings.get_main_board_image()
		screen.blit(chess_board_image,(90,150))

		while True:
			clock.tick(30)
			self.handle_events(all_sprites,screen, game_play,chess_board_image)
			
			# *after* drawing everything
			game_play.chess_sprites.draw(screen)
			pygame.display.update()
		pygame.display.quit()



if __name__ == '__main__':
	play_game = RunGame()
	play_game.main()
