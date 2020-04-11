


class Player(object):
	
	def __init__(self, name = '', color = None, turn  = None, piece_clicked = None, pieces_captured  = [], won = False):
		
		self.name = name
		self.color = color
		self.turn = turn
		self.piece_clicked = piece_clicked
		self.pieces_captured = pieces_captured
		self.won = False


