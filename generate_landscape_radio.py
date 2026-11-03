import os
import re

# Read original clean backup
with open('pocket.html.bak', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Custom CSS for Landscape Tabletop Console & Dual Themes
tabletop_css = '''
    /* ==========================================================================
       TABLETOP LANDSCAPE CONSOLE (LENOVO TB-8505X 1280x800 NATIVE)
       Dual-Theme Architecture: 1978 Royal Teak vs. GyanSetu Carvaan Neo-Edition
       ========================================================================== */

    /* Theme 1: 1978 Vintage Teakwood Cabinet (Default) */
    [data-theme="vintage-1978"] {
      --chassis-bg: radial-gradient(circle at 50% 15%, rgba(255, 170, 17, 0.08), transparent 60%), linear-gradient(145deg, #34200f 0%, #1c1006 45%, #2a180b 100%);
      --chassis-border: 3px solid #5a3818;
      --chassis-shadow: 0 35px 80px rgba(0, 0, 0, 0.95), inset 0 2px 3px rgba(255, 200, 120, 0.25), inset 0 -3px 8px rgba(0, 0, 0, 0.9);
      --accent-metal: #d4af37;
      --accent-glow: #ffaa11;
      --dial-glass: radial-gradient(ellipse at 50% 50%, rgba(255, 170, 17, 0.22), transparent 75%), #1c1408;
      --dial-border: 2px solid #734e1c;
      --needle-color: #ff5500;
      --needle-glow: 0 0 12px #ff5500, 0 0 20px #ff3300;
      --screen-bg: #161106;
      --screen-text: #ffaa11;
      --screen-border: 2px solid #6b4d1b;
      --screen-shadow: inset 0 0 25px rgba(255, 157, 0, 0.25);
      --vu-face: linear-gradient(180deg, #f7f1e1 0%, #e8dcbe 100%);
      --vu-text: #2a1c0d;
      --vu-needle: #111111;
      --vu-glow: inset 0 0 16px rgba(255, 170, 17, 0.4), 0 3px 8px rgba(0,0,0,0.6);
      --grille-bg: radial-gradient(circle at 50% 50%, rgba(212, 175, 55, 0.12), transparent 70%), repeating-linear-gradient(45deg, #2a1f14 0, #2a1f14 3px, #18110a 3px, #18110a 6px);
      --grille-border: 2px solid #543919;
      --jog-face: conic-gradient(from 0deg, #aa820a, #e6ca65, #7a5800, #d4af37, #aa820a);
      --jog-cap: radial-gradient(circle, #2b1f14 0%, #150f08 100%);
      --jog-halo: 0 0 16px rgba(255, 170, 17, 0.6);
      --key-bg: linear-gradient(145deg, #3d2817, #1f140a);
      --key-border: 1px solid #734c26;
      --key-text: #ffca66;
      --badge-metal: linear-gradient(135deg, #ffe082 0%, #d4af37 50%, #8c6d12 100%);
      --magic-eye: #10b981;
    }

    /* Theme 2: GyanSetu Carvaan Neo-Edition (Modern-Vintage Fusion) */
    [data-theme="carvaan-neo"] {
      --chassis-bg: linear-gradient(145deg, #f8fafc 0%, #e2e8f0 55%, #cbd5e1 100%);
      --chassis-border: 3px solid #94a3b8;
      --chassis-shadow: 0 35px 80px rgba(0, 0, 0, 0.6), inset 0 2px 2px rgba(255, 255, 255, 0.95), inset 0 -3px 8px rgba(100, 116, 139, 0.4);
      --accent-metal: #0284c7;
      --accent-glow: #06b6d4;
      --dial-glass: radial-gradient(ellipse at 50% 50%, rgba(6, 182, 212, 0.22), transparent 75%), #05131f;
      --dial-border: 2px solid #0284c7;
      --needle-color: #06b6d4;
      --needle-glow: 0 0 12px #06b6d4, 0 0 22px #0891b2;
      --screen-bg: #020c14;
      --screen-text: #22d3ee;
      --screen-border: 2px solid #0284c7;
      --screen-shadow: inset 0 0 30px rgba(6, 182, 212, 0.35);
      --vu-face: linear-gradient(180deg, #091e2f 0%, #030e18 100%);
      --vu-text: #38bdf8;
      --vu-needle: #38bdf8;
      --vu-glow: inset 0 0 18px rgba(6, 182, 212, 0.4), 0 3px 8px rgba(0,0,0,0.6);
      --grille-bg: radial-gradient(circle at 50% 50%, rgba(6, 182, 212, 0.12), transparent 70%), repeating-radial-gradient(circle, #334155 0, #334155 1.5px, #0f172a 1.5px, #0f172a 4px);
      --grille-border: 2px solid #94a3b8;
      --jog-face: conic-gradient(from 0deg, #94a3b8, #ffffff, #64748b, #f1f5f9, #94a3b8);
      --jog-cap: radial-gradient(circle, #0f172a 0%, #020617 100%);
      --jog-halo: 0 0 20px rgba(6, 182, 212, 0.9), inset 0 0 10px rgba(6, 182, 212, 0.6);
      --key-bg: linear-gradient(145deg, #1e293b, #0f172a);
      --key-border: 1px solid #38bdf8;
      --key-text: #e2e8f0;
      --badge-metal: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #64748b 100%);
      --magic-eye: #06b6d4;
    }

    /* Carvaan Neo Theme Specific Overrides for Porcelain Luxury Contrast */
    [data-theme="carvaan-neo"] .console-top-bar {
      border-bottom: 1px solid rgba(0, 0, 0, 0.12);
    }
    [data-theme="carvaan-neo"] .hardware-switch-btn {
      background: #ffffff;
      color: #0f172a;
      border: 1px solid #94a3b8;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1), inset 0 1px 1px #fff;
    }
    [data-theme="carvaan-neo"] .hardware-switch-btn:hover {
      background: #f1f5f9;
      color: #0284c7;
      border-color: #0284c7;
    }
    [data-theme="carvaan-neo"] .master-theme-toggle-zone {
      background: #e2e8f0;
      border-color: #cbd5e1;
      box-shadow: inset 0 2px 4px rgba(0,0,0,0.15);
    }
    [data-theme="carvaan-neo"] .theme-label {
      color: #64748b;
    }
    [data-theme="carvaan-neo"] .theme-label.active {
      color: #0f172a;
      text-shadow: 0 0 8px rgba(6, 182, 212, 0.8);
    }
    [data-theme="carvaan-neo"] .dual-vu-chassis {
      background: #f8fafc;
      border-color: #cbd5e1;
      box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }
    [data-theme="carvaan-neo"] .vu-badge-label {
      color: #475569;
    }
    [data-theme="carvaan-neo"] .wing-left-controls {
      background: #f8fafc;
      border-color: #cbd5e1;
      box-shadow: 0 3px 8px rgba(0,0,0,0.06);
    }
    [data-theme="carvaan-neo"] .knob-label {
      color: #475569;
    }
    [data-theme="carvaan-neo"] .master-jog-wheel-module {
      background: #f8fafc;
      border-color: #cbd5e1;
      box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    }
    [data-theme="carvaan-neo"] .jog-wheel-header {
      color: #475569;
    }
    [data-theme="carvaan-neo"] .heavy-transport-deck {
      background: #f8fafc;
      border-color: #cbd5e1;
      box-shadow: 0 3px 8px rgba(0,0,0,0.06);
    }
    [data-theme="carvaan-neo"] .hardware-spec-plaque {
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
    }
    [data-theme="carvaan-neo"] .station-list-drawer {
      background: #f8fafc !important;
      border-color: #cbd5e1 !important;
    }
    [data-theme="carvaan-neo"] .station-row {
      color: #334155 !important;
    }
    [data-theme="carvaan-neo"] .station-row.active {
      background: #0284c7 !important;
      color: #ffffff !important;
    }

    /* Hardware Top Bar (Header Panel) */
    .console-top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      margin-bottom: 8px;
      padding-bottom: 8px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      width: 100%;
    }

    .top-bar-left,
    .top-bar-right {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .hardware-switch-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.72rem;
      font-weight: 700;
      color: #cbd5e1;
      text-decoration: none;
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.18);
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.15), 0 2px 4px rgba(0,0,0,0.5);
    }
    .hardware-switch-btn:hover {
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.35);
    }
    .btn-notch {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--accent-metal);
      box-shadow: 0 0 6px var(--accent-glow);
    }

    .antenna-segment-indicator {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.64rem;
      font-weight: 800;
      color: #94a3b8;
      letter-spacing: 0.4px;
    }
    .antenna-led {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
      display: inline-block;
    }

    /* Master Physical Knife-Switch (Theme Switcher) */
    .master-theme-toggle-zone {
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid rgba(255, 255, 255, 0.14);
      padding: 4px 12px;
      border-radius: 9999px;
      box-shadow: inset 0 2px 4px rgba(0,0,0,0.7);
    }

    .theme-label {
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #64748b;
      transition: all 0.25s ease;
      user-select: none;
    }
    .theme-label.active {
      color: #ffffff;
      text-shadow: 0 0 10px var(--accent-glow);
    }

    .physical-knife-switch {
      background: none;
      border: none;
      cursor: pointer;
      padding: 0;
      display: inline-flex;
      align-items: center;
    }
    .switch-housing {
      width: 46px;
      height: 22px;
      background: #0f172a;
      border: 1px solid #475569;
      border-radius: 11px;
      position: relative;
      box-shadow: inset 0 2px 4px rgba(0,0,0,0.8);
      transition: all 0.25s ease;
    }
    .switch-lever {
      position: absolute;
      top: 3px;
      left: 3px;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: radial-gradient(circle, #f8fafc 0%, #d4af37 80%, #aa820a 100%);
      box-shadow: 0 1px 4px rgba(0,0,0,0.8), 0 0 8px var(--accent-glow);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), background 0.25s ease;
    }
    .physical-knife-switch.carvaan-active .switch-lever {
      transform: translateX(26px);
      background: radial-gradient(circle, #ffffff 0%, #38bdf8 80%, #0284c7 100%);
    }

    /* Kiosk Button */
    .btn-kiosk {
      background: linear-gradient(135deg, rgba(255, 170, 17, 0.15), rgba(16, 185, 129, 0.15));
      border-color: var(--accent-metal);
      color: #ffffff;
      font-weight: 800;
    }

    /* ==========================================================================
       PANORAMIC STAGE LAYOUT
       ========================================================================== */
    .console-panoramic-stage {
      display: flex;
      flex-direction: column;
      gap: 10px;
      width: 100%;
    }

    /* Media Query for Tablets & Desktop Landscape (Lenovo Tab M8 1280x800 Native) */
    @media (min-width: 900px) and (orientation: landscape), (min-width: 1024px) {
      body {
        padding: 6px 10px !important;
        height: 100vh !important;
        max-height: 100vh !important;
        overflow: hidden !important;
        justify-content: center !important;
      }
      .pocket-top-nav {
        display: none !important;
      }
      .radio-header {
        display: none !important; /* Managed by console-top-bar in landscape */
      }
      .radio-container {
        max-width: 1260px !important;
        width: 100% !important;
        height: 98vh !important;
        max-height: 785px !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
        padding: 12px 18px !important;
        background: var(--chassis-bg) !important;
        border: var(--chassis-border) !important;
        box-shadow: var(--chassis-shadow) !important;
      }
      .console-panoramic-stage {
        display: grid !important;
        grid-template-columns: 29% 42% 29% !important;
        gap: 12px !important;
        align-items: stretch !important;
        flex: 1 1 auto !important;
        min-height: 0 !important;
      }
      .speaker-grille {
        display: none !important; /* Replaced by rich acoustic left module in landscape */
      }
      .control-chassis {
        display: none !important; /* Replaced by heavy transport deck right module in landscape */
      }
      .station-list-drawer {
        display: flex !important;
        flex-direction: row !important;
        overflow-x: auto !important;
        white-space: nowrap !important;
        max-height: 48px !important;
        padding: 4px 8px !important;
        gap: 8px !important;
        background: rgba(0, 0, 0, 0.45) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
        margin-top: 6px !important;
        scrollbar-width: none !important;
      }
      .station-list-drawer::-webkit-scrollbar {
        display: none !important;
      }
      .station-row {
        display: inline-flex !important;
        align-items: center !important;
        gap: 6px !important;
        padding: 4px 10px !important;
        font-size: 0.65rem !important;
        border-radius: 6px !important;
        flex-shrink: 0 !important;
      }
    }

    /* --- MODULE 1: LEFT WING (ACOUSTIC & METERS) --- */
    .console-wing.wing-left {
      display: flex;
      flex-direction: column;
      gap: 8px;
      height: 100%;
    }

    .acoustic-speaker-module {
      flex: 1 1 48%;
      min-height: 110px;
      background: var(--grille-bg);
      border: var(--grille-border);
      border-radius: 12px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: inset 0 3px 8px rgba(0,0,0,0.8), 0 2px 4px rgba(0,0,0,0.5);
      overflow: hidden;
    }

    .speaker-metal-badge {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 6px 14px;
      background: rgba(0, 0, 0, 0.78);
      border: 1px solid var(--accent-metal);
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.8), inset 0 1px 1px rgba(255,255,255,0.25);
      text-align: center;
    }
    .badge-emblem-icon {
      font-size: 1.05rem;
      font-weight: 900;
      background: var(--badge-metal);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      letter-spacing: 1px;
    }
    .badge-brand-sub {
      font-size: 0.58rem;
      font-weight: 800;
      color: #94a3b8;
      letter-spacing: 0.6px;
    }
    .badge-curator {
      font-size: 0.52rem;
      font-weight: 600;
      color: var(--accent-metal);
      opacity: 0.9;
    }

    /* Dual Real-Time Bouncing Needle VU Meters */
    .dual-vu-chassis {
      flex: 1 1 34%;
      background: rgba(0, 0, 0, 0.55);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 10px;
      padding: 8px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: inset 0 2px 5px rgba(0,0,0,0.9);
    }
    .vu-glass-frame {
      display: flex;
      gap: 8px;
      flex: 1 1 auto;
    }
    .vu-analog-meter {
      flex: 1 1 50%;
      background: var(--vu-face);
      border-radius: 6px;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 4px;
      box-shadow: var(--vu-glow);
      min-height: 56px;
    }
    .vu-meter-scale {
      display: flex;
      justify-content: space-between;
      font-size: 0.52rem;
      font-weight: 800;
      color: var(--vu-text);
      z-index: 2;
    }
    .vu-text-db.red {
      color: #dc2626 !important;
    }
    .vu-needle-assembly {
      position: absolute;
      bottom: -6px;
      left: 50%;
      transform: translateX(-50%);
      width: 4px;
      height: 48px;
      display: flex;
      justify-content: center;
      z-index: 3;
    }
    .vu-physical-needle {
      position: absolute;
      bottom: 6px;
      width: 1.8px;
      height: 40px;
      background: var(--vu-needle);
      transform-origin: bottom center;
      transform: rotate(-38deg);
      transition: transform 0.08s cubic-bezier(0.1, 0.9, 0.2, 1);
      box-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    .vu-pivot-cap {
      position: absolute;
      bottom: 2px;
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #1e293b;
      border: 1px solid #475569;
      box-shadow: 0 1px 2px rgba(0,0,0,0.8);
    }
    .vu-channel-tag {
      font-size: 0.50rem;
      font-weight: 900;
      color: var(--vu-text);
      opacity: 0.7;
      text-align: center;
      z-index: 2;
    }
    .vu-label-bar {
      text-align: center;
      margin-top: 3px;
    }
    .vu-badge-label {
      font-size: 0.50rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #64748b;
    }

    /* Left Wing Knobs (Volume & Tone) */
    .wing-left-controls {
      display: flex;
      justify-content: space-around;
      align-items: center;
      background: rgba(0, 0, 0, 0.35);
      border-radius: 8px;
      padding: 6px 4px;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .rotary-control-group {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 3px;
    }
    .knob-label {
      font-size: 0.50rem;
      font-weight: 800;
      color: #94a3b8;
      letter-spacing: 0.3px;
    }
    .rotary-knob-casing {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: radial-gradient(circle, #334155 0%, #0f172a 100%);
      box-shadow: 0 2px 5px rgba(0,0,0,0.8), inset 0 1px 1px rgba(255,255,255,0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid var(--accent-metal);
      cursor: pointer;
    }
    .rotary-knob {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: conic-gradient(from 0deg, #64748b, #cbd5e1, #475569, #f1f5f9, #64748b);
      position: relative;
      transform: rotate(45deg);
      transition: transform 0.15s ease;
      box-shadow: inset 0 1px 1px rgba(255,255,255,0.4);
    }
    .knob-indicator-dot {
      position: absolute;
      top: 3px;
      left: 50%;
      transform: translateX(-50%);
      width: 3px;
      height: 6px;
      background: var(--accent-metal);
      border-radius: 2px;
    }
    .knob-value-display {
      font-size: 0.52rem;
      font-weight: 800;
      color: var(--accent-metal);
    }

    /* --- MODULE 2: CENTER STAGE (TUNER & KNOWLEDGE SCREEN) --- */
    .console-wing.wing-center {
      display: flex;
      flex-direction: column;
      gap: 8px;
      height: 100%;
    }

    /* Analog Tuning Glass with Magic Eye Phosphor Tube */
    .glass-tuner-chassis {
      background: var(--dial-glass);
      border: var(--dial-border);
      border-radius: 12px;
      padding: 6px 12px;
      box-shadow: inset 0 2px 10px rgba(0,0,0,0.9), 0 3px 6px rgba(0,0,0,0.4);
      position: relative;
    }
    .tuner-scale-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.56rem;
      font-weight: 800;
      color: var(--screen-text);
      margin-bottom: 5px;
      letter-spacing: 0.4px;
    }

    .magic-eye-tube-module {
      display: flex;
      align-items: center;
      gap: 5px;
      background: rgba(0,0,0,0.5);
      border: 1px solid rgba(255,255,255,0.1);
      padding: 2px 6px;
      border-radius: 4px;
    }
    .magic-eye-label {
      font-size: 0.48rem;
      font-weight: 800;
      color: #94a3b8;
    }
    .magic-eye-glass {
      width: 38px;
      height: 8px;
      background: #022c22;
      border-radius: 4px;
      border: 1px solid var(--magic-eye);
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: inset 0 0 4px #000;
    }
    .magic-eye-beam {
      width: 26px;
      height: 100%;
      background: var(--magic-eye);
      box-shadow: 0 0 8px var(--magic-eye);
      transition: width 0.12s ease;
    }

    /* Illuminated Knowledge Screen (LCD/VFD/OLED) */
    .knowledge-screen-chassis {
      background: var(--screen-bg);
      border: var(--screen-border);
      border-radius: 12px;
      padding: 8px 12px;
      box-shadow: var(--screen-shadow);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1 1 auto;
      min-height: 135px;
    }
    .screen-status-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
    }
    .status-left {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .screen-badge-channel {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid var(--accent-metal);
      color: #ffffff;
      font-size: 0.68rem;
      font-weight: 900;
      padding: 2px 6px;
      border-radius: 4px;
    }
    .screen-freq-readout {
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--screen-text);
      letter-spacing: 0.5px;
    }

    /* Real-Time 16-Band Spectrum Analyzer */
    .screen-spectrum-bars {
      display: flex;
      align-items: flex-end;
      gap: 2px;
      height: 18px;
      padding: 0 4px;
    }
    .spec-bar {
      width: 3px;
      height: 20%;
      background: var(--accent-glow);
      border-radius: 1px;
      transition: height 0.08s ease;
      box-shadow: 0 0 4px var(--accent-glow);
    }

    .screen-track-pill {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 9999px;
      color: #ffffff;
      font-size: 0.64rem;
      font-weight: 800;
      padding: 3px 8px;
      display: flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;
    }
    .screen-track-pill.dub-active {
      background: rgba(16, 185, 129, 0.25);
      border-color: #10b981;
      color: #a7f3d0;
    }

    /* Main Screen Copy */
    .screen-main-content {
      margin: 6px 0;
    }
    .screen-episode-title {
      font-size: 1.12rem;
      font-weight: 900;
      color: #ffffff;
      line-height: 1.2;
      margin-bottom: 3px;
      text-shadow: 0 0 12px var(--accent-glow);
    }
    .screen-meta-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.62rem;
      font-weight: 700;
      color: #94a3b8;
    }
    .screen-meta-badge {
      color: var(--screen-text);
    }
    .screen-curator-tag {
      font-size: 0.54rem;
      color: var(--accent-metal);
      letter-spacing: 0.5px;
    }

    /* Live English Teleprompter Ticker */
    .screen-ticker-strip {
      background: rgba(0, 0, 0, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 6px;
      padding: 4px 8px;
      display: flex;
      align-items: center;
      gap: 8px;
      overflow: hidden;
    }
    .ticker-badge {
      background: var(--accent-glow);
      color: #000;
      font-size: 0.52rem;
      font-weight: 900;
      padding: 2px 4px;
      border-radius: 3px;
      flex-shrink: 0;
    }
    .ticker-marquee-wrapper {
      overflow: hidden;
      white-space: nowrap;
      flex: 1 1 auto;
    }
    .ticker-text-content {
      font-size: 0.66rem;
      font-weight: 600;
      color: #e2e8f0;
      letter-spacing: 0.3px;
    }

    /* Category & Mood Quick-Presets (Carvaan Style) */
    .console-mood-presets {
      display: flex;
      gap: 6px;
      justify-content: space-between;
    }
    .mood-preset-key {
      flex: 1 1 20%;
      background: var(--key-bg);
      border: var(--key-border);
      border-radius: 6px;
      padding: 6px 3px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
      cursor: pointer;
      box-shadow: 0 2px 4px rgba(0,0,0,0.6);
      transition: all 0.15s ease;
    }
    .mood-preset-key:hover {
      border-color: var(--accent-metal);
      transform: translateY(-1px);
      box-shadow: 0 3px 8px rgba(0,0,0,0.8), 0 0 8px var(--accent-glow);
    }
    .mood-preset-key.active {
      background: var(--accent-glow) !important;
      color: #000 !important;
    }
    .mood-preset-key.active .key-name,
    .mood-preset-key.active .key-ch-tag {
      color: #000 !important;
    }
    .key-icon { font-size: 0.72rem; }
    .key-name { font-size: 0.52rem; font-weight: 900; color: var(--key-text); letter-spacing: 0.4px; }
    .key-ch-tag { font-size: 0.46rem; font-weight: 700; color: #94a3b8; }

    /* --- MODULE 3: RIGHT WING (CARVAAN ROTARY JOG-WHEEL & PIANO DECK) --- */
    .console-wing.wing-right {
      display: flex;
      flex-direction: column;
      gap: 8px;
      height: 100%;
    }

    /* Master Carvaan Rotary Wheel */
    .master-jog-wheel-module {
      flex: 1 1 54%;
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 12px;
      padding: 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.8);
    }
    .jog-wheel-header {
      display: flex;
      justify-content: space-between;
      width: 100%;
      font-size: 0.54rem;
      font-weight: 800;
      color: #94a3b8;
      letter-spacing: 0.4px;
    }
    .jog-step-indicator {
      color: var(--accent-metal);
    }

    .jog-wheel-assembly {
      position: relative;
      width: 100%;
      height: 125px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 14px;
      margin: 4px auto;
    }
    .jog-wheel-outer-ring {
      width: 115px;
      height: 115px;
      aspect-ratio: 1 / 1;
      border-radius: 50%;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .jog-wheel-halo {
      position: absolute;
      inset: -4px;
      border-radius: 50%;
      border: 2px solid var(--accent-glow);
      box-shadow: var(--jog-halo);
      pointer-events: none;
      transition: all 0.3s ease;
    }
    .jog-wheel-face {
      width: 108px;
      height: 108px;
      aspect-ratio: 1 / 1;
      border-radius: 50%;
      background: var(--jog-face);
      border: 3px solid #334155;
      position: relative;
      cursor: grab;
      box-shadow: 0 4px 10px rgba(0,0,0,0.8), inset 0 1px 2px rgba(255,255,255,0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.05s ease-out;
      user-select: none;
    }
    .jog-wheel-face:active {
      cursor: grabbing;
    }
    .jog-dimple {
      position: absolute;
      top: 14px;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: radial-gradient(circle, #0f172a 0%, #334155 80%, #64748b 100%);
      box-shadow: inset 0 2px 3px rgba(0,0,0,0.9), 0 1px 1px rgba(255,255,255,0.4);
    }
    .jog-index-notch {
      position: absolute;
      top: 3px;
      width: 3px;
      height: 7px;
      background: #ef4444;
      border-radius: 1px;
      box-shadow: 0 0 6px #ef4444;
    }
    .jog-center-cap {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--jog-cap);
      border: 1px solid var(--accent-metal);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 4px rgba(0,0,0,0.8);
      pointer-events: none;
    }
    .jog-cap-text {
      font-size: 0.50rem;
      font-weight: 900;
      letter-spacing: 0.8px;
    }

    .jog-arrow-btn {
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
    }
    .jog-arrow-btn:hover {
      background: var(--accent-glow);
      color: #000;
      border-color: var(--accent-glow);
    }

    /* Heavy Mechanical Transport Deck (Piano-Keys) */
    .heavy-transport-deck {
      flex: 1 1 36%;
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      padding: 6px;
    }
    .transport-keys-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 5px;
    }
    .mechanical-key {
      background: var(--key-bg);
      border: var(--key-border);
      border-radius: 6px;
      padding: 5px 3px;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      box-shadow: 0 3px 6px rgba(0,0,0,0.7), inset 0 1px 1px rgba(255,255,255,0.15);
      transition: all 0.1s ease;
    }
    .mechanical-key:active {
      transform: translateY(2px);
      box-shadow: 0 1px 2px rgba(0,0,0,0.8), inset 0 2px 4px rgba(0,0,0,0.6);
    }
    .key-cap {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1px;
      pointer-events: none;
    }
    .key-icon-sym {
      font-size: 0.78rem;
      color: #ffffff;
    }
    .key-title-txt {
      font-size: 0.48rem;
      font-weight: 800;
      color: var(--key-text);
      letter-spacing: 0.4px;
    }
    .mechanical-key.key-power:hover { border-color: #ef4444; }
    .mechanical-key.key-play:hover { border-color: #10b981; }
    .mechanical-key.key-beam {
      border-color: #f59e0b;
      background: linear-gradient(145deg, rgba(245, 158, 11, 0.2), rgba(180, 83, 9, 0.25));
    }
    .mechanical-key.key-beam .key-icon-sym {
      color: #fbbf24;
    }

    /* Plaque Spec Footer */
    .hardware-spec-plaque {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
      padding: 4px;
      background: rgba(0,0,0,0.5);
      border-radius: 6px;
      border: 1px solid rgba(255,255,255,0.06);
    }
    .plaque-row {
      display: flex;
      align-items: center;
      gap: 5px;
      font-size: 0.50rem;
      font-weight: 800;
      color: #94a3b8;
    }
    .plaque-sub {
      font-size: 0.46rem;
      color: var(--accent-metal);
      letter-spacing: 0.4px;
    }
    .plaque-led-dot.green {
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 6px #10b981;
    }
'''

# 2. Panoramic Tabletop HTML Content inside <main class="radio-container" id="radio-chassis">
panoramic_html = '''<main class="radio-container" id="radio-chassis" data-theme="vintage-1978">
    <!-- Corner Screws -->
    <div class="screw tl"></div>
    <div class="screw tr"></div>
    <div class="screw bl"></div>
    <div class="screw br"></div>

    <!-- Hardware Top Bar: Return Switch, Master Knife Toggle & Tabletop Kiosk Lock -->
    <header class="console-top-bar">
      <div class="top-bar-left">
        <a href="index.html" class="hardware-switch-btn" title="Return to Liquid Studio Desktop">
          <span class="btn-notch"></span>
          <span>&#9664; STUDIO</span>
        </a>
        <div class="antenna-segment-indicator">
          <span class="antenna-led"></span>
          <span>HI-GAIN 13-CH</span>
        </div>
      </div>

      <!-- Master Physical 2-Way Theme Knife-Switch -->
      <div class="master-theme-toggle-zone">
        <span class="theme-label vintage-label active" id="label-vintage">&#128251; 1978 VINTAGE</span>
        <button type="button" id="master-theme-switch" class="physical-knife-switch" aria-label="Toggle Master Chassis Theme (1978 Vintage vs Carvaan Neo)">
          <span class="switch-housing">
            <span class="switch-lever"></span>
          </span>
        </button>
        <span class="theme-label carvaan-label" id="label-carvaan">&#127897;&#65039; CARVAAN NEO</span>
      </div>

      <div class="top-bar-right">
        <button type="button" id="btn-kiosk-fullscreen" class="hardware-switch-btn btn-kiosk" title="Lock Tabletop Kiosk Mode (Edge-to-Edge Fullscreen)">
          <span class="btn-notch"></span>
          <span id="kiosk-btn-text">&#9974; TABLETOP KIOSK</span>
        </button>
      </div>
    </header>

    <!-- Header Brand Plate (Mobile Portrait fallback) -->
    <div class="radio-header">
      <div class="brand-group">
        <h1 class="brand-title">&#2332;&#2381;&#2334;&#2366;&#2344;&#2360;&#2375;&#2340;&#2369;</h1>
        <span class="brand-subtitle">TRANSISTOR 13-CH</span>
      </div>
      <div class="pilot-lamp-group">
        <div id="pilot-lamp" class="pilot-lamp on"></div>
        <span class="pilot-label">POWER</span>
      </div>
    </div>

    <!-- 3-Module Panoramic Hardware Stage -->
    <div class="console-panoramic-stage">
      
      <!-- ==============================================
           MODULE 1: LEFT WING - ACOUSTIC & ANALOG VU STAGE
           ============================================== -->
      <section class="console-wing wing-left">
        <!-- Acoustic Speaker Grille -->
        <div class="acoustic-speaker-module">
          <!-- Centered 3D Metallic Badge -->
          <div class="speaker-metal-badge">
            <span class="badge-emblem-icon">&#2332;&#2381;&#2334;&#2366;&#2344;&#2360;&#2375;&#2340;&#2369; &bull; GYANSETU</span>
            <span class="badge-brand-sub">STUDENT BROADCAST NETWORK</span>
            <span class="badge-curator">Curated by Simran Ailani</span>
          </div>
        </div>

        <!-- Dual Analog Needles VU Meter Box (Audio Reactive) -->
        <div class="dual-vu-chassis">
          <div class="vu-glass-frame">
            <!-- Left Channel Meter -->
            <div class="vu-analog-meter meter-left">
              <div class="vu-meter-scale">
                <span class="vu-text-db">-20</span>
                <span class="vu-text-db">-10</span>
                <span class="vu-text-db">-5</span>
                <span class="vu-text-db">0</span>
                <span class="vu-text-db red">+3</span>
              </div>
              <div class="vu-needle-assembly">
                <div id="vu-needle-left" class="vu-physical-needle"></div>
                <div class="vu-pivot-cap"></div>
              </div>
              <span class="vu-channel-tag">CH-L</span>
            </div>

            <!-- Right Channel Meter -->
            <div class="vu-analog-meter meter-right">
              <div class="vu-meter-scale">
                <span class="vu-text-db">-20</span>
                <span class="vu-text-db">-10</span>
                <span class="vu-text-db">-5</span>
                <span class="vu-text-db">0</span>
                <span class="vu-text-db red">+3</span>
              </div>
              <div class="vu-needle-assembly">
                <div id="vu-needle-right" class="vu-physical-needle"></div>
                <div class="vu-pivot-cap"></div>
              </div>
              <span class="vu-channel-tag">CH-R</span>
            </div>
          </div>
          <div class="vu-label-bar">
            <span class="vu-badge-label">DYNAMIC SOUND PRESSURE LEVEL (dB)</span>
          </div>
        </div>

        <!-- Rotary Output Level (Volume) & Tone Controls -->
        <div class="wing-left-controls">
          <div class="rotary-control-group">
            <div class="knob-label">OUTPUT LEVEL</div>
            <div class="rotary-knob-casing" id="knob-volume-container" title="Click or scroll to adjust volume">
              <div class="rotary-knob" id="knob-volume">
                <div class="knob-indicator-dot"></div>
              </div>
            </div>
            <span class="knob-value-display" id="knob-volume-val">85%</span>
          </div>

          <div class="rotary-control-group">
            <div class="knob-label">ACOUSTIC TONE</div>
            <div class="rotary-knob-casing" id="knob-tone-container" title="Click to toggle Warm Tube / Hi-Fi Tone">
              <div class="rotary-knob" id="knob-tone">
                <div class="knob-indicator-dot"></div>
              </div>
            </div>
            <span class="knob-value-display" id="knob-tone-val">RICH</span>
          </div>
        </div>
      </section>

      <!-- ==============================================
           MODULE 2: CENTER STAGE - THE TUNING & KNOWLEDGE ENGINE
           ============================================== -->
      <section class="console-wing wing-center">
        <!-- 1. Analog Tuning Glass Scale & Magic Eye Tube -->
        <div class="glass-tuner-chassis tuning-dial-panel">
          <div class="tuner-scale-header dial-top-row">
            <span>FM MEGACYCLES (88 - 108 MHz)</span>
            <div class="magic-eye-tube-module" title="EM84 Magic Eye Vacuum Phosphor Tube">
              <span class="magic-eye-label">TUNING LOCK</span>
              <div class="magic-eye-glass">
                <div class="magic-eye-beam" id="magic-eye-beam"></div>
              </div>
            </div>
            <span>GLOBAL KNOWLEDGE SCALE</span>
          </div>

          <!-- Sliding Needle Track -->
          <div class="frequency-track" id="freq-track">
            <div class="freq-ticks">
              <div class="tick major" data-freq="88"></div>
              <div class="tick"></div>
              <div class="tick"></div>
              <div class="tick major" data-freq="92"></div>
              <div class="tick"></div>
              <div class="tick"></div>
              <div class="tick major" data-freq="96"></div>
              <div class="tick"></div>
              <div class="tick"></div>
              <div class="tick major" data-freq="100"></div>
              <div class="tick"></div>
              <div class="tick"></div>
              <div class="tick major" data-freq="104"></div>
              <div class="tick"></div>
              <div class="tick"></div>
              <div class="tick major" data-freq="108"></div>
            </div>
            <div id="tuning-needle" class="tuning-needle" style="left: 92%;"></div>
          </div>
        </div>

        <!-- 2. Illuminated Multi-Band Knowledge Screen (LCD/VFD/OLED) -->
        <div class="knowledge-screen-chassis lcd-display">
          <!-- Top Info Bar -->
          <div class="screen-status-bar lcd-channel-row">
            <div class="status-left">
              <span class="screen-badge-channel lcd-channel-badge" id="lcd-channel">CH-13</span>
              <span class="screen-freq-readout lcd-station-freq" id="lcd-freq">108.0 MHz FM</span>
            </div>
            
            <!-- Real-Time 16-Band Spectrum Equalizer Bars -->
            <div class="screen-spectrum-bars" id="screen-spectrum">
              <div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div>
              <div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div>
              <div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div>
              <div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div><div class="spec-bar"></div>
            </div>

            <!-- Bilingual Track Dub Switcher -->
            <button id="btn-pocket-track" class="screen-track-pill lcd-track-switch-btn" type="button" title="Audio Dub Switcher (Original / English Dub)">
              <span class="track-led" id="pocket-track-led"></span>
              <span id="pocket-track-label">ORG (MR)</span>
            </button>
          </div>

          <!-- Main Episode Title -->
          <div class="screen-main-content">
            <h2 class="screen-episode-title lcd-title" id="lcd-title">&#2344;&#2366;&#2327;&#2346;&#2370;&#2352;&#2330;&#2366; &#2311;&#2340;&#2363;&#2361;&#2366;&#2360;</h2>
            <div class="screen-meta-row lcd-meta-row">
              <span id="lcd-meta" class="screen-meta-badge">HISTORY &bull; 9m 18s &bull; AIR-GAP READY</span>
              <span class="screen-curator-tag">CURATED BY SIMRAN AILANI</span>
              <!-- Mobile VU meter bar fallback -->
              <div class="vu-meter-bar" id="vu-meter" style="display:none;">
                <div class="vu-seg active"></div><div class="vu-seg active"></div><div class="vu-seg active"></div>
                <div class="vu-seg active"></div><div class="vu-seg active"></div><div class="vu-seg red"></div>
              </div>
            </div>
          </div>

          <!-- Live English Teleprompter Ticker Strip -->
          <div class="screen-ticker-strip lcd-transcript-ticker" id="lcd-transcript-ticker" title="Live Synced English Teleprompter">
            <span class="ticker-badge lcd-transcript-tag">ENG LIVE</span>
            <div class="ticker-marquee-wrapper">
              <span id="lcd-transcript-text" class="ticker-text-content lcd-transcript-content">Namaskar! If one truly wishes to understand the history of a city...</span>
            </div>
          </div>
        </div>

        <!-- 3. Category & Mood Quick-Presets (Carvaan Style) -->
        <div class="console-mood-presets">
          <button type="button" class="mood-preset-key" data-target-ch="11" title="Cosmic Curiosity & Astronomy">
            <span class="key-icon">&#127756;</span>
            <span class="key-name">COSMOS</span>
            <span class="key-ch-tag">105.0 MHz</span>
          </button>
          <button type="button" class="mood-preset-key" data-target-ch="13" title="Deep Heritage & Nagpur History">
            <span class="key-icon">&#127963;&#65039;</span>
            <span class="key-name">HISTORY</span>
            <span class="key-ch-tag">108.0 MHz</span>
          </button>
          <button type="button" class="mood-preset-key" data-target-ch="9" title="Biochemistry & Consciousness">
            <span class="key-icon">&#129516;</span>
            <span class="key-name">MOLECULES</span>
            <span class="key-ch-tag">101.8 MHz</span>
          </button>
          <button type="button" class="mood-preset-key" data-target-ch="12" title="Scientific Serendipity">
            <span class="key-icon">&#128161;</span>
            <span class="key-name">ORIGINS</span>
            <span class="key-ch-tag">106.5 MHz</span>
          </button>
          <button type="button" class="mood-preset-key" data-target-ch="10" title="Historical Forensic Science">
            <span class="key-icon">&#128220;</span>
            <span class="key-name">MYSTERY</span>
            <span class="key-ch-tag">103.5 MHz</span>
          </button>
        </div>

        <!-- Scrubber Track -->
        <div class="console-scrubber-module">
          <div class="progress-bar-wrap" id="progress-wrap">
            <div class="progress-fill" id="progress-fill"></div>
          </div>
        </div>
      </section>

      <!-- ==============================================
           MODULE 3: RIGHT WING - MASTER ROTARY JOG-WHEEL & HEAVY TRANSPORT DECK
           ============================================== -->
      <section class="console-wing wing-right">
        <!-- The Master Carvaan Rotary Jog-Wheel -->
        <div class="master-jog-wheel-module">
          <div class="jog-wheel-header">
            <span class="jog-wheel-title">MANUAL TUNER FLYWHEEL</span>
            <span class="jog-step-indicator" id="jog-step-indicator">13 BROADCASTS</span>
          </div>

          <div class="jog-wheel-assembly" id="jog-wheel-assembly" title="Drag, scroll, or swipe to manually rotate and tune between stations">
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
          </div>
        </div>

        <!-- Heavy Mechanical Transport Push-Buttons -->
        <div class="heavy-transport-deck">
          <div class="transport-keys-grid">
            <!-- Power Key -->
            <button id="btn-power" class="mechanical-key key-power retro-btn btn-power" title="Power On / Off">
              <div class="key-cap">
                <span class="key-icon-sym">&#9211;</span>
                <span class="key-title-txt">PWR</span>
              </div>
            </button>

            <!-- Prev Key -->
            <button id="btn-prev" class="mechanical-key retro-btn" title="Previous Station">
              <div class="key-cap">
                <span class="key-icon-sym">&#9198;</span>
                <span class="key-title-txt">PREV</span>
              </div>
            </button>

            <!-- Play/Pause Key -->
            <button id="btn-play" class="mechanical-key key-play retro-btn btn-play" title="Play / Pause">
              <div class="key-cap">
                <span class="key-icon-sym" id="play-icon">&#9654;</span>
                <span class="key-title-txt" id="play-label">PLAY</span>
              </div>
            </button>

            <!-- Next Key -->
            <button id="btn-next" class="mechanical-key retro-btn" title="Next Station">
              <div class="key-cap">
                <span class="key-icon-sym">&#9197;</span>
                <span class="key-title-txt">NEXT</span>
              </div>
            </button>

            <!-- Scan Key -->
            <button id="btn-scan" class="mechanical-key retro-btn" title="Frequency Auto-Seek">
              <div class="key-cap">
                <span class="key-icon-sym">&#128269;</span>
                <span class="key-title-txt">SCAN</span>
              </div>
            </button>

            <!-- Beam Key -->
            <button id="btn-beam" class="mechanical-key key-beam retro-btn btn-beam" title="Classroom P2P Mesh Beamer & 20MB QR Fountain">
              <div class="key-cap">
                <span class="key-icon-sym">&#9889;</span>
                <span class="key-title-txt">BEAM</span>
              </div>
            </button>
          </div>
        </div>

        <!-- Chassis Hardware Spec Plaque -->
        <div class="hardware-spec-plaque">
          <div class="plaque-row">
            <span class="plaque-led-dot green"></span>
            <span id="footer-stats-label">13 BROADCASTS &bull; P2P MESH READY</span>
          </div>
          <div class="plaque-row">
            <span id="vault-mode-label" class="plaque-sub">100% ZERO-DATA OFFLINE TABLETOP CONSOLE</span>
          </div>
        </div>
      </section>
    </div>

    <!-- Speaker Slats fallback for mobile portrait -->
    <div class="speaker-grille">
      <div class="slat"></div><div class="slat"></div><div class="slat"></div><div class="slat"></div>
    </div>

    <!-- Quick Station Switcher Drawer -->
    <div class="station-list-drawer" id="station-list">
      <!-- Generated via JS -->
    </div>
  </main>'''

# 3. JavaScript Controller Extensions (Injected ONLY once before the final </script>)
tabletop_js = '''
    // ==========================================================================
    // TABLETOP LANDSCAPE CONSOLE ENGINES (Web Audio VU Meters, Theme Toggle, Jog-Wheel)
    // ==========================================================================

    // 1. Dual-Theme Toggle Engine (1978 Vintage vs. Carvaan Neo)
    const masterThemeSwitch = document.getElementById('master-theme-switch');
    const labelVintage = document.getElementById('label-vintage');
    const labelCarvaan = document.getElementById('label-carvaan');

    function applyRadioTheme(themeName) {
      const chassisEl = document.getElementById('radio-chassis');
      if (chassisEl) chassisEl.setAttribute('data-theme', themeName);
      localStorage.setItem('gyansetu_radio_theme', themeName);
      if (themeName === 'carvaan-neo') {
        if (masterThemeSwitch) masterThemeSwitch.classList.add('carvaan-active');
        if (labelVintage) labelVintage.classList.remove('active');
        if (labelCarvaan) labelCarvaan.classList.add('active');
        playClickSound(500, 0.04);
      } else {
        if (masterThemeSwitch) masterThemeSwitch.classList.remove('carvaan-active');
        if (labelVintage) labelVintage.classList.add('active');
        if (labelCarvaan) labelCarvaan.classList.remove('active');
        playClickSound(750, 0.03);
      }
    }

    if (masterThemeSwitch) {
      masterThemeSwitch.addEventListener('click', (e) => {
        e.preventDefault();
        const chassisEl = document.getElementById('radio-chassis');
        const cur = (chassisEl ? chassisEl.getAttribute('data-theme') : null) || 'vintage-1978';
        applyRadioTheme(cur === 'vintage-1978' ? 'carvaan-neo' : 'vintage-1978');
      });
    }

    // Restore saved theme preference
    const savedTheme = localStorage.getItem('gyansetu_radio_theme') || 'vintage-1978';
    applyRadioTheme(savedTheme);

    // 2. Tabletop Kiosk Fullscreen Lock
    const btnKiosk = document.getElementById('btn-kiosk-fullscreen');
    const kioskBtnText = document.getElementById('kiosk-btn-text');
    if (btnKiosk) {
      btnKiosk.addEventListener('click', () => {
        playClickSound(1000);
        if (!document.fullscreenElement) {
          document.documentElement.requestFullscreen().then(() => {
            if (kioskBtnText) kioskBtnText.textContent = '✕ EXIT KIOSK';
          }).catch(() => {});
        } else {
          document.exitFullscreen().then(() => {
            if (kioskBtnText) kioskBtnText.textContent = '⛶ TABLETOP KIOSK';
          }).catch(() => {});
        }
      });
      document.addEventListener('fullscreenchange', () => {
        if (kioskBtnText) {
          kioskBtnText.textContent = document.fullscreenElement ? '✕ EXIT KIOSK' : '⛶ TABLETOP KIOSK';
        }
      });
    }

    // 3. Web Audio API Real-Time VU Meters & Spectrum Visualizer
    let analyserNode = null;
    let audioSourceNode = null;
    let timeDomainBuffer = null;
    let freqDomainBuffer = null;
    let vuAnimId = null;

    function initWebAudioEngine() {
      if (audioSourceNode) return;
      try {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        analyserNode = audioCtx.createAnalyser();
        analyserNode.fftSize = 64;
        analyserNode.smoothingTimeConstant = 0.75;
        
        audioSourceNode = audioCtx.createMediaElementSource(audio);
        audioSourceNode.connect(analyserNode);
        analyserNode.connect(audioCtx.destination);
        
        timeDomainBuffer = new Uint8Array(analyserNode.frequencyBinCount);
        freqDomainBuffer = new Uint8Array(analyserNode.frequencyBinCount);
        startRealtimeVisualizerLoop();
      } catch (err) {
        console.warn('Web Audio Analyser fallback:', err);
      }
    }

    function startRealtimeVisualizerLoop() {
      const needleLeft = document.getElementById('vu-needle-left');
      const needleRight = document.getElementById('vu-needle-right');
      const spectrumEl = document.getElementById('screen-spectrum');
      const magicEyeBeam = document.getElementById('magic-eye-beam');

      function tick() {
        vuAnimId = requestAnimationFrame(tick);
        if (!isPlaying || !isPoweredOn) {
          if (needleLeft) needleLeft.style.transform = 'rotate(-38deg)';
          if (needleRight) needleRight.style.transform = 'rotate(-38deg)';
          if (spectrumEl) {
            spectrumEl.querySelectorAll('.spec-bar').forEach(b => b.style.height = '15%');
          }
          if (magicEyeBeam) magicEyeBeam.style.width = '10px';
          return;
        }

        if (analyserNode && timeDomainBuffer && freqDomainBuffer) {
          analyserNode.getByteTimeDomainData(timeDomainBuffer);
          analyserNode.getByteFrequencyData(freqDomainBuffer);

          let sumSquares = 0;
          for (let i = 0; i < timeDomainBuffer.length; i++) {
            const norm = (timeDomainBuffer[i] - 128) / 128;
            sumSquares += norm * norm;
          }
          const rms = Math.sqrt(sumSquares / timeDomainBuffer.length);
          const meterNorm = Math.min(1.0, rms * 3.0);

          // Angle range: -38deg to +38deg
          const angleL = -38 + meterNorm * 76 + (Math.random() * 2 - 1);
          const angleR = -38 + Math.min(1.0, meterNorm * 1.05) * 76 + (Math.random() * 2 - 1);

          if (needleLeft) needleLeft.style.transform = `rotate(${Math.max(-42, Math.min(42, angleL))}deg)`;
          if (needleRight) needleRight.style.transform = `rotate(${Math.max(-42, Math.min(42, angleR))}deg)`;

          // 16-band Spectrum bars
          if (spectrumEl) {
            const bars = spectrumEl.querySelectorAll('.spec-bar');
            for (let i = 0; i < bars.length; i++) {
              const val = freqDomainBuffer[i % freqDomainBuffer.length] / 255;
              const h = Math.max(12, Math.min(100, Math.round(val * 100)));
              bars[i].style.height = `${h}%`;
            }
          }

          // Magic Eye Phosphor Beam width
          if (magicEyeBeam) {
            const w = 14 + Math.round(meterNorm * 24);
            magicEyeBeam.style.width = `${w}px`;
          }
        }
      }
      tick();
    }

    // Attach Web Audio initializer on first user gesture
    ['click', 'touchstart'].forEach(ev => {
      document.addEventListener(ev, () => {
        if (!audioSourceNode) initWebAudioEngine();
        if (audioCtx && audioCtx.state === 'suspended') {
          audioCtx.resume();
        }
      }, { once: true });
    });

    // 4. Carvaan Master Rotary Jog-Wheel Engine
    const jogWheelFace = document.getElementById('jog-wheel-face');
    const jogWheelAssembly = document.getElementById('jog-wheel-assembly');
    const jogStepPrev = document.getElementById('jog-step-prev');
    const jogStepNext = document.getElementById('jog-step-next');
    let currentWheelDeg = 0;
    let isJogDragging = false;
    let jogStartAngle = 0;
    let jogBaseDeg = 0;

    function getCenterAngle(clientX, clientY) {
      if (!jogWheelFace) return 0;
      const r = jogWheelFace.getBoundingClientRect();
      const cx = r.left + r.width / 2;
      const cy = r.top + r.height / 2;
      return Math.atan2(clientY - cy, clientX - cx) * (180 / Math.PI);
    }

    if (jogWheelFace) {
      jogWheelFace.addEventListener('mousedown', (e) => {
        isJogDragging = true;
        jogStartAngle = getCenterAngle(e.clientX, e.clientY);
        jogBaseDeg = currentWheelDeg;
        e.preventDefault();
      });

      window.addEventListener('mousemove', (e) => {
        if (!isJogDragging) return;
        const curA = getCenterAngle(e.clientX, e.clientY);
        const diff = curA - jogStartAngle;
        currentWheelDeg = jogBaseDeg + diff;
        jogWheelFace.style.transform = `rotate(${currentWheelDeg}deg)`;
      });

      window.addEventListener('mouseup', () => {
        if (isJogDragging) {
          isJogDragging = false;
        }
      });

      // Touch handlers for Lenovo tablet screen
      jogWheelFace.addEventListener('touchstart', (e) => {
        if (!e.touches[0]) return;
        isJogDragging = true;
        jogStartAngle = getCenterAngle(e.touches[0].clientX, e.touches[0].clientY);
        jogBaseDeg = currentWheelDeg;
      }, { passive: true });

      window.addEventListener('touchmove', (e) => {
        if (!isJogDragging || !e.touches[0]) return;
        const curA = getCenterAngle(e.touches[0].clientX, e.touches[0].clientY);
        const diff = curA - jogStartAngle;
        currentWheelDeg = jogBaseDeg + diff;
        jogWheelFace.style.transform = `rotate(${currentWheelDeg}deg)`;
      }, { passive: true });

      window.addEventListener('touchend', () => {
        if (isJogDragging) isJogDragging = false;
      });

      // Wheel scroll
      if (jogWheelAssembly) {
        jogWheelAssembly.addEventListener('wheel', (e) => {
          e.preventDefault();
          if (e.deltaY > 0) {
            rotateJogStep(1);
          } else {
            rotateJogStep(-1);
          }
        }, { passive: false });
      }
    }

    function rotateJogStep(direction) {
      currentWheelDeg += direction * (360 / 13);
      if (jogWheelFace) jogWheelFace.style.transform = `rotate(${currentWheelDeg}deg)`;
      playClickSound(950, 0.025);
      if (direction > 0) {
        tuneToEpisode(currentIndex + 1, true);
      } else {
        tuneToEpisode(currentIndex - 1, true);
      }
    }

    if (jogStepPrev) jogStepPrev.addEventListener('click', () => rotateJogStep(-1));
    if (jogStepNext) jogStepNext.addEventListener('click', () => rotateJogStep(1));

    // Update jog wheel orientation on station change
    const origUpdateDisplay = updateDisplay;
    updateDisplay = function(ep) {
      origUpdateDisplay(ep);
      const angle = (currentIndex / EPISODES.length) * 360;
      currentWheelDeg = angle;
      if (jogWheelFace) jogWheelFace.style.transform = `rotate(${angle}deg)`;
      
      // Update mood preset active state
      document.querySelectorAll('.mood-preset-key').forEach(btn => {
        const targetCh = parseInt(btn.getAttribute('data-target-ch'), 10);
        if (targetCh === ep.num) {
          btn.classList.add('active');
        } else {
          btn.classList.remove('active');
        }
      });
    };

    // 5. Carvaan Mood Preset Keys
    document.querySelectorAll('.mood-preset-key').forEach(btn => {
      btn.addEventListener('click', () => {
        const targetCh = parseInt(btn.getAttribute('data-target-ch'), 10);
        const targetIdx = EPISODES.findIndex(e => e.num === targetCh);
        if (targetIdx !== -1) {
          playClickSound(800, 0.03);
          tuneToEpisode(targetIdx, true);
        }
      });
    });

    // 6. Volume Knob Controller
    const knobVolContainer = document.getElementById('knob-volume-container');
    const knobVol = document.getElementById('knob-volume');
    const knobVolVal = document.getElementById('knob-volume-val');
    let curVolPct = 85;

    function setVolumePercent(pct) {
      curVolPct = Math.max(0, Math.min(100, pct));
      audio.volume = curVolPct / 100;
      const rot = -135 + (curVolPct / 100) * 270;
      if (knobVol) knobVol.style.transform = `rotate(${rot}deg)`;
      if (knobVolVal) knobVolVal.textContent = `${curVolPct}%`;
    }
    setVolumePercent(85);

    if (knobVolContainer) {
      knobVolContainer.addEventListener('click', () => {
        playClickSound(700);
        // Cycle volume: 85% -> 100% -> 30% -> 60% -> 85%
        if (curVolPct === 85) setVolumePercent(100);
        else if (curVolPct === 100) setVolumePercent(30);
        else if (curVolPct === 30) setVolumePercent(60);
        else setVolumePercent(85);
      });
      knobVolContainer.addEventListener('wheel', (e) => {
        e.preventDefault();
        setVolumePercent(curVolPct + (e.deltaY < 0 ? 5 : -5));
      }, { passive: false });
    }

    // 7. Tone Knob Controller
    const knobToneContainer = document.getElementById('knob-tone-container');
    const knobTone = document.getElementById('knob-tone');
    const knobToneVal = document.getElementById('knob-tone-val');
    const TONES = [
      { name: 'WARM', rot: -90 },
      { name: 'RICH', rot: 0 },
      { name: 'CLEAR', rot: 90 }
    ];
    let curToneIdx = 1;

    if (knobToneContainer) {
      knobToneContainer.addEventListener('click', () => {
        playClickSound(850);
        curToneIdx = (curToneIdx + 1) % TONES.length;
        const t = TONES[curToneIdx];
        if (knobTone) knobTone.style.transform = `rotate(${t.rot}deg)`;
        if (knobToneVal) knobToneVal.textContent = t.name;
      });
    }
'''

# 1. Insert CSS before </style> (only first or last </style>)
style_idx = code.rfind('</style>')
code = code[:style_idx] + tabletop_css + '\n' + code[style_idx:]

# 2. Replace <main class="radio-container" id="radio-chassis"> ... </main>
pattern = re.compile(r'<main class="radio-container" id="radio-chassis">.*?</main>', re.DOTALL)
if pattern.search(code):
    code = pattern.sub(panoramic_html, code)
    print("SUCCESS: replaced radio-chassis HTML")
else:
    print("ERROR: radio-chassis pattern not found!")

# 3. Insert JS before the LAST </script> tag ONLY
last_script_idx = code.rfind('</script>')
code = code[:last_script_idx] + tabletop_js + '\n' + code[last_script_idx:]

# Write to pocket.html
with open('pocket.html', 'w', encoding='utf-8') as f:
    f.write(code)

print("SUCCESS: pocket.html fully generated with clean single script injection!")
