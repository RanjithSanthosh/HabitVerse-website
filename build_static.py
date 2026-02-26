import os
import shutil

def build():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    DIST_DIR = os.path.join(BASE_DIR, 'dist')

    phone_number = "919790563993"
    display_phone = "+91 9790563993"

    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR)

    # Copy static assets
    shutil.copytree(STATIC_DIR, os.path.join(DIST_DIR, 'static'))

    pages = {
        'home.html': 'index.html',
        'privacy_policy.html': 'privacy-policy.html',
        'terms.html': 'terms.html',
        'messages.html': 'messages.html',
    }

    for tpl, out in pages.items():
        path = os.path.join(TEMPLATES_DIR, tpl)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Sub variables
            content = content.replace('{{ phone_number }}', phone_number)
            content = content.replace('{{ display_phone }}', display_phone)
            # Fix static paths to be relative for Netlify
            content = content.replace('../static/', './static/')
            
            out_dir = os.path.join(DIST_DIR, out)
            with open(out_dir, 'w', encoding='utf-8') as f:
                f.write(content)

    print("Successfully built static site to 'dist' directory!")

if __name__ == "__main__":
    build()
