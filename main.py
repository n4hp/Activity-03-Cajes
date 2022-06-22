import Cajes_script_1_stat as statsc 
import Cajes_script_2_ev as evsc

def option_menu():
    opt = int(input("Press 1 to compute again Press 2 to exit. "))
    if opt ==1:
        main()
    elif opt ==2:
        exit()
    else:   
        option_menu()

def main():
    base = int(input("Base: "))
    trap = 1
    while trap == 1:
        iv = int(input("Individual Value: "))
        if iv >= 0 or iv<=31:
            trap=0
        
    
    ctr = 1

    while ctr == 1:
        ev = int(input("Effort Values: "))
        if ev >= 0 or ev <= 255:
            ctr=0

    

    Level = int(input(" Input Level: "))
    nature_input = int(input("1. beneficial or 2. Hindering:" ))
    if nature_input==1:
        nature = 1.1
    else:
        nature=0.9

    select = int(input("1. Stat or 2. EV: "))
    if select ==1:
        hp = statsc.pokestats.statHP(base,iv,ev,Level)
        otherstat =statsc.pokestats.statOtherStat(base,iv,ev,Level,nature)
        print("HP: ", hp)
        print("Other stats: ", otherstat)
        option_menu();

    elif select==2:
        stats = int(input("Stats: "))
        d= evsc.pokeev.statD(base,iv,ev,Level)
        print("Desired Stat Increase: ", d)
        evs = evsc.pokeev.statEvs(stats,nature,d,Level)
        print("Evs Need: ", evs,'\n')
        option_menu()

    else:
        print("Wrong Input!: ")
main()
