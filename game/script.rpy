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

    dwalin "While we dwarves love exploring caves, you would probably be more comfortable elsewhere"
    dwalin "Lets head to a tavern for a drink"

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

    filia "It's nice to meet you!"

    # This ends the game.

    return
