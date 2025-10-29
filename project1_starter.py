"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Aidan Miles 
Date: 10-22-2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
import os   
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
     # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    
    character_creation={"name": name,"class": character_class,"level":1,"strength":5,"magic":15,"health":80,"gold":100}
    
    return character_creation

def calculate_stats(character_class, level):
   
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)

    if character_class == "Warrior":
        strength = 20 + (level*6)
        magic = 5 + (level*2)
        health = 40 + (level*5)
    elif character_class == "Mage":
        strength = 5 + (level*2)
        magic = 40 + (level*3)
        health = 20 + (level*3)
    elif character_class == "Rogue":
        strength = 10 + (level*4)
        magic = 15 + (level*3)
        health = 30 + (level*4)
    elif character_class == "Cleric":
        strength = 30 + (level*3)
        magic = 40 + (level*3)
        health = 60 + (level*4)

    else:
        return (0,0,0)

    return (strength,magic,health)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    if character == {} or filename == "":
        return False

    file = open(filename,"w")
    file.write(f"Character Name:{character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()
    return True


    # TODO: Implement this function
    # Remember to handle file errors gracefully


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    if not os.path.exists(filename):   
        return None
        
    character={}
    file=open(filename,"r")
    #needed ai assitance with the key,value part of the for loop
    for line in file:
        key,value = line.strip().split(":") 
        character[key] = value.strip() 
    
    file.close()
    return character



    # TODO: Implement this function
    # Remember to handle file not found errors
    

def display_character(character):
    print("=== CHARACTER SHEET ===")
    
    
    
    
    
    
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    print(create_character("Aria","Mage"))
    print(calculate_stats("Warrior",5))
    print(calculate_stats("Mage",5))
    print(calculate_stats("Rogue",5))
    print(calculate_stats("Cleric",5))
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
