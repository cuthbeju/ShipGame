# Author: Juliet Cuthbert
# GitHub username: cuthbeju
# Date: 03/08/2022
# Description: The ShipGame (BattleShip)


class ShipGame:

    """
    Represents a game of Battleship, played by two players. Each player has their own 10x10 grid they place their ships
    on. On their turn, they can fire a torpedo at a square on the enemy's grid. Player 'first' gets the first turn to
    fire a torpedo, after which players alternate firing torpedoes. A ship is sunk when all of its squares have been
    hit. When a player sinks their opponent's final ship, they win.
    """

    def __init__(self):

        """
        Takes no parameters.
        Initializes two 10x10 grids for each player to place their
        ships on.
        Initializes a ships_first list to track the ships for the first player.
        Initializes a ships_second list to track the ships for the second player.
        Initializes a turn variable to track the players’ turns.
        Initializes a current_status variable to track the current status of the game.
        """

        self._grid_first = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self._grid_second = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self._ships_first = []
        self._ships_second = []
        self._turn = 0
        self._game_state = 'UNFINISHED'


    def place_ship(self, player_num, ship_length, coordinates, ship_orientation):

        """
        Takes four parameters -
        player_num: the player (either 'first' or 'second')
        ship_length: the length of the ship
        coordinates: the coordinates of the square it will occupy that is closest to A1
        ship_orientation: the ship's orientation - either 'R' if its squares occupy the same row, or 'C' if its squares
        occupy the same column.
        Returns False and ship is not added if a ship would not fit entirely on the relative player’s grid.
        Returns False and ship is not added if a ship would overlap any previously placed ships on the relative
        player’s grid.
        Returns False and ship is not added if the length of the ship is less than 2.
        Returns True otherwise and adds ship to relative player’s grid.
        """

        if ship_length < 2:
            return False

        x = coordinates[0]
        y = (int(coordinates[1]))-1
        if x == 'A':
            x = 0
        if x == 'B':
            x = 1
        if x == 'C':
            x = 2
        if x == 'D':
            x = 3
        if x == 'E':
            x = 4
        if x == 'F':
            x = 5
        if x == 'G':
            x = 6
        if x == 'H':
            x = 7
        if x == 'I':
            x = 8
        if x == 'J':
            x = 9

        if player_num == 'first':

            if ship_orientation == 'R':
                # check if ship would fit on player's grid
                if y + (ship_length - 1) > 9:
                    return False
                # check for overlap on previously placed ships
                for num in range(0, ship_length):
                    if self._grid_first[x][y+num] == 'X':
                        return False
                # place ship on player's grid
                for num in range(0, ship_length):
                    self._grid_first[x][y+num] = 'X'
                # add ship to player's ship tracker
                self._ships_first.append([ship_length, coordinates, ship_orientation])
                return True

            if ship_orientation == 'C':
                # check if ship would fit on player's grid
                if x + (ship_length - 1) > 9:
                    return False
                # check for overlap on previously placed ships
                for num in range(0, ship_length):
                    if self._grid_first[x+num][y] == 'X':
                        return False
                # place ship on player's grid
                for num in range(0, ship_length):
                    self._grid_first[x + num][y] = 'X'
                # add ship to player's ship count
                self._ships_first.append([ship_length, coordinates, ship_orientation])
                #print(self._grid_first)
                return True

        if player_num == 'second':

            if ship_orientation == 'R':
                # check if ship would fit on player's grid
                if y + (ship_length - 1) > 9:
                    return False
                # check for overlap on previously placed ships
                for num in range(0, ship_length):
                    if self._grid_second[x][y + num] == 'X':
                        return False
                # place ship on player's grid
                for num in range(0, ship_length):
                    self._grid_second[x][y + num] = 'X'
                # add ship to player's ship tracker
                self._ships_second.append([ship_length, coordinates, ship_orientation])
                #print(self._grid_second)
                return True

            if ship_orientation == 'C':
                # check if ship would fit on player's grid
                if x + (ship_length - 1) > 9:
                    return False
                # check for overlap on previously placed ships
                for num in range(0, ship_length):
                    if self._grid_second[x + num][y] == 'X':
                        return False
                # place ship on player's grid
                for num in range(0, ship_length):
                    self._grid_second[x + num][y] = 'X'
                # add ship to player's ship tracker
                self._ships_second.append([ship_length, coordinates, ship_orientation])
                #print(self._grid_second)
                return True

    def get_current_state(self):

        """
        Takes no parameters.
        Returns the state of the game: either ‘FIRST_WON’, ‘SECOND_WON’, or ‘UNFINISHED’.
        """

        return self._game_state

    def fire_torpedo(self, player_num, target_coordinates):

        """
        Takes two parameters -
        player_num: the player firing the torpedo (either 'first' or 'second')
        target_coordinates: the coordinates of the target square, e.g. 'B7'
        Returns False if it’s not the relative player's turn.
        Returns False if the game has already been won.
        Returns True otherwise, records the move, updates whose turn it is, and updates the current state of the game.
        """

        if player_num == 'first' and self._turn % 2 != 0:
            return False
        if player_num == 'second' and self._turn % 2 == 0:
            return False
        if self._game_state != 'UNFINISHED':
            return False

        x = target_coordinates[0]
        y = (int(target_coordinates[1])) - 1
        if x == 'A':
            x = 0
        if x == 'B':
            x = 1
        if x == 'C':
            x = 2
        if x == 'D':
            x = 3
        if x == 'E':
            x = 4
        if x == 'F':
            x = 5
        if x == 'G':
            x = 6
        if x == 'H':
            x = 7
        if x == 'I':
            x = 8
        if x == 'J':
            x = 9

        if player_num == 'first':
            if self._grid_second[x][y] == 0 or self._grid_second[x][y] == 'S':
                self._turn += 1
                return True
            if self._grid_second[x][y] == 'X':
                self._grid_second[x][y] = 'S'
                #print(self._grid_second)
                self._turn += 1
                self.check_ships('second', self._ships_second)

        if player_num == 'second':
            if self._grid_first[x][y] == 0 or self._grid_first[x][y] == 'S':
                self._turn += 1
                return True
            if self._grid_first[x][y] == 'X':
                self._grid_first[x][y] = 'S'
                #print(self._grid_first)
                self._turn += 1
                self.check_ships('first', self._ships_first)


    def check_ships(self, player_num, player_ships):

        """
        Takes two parameters -
        player_num: the player whose ships are being checked ('first' or 'second')
        player_ships: the list of ships a player has
        Checks if any of player's ships has sunk and updates the state of the game.
        [ship_length, coordinates, ship_orientation]
        """
        for ship in range(0, len(player_ships)):

            ship_length = player_ships[ship][0]
            ship_orientation = player_ships[ship][2]
            coordinates = player_ships[ship][1]
            x = coordinates[0]
            y = (int(coordinates[1])) - 1
            if x == 'A':
                x = 0
            if x == 'B':
                x = 1
            if x == 'C':
                x = 2
            if x == 'D':
                x = 3
            if x == 'E':
                x = 4
            if x == 'F':
                x = 5
            if x == 'G':
                x = 6
            if x == 'H':
                x = 7
            if x == 'I':
                x = 8
            if x == 'J':
                x = 9

            if player_num == 'second':

                if ship_orientation == 'R':
                    # check how many pieces of ship have sunk
                    count = 0
                    for num in range(0, ship_length):
                        if self._grid_second[x][y + num] == 'S':
                            count += 1
                    # check if all of ship is sunk
                    if count == ship_length:
                        sunken_ship = player_ships[ship]
                        player_ships.remove(sunken_ship)
                    # check if game is won and update game status
                    if len(player_ships) == 0:
                        self._game_state = 'FIRST_WON'
                    return True

                if ship_orientation == 'C':
                    # check how many pieces of ship have sunk
                    count = 0
                    for num in range(0, ship_length):
                        if self._grid_second[x+num][y] == 'S':
                            count += 1
                    # check if all of ship is sunk
                    if count == ship_length:
                        sunken_ship = player_ships[ship]
                        player_ships.remove(sunken_ship)
                        # check if game is won and update game status
                    if len(player_ships) == 0:
                        self._game_state = 'FIRST_WON'
                    return True


            if player_num == 'first':

                if ship_orientation == 'R':
                    # check how many pieces of ship have sunk
                    count = 0
                    for num in range(0, ship_length):
                        if self._grid_first[x][y + num] == 'S':
                            count += 1
                    # check if all of ship is sunk
                    if count == ship_length:
                        sunken_ship = player_ships[ship]
                        player_ships.remove(sunken_ship)
                    # check if game is won and update game status
                    if len(player_ships) == 0:
                        self._game_state = 'SECOND_WON'
                    return True

                if ship_orientation == 'C':
                    # check how many pieces of ship have sunk
                    count = 0
                    for num in range(0, ship_length):
                        if self._grid_first[x + num][y] == 'S':
                            count += 1
                    # check if all of ship is sunk
                    if count == ship_length:
                        sunken_ship = player_ships[ship]
                        player_ships.remove(sunken_ship)
                        # check if game is won and update game status
                    if len(player_ships) == 0:
                        self._game_state = 'SECOND_WON'
                    return True


    def get_num_ships_remaining(self, player_num):

        """
        Takes one parameter -
        player_num: the player (either ‘first’ or 'second’)
        Returns how many ships the specified player has left.
        """

        if player_num == 'first':
            ship_count_first = len(self._ships_first)
            return ship_count_first
        if player_num == 'second':
            ship_count_second = len(self._ships_second)
            return ship_count_second


#game = ShipGame()
#game.place_ship('first', 3, 'A1', 'R')
#game.place_ship('second', 3, 'C3', 'R')
#game.place_ship('first', 2, 'E5', 'C')
#game.fire_torpedo('first', 'A1')
#game.fire_torpedo('second', 'A1')
#print(game.get_current_state())
#print(game.get_num_ships_remaining('first'))
#print(game.get_num_ships_remaining('second'))
#game.fire_torpedo('first', 'A2')
#game.fire_torpedo('second', 'A2')
#print(game.get_current_state())
#game.fire_torpedo('first', 'A3')
#game.fire_torpedo('second', 'A3')
#print(game.get_num_ships_remaining('first'))
#print(game.get_num_ships_remaining('second'))
#print(game.get_current_state())
#game.fire_torpedo('first', 'E3')
#game.fire_torpedo('second', 'E5')
#print(game.get_num_ships_remaining('first'))
#print(game.get_num_ships_remaining('second'))
#print(game.get_current_state())
#game.fire_torpedo('first', 'E3')
#game.fire_torpedo('second', 'F5')
##print(game.get_num_ships_remaining('first'))
#print(game.get_num_ships_remaining('second'))
#print(game.get_current_state())
