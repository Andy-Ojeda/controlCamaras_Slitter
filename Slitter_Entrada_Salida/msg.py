import time
import ctypes
import os

def imprimir_mensaje():


    os.system('cls')

    print("                     _                         ")
    print("                    |_)o _ ._    _ ._ o _| _   ")
    print("                    |_)|(/_| |\/(/_| ||(_|(_)  ")
    print("                                               ")
    print("                                  ")
    print("                               _. ")
    print("                              (_| ")
    print("                                  ")
    print("                                  ")
    print("                    _____ ___ __  __           ")
    print("                   / ___// (_) /_/ /____  _____")
    print("                   \__ \/ / / __/ __/ _ \/ ___/")
    print("          /\/|    ___/ / / / /_/ /_/  __/ /       /\/|")
    print("          |/\/   /____/_/_/\__/\__/\___/_/        |/\/")
                              
 
    time.sleep(1)

    
    print("")
    print("")
    print("")  
    print("                             |_    ")
    print("                             |_)\/ ")
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







    archivo = input("Entrada o Salida? Escribe 'e' o 's': "+ "\n\n")

    # Determinar el nombre del archivo basado en la elección
    if archivo == 'e':
        archivo_json = 'in'
    elif archivo == 's':
        archivo_json = 'out'
    else:
        print("Selección no válida. Cargando Entrada por defecto.")
        archivo_json = 'in'


    time.sleep(2)
    os.system('cls')

    if archivo_json == 'in':
        print("")
        print("")
        
        print(" ______       _                 _       ")
        print("|  ____|     | |               | |      ")
        print("| |__   _ __ | |_ _ __ __ _  __| | __ _ ")
        print("|  __| | '_ \| __| '__/ _` |/ _` |/ _` |")
        print("| |____| | | | |_| | | (_| | (_| | (_| |")
        print("|______|_| |_|\__|_|  \__,_|\__,_|\__,_|")
                                        
        print("")
        print("")
                              
        
    if archivo_json == "out":
        print("")
        print("")
                  
        print("  _____       _ _     _       ")
        print(" / ____|     | (_)   | |      ")
        print("| (___   __ _| |_  __| | __ _ ")
        print(" \___ \ / _` | | |/ _` |/ _` |")
        print(" ____) | (_| | | | (_| | (_| |")
        print("|_____/ \__,_|_|_|\__,_|\__,_|")
                              
        print("")
        print("")
                                        
    time.sleep(1)
                         





    # # Minimizar la consola
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

    
    # Cierra consola
    # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


    return archivo_json




