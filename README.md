# TortoiseAndHareGame
#implementation in python
# Implements stratergy design pattern

Problem to implement a game between tortoise and hare.

Imagine both animals at a tree and they want to reach a pond, which is 10 steps away from the tree. both animals start at same time. tortoise keep 1 step for 1 sec, while keeps 2 steps for 1sec. Now there is a random time [1-3]sec, a carrot will appear in hares path, In this case hare stops for 1 sec and then continue. Now design a game. Simple right í ½í¸Š

how to code: 
Use strategy design pattern [learn it its easy]
make animal class and inherit tortoise and hare class 
have variable and count number of steps done or number of steps remaing
generate a random number and pass to hare object.
and play the game.

Output [should look like]:
Hare Tortoise
2        1                 ----> generated random number which is 2 means at 2nd call hare should stop
2        2                 -------> hare stops [again generated which is 3 it means from here 3/ including this]
4        3
6        4
6        5                ---> again generate

Like this see who will win
