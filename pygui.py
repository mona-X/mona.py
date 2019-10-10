import pyautogui as p
import time

time.sleep(20)

p.hotkey("winleft","r")

p.typewrite("notepad" )

p.hotkey("enter")

mywords = """

Hello My friend,
    my name is john, This PC is mine.
    i live in here as the soul of this computer.
    i also want you to come to this place.

    I am coming for you.......
    i want your soul and i want you to be dead..
    We are going to have so much fun today...
    you have only 5 sec to run.......
     
 """

p.typewrite(mywords, 0.05)

mywords = """
1
2
3
4
5

"""
p.typewrite(mywords, 1)

mywords = """
                             ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      \
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \\`\ |  |  | /,//' \,'  \
            /   /     ||--+--|--+-/-|     \   \
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'

"""

p.typewrite(mywords)
