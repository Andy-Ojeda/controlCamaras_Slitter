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



        # "MMMMMMMMMMMMMMWWNNNNNNNNNWMMMMMMMMMMMMMMMMMMMMMMMM",
        # "MMMMMMMMMMMMMMMMMMMWNNNWKo::::::::oKWNNNWMMMMMMMMMMMMMMMMMMM",
        # "MMMMMMMMMMMMMMMMMWXk:;cdkxxxxxxxxxkOkc;:kXWMMMMMMMMMMMMMMMMM",
        # "MMMMMMMMMMMMMMMMWx;;coxkO0000000000KK0Oxl;xWMMMMMMMMMMMMMMMM",
        # "MMMMMMMMMMMMMMWX0l;ldk00000000000000XWWWOcoKNMMMMMMMMMMMMMMM",
        # "MMMMMMMMMMMMMMNo,coddk00000000000000KXNWXOx:oNMMMMMMMMMMMMMM",
        # "MMMMMMMMMMMMMXk:,ldddk0000000000000000KXK0kcckXMMMMMMMMMMMMM",
        # "MMMMMMMMMMMMWo.;oddddk000000000000000000000Oc.oWMMMMMMMMMMMM",
        # "MMMMMMMMMMMMWo.,looddk0000000000000000000OOkc.oWMMMMMMMMMMMM",
        # "MMMMMMMMMMMMWo.':coddk0000000000000000000Oxd;.oWMMMMMMMMMMMM",
        # "MMMMMMMMMMMMWo.':colcdO000000000000000koxkxd;.oWMMMMMMMMMMMM",
        # "MMMMMMMMMMMWXl.':;;. 'clllldO00Odllllc'.'cod;.cXWMMMMMMMMMMM",
        # "MMMMMMMMMWKkl,.';,..      .;k00k;.      ..:l,.,lkKWMMMMMMMMM",
        # "MMMMMMMMMX:.coc..,':l'  .llok00Oool.  'l:,c,'coc.:XMMMMMMMMM",
        # "MMMMMMMMMK;.;:'..ldOKo''l0OxO000OK0l''oK0kx,.'::.;KMMMMMMMMM",
        # "MMMMMMMMMNo;;:;..lxOOkkkO0kxOKKKKK0OkkO000k,.;:;;oXMMMMMMMMM",
        # "MMMMMMMMMMWKoc:..,cdkO000OdodkOOOO00000Oxl:..:cdKWMMMMMMMMMM",
        # "MMMMMMMMMMMMMKd'   ,dk0OOk:......ckO00Ok;   ,dKWMMMMMMMMMMMM",
        # "MMMMMMMMMMMMMMWKx; .'lkd;..      ..;dko,. ;xKWMMMMMMMMMMMMMM",
        # "MMMMMMMMMMMMMMMMWo   .'...,::::::;...'..  lWMMMMMMMMMMMMMMMM",
        # "MMMMMMMMMMMMMKxdo,      .cdl;'';ldc.      ,odxKMMMMMMMMMMMMM",
        # "MMMMMMMMMMMXd'           ...    ...           'dXMMMMMMMMMMM",
        # "MMMMMMMMWXd,. ..      ..            ..      .. .,dXWMMMMMMMM",
        # "MMMMMMMNd,......     .,;''.      .',;;.     ......,dNMMMMMMM",
        # "MMMMMMMX;   ....     .coc;,,;::;,,:oxd.     ....   ;XMMMMMMM",
        # "MMMMMMW0;   .....    .cdoc:ldxxxlclk0x'    .....   ;0WMMMMMM",
        # "MNK000d,.     ....   .;cllldkOOOxddddl.   ....     .,x000KNM",
        # "0l........       ...   .:ddx00K0Okkc..  ..        ........l0",
        # ".   .......          ...:d0NNNWNXOx:...          .......   .",
        # "   ...........        ....oXNNNXOc....        ...........   ",
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


    time.sleep(1)
    os.system('cls')

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
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

    
    # Cierra consola
    # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


    return archivo_json




