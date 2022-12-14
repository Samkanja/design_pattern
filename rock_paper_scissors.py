from dataclasses import dataclass
from typing import Optional
import random

OPTIONS = ['rock','paper','scissors']

@dataclass
class RockPaperScissors:
    human_choice : Optional[str] = None
    computer_choice : Optional[str] = None

    def get_human_choice(self) -> str:
        num = int(input('Enter Choice reference Number: '))
        self.human_choice = OPTIONS[num-1]
    
    def get_computer_choice(self) -> str:
        self.computer_choice = random.choice(OPTIONS)

    def display_options(self):
        print('\n'.join(f'{i} {option.title()}' for i, option in enumerate(OPTIONS)))