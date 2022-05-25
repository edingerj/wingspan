from enum import Enum


class TurnPhase(Enum):
    STARTING = 'STARTING'
    ENDING = 'ENDING'

    def get_continue_information_text(self: 'TurnPhase') -> str:
        if self is TurnPhase.STARTING:
            return 'Continue to your move phase'
        elif self is TurnPhase.ENDING:
            return 'End your turn'
