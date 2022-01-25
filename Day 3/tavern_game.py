print('''
 ********************************************************************************
*                    /   \              /'\       _                              *
*\_..           /'.,/     \_         .,'   \     / \_                            *
*    \         /            \      _/       \_  /    \     _                     *
*     \__,.   /              \    /           \/.,   _|  _/ \                    *
*          \_/                \  /',.,''\      \_ \_/  \/    \                   *
*                           _  \/   /    ',../',.\    _/      \                  *
*             /           _/m\  \  /    |         \  /.,/'\   _\                 *
*           _/           /MMmm\  \_     |          \/      \_/  \                *
*          /      \     |MMMMmm|   \__   \          \_       \   \_              *
*                  \   /MMMMMMm|      \   \           \       \    \             *
*                   \  |MMMMMMmm\      \___            \_      \_   \            *
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *
*                    /'.,___________...,,'   \            \   \        \         *
*                   /       \          |      \    |__     \   \_       \        *
*                 _/        |           \      \_     \     \    \       \_      *
*                /                               \     \     \_   \        \     *
*                                                 \     \      \   \__      \    *
*                                                  \     \_     \     \      \   *
*                                                   |      \     \     \      \  *
*                                                    \ms          |            \ *
 ********************************************************************************
''')
print("\nWelcome to the tavern survival game, can you escape before it collapses?")
print("The origin path has collapsed, you either can go deeper into the tavern or dig through the side wall.")
print("1. Go deeper into the tavern")
print("2. Dig into the sidewall")
decision = int(input("What would you like to do? "))
if decision == 1:
    print("After some time, you arrive to a chasm. Your only options is walk along the edge wall or attempt to climb down")
    print("1. Walk along the edge of the chasm")
    print("2. Climb down")
    decision = int(input("What would you like to do? "))
    if decision == 1:
        print("You climb down the chasm and find yourself at a river, would you like to swim or walk along the river?")
        print("1. Swim")
        print("2. Walk")
        decision = int(input("What would you like to do? "))
        if decision == 1:
            print("You enter the river, and despite a rough ride, you make it to the lake outside the tavern.")
            print("Congratulations! You survived!")
        else:
            print("You've been walking for hours now, dehydrated and hungry you slip into a deep sleep")
            print("Game over!")
    else:
        print("As you walk along the edge, you lose your footing and fall off, rendering you immobile")
        print("Game over!")
else:
    print("After digging for some time you break through to an underground river, would you like to swim or turn back?")
    print("1. Swim")
    print("2. Turn back")
    decision = int(input("What would you like to do? "))
    if decision == 1:
        print("You enter the river, and despite a rough ride, you make it to the lake outside the tavern.")
        print("Congratulations! You survived!")
    else:
        print("You turn back only to find that the cave has collapsed, and the riverside has also just collapsed.")
        print("Game over!")