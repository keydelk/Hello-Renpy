# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define dwalin = Character("Dwalin", color="#876543")
define filia = Character("Filia", color="#BF40BF" )

# Defining the background with fixed dimensions
image bg cave = Transform("bg cave.jpg", size=(1920, 1080))
image bg tavern = Transform("bg tavern.jpg", size=(1920, 1080))

# Defining transform for Filia
transform floatright:
    xalign 0.66 yalign 0.5

transform floatleft:
    xalign 0.33 yalign 0.5

transform highmiddle:
    xalign 0.5 yalign 0.2

transform lowmiddle:
    xalign 0.5 yalign 0.7


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "Dungeon_Under_The_Castle.ogg"

    scene bg cave
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    pause 0.5

    show dwalin at right
    with easeinright

    # These display lines of dialogue.

    dwalin "Greetings lad!"

    dwalin "This here\'s the start of a new Renpy adventure"

    python:
        name = renpy.input("But first, what should I call you?")
        name = name.strip() or "stranger"

    dwalin "Nice to meet you [name]"

    dwalin "While we dwarves love exploring caves, you would probably be more comfortable elsewhere"
    dwalin "Lets head to a tavern for a drink"

label tavern:

    scene bg tavern
    with dissolve
    play music "Town_Country_Market.ogg"

    pause 0.3

    show dwalin at left
    with easeinleft

    dwalin "How's this? Better?"
    dwalin "I'd like you to meet a friend of mine. Say hi to Filia"

    show filia at floatright
    with easeintop

    filia "Hi, I'm Filia! You must be the [name] that Dwalin was telling me about!"
    filia "While I'm just a single sprite (pun intended), there's a lot I can do!"

label flyaround:
    show filia at highmiddle
    with move
    show filia at floatleft
    with move
    show filia at lowmiddle
    with move
    show filia at floatright
    with move

    filia "See, I can fly all around the screen!"

    filia "Want to see that again?"

menu:
    "Sure, that was cool!":
        jump flyaround

    "That was enough, let's move on.":
        jump effects

label effects:
    filia "I can also do other effect!"


    # This ends the game.

    return
