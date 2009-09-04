import levels
__all__ = [ 'state' ]


class State( object ):

    STATE_PAUSE, STATE_PLAY, STATE_WIN, STATE_OVER = range(4)

    def __init__( self ):

        # current score
        self.score = 0

        # current level idx
        self.level_idx = 0

        # time
        self.time = 0

        # eated coins
        self.coins = 0

        # farts
        self.farts = 0

        # game state
        self.game_state = self.STATE_PAUSE

        # start level
        self.start_level = 0

        # last level
        self.last_level = 1

    def reset( self ):
        self.score = 0
        self.coins = 0
        self.farts = 0
        self.state = self.STATE_PAUSE

    def set_level( self, l ):
        self.level_idx = l
        self.coins = 0
        self.farts = 0
        self.time = self.level.time

state = State()