import os
import re

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace common patterns I used with the actual filenames
    replacements = {
        "service_infant_care": "service-infant-care",
        "service_toddler_active_play": "service-toddler-care", # Correcting my made-up name
        "service_toddler_care": "service-toddler-care",
        "service_preschool_learning": "service-preschool",
        "service_preschool": "service-preschool",
        "service_after_school_homework": "service-after-school",
        "service_after_school": "service-after-school",
        "service_night_weekend_care": "service-night-weekend",
        "service_night_weekend": "service-night-weekend",
        "service_summer_camp_outdoor": "service-summer-camp",
        "service_summer_camp": "service-summer-camp"
    }
    
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
    
    if content != new_content:
        print(f"Updating image paths in {path}")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)

def run_mass_fix(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    run_mass_fix("/Users/mediusa/NOVA/Repos/DayCare")
