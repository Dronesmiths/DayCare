import os
import re
import subprocess

# Configuration
base_dir = "/Users/mediusa/NOVA/Repos/DayCare"
images_dir = os.path.join(base_dir, "images")
extensions_to_convert = (".png", ".jpg", ".jpeg")

# Mapping of original names to kebab-case
name_mapping = {
    "hero-home.png": "hero-home.webp",
    "backyard.png": "backyard.webp",
    "logo.webp": "logo.webp",
}

def convert_to_webp(src, dest):
    print(f"Converting {src} -> {dest}")
    # Check if src is already webp
    if src.endswith(".webp"):
        print(f"  Already webp, skipping conversion: {src}")
        return
    subprocess.run(["cwebp", "-q", "80", src, "-o", dest], check=True)

def update_references(old_name, new_name):
    print(f"Updating references: {old_name} -> {new_name}")
    # Escape special characters for regex
    escaped_old = re.escape(old_name)
    pattern = f"(?i){escaped_old}"
    
    for root, dirs, files in os.walk(base_dir):
        if ".git" in root or "factory" in root: continue
        for file in files:
            if file.endswith((".html", ".css", ".js")):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = re.sub(pattern, new_name, content)
                    
                    if content != new_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"  Updated {filepath}")
                except Exception as e:
                    print(f"  Error processing {filepath}: {e}")

def main():
    # Loop through all files in images_dir
    if not os.path.exists(images_dir):
        print(f"Directory not found: {images_dir}")
        return

    for filename in os.listdir(images_dir):
        if filename.endswith(extensions_to_convert):
            old_path = os.path.join(images_dir, filename)
            new_name = os.path.splitext(filename)[0] + ".webp"
            new_path = os.path.join(images_dir, new_name)
            
            convert_to_webp(old_path, new_path)
            update_references(filename, new_name)

if __name__ == "__main__":
    main()
