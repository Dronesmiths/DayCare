import os
import re

domain = "https://fairytalechildcare.com"

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Keep canonical and OG:URL as full absolute domain
    new_content = re.sub(r'<link rel="canonical" href="/', f'<link rel="canonical" href="{domain}/', content)
    new_content = re.sub(r'<meta property="og:url" content="/', f'<meta property="og:url" content="{domain}/', new_content)

    # 2. Revert Assets (images, css, js) to root-relative / for dual-environment compatibility
    # This replaces https://fairytalechildcare.com/xyz with /xyz for assets
    new_content = re.sub(rf'src="{domain}/', 'src="/', new_content)
    new_content = re.sub(rf'href="{domain}/css/', 'href="/css/', new_content)
    new_content = re.sub(rf'src="{domain}/js/', 'src="/js/', new_content)
    # Also for OG image if it was absolute
    new_content = re.sub(rf'content="{domain}/images/', 'content="/images/', new_content)
    
    # 3. Nav Links: Use root-relative / for better local testing
    new_content = re.sub(rf'href="{domain}/"', 'href="/"', new_content)
    new_content = re.sub(rf'href="{domain}/services/"', 'href="/services/"', new_content)
    new_content = re.sub(rf'href="{domain}/about/"', 'href="/about/"', new_content)
    new_content = re.sub(rf'href="{domain}/contact/"', 'href="/contact/"', new_content)
    new_content = re.sub(rf'href="{domain}/blog/"', 'href="/blog/"', new_content)
    
    if content != new_content:
        print(f"Updating {path} to root-relative")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)

def run_mass_fix(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    run_mass_fix("/Users/mediusa/NOVA/Repos/DayCare")
