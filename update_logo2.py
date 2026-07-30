import glob
import re

html_files = glob.glob("*.html")

new_logo_block = """            <!-- Left: Logo -->
            <div style="display: flex; align-items: center;">
                <a href="./" class="logo" style="display: flex; align-items: center; text-decoration: none;">
                    <img src="CS-Capital_Horiz_OnLight.svg" alt="Center Street Capital Logo" class="logo-image" style="height: 30px; width: auto; object-fit: contain;">
                </a>
                <span style="color: #cbd5e1; margin: 0 16px; font-size: 1.25rem; font-weight: 300; line-height: 1;">|</span>
                <span style="color: #000000; font-weight: 500; font-size: 1.15rem; letter-spacing: -0.01em;">Riviera Capital</span>
            </div>"""

for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
        
    # Replace the block
    pattern = r"            <!-- Left: Logo -->\n            <div style=\"display: flex; align-items: center;\">[\s\S]*?</div>"
    
    content = re.sub(pattern, new_logo_block, content)
    
    with open(f, 'w') as file:
        file.write(content)

print("Updated logo blocks on all pages to be black, larger, and unlinked.")
