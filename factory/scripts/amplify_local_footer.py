
import os

# New footer section with granular Palmdale/AV keywords
neighborhood_block = """
                    <!-- Neighborhoods SEO Block -->
                    <div class="aw-footer-neighborhoods" style="margin-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px;">
                        <h4 style="font-size: 0.9rem; color: #aaa; margin-bottom: 10px;">Neighborhoods Served</h4>
                        <p style="font-size: 0.8rem; color: #888; line-height: 1.6;">
                            West Palmdale • East Palmdale • Rancho Vista • Anaverde • Quartz Hill • White Fence Farms • 
                            Desert View Highlands • Joshua Ranch • Sun Village • Littlerock • Pearblossom • 
                            Anaverde Hills • Palmdale 93551 • Palmdale 93550 • Palmdale 93552
                        </p>
                    </div>
"""

def update_footer(filepath):
    # Skip non-HTML or factory files
    if not filepath.endswith(".html") or "factory" in filepath:
        return

    with open(filepath, 'r') as f:
        content = f.read()
    
    # Avoid duplicate injection
    if "Neighborhoods Served" in content:
        print(f"Skipping {filepath}: Already has neighborhood block.")
        return

    # Targeting the end of the inner footer container
    # We'll look for the last </div> before </footer>
    target = '</footer>'
    
    if target in content:
         # Insert before footer close
        last_div = content.rfind('</div>', 0, content.find(target))
        if last_div != -1:
            # Try to be a bit more precise - find the one that looks like it's the end of a container
            new_content = content[:last_div] + neighborhood_block + content[last_div:]
        else:
            new_content = content.replace(target, neighborhood_block + '\n' + target)
    else:
        print(f"Could not find footer target in {filepath}")
        return

    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Updated footer in {filepath}")

def main():
    for root, dirs, files in os.walk("."):
        if ".git" in root or ".gemini" in root or "factory" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                update_footer(os.path.join(root, file))

if __name__ == "__main__":
    main()
