import re
import glob

# Get all target files
files = glob.glob("/home/user/Megha/Digitaxpro/*.html")
files.append("/home/user/Megha/Digitaxpro/services/google-business-profile.html")

# The files we ALREADY updated and shouldn't touch:
skip_files = [
    "/home/user/Megha/Digitaxpro/blog-landing-page-elements.html",
    "/home/user/Megha/Digitaxpro/contact.html"
]

def repl(m):
    block = m.group(0)
    block = block.replace("text-white-50 text-decoration-none", "text-white text-decoration-none")
    block = block.replace("text-primary", "text-white")
    return block

for filepath in files:
    if filepath in skip_files: continue
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    new_content = re.sub(r'<!-- Quick Links -->.*?</ul>\s*</div>', repl, content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(new_content)

print("Done fixing links")
