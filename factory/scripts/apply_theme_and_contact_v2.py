import os
import re

# New Business Data
NEW_PHONE = "(818) 966-4875"
RAW_PHONE = "8189664875"
NEW_ADDRESS = "39300 Kennedy Drive, Palmdale, CA 93551"
FACILITY_NUMBER = "197701048"

# Theme Colors (Rainbow Magical Palette)
COLORS = {
    "--p": "#FFD93D",       # Magic Yellow
    "--p-pink": "#FF6B6B",  # Storybook Pink
    "--p-blue": "#2E91D3",  # Sky Blue
    "--p-orange": "#FF9F43",# Sunrise Orange
    "--p-green": "#8BC34A", # Meadow Green
    "--d": "#00457C",       # Dark Blue
    "--l": "#FFFDF7",       # Light Cream
}

# CSS for the Multi-colored Logo
LOGO_CSS = """
        .logo { font-family: var(--f-h); font-weight: 400; }
        .logo .l-1 { color: #2E91D3; } /* F */
        .logo .l-2 { color: #FF9F43; } /* a */
        .logo .l-3 { color: #8BC34A; } /* i */
        .logo .l-4 { color: #FFD93D; } /* r */
        .logo .l-5 { color: #FF6B6B; } /* y */
        .logo .l-space { margin-right: 5px; }
        .logo .l-6 { color: #FF9F43; } /* T */
        .logo .l-7 { color: #2E91D3; } /* a */
        .logo .l-8 { color: #FF6B6B; } /* l */
        .logo .l-9 { color: #FFD93D; } /* e */
        .logo span.cc { color: var(--p-pink); margin-left: 8px; font-weight: 700; font-family: var(--s); font-size: 0.9em; }
"""

LOGO_HTML = """<a href="/" class="logo" aria-label="Fairy Tale Child Care Home"><span class="l-1">F</span><span class="l-2">a</span><span class="l-3">i</span><span class="l-4">r</span><span class="l-5">y</span><span class="l-space"></span><span class="l-6">T</span><span class="l-7">a</span><span class="l-8">l</span><span class="l-9">e</span> <span class="cc">Child Care</span></a>"""

def update_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Basic Replacements
    content = content.replace("661-XXX-XXXX", NEW_PHONE)
    content = content.replace("6614984444", RAW_PHONE)
    content = content.replace("661.498.4444", NEW_PHONE)
    content = content.replace("Palmdale, CA (Residential Setting)", NEW_ADDRESS)
    content = content.replace("Fairy Tale <span>Child Care</span>", LOGO_HTML)
    content = content.replace('logo" aria-label="Fairy Tale Child Care Home">Fairy Tale <span>Child Care</span>', 'logo" aria-label="Fairy Tale Child Care Home">' + LOGO_HTML)

    # 2. CSS Variables
    for var, val in COLORS.items():
        content = re.sub(rf'{var}:\s*#[^;}}]+', f'{var}: {val}', content)

    # 3. Inject Logo CSS if missing
    if ".logo .l-1" not in content and "</style>" in content:
        content = content.replace("</style>", LOGO_CSS + "\n    </style>")

    # 4. Facility Number
    if FACILITY_NUMBER not in content and "footer" in content.lower():
        license_html = f'<p style="opacity:0.6; font-size:0.8rem; margin-top:10px;">Facility Number: {FACILITY_NUMBER}</p>'
        content = re.sub(r'(&copy; 2026 Fairy Tale Child Care. All rights reserved.</p>)', r'\1' + license_html, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    directory = "/Users/mediusa/NOVA/Repos/DayCare"
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                update_html_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
