import time
import ctypes
import os

def imprimir_mensaje():


    # os.system('cls')  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11

    print("                     _                         ")
    print("                    |_)o _ ._    _ ._ o _| _   ")
    print("                    |_)|(/_| |\\/(/_| ||(_|(_)  ")
    print("                                               ")
    print("                                  ")
    print("                               _. ")
    print("                              (_| ")
    print("                                  ")
    print("                                  ")
    print("                    _____ ___ __  __           ")
    print("                   / ___// (_) /_/ /____  _____")
    print("                   \\__ \\/ / / __/ __/ _ \\/ ___/")
    print("          /\\/|    ___/ / / / /_/ /_/  __/ /       /\\/|")
    print("          |/\\/   /____/_/_/\\__/\\__/\\___/_/        |/\\/")
                              
 
    time.sleep(1)

    
    print("")
    print("")
    print("")  
    print("                             |_    ")
    print("                             |_)\\/ ")
    print("                                /  ")

    print("")
    print("")


    print("                              _         ____  ")
    print("              /\\             | |       / __ \\ ")
    print("             /  \\   _ __   __| |_   _ | |  | |")
    print("            / /\\ \\ | '_ \\ / _` | | | || |  | |")
    print("           / ____ \\| | | | (_| | |_| || |__| |")
    print("          /_/    \\_\\_| |_|\\__,_|\\__, (_)____/ ")
    print("                                 __/ |        ")
    print("                                |___/         ")

    print("")

    time.sleep(1)


    lines = [
        "     MMMMMMMMMMMMMMMMMMMMNK000000KNMMMMMMMMMMMMMMMMMMMM",
        "     MMMMMMMMMMMMMMMW0kO0klcccccclkKOk0WMMMMMMMMMMMMMMM",
        "     MMMMMMMMMMMMMW0o:;cdOO00000000Ooclo0WMMMMMMMMMMMMM",
        "     MMMMMMMMMMMMWXo,lxO0000000000KXWWOcoXWMMMMMMMMMMMM",
        "     MMMMMMMMMMMMO:codxO00000000000KNWNOdlOMMMMMMMMMMMM",
        "     MMMMMMMMMMNOc:lddxO0000000000000KK0kllONMMMMMMMMMM",
        "     MMMMMMMMMMX;'ldddxO00000000000000000k,;XMMMMMMMMMM",
        "     MMMMMMMMMMX;.:lodxO000000000000000Okd';XMMMMMMMMMM",
        "     MMMMMMMMMMX;.;clldO000000000000Okkkxo';XMMMMMMMMMM",
        "     MMMMMMMMMW0,.;:,..:lllok00kolllc'.:oo',0WMMMMMMMMM",
        "     MMMMMMMW0dc;','...   .,d00d,.   ...;:,;ld0WMMMMMMM",
        "     MMMMMMMNc.cl'.;:dl..:xdk00kxx: .lxcc,'lc.cNMMMMMMM",
        "     MMMMMMMNo':;..lk0kolk0kk0000KxloOK0x'.;:'lNMMMMMMM",
        "     MMMMMMMMXkl:'.;oxO000kdxOOO0O0000Oxc.':lkXWMMMMMMM",
        "     MMMMMMMMMWNO:. .:xOOOo,....,oOO0Ol. .:ONMMMMMMMMMM",
        "     MMMMMMMMMMMMNO; .;ol'..    ..'ld:. ;ONMMMMMMMMMMMM",
        "     MMMMMMMMMMMWNXc   ...:c:;;:c:. ..  lXNWMMMMMMMMMMM",
        "     MMMMMMMMMNOc,,.     .;,....,;.     .,,cONMMMMMMMMM",
        "     MMMMMMMWO:. ..    .            .       .:OWMMMMMMM",
        "     MMMMMM0c.....     ','..    ..';,     .....c0MMMMMM",
        "     MMMMMMk.  ...    .;oc;,::::;;lxl.    ...  .kMMMMMM",
        "     MMMMWKc.   ...   .:dolldkkxooxOo.   ...   .cKWMMMM",
        "     Xxccc,..     ...  .,clok0OOxdl;.  ...     ..,cccxX",
        "     ;. ......       .  .:x0XNXX0kc.  .       ...... .;",
        "     ........       ...:0NNNXx;...       ........   ",
        "",
        "",
        ""]

    for line in lines:
        print(line)
        time.sleep(0.01)







    archivo = input("¿Torcha1 o Torcha2? Escribe '1' o '2': "+ "\n\n")

    # Determinar el nombre del archivo basado en la elección
    if archivo == '1':
        archivo_json = 'T1'
    elif archivo == '2':
        archivo_json = 'T2'
    else:
        print("Selección no válida. Cargando Torcha1 por defecto.")
        archivo_json = 'T1'


    time.sleep(2)
    os.system('cls')  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11

    if archivo_json == 'T1':
        print("")
        print("")
        print("           _______             _             __ ")
        print("          |__   __|           | |           /_ |")
        print("             | | ___  _ __ ___| |__   __ _   | |")
        print("             | |/ _ \| '__/ __| '_ \ / _` |  | |")
        print("             | | (_) | | | (__| | | | (_| |  | |")
        print("             |_|\___/|_|  \___|_| |_|\__,_|  |_|")
        print("")
        print("")
        
    if archivo_json == "T2":
        print("")
        print("")
        print("           _______             _             ___  ")
        print("          |__   __|           | |           |__ \ ")
        print("             | | ___  _ __ ___| |__   __ _     ) |")
        print("             | |/ _ \| '__/ __| '_ \ / _` |   / / ")
        print("             | | (_) | | | (__| | | | (_| |  / /_ ")
        print("             |_|\___/|_|  \___|_| |_|\__,_| |____|")
        print("")
        print("")
        
                                        
    time.sleep(1)
                         





    # # Minimizar la consola
    #!!!!!!!!! ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

    
    # Cierra consola
    # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


    return archivo_json




