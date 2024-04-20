import requests, random, os, pyfiglet, ctypes, json as a

def l():
    try:
        with open('config.json', 'r') as b:
            c = a.load(b)
    except FileNotFoundError:
        c = {}
    return c

def s(c):
    with open('config.json', 'w') as b:
        if not c:
            c = {'exclude_flogs': True, 'exclude_strings': True, 'exclude_fflags': False, 'exclude_ints': False}
        a.dump(c, b, indent=4)

def f(d, e):
    f = requests.get(d)
    if f.status_code == 200:
        g = f.text.split('\n')
        h = []
        for i in g:
            if "[C++] SFFlag" in i or "[Lua] SFFlag" in i:
                continue
            if (e.get('exclude_flogs', True) and ("[C++] FLog" in i or "[C++] DFLog" in i or "[Lua] FLog" in i or "[Lua] DFLog" in i)) or (e.get('exclude_strings', True) and ("[C++] FString" in i or "[C++] DFString" in i or "[Lua] FString" in i or "[Lua] DFString" in i)) or (e.get('exclude_fflags', False) and ("[C++] FFlag" in i or "[C++] DFFlag" in i or "[Lua] FFlag" in i or "[Lua] DFFlag" in i)) or (e.get('exclude_ints', False) and ("[C++] FInt" in i or "[C++] DFInt" in i or "[Lua] FInt" in i or "[Lua] DFInt" in i)):
                continue
            h.append(i)
        return random.choice(h) if h else None
    else:
        print("Failed to fetch data from URL:", d)
        return None

def m():
    if not os.path.exists('config.json'):
        s({})
    e = l()
    d = "https://raw.githubusercontent.com/MaximumADHD/Roblox-Client-Tracker/roblox/FVariables.txt"
    i = pyfiglet.Figlet(font='big')
    ctypes.windll.kernel32.SetConsoleTitleW("Roblox FFlag Randomizer")
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1;31m")
        for j in i.renderText('FVariables Randomizer').split('\n'):
            print(j.center(80))
        print("\033[0m")
        if all(e.get(k, True) for k in ['exclude_flogs', 'exclude_strings', 'exclude_fflags', 'exclude_ints']):
            print("What did you expect?")
        else:
            k = f(d, e)
            if k:
                if '[Lua]' in k:
                    k = k.replace('[Lua]', '\033[38;2;58;0;131m[Lua]\033[0m')
                elif '[C++]' in k:
                    k = k.replace('[C++]', '\033[1;31m[C++]\033[0m')
                print(k)
            else:
                print("No item fetched.")
        input()

if __name__ == "__main__":
    m()
