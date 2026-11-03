import re
import os

def generate():
    with open('pocket.html.bak', 'r', encoding='utf-8') as f:
        html = f.read()

    # Read the CSS from the file or define it
    # We will import the CSS and HTML definitions
    from masterpiece_assets import masterpiece_css, masterpiece_html, masterpiece_js

    # 1. Inject CSS into <head>
    head_close = html.find('</head>')
    assert head_close != -1, "Could not find </head>"
    html = html[:head_close] + f"<style>\n{masterpiece_css}\n</style>\n" + html[head_close:]

    # 2. Replace radio container
    start_marker = '<main class="radio-container"'
    s_idx = html.find(start_marker)
    assert s_idx != -1, "Could not find start of radio container"

    # Find the modal start
    end_marker = 'P2P CLASSROOM MESH BEAMER MODAL'
    m_idx = html.find(end_marker)
    assert m_idx != -1, "Could not find P2P modal"
    # Find the opening comment <!-- before m_idx
    c_idx = html.rfind('<!--', 0, m_idx)
    e_idx = c_idx if c_idx != -1 else m_idx

    html = html[:s_idx] + masterpiece_html + "\n\n" + html[e_idx:]
    print("SUCCESS: replaced radio-chassis with Masterpiece Console HTML!")

    # 3. Inject JS before last </script>
    last_script_close = html.rfind('</script>')
    assert last_script_close != -1, "Could not find </script>"
    html = html[:last_script_close] + f"\n{masterpiece_js}\n" + html[last_script_close:]
    print("SUCCESS: injected Masterpiece JS engine!")

    with open('pocket.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESS: pocket.html fully generated with Masterpiece Tabletop Console!")

if __name__ == '__main__':
    generate()
