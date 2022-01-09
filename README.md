# war-tactics
We will be analyzing the very skill based game "War". Below you will learn how to simulate games of War and extract data for further exploration.

## setup

In order to run the similaor you need to do the following:

1. Clone the repo `git clone https://github.com/TomPed/war-tactics.git`
2. Create a virtual Python 3 environment `virtualenv -p python3 /path/to/environments/python/war`
3. Source your ennvironment `source /path/to/environments/python/war/bin/activate.fish`
4. `cd` to rood directory of repo
5. Install the cli `pip install .`

Soon this will be available via the `pip`.

## usage

In order to run the `war` command we need enter two numbers: the number of players in the game, and the number of simulations to run. If we want to simulate 4 games of 2 players we can run: `war 2 4`

4 games of 7 players: `war 7 4` ... and so on. 

## Data extraction

Note, this part is still in progress and more data will be added.

Right now if we run ` war 2 7` the following output is returned:
```
Game 1/7
player: 0 starts with value 173
player: 1 starts with value 139
player 1 wins

Game 2/7
player: 0 starts with value 124
player: 1 starts with value 188
player 0 wins

Game 3/7
player: 0 starts with value 174
player: 1 starts with value 138
player 1 wins

Game 4/7
player: 0 starts with value 146
player: 1 starts with value 166
player 0 wins

Game 5/7
player: 0 starts with value 174
player: 1 starts with value 138
player 1 wins

Game 6/7
player: 0 starts with value 153
player: 1 starts with value 159
player 1 wins

Game 7/7
player: 0 starts with value 151
player: 1 starts with value 161
player 1 wins

[192, 248, 1090, 180, 548, 144, 115]
```

We can see the starting value of each player, who one the round, and finally, a sum of the turns for each game. From the above we can reason that player 0 lost game 5 even though they started with a better deck, valued at 174. The value of a deck is taken by adding up the card numbers.

Mapping of card values:
- 2  -> `0`
- 3  -> `1`
- 4  -> `2`
- 5  -> `3`
- 6  -> `4`
- 7  -> `5`
- 8  -> `6`
- 9  -> `7`
- 10 -> `8`
- J  -> `9`
- Q  -> `10`
- K  -> `11`
- A  -> `12`
 
