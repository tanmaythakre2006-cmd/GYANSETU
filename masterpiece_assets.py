# -*- coding: utf-8 -*-
masterpiece_css = """
/* ==========================================================================
   GYANSETU MASTERPIECE TABLETOP RADIO CONSOLE (LENOVO TAB M8 1280x800 NATIVE)
   Flagship Tablet Appliance Design - Curated by Simran Ailani
   ========================================================================== */

:root {
  --font-display: 'Cinzel Decorative', 'Cinzel', serif;
  --font-mono: 'Space Mono', monospace;
  --font-ui: 'Plus Jakarta Sans', system-ui, sans-serif;
}

/* THEME 1: 1978 VINTAGE TEAKWOOD CABINET (Classical Purist Hardware) */
[data-theme="vintage-1978"] {
  --cabinet-bg: linear-gradient(145deg, #1f140e 0%, #2e1c12 40%, #1a0f09 100%);
  --cabinet-border: 10px solid #140b06;
  --cabinet-bevel: inset 0 0 0 2px #5a381e, inset 0 0 25px rgba(0,0,0,0.9), 0 15px 40px rgba(0,0,0,0.85);
  --faceplate-bg: linear-gradient(180deg, #1b120c 0%, #26170d 100%);
  --faceplate-border: 1px solid #4a2d18;
  
  --accent-metal: #d4af37;
  --accent-metal-border: #8c6d1f;
  --accent-glow: #ffaa11;
  
  --speaker-grille: repeating-linear-gradient(45deg, #2b1f15 0px, #2b1f15 2px, #18110b 2px, #18110b 5px),
                    repeating-linear-gradient(-45deg, #3d2c1e 0px, #3d2c1e 2px, #150f09 2px, #150f09 5px);
  --speaker-border: 2px solid #5a3c1e;
  --badge-bg: linear-gradient(135deg, #e6ca65 0%, #a88118 50%, #d4af37 100%);
  --badge-text: #1b1208;
  
  --vu-face: #fdf8e6;
  --vu-text: #1a160f;
  --vu-needle: #c5221f;
  --vu-border: 2px solid #54391e;
  
  --dial-glass-bg: radial-gradient(ellipse at center, #26170d 0%, #0d0804 100%);
  --dial-glass-border: 1px solid #6b471f;
  --dial-text: #ffbe3b;
  
  --screen-bg: radial-gradient(circle at center, #1c1308 0%, #0c0803 100%);
  --screen-border: 2px solid #6b471f;
  --screen-text: #ffbe3b;
  --screen-sub: #b37d1e;
  --spec-bar-bg: #ffaa11;
  --screen-shadow: inset 0 0 16px rgba(0,0,0,0.95), 0 0 8px rgba(255, 170, 17, 0.2);
  
  --dir-bg: #0d0905;
  --dir-border: 1px solid #422a14;
  --dir-item-hover: rgba(212, 175, 55, 0.15);
  --dir-item-active: linear-gradient(90deg, #d4af37 0%, #916f1a 100%);
  --dir-item-active-text: #000000;
  
  --piano-key-bg: linear-gradient(180deg, #e2cf9f 0%, #c4a96b 50%, #876d33 100%);
  --piano-key-border: 1px solid #574116;
  --piano-key-text: #181105;
  --piano-key-shadow: 0 4px 6px rgba(0,0,0,0.8), inset 0 1px 0 rgba(255,255,255,0.4);
  --piano-key-active-bg: linear-gradient(180deg, #ffd700 0%, #d4af37 100%);
}

/* THEME 2: GYANSETU CARVAAN NEO (PANORAMIC OLED & CYBER COCKPIT) */
/* "Version just has more screen!" - Left panel turns into 3D Spectrogram display */
[data-theme="carvaan-neo"] {
  --cabinet-bg: linear-gradient(135deg, #0b1120 0%, #0f172a 50%, #030712 100%);
  --cabinet-border: 10px solid #1e293b;
  --cabinet-bevel: inset 0 0 0 2px #0284c7, inset 0 0 25px rgba(2, 132, 199, 0.25), 0 15px 40px rgba(0,0,0,0.9);
  --faceplate-bg: linear-gradient(180deg, #090e17 0%, #04070d 100%);
  --faceplate-border: 1px solid rgba(56, 189, 248, 0.3);
  
  --accent-metal: #38bdf8;
  --accent-metal-border: #0284c7;
  --accent-glow: #00f0ff;
  
  --speaker-grille: #030712;
  --speaker-border: 2px solid #0284c7;
  --badge-bg: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
  --badge-text: #ffffff;
  
  --vu-face: #030712;
  --vu-text: #38bdf8;
  --vu-needle: #00f0ff;
  --vu-border: 2px solid #0284c7;
  
  --dial-glass-bg: radial-gradient(ellipse at center, #0b1528 0%, #020610 100%);
  --dial-glass-border: 1px solid #0284c7;
  --dial-text: #38bdf8;
  
  --screen-bg: radial-gradient(circle at center, #081324 0%, #020610 100%);
  --screen-border: 2px solid #0284c7;
  --screen-text: #38bdf8;
  --screen-sub: #7dd3fc;
  --spec-bar-bg: #00f0ff;
  --screen-shadow: inset 0 0 20px rgba(2, 132, 199, 0.3), 0 0 14px rgba(2, 132, 199, 0.4);
  
  --dir-bg: #030712;
  --dir-border: 1px solid rgba(56, 189, 248, 0.25);
  --dir-item-hover: rgba(56, 189, 248, 0.15);
  --dir-item-active: linear-gradient(90deg, #0284c7 0%, #0369a1 100%);
  --dir-item-active-text: #ffffff;
  
  --piano-key-bg: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
  --piano-key-border: 1px solid rgba(56, 189, 248, 0.35);
  --piano-key-text: #e2e8f0;
  --piano-key-shadow: 0 4px 10px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.1);
  --piano-key-active-bg: linear-gradient(180deg, #0284c7 0%, #0369a1 100%);
}

/* ==========================================================================
   GLOBAL CHASSIS (Strictly 1280x800 Native Tablet Edge-to-Edge)
   ========================================================================== */
html, body {
  margin: 0 !important;
  padding: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  max-width: 100vw !important;
  max-height: 100vh !important;
  overflow: hidden !important;
  background: #000000 !important;
  user-select: none;
  -webkit-user-select: none;
  font-family: var(--font-ui);
}

.radio-chassis {
  position: relative;
  width: 100vw;
  height: 100vh;
  max-width: 1280px;
  max-height: 800px;
  margin: 0 auto;
  box-sizing: border-box;
  background: var(--cabinet-bg);
  border: var(--cabinet-border);
  box-shadow: var(--cabinet-bevel);
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 10px 14px 8px 14px;
  overflow: hidden;
  transition: background 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease;
}

/* Top Hardware Trim Bar */
.console-top-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 38px;
  padding: 0 8px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  flex-shrink: 0;
}

.top-bar-left, .top-bar-right {
  display: flex;
  align-items: center;
  gap: 10px;
}

.hardware-switch-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(0, 0, 0, 0.6);
  border: 1px solid var(--accent-metal-border);
  color: var(--accent-metal);
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.6px;
  padding: 4px 12px;
  border-radius: 4px;
  cursor: pointer;
  text-decoration: none;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.15), 0 2px 4px rgba(0,0,0,0.5);
  transition: all 0.2s ease;
}

.hardware-switch-btn:hover {
  filter: brightness(1.2);
  transform: translateY(-1px);
}

.top-led-indicator {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 0.66rem;
  font-weight: 800;
  color: #a8a29e;
  letter-spacing: 0.6px;
}

.led-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}
.led-dot.green {
  background: #22c55e;
  box-shadow: 0 0 8px #22c55e;
}

/* Master Theme Knife Switch */
.theme-switch-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.master-theme-toggle-zone {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(0, 0, 0, 0.7);
  padding: 3px 12px;
  border-radius: 9999px;
  border: 1px solid var(--accent-metal-border);
  cursor: pointer;
}

.theme-label {
  font-size: 0.70rem;
  font-weight: 800;
  letter-spacing: 0.5px;
  color: #78716c;
  transition: color 0.2s ease;
}

.theme-label.active {
  color: var(--accent-metal);
  text-shadow: 0 0 8px var(--accent-glow);
}

.theme-toggle-switch {
  width: 40px;
  height: 18px;
  background: #1c1917;
  border-radius: 9999px;
  border: 1px solid #44403c;
  position: relative;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.8);
}

.theme-toggle-lever {
  width: 14px;
  height: 14px;
  background: radial-gradient(circle, #fff, #bbb);
  border-radius: 50%;
  position: absolute;
  top: 1px;
  left: 2px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.8);
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="carvaan-neo"] .theme-toggle-lever {
  transform: translateX(20px);
  background: radial-gradient(circle, #38bdf8, #0284c7);
  box-shadow: 0 0 6px #00f0ff;
}

/* ==========================================================================
   PANORAMIC 3-COLUMN STAGE (1280x800 Native)
   ========================================================================== */
.console-panoramic-stage {
  display: grid;
  grid-template-columns: 29% 43% 28%;
  gap: 12px;
  flex: 1 1 auto;
  margin: 6px 0;
  min-height: 0;
  overflow: hidden;
}

.console-column {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 0;
  overflow: hidden;
}

/* ==========================================================================
   COLUMN 1 (LEFT): DUAL ARCHITECTURE
   - Vintage 1978: Cloth Speaker + Dual Analog VU Needle Meters + Rotary Knobs
   - Carvaan Neo: High-Tech Cyber Spectrogram & Telemetry Touchscreen (MORE SCREEN!)
   ========================================================================== */
.col-speaker {
  background: rgba(0,0,0,0.3);
  border-radius: 12px;
  border: var(--speaker-border);
  padding: 8px;
  box-sizing: border-box;
}

/* 1. Vintage Cluster */
.speaker-vintage-cluster {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

[data-theme="carvaan-neo"] .speaker-vintage-cluster {
  display: none !important;
}

.speaker-grille-chamber {
  position: relative;
  height: 180px;
  background: var(--speaker-grille);
  background-size: 8px 8px;
  border-radius: 8px;
  border: 1px solid rgba(0,0,0,0.6);
  box-shadow: inset 0 0 30px rgba(0,0,0,0.9), 0 2px 6px rgba(0,0,0,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.speaker-diaphragm-pulse {
  position: absolute;
  width: 140px;
  height: 140px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0,0,0,0.4) 0%, transparent 70%);
  opacity: 0.6;
  pointer-events: none;
}

.metallic-brand-plaque {
  position: relative;
  z-index: 2;
  background: var(--badge-bg);
  color: var(--badge-text);
  border: 2px solid #fff3c4;
  border-radius: 6px;
  padding: 8px 16px;
  text-align: center;
  box-shadow: 0 4px 15px rgba(0,0,0,0.8), inset 0 1px 0 rgba(255,255,255,0.7);
}

.badge-sub-text {
  font-size: 0.72rem;
  font-weight: 800;
  display: block;
  letter-spacing: 1px;
}

.badge-main-text {
  font-family: var(--font-display);
  font-size: 1.35rem;
  margin: 2px 0;
  letter-spacing: 2px;
  font-weight: 900;
}

.badge-lead-caption {
  font-size: 0.54rem;
  font-weight: 800;
  letter-spacing: 1.2px;
  display: block;
  opacity: 0.9;
}

.badge-curator-line {
  font-size: 0.52rem;
  font-weight: 700;
  display: block;
  margin-top: 2px;
  letter-spacing: 0.5px;
  opacity: 0.85;
}

/* Dual Analog VU Meters */
.vu-meter-chambers-wrap {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 6px 0;
}

.vu-meter-box {
  background: var(--vu-face);
  border: var(--vu-border);
  border-radius: 6px;
  padding: 6px 8px 4px 8px;
  box-shadow: inset 0 0 12px rgba(0,0,0,0.6), 0 3px 6px rgba(0,0,0,0.7);
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  overflow: hidden;
  height: 95px;
  box-sizing: border-box;
}

.vu-dial-scale {
  width: 100%;
  display: flex;
  justify-content: space-between;
  font-size: 0.52rem;
  font-weight: 800;
  color: var(--vu-text);
  margin-bottom: 2px;
}

.vu-tick-lbl.red { color: #dc2626; }

.vu-needle-assembly {
  position: relative;
  width: 100%;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: flex-end;
}

.vu-physical-needle {
  position: absolute;
  bottom: 0;
  width: 2px;
  height: 52px;
  background: var(--vu-needle);
  transform-origin: bottom center;
  transform: rotate(-35deg);
  transition: transform 0.08s cubic-bezier(0.1, 0.9, 0.2, 1);
  box-shadow: 0 0 4px rgba(0,0,0,0.5);
}

.vu-needle-pivot {
  position: absolute;
  bottom: -4px;
  width: 10px;
  height: 10px;
  background: #111;
  border-radius: 50%;
  border: 1px solid #777;
}

.vu-ch-label {
  font-size: 0.48rem;
  font-weight: 800;
  color: var(--vu-text);
  margin-top: 2px;
  letter-spacing: 0.6px;
}

/* Rotary Knobs in Column 1 */
.speaker-bottom-knobs {
  display: flex;
  justify-content: space-around;
  align-items: center;
  background: rgba(0,0,0,0.5);
  border-radius: 8px;
  border: 1px solid rgba(255,255,255,0.06);
  padding: 6px 4px;
}

.rotary-control-unit {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}

.rotary-knob {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: conic-gradient(from 0deg, #666, #ccc, #333, #bbb, #666);
  border: 2px solid #222;
  position: relative;
  cursor: pointer;
  box-shadow: 0 3px 6px rgba(0,0,0,0.7);
}

.knob-cap {
  position: absolute;
  inset: 3px;
  background: radial-gradient(circle, #555, #222);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.knob-notch {
  width: 2px;
  height: 8px;
  background: #fff;
  border-radius: 1px;
  position: absolute;
  top: 1px;
}

.knob-label {
  font-size: 0.50rem;
  font-weight: 800;
  color: #a8a29e;
  letter-spacing: 0.4px;
}

.knob-val-readout {
  font-size: 0.48rem;
  font-weight: 800;
  color: var(--accent-metal);
}

/* ==========================================================================
   2. CARVAAN NEO OLED LEFT SCREEN ("VERSION JUST HAS MORE SCREEN!")
   ========================================================================== */
.modern-oled-left-screen {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  background: radial-gradient(circle at center, #071526 0%, #020610 100%);
  border: 2px solid #0284c7;
  border-radius: 10px;
  padding: 8px;
  box-sizing: border-box;
  box-shadow: inset 0 0 25px rgba(2, 132, 199, 0.35), 0 0 16px rgba(2, 132, 199, 0.4);
}

[data-theme="carvaan-neo"] .modern-oled-left-screen {
  display: flex !important;
}

.modern-screen-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(56, 189, 248, 0.3);
  padding-bottom: 4px;
}

.cyber-badge-tag {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 0.58rem;
  font-weight: 800;
  color: #38bdf8;
  letter-spacing: 0.8px;
}

.cyber-pulse-dot {
  width: 6px;
  height: 6px;
  background: #00f0ff;
  border-radius: 50%;
  box-shadow: 0 0 8px #00f0ff;
  animation: cyberPulse 1.2s infinite alternate;
}

@keyframes cyberPulse {
  from { opacity: 0.4; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1.2); }
}

.cyber-curator-tag {
  font-size: 0.52rem;
  font-weight: 800;
  color: #94a3b8;
  letter-spacing: 0.6px;
}

/* 3D Holographic Spectrogram Canvas */
.modern-canvas-container {
  position: relative;
  width: 100%;
  height: 155px;
  background: #020610;
  border: 1px solid rgba(56, 189, 248, 0.25);
  border-radius: 6px;
  overflow: hidden;
  margin: 6px 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

#neo-spectrogram-canvas {
  width: 100%;
  height: 100%;
  display: block;
}

.canvas-grid-overlay {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg, rgba(2, 132, 199, 0.05) 0px, rgba(2, 132, 199, 0.05) 1px, transparent 1px, transparent 10px),
              repeating-linear-gradient(90deg, rgba(2, 132, 199, 0.05) 0px, rgba(2, 132, 199, 0.05) 1px, transparent 1px, transparent 10px);
  pointer-events: none;
}

/* Modern Telemetry Box */
.modern-telemetry-box {
  background: rgba(0, 0, 0, 0.6);
  border: 1px solid rgba(56, 189, 248, 0.2);
  border-radius: 6px;
  padding: 6px 8px;
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.telem-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.48rem;
  font-weight: 700;
}

.telem-key { color: #64748b; letter-spacing: 0.4px; }
.telem-val { color: #38bdf8; font-family: var(--font-mono); }
.telem-val.highlight { color: #00f0ff; font-weight: 800; }
.telem-val.author { color: #fde047; }

/* Modern Capacitive Touch Faders */
.modern-touch-faders {
  display: flex;
  justify-content: space-around;
  align-items: center;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 6px;
  border: 1px solid rgba(56, 189, 248, 0.2);
  padding: 6px 8px;
  margin-top: 4px;
}

.cyber-fader-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.fader-label {
  font-size: 0.48rem;
  font-weight: 800;
  color: #94a3b8;
  letter-spacing: 0.6px;
}

.cyber-slider-track {
  width: 8px;
  height: 48px;
  background: #0f172a;
  border: 1px solid #334155;
  border-radius: 4px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
}

.cyber-slider-fill {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(180deg, #00f0ff 0%, #0284c7 100%);
  border-radius: 4px;
  box-shadow: 0 0 8px #00f0ff;
}

.fader-val {
  font-size: 0.46rem;
  font-weight: 800;
  color: #38bdf8;
  font-family: var(--font-mono);
}

/* ==========================================================================
   COLUMN 2 (CENTER): DUAL SCREENS & FM SCALE
   ========================================================================== */
.col-screens {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 6px;
}

/* Analog FM Dial Frequency Scale */
.analog-frequency-scale {
  background: var(--dial-glass-bg);
  border: var(--dial-glass-border);
  border-radius: 6px;
  height: 30px;
  padding: 2px 10px;
  box-shadow: inset 0 0 10px rgba(0,0,0,0.9), 0 2px 5px rgba(0,0,0,0.6);
  display: flex;
  align-items: center;
  position: relative;
  overflow: hidden;
  flex-shrink: 0;
}

.dial-markings-track {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
}

.freq-tick {
  font-size: 0.60rem;
  font-weight: 800;
  color: var(--dial-text);
  font-family: var(--font-mono);
  letter-spacing: 0.5px;
}

.physical-dial-needle {
  position: absolute;
  top: -8px;
  bottom: -8px;
  width: 3px;
  background: #dc2626;
  left: 88%;
  box-shadow: 0 0 8px #dc2626;
  transition: left 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

[data-theme="carvaan-neo"] .physical-dial-needle {
  background: #00f0ff;
  box-shadow: 0 0 10px #00f0ff;
}

/* Main LCD Display */
.main-lcd-display {
  background: var(--screen-bg);
  border: var(--screen-border);
  border-radius: 8px;
  padding: 10px 14px;
  box-shadow: var(--screen-shadow);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex: 1 1 auto;
  min-height: 180px;
}

.lcd-header-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  padding-bottom: 4px;
}

.lcd-station-badge {
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.lcd-badge-tag {
  background: var(--accent-metal);
  color: #000;
  font-size: 0.65rem;
  font-weight: 900;
  padding: 2px 6px;
  border-radius: 4px;
}

.lcd-freq-num {
  font-size: 0.85rem;
  font-weight: 800;
  color: var(--screen-text);
  font-family: var(--font-mono);
}

.lcd-spectrum-visualizer {
  display: flex;
  align-items: flex-end;
  gap: 2px;
  height: 16px;
}

.spec-bar {
  width: 3px;
  height: 4px;
  background: var(--spec-bar-bg);
  border-radius: 1px;
}

.lcd-dub-btn {
  background: rgba(0,0,0,0.6);
  border: 1px solid var(--accent-metal-border);
  color: var(--accent-metal);
  font-size: 0.60rem;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 9999px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.dub-dot {
  width: 5px;
  height: 5px;
  background: #22c55e;
  border-radius: 50%;
  box-shadow: 0 0 6px #22c55e;
}

.lcd-body-content {
  margin: 6px 0;
}

.lcd-title-row {
  margin-bottom: 4px;
}

.lcd-track-title {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--screen-text);
  line-height: 1.2;
}

.lcd-curator-name {
  font-size: 0.60rem;
  font-weight: 800;
  color: var(--screen-sub);
  letter-spacing: 0.8px;
  display: block;
  margin-top: 2px;
}

.lcd-meta-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.58rem;
  font-weight: 700;
  color: var(--screen-sub);
  margin-bottom: 8px;
}

.lcd-progress-track {
  display: flex;
  align-items: center;
  gap: 8px;
}

.lcd-time-txt {
  font-size: 0.60rem;
  font-weight: 800;
  color: var(--screen-text);
  font-family: var(--font-mono);
}

.lcd-progress-bar-bg {
  flex: 1 1 auto;
  height: 6px;
  background: rgba(0,0,0,0.7);
  border-radius: 3px;
  position: relative;
  cursor: pointer;
  overflow: visible;
}

.lcd-progress-fill {
  height: 100%;
  width: 0%;
  background: var(--accent-metal);
  border-radius: 3px;
  box-shadow: 0 0 8px var(--accent-glow);
}

.lcd-progress-scrubber-head {
  position: absolute;
  top: -4px;
  left: 0%;
  width: 14px;
  height: 14px;
  background: #fff;
  border: 2px solid var(--accent-metal);
  border-radius: 50%;
  transform: translateX(-50%);
  box-shadow: 0 0 8px var(--accent-glow);
}

.lcd-teleprompter-strip {
  background: rgba(0,0,0,0.6);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 4px;
  padding: 3px 6px;
  display: flex;
  align-items: center;
  gap: 6px;
  overflow: hidden;
}

.tp-badge {
  background: var(--accent-metal);
  color: #000;
  font-size: 0.50rem;
  font-weight: 900;
  padding: 1px 4px;
  border-radius: 3px;
  flex-shrink: 0;
}

.tp-marquee-mask {
  overflow: hidden;
  white-space: nowrap;
  flex: 1 1 auto;
}

.tp-text {
  font-size: 0.56rem;
  color: var(--screen-text);
  font-family: var(--font-mono);
}

/* Secondary Screen: Digital Directory */
.directory-screen-chassis {
  background: var(--dir-bg);
  border: var(--dir-border);
  border-radius: 6px;
  padding: 6px 8px;
  height: 125px;
  display: flex;
  flex-direction: column;
  box-shadow: inset 0 0 10px rgba(0,0,0,0.9);
  flex-shrink: 0;
}

.dir-header-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  padding-bottom: 3px;
  margin-bottom: 3px;
}

.dir-title {
  font-size: 0.56rem;
  font-weight: 800;
  color: var(--screen-sub);
  letter-spacing: 0.6px;
}

.dir-count-pill {
  font-size: 0.50rem;
  font-weight: 800;
  color: var(--screen-text);
  font-family: var(--font-mono);
}

.dir-episodes-scroll-list {
  flex: 1 1 auto;
  overflow-y: auto;
  scrollbar-width: thin;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.station-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 3px 6px;
  border-radius: 3px;
  cursor: pointer;
  font-size: 0.56rem;
  color: #a8a29e;
  font-family: var(--font-mono);
}

.station-item:hover {
  background: var(--dir-item-hover);
  color: #fff;
}

.station-item.active {
  background: var(--dir-item-active);
  color: var(--dir-item-active-text);
  font-weight: 800;
}

/* Category Mood Presets */
.mood-presets-deck {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 4px;
  height: 38px;
  flex-shrink: 0;
}

.mood-preset-key {
  background: rgba(0,0,0,0.6);
  border: 1px solid var(--accent-metal-border);
  border-radius: 5px;
  color: #d6d3d1;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2px;
  transition: all 0.2s ease;
}

.mood-preset-key.active, .mood-preset-key:hover {
  background: var(--accent-metal);
  color: #000;
  font-weight: 800;
}

.mood-icon { font-size: 0.65rem; }
.mood-title { font-size: 0.50rem; font-weight: 800; letter-spacing: 0.4px; }
.mood-freq { font-size: 0.44rem; font-family: var(--font-mono); opacity: 0.8; }

/* ==========================================================================
   COLUMN 3 (RIGHT): ARTWORK & DUAL DIAL HUB
   ========================================================================== */
.col-artwork-dials {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 6px;
}

/* Framed Album Artwork */
.album-artwork-frame-box {
  background: #000;
  border: 4px solid var(--accent-metal-border);
  border-radius: 8px;
  overflow: hidden;
  height: 185px;
  position: relative;
  box-shadow: 0 6px 16px rgba(0,0,0,0.8), inset 0 0 10px rgba(0,0,0,0.7);
  flex-shrink: 0;
}

.artwork-outer-bezel {
  width: 100%;
  height: 100%;
  position: relative;
}

.current-album-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.artwork-glass-reflection {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, transparent 50%);
  pointer-events: none;
}

.artwork-overlay-pill {
  position: absolute;
  bottom: 6px;
  left: 6px;
  right: 6px;
  background: rgba(0,0,0,0.75);
  backdrop-filter: blur(4px);
  border-radius: 4px;
  padding: 2px 6px;
  display: flex;
  justify-content: space-between;
  font-size: 0.50rem;
  font-weight: 800;
  color: var(--accent-metal);
}

/* Dual Rotary Dials Hub */
.dual-rotary-dials-hub {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  align-items: center;
  justify-content: center;
  background: rgba(0,0,0,0.4);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 8px;
  padding: 8px;
  flex: 1 1 auto;
}

.rotary-station-unit {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.jog-wheel-outer-ring, .secondary-scroll-knob-outer {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: conic-gradient(from 0deg, #d4af37, #8c6d1f, #d4af37, #5c4410, #d4af37);
  padding: 4px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.8), inset 0 2px 4px rgba(255,255,255,0.3);
  position: relative;
  cursor: grab;
}

[data-theme="carvaan-neo"] .jog-wheel-outer-ring,
[data-theme="carvaan-neo"] .secondary-scroll-knob-outer {
  background: conic-gradient(from 0deg, #38bdf8, #0284c7, #38bdf8, #0369a1, #38bdf8);
  box-shadow: 0 0 16px rgba(56, 189, 248, 0.4);
}

.jog-wheel-face, .secondary-knob-face {
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, #2b1f15, #120b06);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: transform 0.05s linear;
}

[data-theme="carvaan-neo"] .jog-wheel-face,
[data-theme="carvaan-neo"] .secondary-knob-face {
  background: radial-gradient(circle, #0f172a, #020610);
}

.jog-dimple {
  position: absolute;
  top: 8px;
  width: 8px;
  height: 8px;
  background: radial-gradient(circle, #000, #555);
  border-radius: 50%;
  box-shadow: inset 0 1px 2px rgba(0,0,0,0.9);
}

.jog-center-cap, .secondary-center-cap {
  font-size: 0.52rem;
  font-weight: 900;
  color: var(--accent-metal);
  letter-spacing: 0.5px;
}

.dial-caption-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}

.dial-title-label {
  font-size: 0.50rem;
  font-weight: 800;
  color: #a8a29e;
  letter-spacing: 0.5px;
}

.dial-nudge-buttons {
  display: flex;
  gap: 4px;
}

.dial-nudge-btn {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: rgba(255,255,255,0.08);
  border: 1px solid var(--accent-metal-border);
  color: var(--accent-metal);
  font-size: 0.54rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Hardware Spec Plaque */
.hardware-spec-plaque {
  background: rgba(0,0,0,0.6);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 4px;
  padding: 3px 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-shrink: 0;
}

.plaque-row {
  font-size: 0.46rem;
  font-weight: 800;
  color: #94a3b8;
  letter-spacing: 0.4px;
}

.plaque-sub {
  font-size: 0.42rem;
  font-weight: 700;
  color: var(--accent-metal);
  letter-spacing: 0.5px;
}

/* ==========================================================================
   BOTTOM DECK PIANO KEYS
   ========================================================================== */
.console-bottom-deck {
  height: 48px;
  border-top: 2px solid var(--accent-metal-border);
  padding-top: 4px;
  width: 100%;
  flex-shrink: 0;
}

.piano-transport-keys-grid {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 6px;
  height: 100%;
}

.mechanical-piano-key {
  background: var(--piano-key-bg);
  border: var(--piano-key-border);
  border-radius: 4px;
  color: var(--piano-key-text);
  box-shadow: var(--piano-key-shadow);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.08s ease, background 0.15s ease;
  outline: none;
}

.mechanical-piano-key:active, .mechanical-piano-key.depressed {
  transform: translateY(3px);
  background: var(--piano-key-active-bg);
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.6);
}

.piano-cap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1px;
}

.piano-icon { font-size: 0.70rem; }
.piano-txt { font-size: 0.48rem; font-weight: 900; letter-spacing: 0.5px; }

/* Hide legacy web navigations */
.pocket-top-nav, .antenna-mount {
  display: none !important;
}

"""

masterpiece_html = """
<div class="radio-chassis" id="radio-chassis" data-theme="vintage-1978">
  <!-- Top Hardware Accent Trim -->
  <header class="console-top-bar">
    <div class="top-bar-left">
      <a href="index.html" class="hardware-switch-btn btn-studio" title="Return to Global Studio">
        <span>◄ STUDIO</span>
      </a>
      <span class="top-led-indicator">
        <span class="led-dot green"></span> HI-GAIN 13-CH
      </span>
    </div>

    <!-- Master Theme Toggle Knife-Switch -->
    <div class="theme-switch-container">
      <div class="master-theme-toggle-zone" id="master-theme-switch" role="button" tabindex="0" title="Toggle between 1978 Vintage Teakwood & GyanSetu Carvaan Neo">
        <span class="theme-label active" id="label-vintage">📻 1978 VINTAGE</span>
        <div class="theme-toggle-switch">
          <div class="theme-toggle-lever" id="theme-lever"></div>
        </div>
        <span class="theme-label" id="label-carvaan">✨ CARVAAN NEO (OLED)</span>
      </div>
    </div>

    <div class="top-bar-right">
      <button type="button" id="btn-kiosk-fullscreen" class="hardware-switch-btn btn-kiosk" title="Lock Tabletop Kiosk Mode (Edge-to-Edge Fullscreen)">
        <span id="kiosk-btn-text">⛶ TABLETOP KIOSK</span>
      </button>
    </div>
  </header>

  <!-- Main 3-Column Appliance Stage (1280x800 Native) -->
  <main class="console-panoramic-stage">
    
    <!-- COLUMN 1 (LEFT): DUAL ARCHITECTURE -->
    <section class="console-column col-speaker">
      
      <!-- VINTAGE 1978 CLUSTER: Cloth Speaker + Dual Analog VU Meters + Rotary Knobs -->
      <div class="speaker-vintage-cluster">
        <div class="speaker-grille-chamber">
          <div class="speaker-diaphragm-pulse" id="speaker-pulse"></div>
          <div class="metallic-brand-plaque">
            <span class="badge-sub-text">ज्ञानसेतु</span>
            <h1 class="badge-main-text">GYANSETU</h1>
            <span class="badge-lead-caption">STUDENT BROADCAST NETWORK</span>
            <span class="badge-curator-line">Curated by Simran Ailani</span>
          </div>
        </div>

        <div class="vu-meter-chambers-wrap">
          <div class="vu-meter-box">
            <div class="vu-dial-scale">
              <span class="vu-tick-lbl left">-20</span>
              <span class="vu-tick-lbl mid">-5</span>
              <span class="vu-tick-lbl zero">0</span>
              <span class="vu-tick-lbl red">+3</span>
            </div>
            <div class="vu-needle-assembly">
              <div id="vu-needle-left" class="vu-physical-needle"></div>
              <div class="vu-needle-pivot"></div>
            </div>
            <span class="vu-ch-label">CHANNEL LEVEL (dB)</span>
          </div>

          <div class="vu-meter-box">
            <div class="vu-dial-scale">
              <span class="vu-tick-lbl left">-20</span>
              <span class="vu-tick-lbl mid">-5</span>
              <span class="vu-tick-lbl zero">0</span>
              <span class="vu-tick-lbl red">+3</span>
            </div>
            <div class="vu-needle-assembly">
              <div id="vu-needle-right" class="vu-physical-needle"></div>
              <div class="vu-needle-pivot"></div>
            </div>
            <span class="vu-ch-label">SIGNAL STRENGTH (dB)</span>
          </div>
        </div>

        <div class="speaker-bottom-knobs">
          <div class="rotary-control-unit" id="unit-vol" title="Output Volume (0 - 100%)">
            <div class="rotary-knob knob-vol" id="knob-volume">
              <div class="knob-cap"><div class="knob-notch"></div></div>
            </div>
            <span class="knob-label">OUTPUT VOL</span>
            <span class="knob-val-readout" id="lbl-volume">85%</span>
          </div>

          <div class="rotary-control-unit" id="unit-bass" title="BASS EQ Resonance">
            <div class="rotary-knob knob-bass" id="knob-bass">
              <div class="knob-cap"><div class="knob-notch"></div></div>
            </div>
            <span class="knob-label">BASS EQ</span>
            <span class="knob-val-readout" id="lbl-bass">+3 dB</span>
          </div>

          <div class="rotary-control-unit" id="unit-treble" title="TREBLE Acoustic Tone">
            <div class="rotary-knob knob-tone" id="knob-treble">
              <div class="knob-cap"><div class="knob-notch"></div></div>
            </div>
            <span class="knob-label">TREBLE TONE</span>
            <span class="knob-val-readout" id="lbl-treble">WARM</span>
          </div>
        </div>
      </div>

      <!-- CARVAAN NEO OLED LEFT SCREEN: MORE SCREEN! -->
      <div class="modern-oled-left-screen" id="modern-left-screen">
        <div class="modern-screen-header">
          <div class="cyber-badge-tag">
            <span class="cyber-pulse-dot"></span>
            <span>QUANTUM SPECTROGRAM • HD DSP</span>
          </div>
          <span class="cyber-curator-tag">SIMRAN AILANI</span>
        </div>
        
        <!-- 3D Holographic Audio Spectrogram Visualizer Canvas -->
        <div class="modern-canvas-container">
          <canvas id="neo-spectrogram-canvas" width="280" height="155"></canvas>
          <div class="canvas-grid-overlay"></div>
        </div>

        <!-- Live Telemetry Matrix -->
        <div class="modern-telemetry-box">
          <div class="telem-row">
            <span class="telem-key">SIGNAL CARRIER</span>
            <span class="telem-val" id="telem-freq">108.00 MHz FM</span>
          </div>
          <div class="telem-row">
            <span class="telem-key">AUDIO BITRATE</span>
            <span class="telem-val highlight">320 KBPS / 48kHz LOSSLESS</span>
          </div>
          <div class="telem-row">
            <span class="telem-key">P2P MESH VAULT</span>
            <span class="telem-val">13 OFFLINE CHUNKS READY</span>
          </div>
          <div class="telem-row">
            <span class="telem-key">STATION CURATOR</span>
            <span class="telem-val author">SIMRAN AILANI</span>
          </div>
        </div>

        <!-- Modern Capacitive Touch Equalizer Faders -->
        <div class="modern-touch-faders">
          <div class="cyber-fader-item" id="touch-fader-vol">
            <span class="fader-label">GAIN</span>
            <div class="cyber-slider-track">
              <div class="cyber-slider-fill" id="fader-vol-fill" style="height: 85%;"></div>
            </div>
            <span class="fader-val" id="fader-vol-val">85%</span>
          </div>
          <div class="cyber-fader-item" id="touch-fader-bass">
            <span class="fader-label">BASS</span>
            <div class="cyber-slider-track">
              <div class="cyber-slider-fill" id="fader-bass-fill" style="height: 65%;"></div>
            </div>
            <span class="fader-val" id="fader-bass-val">+3dB</span>
          </div>
          <div class="cyber-fader-item" id="touch-fader-treble">
            <span class="fader-label">TONE</span>
            <div class="cyber-slider-track">
              <div class="cyber-slider-fill" id="fader-treble-fill" style="height: 75%;"></div>
            </div>
            <span class="fader-val" id="fader-treble-val">WARM</span>
          </div>
        </div>
      </div>

    </section>

    <!-- COLUMN 2 (CENTER): DUAL SCREENS & FREQUENCY SCALE -->
    <section class="console-column col-screens">
      
      <!-- Analog Radio Dial Frequency Scale with Active Needle -->
      <div class="analog-frequency-scale" id="analog-dial-scale" title="Radio Megacycles (88 - 108 MHz FM)">
        <div class="dial-markings-track">
          <span class="freq-tick">88</span>
          <span class="freq-tick">92</span>
          <span class="freq-tick">96</span>
          <span class="freq-tick">100</span>
          <span class="freq-tick">104</span>
          <span class="freq-tick">108</span>
          <div class="physical-dial-needle" id="tuning-needle"></div>
        </div>
      </div>

      <!-- Screen 1: Primary Information Screen (LCD/VFD) -->
      <div class="main-lcd-display" id="main-lcd">
        <div class="lcd-header-bar">
          <div class="lcd-station-badge">
            <span class="lcd-badge-tag" id="lcd-channel">CH-13</span>
            <span class="lcd-freq-num" id="lcd-freq">108.0 MHz FM</span>
          </div>
          <div class="lcd-spectrum-visualizer" id="screen-spectrum">
            <div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div>
            <div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div>
            <div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div>
            <div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div>
          </div>
          <button id="btn-pocket-track" class="lcd-dub-btn" type="button" title="Toggle Bilingual Dub (Original / English Dub)">
            <span class="dub-dot" id="pocket-track-led"></span>
            <span id="pocket-track-label">ORG (MR)</span>
          </button>
        </div>

        <div class="lcd-body-content">
          <div class="lcd-title-row">
            <h2 class="lcd-track-title" id="lcd-title">नागपूरचा इतिहास</h2>
            <span class="lcd-curator-name">CURATOR: SIMRAN AILANI</span>
          </div>

          <div class="lcd-meta-row">
            <span class="lcd-category-badge" id="lcd-meta">HISTORY • 9m 18s</span>
            <span class="lcd-signal-lock" id="lcd-signal">SIGNAL: OPTIMAL 99.8%</span>
          </div>

          <div class="lcd-progress-track" id="lcd-progress-track">
            <span class="lcd-time-txt" id="time-current">00:00</span>
            <div class="lcd-progress-bar-bg" id="progress-container">
              <div class="lcd-progress-fill" id="progress-bar"></div>
              <div class="lcd-progress-scrubber-head" id="progress-head"></div>
            </div>
            <span class="lcd-time-txt" id="time-duration">09:18</span>
          </div>
        </div>

        <div class="lcd-teleprompter-strip" id="lcd-transcript-ticker" title="Live Synced English Teleprompter">
          <span class="tp-badge">ENG LIVE</span>
          <div class="tp-marquee-mask">
            <span id="lcd-transcript-text" class="tp-text">Namaskar! If one truly wishes to understand the history of a city...</span>
          </div>
        </div>
      </div>

      <!-- Screen 2: Secondary Scrollable Episode Directory Screen -->
      <div class="directory-screen-chassis" id="directory-screen">
        <div class="dir-header-bar">
          <span class="dir-title">📚 BROADCAST ARCHIVE DIRECTORY</span>
          <span class="dir-count-pill" id="dir-count">13 EPISODES LOADED</span>
        </div>
        <div class="dir-episodes-scroll-list" id="station-list">
        </div>
      </div>

      <!-- Mood Presets Deck -->
      <div class="mood-presets-deck">
        <button type="button" class="mood-preset-key active" data-mood="HISTORY" title="Tune History Stations">
          <span class="mood-icon">🏛️</span>
          <span class="mood-title">HISTORY</span>
          <span class="mood-freq">108.0 MHz</span>
        </button>
        <button type="button" class="mood-preset-key" data-mood="COSMOS" title="Tune Cosmos Stations">
          <span class="mood-icon">🌌</span>
          <span class="mood-title">COSMOS</span>
          <span class="mood-freq">106.0 MHz</span>
        </button>
        <button type="button" class="mood-preset-key" data-mood="MOLECULES" title="Tune Molecules Stations">
          <span class="mood-icon">🧬</span>
          <span class="mood-title">MOLECULES</span>
          <span class="mood-freq">101.8 MHz</span>
        </button>
        <button type="button" class="mood-preset-key" data-mood="ORIGINS" title="Tune Origins Stations">
          <span class="mood-icon">💡</span>
          <span class="mood-title">ORIGINS</span>
          <span class="mood-freq">108.6 MHz</span>
        </button>
        <button type="button" class="mood-preset-key" data-mood="MYSTERY" title="Tune Mystery Stations">
          <span class="mood-icon">📜</span>
          <span class="mood-title">MYSTERY</span>
          <span class="mood-freq">103.6 MHz</span>
        </button>
      </div>
    </section>

    <!-- COLUMN 3 (RIGHT): ARTWORK & DUAL DIAL HUB -->
    <section class="console-column col-artwork-dials">
      <!-- 1. Physical Framed Album Artwork Display -->
      <div class="album-artwork-frame-box" id="album-art-box">
        <div class="artwork-outer-bezel">
          <img id="current-episode-art" src="assets/images/ep13-nagpurcha-itihas.jpg" alt="Current Episode Artwork" class="current-album-img" />
          <div class="artwork-glass-reflection"></div>
          <div class="artwork-overlay-pill">
            <span id="artwork-channel-tag">CH-13</span>
            <span id="artwork-curator-tag">SIMRAN AILANI</span>
          </div>
        </div>
      </div>

      <!-- 2. Dual Knurled Rotary Dials -->
      <div class="dual-rotary-dials-hub">
        <!-- Master Episode Tuner Flywheel -->
        <div class="rotary-station-unit" title="Master Episode Tuner Flywheel">
          <div class="jog-wheel-outer-ring" id="jog-wheel-assembly">
            <div class="jog-wheel-halo" id="jog-wheel-halo"></div>
            <div class="jog-wheel-face" id="jog-wheel-face">
              <div class="jog-dimple"></div>
              <div class="jog-index-notch"></div>
              <div class="jog-center-cap">
                <span class="jog-cap-text" id="jog-cap-txt">TUNER</span>
              </div>
            </div>
          </div>
          <div class="dial-caption-group">
            <span class="dial-title-label">MASTER TUNER</span>
            <div class="dial-nudge-buttons">
              <button type="button" id="jog-step-prev" class="dial-nudge-btn" title="Previous Station">◀</button>
              <button type="button" id="jog-step-next" class="dial-nudge-btn" title="Next Station">▶</button>
            </div>
          </div>
        </div>

        <!-- Directory Scroll Knob -->
        <div class="rotary-station-unit" title="Directory Scroll Knob">
          <div class="secondary-scroll-knob-outer" id="dir-knob-assembly">
            <div class="secondary-knob-halo" id="dir-knob-halo"></div>
            <div class="secondary-knob-face" id="dir-knob-face">
              <div class="secondary-knob-notch"></div>
              <div class="secondary-center-cap">
                <span class="dir-cap-text" id="dir-cap-txt">SCROLL</span>
              </div>
            </div>
          </div>
          <div class="dial-caption-group">
            <span class="dial-title-label">DIR SCROLL</span>
            <div class="dial-nudge-buttons">
              <button type="button" id="dir-scroll-up" class="dial-nudge-btn" title="Scroll Directory Up">▲</button>
              <button type="button" id="dir-scroll-down" class="dial-nudge-btn" title="Scroll Directory Down">▼</button>
            </div>
          </div>
        </div>
      </div>

      <!-- 3. Hardware Spec Plaque -->
      <div class="hardware-spec-plaque">
        <div class="plaque-row">
          <span class="spec-led online"></span>
          <span>13 BROADCASTS • P2P MESH READY</span>
        </div>
        <span class="plaque-sub">100% ZERO-DATA OFFLINE TABLETOP CONSOLE</span>
      </div>
    </section>

  </main>

  <!-- Bottom Mechanical Piano Keys Deck -->
  <footer class="console-bottom-deck">
    <div class="piano-transport-keys-grid">
      <button id="btn-power" class="mechanical-piano-key" type="button" title="Master Power">
        <span class="piano-cap">
          <span class="piano-icon">⏻</span>
          <span class="piano-txt">PWR</span>
        </span>
      </button>

      <button id="btn-prev" class="mechanical-piano-key" type="button" title="Previous Episode">
        <span class="piano-cap">
          <span class="piano-icon">⏮</span>
          <span class="piano-txt">PREV</span>
        </span>
      </button>

      <button id="btn-play" class="mechanical-piano-key" type="button" title="Play / Pause">
        <span class="piano-cap">
          <span class="piano-icon" id="piano-play-icon">▶</span>
          <span class="piano-txt" id="piano-play-txt">PLAY</span>
        </span>
      </button>

      <button id="btn-next" class="mechanical-piano-key" type="button" title="Next Episode">
        <span class="piano-cap">
          <span class="piano-icon">⏭</span>
          <span class="piano-txt">NEXT</span>
        </span>
      </button>

      <button id="btn-scan" class="mechanical-piano-key" type="button" title="Auto Scan FM Band">
        <span class="piano-cap">
          <span class="piano-icon">🔍</span>
          <span class="piano-txt">SCAN</span>
        </span>
      </button>

      <button id="btn-beam" class="mechanical-piano-key" type="button" title="Optical Mesh Beamer">
        <span class="piano-cap">
          <span class="piano-icon">⚡</span>
          <span class="piano-txt">BEAM</span>
        </span>
      </button>

      <button id="btn-dub" class="mechanical-piano-key" type="button" title="Toggle English/Hindi Dub">
        <span class="piano-cap">
          <span class="piano-icon">🌐</span>
          <span class="piano-txt">DUB</span>
        </span>
      </button>

      <button id="btn-mute" class="mechanical-piano-key" type="button" title="Mute Audio">
        <span class="piano-cap">
          <span class="piano-icon" id="mute-icon">🔈</span>
          <span class="piano-txt" id="mute-label">MUTE</span>
        </span>
      </button>
    </div>
  </footer>

  <!-- Complete Fallback Compatibility Nodes -->
  <div id="vu-meter" style="display:none;"><div class="vu-seg"></div></div>
  <div id="progress-wrap" style="display:none;"><div id="progress-fill"></div></div>
  <div id="pilot-lamp" class="pilot-lamp on" style="display:none;"></div>
  <div id="play-icon" style="display:none;"></div>
  <div id="play-label" style="display:none;"></div>
  <div id="pocket-retro-toast" style="display:none;"></div>
  <div id="pocket-beam-modal" style="display:none;"></div>
  <div id="beamer-modal" style="display:none;"></div>
  <button id="prev-btn" style="display:none;"></button>
  <button id="next-btn" style="display:none;"></button>
  <button id="play-btn" style="display:none;"></button>
  <button id="pocket-prev-btn" style="display:none;"></button>
  <button id="pocket-next-btn" style="display:none;"></button>
  <button id="pocket-play-pause-btn" style="display:none;"></button>
</div>
"""

masterpiece_js = """
// =========================================================================
// MASTERPIECE HARDWARE CONSOLE INTERACTIVE ENGINE
// Dual-Mode Architecture: 1978 Vintage Teakwood & Carvaan Neo Panoramic OLED
// =========================================================================

(function initMasterpieceConsole() {
  const chassis = document.getElementById('radio-chassis');
  const themeSwitch = document.getElementById('master-theme-switch');
  const labelVintage = document.getElementById('label-vintage');
  const labelCarvaan = document.getElementById('label-carvaan');

  let currentTheme = localStorage.getItem('gyansetu_masterpiece_theme') || 'vintage-1978';

  function setRadioTheme(themeName) {
    currentTheme = themeName;
    localStorage.setItem('gyansetu_masterpiece_theme', themeName);
    if (chassis) chassis.setAttribute('data-theme', themeName);
    
    if (labelVintage && labelCarvaan) {
      if (themeName === 'carvaan-neo') {
        labelVintage.classList.remove('active');
        labelCarvaan.classList.add('active');
      } else {
        labelVintage.classList.add('active');
        labelCarvaan.classList.remove('active');
      }
    }
  }

  // Set initial theme
  setRadioTheme(currentTheme);

  if (themeSwitch) {
    themeSwitch.addEventListener('click', () => {
      const next = currentTheme === 'vintage-1978' ? 'carvaan-neo' : 'vintage-1978';
      setRadioTheme(next);
      playClickSound(1200, 0.05);
    });
  }

  // Kiosk Fullscreen
  const btnKiosk = document.getElementById('btn-kiosk-fullscreen');
  const kioskBtnText = document.getElementById('kiosk-btn-text');
  if (btnKiosk) {
    btnKiosk.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
        if (kioskBtnText) kioskBtnText.textContent = '✖ EXIT KIOSK';
      } else {
        document.exitFullscreen().catch(() => {});
        if (kioskBtnText) kioskBtnText.textContent = '⛶ TABLETOP KIOSK';
      }
    });
  }

  // Web Audio Context & Analyser for Dual VU Meters & 3D Spectrogram
  let audioCtx = null;
  let analyserNode = null;
  let audioSource = null;
  const audioEl = document.getElementById('radio-audio') || document.querySelector('audio');

  function initAudioDSP() {
    if (audioCtx || !audioEl) return;
    try {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      audioCtx = new AudioContextClass();
      analyserNode = audioCtx.createAnalyser();
      analyserNode.fftSize = 64;
      analyserNode.smoothingTimeConstant = 0.8;
      
      audioSource = audioCtx.createMediaElementSource(audioEl);
      audioSource.connect(analyserNode);
      analyserNode.connect(audioCtx.destination);
    } catch (e) {
      console.warn("Web Audio DSP initialized in fallback mode:", e);
    }
  }

  // Click & Mechanical Sound FX Synthesizer
  function playClickSound(freq = 1000, duration = 0.04) {
    try {
      const ctx = audioCtx || new (window.AudioContext || window.webkitAudioContext)();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(freq, ctx.currentTime);
      gain.gain.setValueAtTime(0.12, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + duration);
    } catch (e) {}
  }

  // Visualizer Render Loop (Ballistic Analog VU Needles + 3D Spectrogram Canvas)
  const needleLeft = document.getElementById('vu-needle-left');
  const needleRight = document.getElementById('vu-needle-right');
  const specCanvas = document.getElementById('neo-spectrogram-canvas');
  let specCtx = specCanvas ? specCanvas.getContext('2d') : null;

  let leftAngle = -35;
  let rightAngle = -35;
  const dataArray = new Uint8Array(32);

  function renderVisualizers() {
    requestAnimationFrame(renderVisualizers);

    let levelL = 0;
    let levelR = 0;

    if (analyserNode && audioEl && !audioEl.paused) {
      analyserNode.getByteFrequencyData(dataArray);
      let sumL = 0;
      let sumR = 0;
      for (let i = 0; i < 16; i++) sumL += dataArray[i];
      for (let i = 16; i < 32; i++) sumR += dataArray[i];
      levelL = sumL / (16 * 255);
      levelR = sumR / (16 * 255);
    } else if (audioEl && !audioEl.paused) {
      levelL = 0.3 + Math.random() * 0.4;
      levelR = 0.3 + Math.random() * 0.4;
    }

    // 1. Vintage Mode: Analog Ballistic Needles
    if (needleLeft && needleRight && currentTheme === 'vintage-1978') {
      const targetL = -35 + (levelL * 70);
      const targetR = -35 + (levelR * 70);
      leftAngle += (targetL - leftAngle) * 0.25;
      rightAngle += (targetR - rightAngle) * 0.25;
      needleLeft.style.transform = `rotate(${leftAngle.toFixed(1)}deg)`;
      needleRight.style.transform = `rotate(${rightAngle.toFixed(1)}deg)`;
    }

    // 2. Carvaan Neo Mode: High-Tech Cyber Spectrogram Canvas
    if (specCtx && currentTheme === 'carvaan-neo') {
      const w = specCanvas.width;
      const h = specCanvas.height;
      specCtx.clearRect(0, 0, w, h);

      // Radar circles in background
      specCtx.strokeStyle = 'rgba(56, 189, 248, 0.15)';
      specCtx.lineWidth = 1;
      const cx = w / 2;
      const cy = h / 2;
      specCtx.beginPath();
      specCtx.arc(cx, cy, 30, 0, Math.PI * 2);
      specCtx.arc(cx, cy, 60, 0, Math.PI * 2);
      specCtx.stroke();

      // 32-Band FFT Bars
      const numBars = 24;
      const barWidth = (w - (numBars * 2)) / numBars;
      for (let i = 0; i < numBars; i++) {
        const val = dataArray[i] || (audioEl && !audioEl.paused ? Math.random() * 160 + 40 : 10);
        const barH = (val / 255) * (h - 20);
        const x = i * (barWidth + 2) + 2;
        const y = h - barH - 4;

        const grad = specCtx.createLinearGradient(0, y, 0, h);
        grad.addColorStop(0, '#00f0ff');
        grad.addColorStop(0.5, '#0284c7');
        grad.addColorStop(1, '#0369a1');

        specCtx.fillStyle = grad;
        specCtx.fillRect(x, y, barWidth, barH);

        // Peak dot
        specCtx.fillStyle = '#ffffff';
        specCtx.fillRect(x, y - 2, barWidth, 1.5);
      }
    }

    // 3. Center Screen Mini Spectrum Bars
    const centerBars = document.querySelectorAll('.lcd-spectrum-visualizer .spec-bar');
    if (centerBars.length > 0) {
      centerBars.forEach((bar, idx) => {
        const val = dataArray[idx % 16] || (audioEl && !audioEl.paused ? Math.random() * 180 + 30 : 6);
        const barH = Math.max(3, (val / 255) * 16);
        bar.style.height = `${barH}px`;
      });
    }
  }

  renderVisualizers();

  // Rotary Dial 1: Master Tuner Flywheel
  const jogFace = document.getElementById('jog-wheel-face');
  const jogHalo = document.getElementById('jog-wheel-halo');
  const jogPrev = document.getElementById('jog-step-prev');
  const jogNext = document.getElementById('jog-step-next');
  let currentJogAngle = 0;

  function rotateJog(deltaDeg) {
    currentJogAngle += deltaDeg;
    if (jogFace) jogFace.style.transform = `rotate(${currentJogAngle}deg)`;
    if (jogHalo) jogHalo.style.transform = `rotate(${currentJogAngle}deg)`;
    playClickSound(800 + Math.abs(currentJogAngle % 360), 0.02);
  }

  if (jogPrev) {
    jogPrev.addEventListener('click', () => {
      rotateJog(-30);
      const prevBtn = document.getElementById('btn-piano-prev') || document.getElementById('prev-btn');
      if (prevBtn) prevBtn.click();
    });
  }

  if (jogNext) {
    jogNext.addEventListener('click', () => {
      rotateJog(30);
      const nextBtn = document.getElementById('btn-piano-next') || document.getElementById('next-btn');
      if (nextBtn) nextBtn.click();
    });
  }

  // Rotary Dial 2: Directory Scroll Knob
  const dirFace = document.getElementById('dir-knob-face');
  const dirHalo = document.getElementById('dir-knob-halo');
  const dirUp = document.getElementById('dir-scroll-up');
  const dirDown = document.getElementById('dir-scroll-down');
  const stationList = document.getElementById('station-list');
  let currentDirAngle = 0;

  function rotateDir(deltaDeg) {
    currentDirAngle += deltaDeg;
    if (dirFace) dirFace.style.transform = `rotate(${currentDirAngle}deg)`;
    if (dirHalo) dirHalo.style.transform = `rotate(${currentDirAngle}deg)`;
    if (stationList) {
      stationList.scrollTop += (deltaDeg > 0 ? 32 : -32);
    }
    playClickSound(1400, 0.015);
  }

  if (dirUp) dirUp.addEventListener('click', () => rotateDir(-25));
  if (dirDown) dirDown.addEventListener('click', () => rotateDir(25));

  // Connect Piano Bottom Keys to Audio Engine
  const pianoPlay = document.getElementById('btn-piano-play');
  const pianoPlayIcon = document.getElementById('piano-play-icon');
  const pianoPlayTxt = document.getElementById('piano-play-txt');
  const pianoPrev = document.getElementById('btn-piano-prev');
  const pianoNext = document.getElementById('btn-piano-next');
  const pianoMute = document.getElementById('btn-piano-mute');
  const pianoDub = document.getElementById('btn-piano-dub');
  const pianoBeam = document.getElementById('btn-piano-beam');

  if (pianoPlay) {
    pianoPlay.addEventListener('click', () => {
      initAudioDSP();
      const legacyPlay = document.getElementById('play-btn') || document.getElementById('pocket-play-pause-btn');
      if (legacyPlay) legacyPlay.click();
      else if (audioEl) {
        if (audioEl.paused) audioEl.play();
        else audioEl.pause();
      }
      playClickSound(1000, 0.04);
    });
  }

  if (audioEl) {
    audioEl.addEventListener('play', () => {
      if (pianoPlayIcon) pianoPlayIcon.textContent = '⏸';
      if (pianoPlayTxt) pianoPlayTxt.textContent = 'PAUSE';
      if (pianoPlay) pianoPlay.classList.add('depressed');
    });
    audioEl.addEventListener('pause', () => {
      if (pianoPlayIcon) pianoPlayIcon.textContent = '▶';
      if (pianoPlayTxt) pianoPlayTxt.textContent = 'PLAY';
      if (pianoPlay) pianoPlay.classList.remove('depressed');
    });
  }

  if (pianoPrev) {
    pianoPrev.addEventListener('click', () => {
      const prev = document.getElementById('prev-btn') || document.getElementById('pocket-prev-btn');
      if (prev) prev.click();
      playClickSound(900, 0.03);
    });
  }

  if (pianoNext) {
    pianoNext.addEventListener('click', () => {
      const next = document.getElementById('next-btn') || document.getElementById('pocket-next-btn');
      if (next) next.click();
      playClickSound(1100, 0.03);
    });
  }

  if (pianoDub) {
    pianoDub.addEventListener('click', () => {
      const dubBtn = document.getElementById('btn-pocket-track');
      if (dubBtn) dubBtn.click();
      playClickSound(1300, 0.03);
    });
  }

  if (pianoBeam) {
    pianoBeam.addEventListener('click', () => {
      const beamModal = document.getElementById('beamer-modal') || document.getElementById('pocket-beam-modal');
      if (beamModal) beamModal.style.display = 'flex';
      playClickSound(1500, 0.04);
    });
  }

  // Modern Fader Click Handlers (Volume, Bass, Treble)
  const faderVol = document.getElementById('touch-fader-vol');
  const faderVolFill = document.getElementById('fader-vol-fill');
  const faderVolVal = document.getElementById('fader-vol-val');
  if (faderVol && audioEl) {
    faderVol.addEventListener('click', (e) => {
      const rect = faderVol.getBoundingClientRect();
      const pct = Math.max(0, Math.min(1, 1 - ((e.clientY - rect.top) / rect.height)));
      audioEl.volume = pct;
      if (faderVolFill) faderVolFill.style.height = `${(pct * 100).toFixed(0)}%`;
      if (faderVolVal) faderVolVal.textContent = `${(pct * 100).toFixed(0)}%`;
      playClickSound(900 + pct * 600, 0.02);
    });
  }

  window.setRadioTheme = setRadioTheme;
})();

"""
