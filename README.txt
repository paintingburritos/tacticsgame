# tacticsgame

Unit information
        |Team 1|Team 2|Health|Attack|Movement|Range|Cost|
  tank  |  T   |   t  |  12  |   6  |    1   |  2  | 35 |
  land  |  L   |   l  |  10  |   3  |    2   |  1  | 20 |
  range |  R   |   r  |   6  |   4  |    3   |  3  | 30 |

Tower information
  No team: $
  Team 1: #
  Team 2: @
  
  At the start of each a turn the player will recieve $5, plus $10 for every tower that is theirs at the start of their turn.
  
  Tower influcence:
    Towers will change at the start of each turn towards the team that has more troops directly next to it (not diagonal)
    for example:
          T
          $
     on the next turn this tower will become
          T
          #
     if this tower was influnced by the other team however
          T
         t#
          l
      on the next turn it would become this
          T
         t$
          l
      and on the turn after it would change into a team 2 tower
          T
         t@
          l

Flag info
  Each flag has a total of 10 health. If it loses all it's health the game ends and the player that destroyed the opposing teams
  flag wins
 
Command usages
  Attack:
    type "attack"
    prompted for x1 and y1, which are the cordinates of the unit you wish to attack with
    prompted for x2 and y2, which are the cordinates of the unit or object you wish to attack
  Move:
    type "move"
    prompted for x1 and y1, which are the cordinates of which unit you wish to move
    prompted for x2 and y2, which are the cordinates of where you wish to move to
  Info:
    type "info"
    prompted for x and y
    will print out info for that cell
  end:
    type "end"
    will end turn
  buy:
    type "buy"
    will open new shop interface where you can buy units and place them in your starting x (0 or 9) at a choosen y
  
