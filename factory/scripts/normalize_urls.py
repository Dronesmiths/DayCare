import os
import re

domain = "https://fairytalechildcare.com"

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Canonical and OG:URL to full domain
    # First normalize to root-relative if they were absolute or weird
    temp_content = re.sub(rf'{domain}/', '/', content)
    
    # Now set them correctly
    new_content = re.sub(r'<link rel="canonical" href="/', f'<link rel="canonical" href="{domain}/', temp_content)
    new_content = re.sub(r'<meta property="og:url" content="/', f'<meta property="og:url" content="{domain}/', new_content)

    # 2. Normalize Assets
    new_content = re.sub(rf'src="{domain}/', 'src="/', new_content)
    new_content = re.sub(rf'href="{domain}/css/', 'href="/css/', new_content)
    new_content = re.sub(rf'src="{domain}/js/', 'src="/js/', new_content)
    new_content = re.sub(rf'content="{domain}/images/', 'content="/images/', new_content)
    
    # 3. Normalize all internal links to explicit index.html for S3/CloudFront
    def normalize_href(match):
        href = match.group(1)
        # Skip absolute URLs, anchors, and files with extensions
        if href.startswith('http') or href.startswith('tel:') or href.startswith('mailto:') or href.startswith('#'):
            return f'href="{href}"'
        
        # If it's a directory (ends with / or has no dot in last segment)
        last_segment = href.split('/')[-1]
        if '.' not in last_segment:
            if not href.endswith('/'):
                href += '/'
            href += 'index.html'
        
        # Cleanup double slashes if any
        href = href.replace('//', '/')
        if not href.startswith('/'):
            href = '/' + href
            
        return f'href="{href}"'

    new_content = re.sub(r'href="(/?[^"]*)"', normalize_href, new_content)
    
    # Special fix for Home link: /index.html/index.html -> /index.html
    new_content = new_content.replace('/index.html/index.html', '/index.html')
    
    # 4. Fix double <a> tag in logo area
    # Pattern matches nested logo links
    new_content = re.sub(r'<a href="[^"]+" class="logo">\s*(<a href="[^"]+" class="logo".*?</a>)\s*</a>', r'\1', new_content, flags=re.DOTALL)

    if content != new_content:
        print(f"Updating {path}")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)

def run_mass_fix(directory):
    for root, dirs, files in os.walk(directory):
        if any(x in root for x in [".git", "factory", "node_modules"]): continue
        for file in files:
            if file.endswith(".html"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    run_mass_fix("/Users/mediusa/NOVA/Repos/DayCare")
