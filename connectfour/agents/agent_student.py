from connectfour.agents.computer_player import RandomAgent
import random

class StudentAgent(RandomAgent):
    def __init__(self, name):
        super().__init__(name)
        self.MaxDepth = 1


    def get_move(self, board):
        """
        Args:
            board: An instance of `Board` that is the current state of the board.

        Returns:
            A tuple of two integers, (row, col)
        """

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            next_state = board.next_state(self.id, move[1])
            moves.append( move )
            vals.append( self.dfMiniMax(next_state, 1) )

        bestMove = moves[vals.index( max(vals) )]
        return bestMove

    def dfMiniMax(self, board, depth):
        # Goal return column with maximized scores of all possible next states

        if depth == self.MaxDepth:
            return self.evaluateBoardState(board)

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            if depth % 2 == 1:
                next_state = board.next_state(self.id % 2 + 1, move[1])
            else:
                next_state = board.next_state(self.id, move[1])

            moves.append( move )
            vals.append( self.dfMiniMax(next_state, depth + 1) )


        if depth % 2 == 1:
            bestVal = min(vals)
        else:
            bestVal = max(vals)

        return bestVal

    def evaluateBoardState(self, board):
        """
        possible vars and functions from board.def

        functions:
            def get_cell_value(self, row, col): returns 1 if cell has player1 token, 2 if player's2 token, 0 if empty
            def try_move(self, move): returns raw num where token will be located, if move is impossible returns -1
            def valid_move(self, row, col): returns true if row and column exists and Empty
            def valid_moves(self): iterator of valid moves for current_board
            def terminal(self): true if game is finished, false otherwise
            def legal_moves(self): returns valid moves for the next player
            def next_state(self, turn, col): returns the next board after the proposed move
            def _empty_board(self, height, width): returns empty board
            def winner(self): returns 1 or 2 if player1 or player2 win otherwise 0
            def _check_rows(self): returns the number of connected tokens of the same color or 0 if no tokens connected for rows
            def _check_columns(self): returns the number of connected tokens of the same color or 0 if no tokens connected for columns
            def _check_diagonals(self): returns the number of connected tokens of the same color or 0 if no tokens connected for _check_diagonals

        vars:
            board=None
            height=None - num
            width=None - num
            last_move=[None, None] - [raw, col] of last move
            num_to_connect=4
            winning_zones - as far as I understand it is tuple of valid moves [raw, col] where putting a token makes sense
            score_array - scores of players [player1, player2], not sure what scores mean here
            current_player_score - not used anywhere, have no idea what is it's purpose
        """

        current_board = board
        next_board = NULL



        #return random.uniform(0, 1)
