# Rock-Paper-Scissors Bot
This is a rock-paper-scissors game that lets you play rock-paper-scissors against a computer. The computer is hard to beat, and it's not because it cheats!
The reason why the computer is hard to beat is because it starts at rock. If the user wants to play again, and it loses, it goes back one in the order of rock, paper, scissors. So, it does scissors. If it wins, it goes foward one in the order, which is paper.
# The logic behind this strategy:
When an opponent loses, they are likely to switch to the sign that would have beaten the computer's previous throw. By moving to the next item in the sequence (e.g., if the computer won with rock, switch to paper), the computer counters their expected shift to scissors. When the computer loses (which won't happen much), it's opponent is likely to stay with the same winning move. To counter this, the computer will play the sign that beats it's last move.

Copyright (c) 2026 Elijah Corwin
