# Modifying Global Scope

enemies = 1


def increase_enemies(enemy):

#     global enemies
#     enemies += 1
    print(f"enemies inside function: {enemies}")
    return enemy+1

#     instead of this we dont usually modifies the global scope we can create a function with input to modifyes any things


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


