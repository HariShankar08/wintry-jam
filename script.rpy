# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.


define r = Character("Ryan")

label start:
    call prologue

    call am9

    return

label prologue:
    "It’s been a while since I had a dream like that."

    "Okay, no - it’s been a really long time.{w=0.17} Long enough for me to laugh at it now.{p=1}You know what, I’ll even tell you about it."

    "It was Christmas Eve, and I was sleeping in."

    "Usually when this kind of thing happens, Dad pulls me out of bed and I run around the neighbourhood with him.{w=0.12} I'm forced to."
    
    "It’s never fun, especially on the weekends."

    "Well, this time, none of that happened.{w=0.25} At least, in the dream.{p=0.5}In the dream I was woken up by Ryan, my boyfriend."

    r "Rise and shine, {w=0.5}{i}dumbass{/i}."

    "Yeah, no way in hell that’s really happening.{fast}{p=0.4}First off, that’s not the way he talks."

    "Second{w=0.25} - and more importantly{w=0.25} -  there’s no way Dad would let a {i}boy{/i}{w=0.15} into my room."

    "Mom wouldn’t allow it, either.{p=0.5}Hell, {b}I wouldn’t allow it.{/b}"

    "Mom woke me up today, by the by.{w=0.5} Something about getting out of bed before Dad got back from his walk." 
    
    "Looks like they’d been fighting last night, maybe."

    "The rest of that dream{w=0.5} - well, I don’t think I’ll go into details. 
    {p=0.3}Mom said my ears looked pretty red, or something." 
    
    "And anyway{fast}{w=0.6}, you’d find more entertaining stuff along that vein on Wattpad{w=0.24} or AO3."

    return

label am9:
    return
