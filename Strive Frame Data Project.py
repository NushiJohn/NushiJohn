#Characteristics that make up a character
class GG_character:
    def __init__(character, name, defense, guts, prejump, backdash_length, backdash_invul, weight, extra_characteristic):
        character.name = name
        character.defense = defense
        character.guts = guts
        character.backdash_length = backdash_length
        character.backdash_invul = backdash_invul
        character.weight = weight
        character.prejump = prejump
        character.extra_characteristic = extra_characteristic

#Strings that list and state these character stats
def character_stats(GG_character):
    character_name_string = "Character: %s"
    print(character_name_string % GG_character.name)
    character_defense_string = "%s's defense value: %s"
    print(character_defense_string % (GG_character.name, GG_character.defense))
    character_guts_string = "%s's guts value: %s"
    print(character_guts_string % (GG_character.name, GG_character.guts))
    character_prejump_string = "%s's prejump frames: %s"
    print(character_prejump_string % (GG_character.name, GG_character.prejump))
    character_backdash_string = "%s's backdash length & invulnerability: %s length, %s invul"
    print(character_backdash_string % (GG_character.name, GG_character.backdash_length, GG_character.backdash_invul))
    character_weight_string = "%s's weight class: %s"
    print(character_weight_string % (GG_character.name, GG_character.weight))
    character_extra_characteristic_string = "%s's extra features + unique movement options: %s"
    print(character_extra_characteristic_string % (GG_character.name, GG_character.extra_characteristic))
          
print("All frame data, numbers, and info are thanks to the community at dustloop wiki, https://www.dustloop.com/wiki/index.php?title=Guilty_Gear_-Strive-")
print()
print("character_stats(*insert character*) will tell you the general stats and data about a given character.")

#Characters' data
sol_badguy = GG_character("Sol 'Frederick' Badguy", 0.98, 2, 4, 20, 5, "Normal", "None")
sol = Sol = Sol_Badguy = sol_badguy
character_stats_set = {sol_badguy}

ky_kiske = GG_character("Ky Kiske", 1.0, 2, 4, 20, 5, "Normal", "None")
ky = Ky = Ky_Kiske = ky_kiske
character_stats_set.add(ky_kiske)

may = GG_character("May", 1.06, 4, 4, 16, 4, "Light", "None")
May = may
character_stats_set.add(may)

chipp_zanuff = GG_character("Chipp Zanuff", 1.26, 4, 4, 20, 5, "Normal", "Triple jump & wall run")
chipp = Chipp = Chipp_Zanuff = Joe_Biden = Mr_President = chipp_zanuff
character_stats_set.add(chipp_zanuff)

millia_rage = GG_character("Millia Rage", 1.18, 2, 4, 16, 4, "Light", "Two air dashes + Kapel")
millia = Millia = Millia_Rage = millia_rage
character_stats_set.add(millia_rage)

nagoriyuki = GG_character("Nagoriyuki", 0.96, 4, 5, 23, 6, "Heavy", "Unique super jump (10 frames), Fukyo, dash-step, no airdash or double jump")
nago = Nago = Nagoriyuki = nagoriyuki
character_stats_set.add(nagoriyuki)

i_no = GG_character("I-no", 1.06, 1, 4, 20, 5, "Light", "Hover-dash")
ino = Ino = I_no = i_no
character_stats_set.add(i_no)

zato_1 = GG_character("Zato-1", 1.07, 0, 4, 20, 5, "Normal", "Flight, Eddie")
zato = Zato = Zato_1 = zato_1
character_stats_set.add(zato_1)

ramlethal_valentine = GG_character("Ramlethal Valentine", 1.06, 1, 4, 20, 5, "Light", "None")
ram = Ram = Ramlethal_Valentine = ramlethal = ramlethal_valentine
character_stats_set.add(ramlethal_valentine)

potemkin = GG_character("Potemkin", 0.93, 3, 5, 24, 6, "Heavy", "Cannot run nor airdash, hammerfall")
pot = Pot = Potemkin = potemkin
character_stats_set.add(potemkin)

axl_low = GG_character("Axl Low", 1.07, 1, 4, 20, 5, "Normal", "None")
axl = Axl = Axl_Low = axl_low
character_stats_set.add(axl_low)

faust = GG_character("Faust", 1.01, 0, 4, 20, 5, "Normal", "Scarecrow, crawl, floaty air-dash")
Faust = Dr_Baldman = faust
character_stats_set.add(faust)

leo_whitefang = GG_character("Leo Whitefang", 1.0, 3, 4, 20, 5, "Heavy", "Brynhildr Stance, step-dash during Brynhildr stance")
leo = Leo = Leo_Whitefang = leo_whitefang
character_stats_set.add(leo_whitefang)

anji_mito = GG_character("Anji Mito", 1.06, 5, 4, 20, 5, "Normal", "Issokutobi (Fuujin hop), Fuujin (spin, hold ok), Suigetsu No Hakobi (spin, hold ok)")
anji = Anji = Anji_Mito = anji_mito
character_stats_set.add(anji_mito)

giovanna = GG_character("Giovanna", 1.03, 1, 4, 20, 5, "Light", "Step-dash, meter stat boosts @ 50% & 100%")
Giovanna = gio = Gio = giovanna
character_stats_set.add(giovanna)

goldlewis_dickinson = GG_character("Goldlewis Dickinson", 0.96, 3, 5, 22, 6, "Heavy", "No double jump, security level")
goldlewis = Goldlewis = dickinson = Dickinson = Goldlewis_Dickinson = Burger_Sheriff = goldlewis_dickinson
character_stats_set.add(goldlewis_dickinson)


def all_character_stats(character_stats_set):
    for val in character_stats_set:
        character_stats()


#Next planned functions: General glossary (add a function to print the whole glossary at once as well), character tips and overviews,
#frame data + gatling charts, *stretch goal* attack simulations

class GG_term:
    def __init__(term, name, definition):
        term.name = name
        term.definition = definition

def define(GG_term):
    term_string = "%s:"
    print(term_string % GG_term.name)
    term_definition_string = "%s"
    print(term_definition_string % GG_term.definition)

bullshit = GG_term("Bullshit", "That is blazing")
what_am_i = GG_term("What am I?", "Just a small part of the world")
