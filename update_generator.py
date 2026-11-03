with open('generate_landscape_radio.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update [data-theme='carvaan-neo']
old_carvaan_block = '''    [data-theme="carvaan-neo"] .hardware-spec-plaque {
      background: #e2e8f0;
      border-color: #cbd5e1;
    }'''

new_carvaan_block = '''    [data-theme="carvaan-neo"] .hardware-spec-plaque {
      background: #e2e8f0;
      border-color: #cbd5e1;
    }
    [data-theme="carvaan-neo"] .plaque-row {
      color: #334155;
    }
    [data-theme="carvaan-neo"] .plaque-sub {
      color: #0369a1;
      font-weight: 700;
    }
    [data-theme="carvaan-neo"] .jog-arrow-btn {
      background: #e2e8f0;
      border: 1px solid #cbd5e1;
      color: #0f172a;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    [data-theme="carvaan-neo"] .jog-arrow-btn:hover {
      background: #0284c7;
      color: #ffffff;
      border-color: #0284c7;
    }'''

assert old_carvaan_block in content, 'old_carvaan_block not found'
content = content.replace(old_carvaan_block, new_carvaan_block, 1)

# 2. Update .jog-wheel-assembly CSS
old_assembly_css = '''.jog-wheel-assembly {
      position: relative;
      width: 125px;
      height: 125px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 4px auto;
    }'''

new_assembly_css = '''.jog-wheel-assembly {
      position: relative;
      width: 100%;
      height: 125px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      margin: 4px auto;
    }'''

assert old_assembly_css in content, 'old_assembly_css not found'
content = content.replace(old_assembly_css, new_assembly_css, 1)

# 3. Update .jog-arrow-btn CSS
old_btn_css = '''.jog-quick-arrows {
      display: flex;
      gap: 12px;
      margin-top: 2px;
    }
    .jog-arrow-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.18);
      color: #ffffff;
      font-size: 0.82rem;
      font-weight: 800;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.15s ease;
    }'''

new_btn_css = '''.jog-arrow-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.18);
      color: #ffffff;
      font-size: 0.72rem;
      font-weight: 800;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
      flex-shrink: 0;
    }'''

assert old_btn_css in content, 'old_btn_css not found'
content = content.replace(old_btn_css, new_btn_css, 1)

# 4. Update HTML assembly layout
old_assembly_html = '''          <div class="jog-wheel-assembly" id="jog-wheel-assembly" title="Drag, scroll, or swipe to manually rotate and tune between stations">
            <div class="jog-wheel-outer-ring">
              <!-- Illuminated Ring Gauge -->
              <div class="jog-wheel-halo" id="jog-wheel-halo"></div>
              <!-- Rotating Wheel Face -->
              <div class="jog-wheel-face" id="jog-wheel-face">
                <div class="jog-dimple"></div>
                <div class="jog-index-notch"></div>
                <div class="jog-center-cap">
                  <span class="jog-cap-text">TUNE</span>
                </div>
              </div>
            </div>
            <div class="jog-quick-arrows">
              <button type="button" id="jog-step-prev" class="jog-arrow-btn" title="Previous Station (Counter-Clockwise)">&larr;</button>
              <button type="button" id="jog-step-next" class="jog-arrow-btn" title="Next Station (Clockwise)">&rarr;</button>
            </div>
          </div>'''

new_assembly_html = '''          <div class="jog-wheel-assembly" id="jog-wheel-assembly" title="Drag, scroll, or swipe to manually rotate and tune between stations">
            <button type="button" id="jog-step-prev" class="jog-arrow-btn" title="Previous Station (Counter-Clockwise)">&#9664;</button>
            <div class="jog-wheel-outer-ring">
              <!-- Illuminated Ring Gauge -->
              <div class="jog-wheel-halo" id="jog-wheel-halo"></div>
              <!-- Rotating Wheel Face -->
              <div class="jog-wheel-face" id="jog-wheel-face">
                <div class="jog-dimple"></div>
                <div class="jog-index-notch"></div>
                <div class="jog-center-cap">
                  <span class="jog-cap-text">TUNE</span>
                </div>
              </div>
            </div>
            <button type="button" id="jog-step-next" class="jog-arrow-btn" title="Next Station (Clockwise)">&#9654;</button>
          </div>'''

assert old_assembly_html in content, 'old_assembly_html not found'
content = content.replace(old_assembly_html, new_assembly_html, 1)

with open('generate_landscape_radio.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('SUCCESS: generate_landscape_radio.py updated!')
