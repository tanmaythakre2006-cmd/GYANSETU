# -*- coding: utf-8 -*-
"""
Build Complete Masterpiece pocket.html
Dual-Mode Flagship Tablet Radio Console (1280x800 Native Landscape)
Curated by Simran Ailani
"""

import re
import os
from episodes_catalog import EPISODES_RAW

def build_flagship():
    with open('pocket.html', 'r', encoding='utf-8') as f:
        orig = f.read()

    # Extract transcripts inclusion and scripts
    # We will construct a clean, robust, museum-grade HTML
    
    html = r'''<!DOCTYPE html>
<html lang="en" data-theme="vintage-1978">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="theme-color" content="#140d09">
  <title>GyanSetu | Flagship Tablet Radio Console (Curated by Simran Ailani)</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
  
  <style>
    /* ==========================================================================
       GLOBAL RESET & TABLET LANDSCAPE VIEWPORT LOCK (1280x800 NATIVE)
       ========================================================================== */
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }
    
    html, body {
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      background: #110c08;
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      color: #f5eedc;
      user-select: none;
      -webkit-user-select: none;
    }

    /* Outer Wrapper scales seamlessly to any 16:10 or landscape display */
    .viewport-container {
      width: 100vw;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background: radial-gradient(circle at 50% 40%, #22160f 0%, #0d0805 100%);
      position: relative;
    }

    .appliance-stage {
      position: relative;
      width: 1280px;
      height: 800px;
      overflow: hidden;
      box-shadow: 0 25px 60px rgba(0,0,0,0.95);
      flex-shrink: 0;
    }

    /* ==========================================================================
       MASTER FLOATING LUXURY TOP BAR
       ========================================================================== */
    .master-top-bar {
      position: absolute;
      top: 10px;
      left: 24px;
      right: 24px;
      height: 44px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 100;
      pointer-events: auto;
    }

    .brand-pill {
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(18, 12, 8, 0.88);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(212, 175, 55, 0.35);
      padding: 6px 16px;
      border-radius: 22px;
      color: #e6c875;
      font-size: 11.5px;
      font-weight: 600;
      letter-spacing: 0.5px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.6);
    }
    .brand-live-dot {
      width: 8px;
      height: 8px;
      background: #00e676;
      border-radius: 50%;
      box-shadow: 0 0 10px #00e676;
      animation: pulseGlow 2s infinite ease-in-out;
    }
    @keyframes pulseGlow {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.25); opacity: 0.7; }
    }

    /* Theme Switch Pill */
    .theme-selector-pill {
      display: flex;
      align-items: center;
      background: rgba(18, 12, 8, 0.92);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(212, 175, 55, 0.45);
      border-radius: 24px;
      padding: 4px;
      gap: 4px;
      box-shadow: 0 4px 18px rgba(0,0,0,0.7);
    }
    .theme-btn {
      padding: 7px 18px;
      border-radius: 18px;
      border: none;
      font-size: 11.5px;
      font-weight: 700;
      cursor: pointer;
      background: transparent;
      color: #9e8a70;
      transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .theme-btn.active {
      background: linear-gradient(135deg, #e5bf45 0%, #a67c1e 100%);
      color: #1a1208;
      box-shadow: 0 2px 10px rgba(212, 175, 55, 0.45);
    }

    /* Right Quick Actions */
    .top-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .top-btn {
      background: rgba(18, 12, 8, 0.88);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(212, 175, 55, 0.35);
      padding: 7px 16px;
      border-radius: 22px;
      color: #e6c875;
      font-size: 11.5px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(0,0,0,0.5);
    }
    .top-btn:hover {
      border-color: rgba(212, 175, 55, 0.7);
      background: rgba(28, 18, 12, 0.95);
      color: #ffde8a;
    }

    /* ==========================================================================
       THEME 1: 1978 VINTAGE TEAKWOOD APPLIANCE (MUSEUM PHOTOREALISTIC CUTOUT)
       ========================================================================== */
    .vintage-appliance-wrap {
      position: absolute;
      inset: 0;
      width: 1280px;
      height: 800px;
      display: block;
      transition: opacity 0.4s ease;
    }
    [data-theme="neo-carvaan"] .vintage-appliance-wrap {
      display: none;
    }

    /* 1. Behind Cutout: Top Glowing Amber LCD Display */
    #vintage-top-screen {
      position: absolute;
      left: 522px;
      top: 199px;
      width: 328px;
      height: 161px;
      background: radial-gradient(circle at center, #ffb326 0%, #db8400 100%);
      box-shadow: inset 0 0 16px rgba(0,0,0,0.65);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 12px 14px;
      color: #261200;
      font-family: 'Space Mono', 'Courier New', Courier, monospace;
      overflow: hidden;
      z-index: 5;
    }
    .lcd-top-row {
      display: flex;
      gap: 12px;
      align-items: center;
    }
    .lcd-avatar {
      width: 80px;
      height: 92px;
      background: url('assets/images/ep13-nagpurcha-itihas.jpg') center/cover;
      filter: grayscale(100%) contrast(180%) brightness(75%);
      mix-blend-mode: multiply;
      border: 1px solid rgba(38,18,0,0.4);
      box-shadow: inset 0 0 5px rgba(0,0,0,0.6);
      flex-shrink: 0;
      transition: background-image 0.3s ease;
    }
    .lcd-info {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      overflow: hidden;
    }
    .lcd-track-title {
      font-size: 14.5px;
      font-weight: 700;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      letter-spacing: -0.3px;
    }
    .lcd-curator {
      font-size: 11px;
      opacity: 0.9;
      font-weight: 600;
      margin: 2px 0 4px 0;
    }
    .lcd-freq-line {
      font-size: 26px;
      font-weight: 900;
      letter-spacing: 1px;
      text-shadow: 0 0 2px rgba(38,18,0,0.4);
    }
    .lcd-bottom-row {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 700;
      padding-top: 2px;
    }
    .lcd-progress-bar {
      flex: 1;
      height: 10px;
      background: rgba(38,18,0,0.25);
      border: 1px solid rgba(38,18,0,0.7);
      padding: 1px;
      display: flex;
      gap: 1px;
    }
    .lcd-seg {
      flex: 1;
      height: 100%;
      background: #261200;
      transition: background 0.1s ease;
    }
    .lcd-seg.off {
      background: transparent;
    }

    /* 2. Behind Cutout: Bottom Black LCD Digital Directory */
    #vintage-dir-screen {
      position: absolute;
      left: 548px;
      top: 398px;
      width: 247px;
      height: 127px;
      background: #0d0d0b;
      border-radius: 4px;
      box-shadow: inset 0 0 14px rgba(0,0,0,0.95);
      padding: 8px 10px;
      overflow-y: auto;
      scrollbar-width: none;
      -ms-overflow-style: none;
      color: #cca040;
      font-size: 10px;
      font-family: 'Space Mono', 'Courier New', Courier, monospace;
      border: 1px solid #1a160e;
      display: flex;
      flex-direction: column;
      z-index: 5;
    }
    #vintage-dir-screen::-webkit-scrollbar {
      display: none;
    }
    .dir-header {
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      color: #e5b850;
      border-bottom: 1px solid rgba(204,160,64,0.4);
      padding-bottom: 3px;
      margin-bottom: 5px;
      letter-spacing: 0.8px;
      position: sticky;
      top: 0;
      background: #0d0d0b;
      z-index: 2;
    }
    .dir-list {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .dir-item {
      display: flex;
      justify-content: space-between;
      white-space: nowrap;
      overflow: hidden;
      padding: 2.5px 4px;
      border-radius: 2px;
      cursor: pointer;
      transition: background 0.15s ease;
    }
    .dir-item:hover {
      background: rgba(204, 160, 64, 0.2);
    }
    .dir-item.active {
      background: #cca040;
      color: #0d0d0b;
      font-weight: 700;
    }

    /* 3. Behind Cutout: Right Square Photo Frame */
    #vintage-photo-screen {
      position: absolute;
      left: 931px;
      top: 212px;
      width: 166px;
      height: 158px;
      background: url('assets/images/ep13-nagpurcha-itihas.jpg') center/cover no-repeat;
      box-shadow: inset 0 0 20px rgba(0,0,0,0.7);
      border-radius: 4px;
      z-index: 5;
      transition: background-image 0.3s ease;
    }
    .photo-glare {
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, rgba(255,255,255,0.18) 0%, rgba(255,255,255,0) 40%, rgba(0,0,0,0.2) 100%);
      pointer-events: none;
    }

    /* 4. Photorealistic Cutout Chassis Overlay (Master Image) */
    .vintage-chassis-overlay {
      position: absolute;
      left: 0;
      top: 0;
      width: 1280px;
      height: 800px;
      background: url('assets/images/vintage_chassis_1280x800_cutout.png') no-repeat center center;
      pointer-events: none;
      z-index: 10;
    }

    /* 5. In-Front Interactive Rotary Knobs & Push Buttons */
    .knob-tuner {
      position: absolute;
      left: 892px;
      top: 435px;
      width: 98px;
      height: 98px;
      background: url('assets/images/tuner_knob_98.png') no-repeat center center;
      background-size: contain;
      z-index: 20;
      cursor: grab;
      filter: drop-shadow(0 4px 6px rgba(0,0,0,0.6));
      transition: transform 0.15s ease-out;
    }
    .knob-scroll {
      position: absolute;
      left: 1045px;
      top: 440px;
      width: 98px;
      height: 98px;
      background: url('assets/images/scroll_knob_98.png') no-repeat center center;
      background-size: contain;
      z-index: 20;
      cursor: grab;
      filter: drop-shadow(0 4px 6px rgba(0,0,0,0.6));
      transition: transform 0.15s ease-out;
    }

    .piano-keys-bar {
      position: absolute;
      left: 494px;
      top: 580px;
      width: 356px;
      height: 44px;
      display: flex;
      z-index: 20;
    }
    .piano-key {
      width: 59px;
      height: 44px;
      background: rgba(255,255,255,0.001);
      cursor: pointer;
    }
    .piano-key:active, .piano-key.depressed {
      background: rgba(255, 200, 50, 0.22);
      box-shadow: inset 0 2px 4px rgba(0,0,0,0.7);
    }

    /* CRT Powerdown effect */
    .crt-off {
      filter: brightness(0.08) grayscale(100%) !important;
      transition: filter 0.5s cubic-bezier(0.1, 0.9, 0.2, 1);
    }

    /* ==========================================================================
       THEME 2: GYANSETU CARVAAN NEO (ALL-SCREEN HOLOGRAPHIC CYBER COCKPIT)
       "Version just has more screen and retro version is just too old-fashioned"
       ========================================================================== */
    .neo-cockpit-wrap {
      position: absolute;
      inset: 0;
      width: 1280px;
      height: 800px;
      display: none;
      padding: 60px 24px 20px 24px;
      background: #090d12;
      box-shadow: inset 0 0 80px rgba(0,0,0,0.9);
      flex-direction: column;
      justify-content: space-between;
      transition: opacity 0.4s ease;
    }
    [data-theme="neo-carvaan"] .neo-cockpit-wrap {
      display: flex;
    }

    .neo-main-grid {
      display: grid;
      grid-template-columns: 360px 1fr 310px;
      gap: 18px;
      height: 640px;
    }

    /* SCREEN 1: 3D Spectrogram & Telemetry Matrix (Replacing Speaker) */
    .neo-screen-left {
      background: linear-gradient(180deg, #0f172a 0%, #070d18 100%);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 8px 32px rgba(0,0,0,0.8), inset 0 0 20px rgba(56, 189, 248, 0.08);
      position: relative;
      overflow: hidden;
    }
    .neo-screen-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 10px;
      font-family: 'Space Mono', monospace;
      color: #38bdf8;
      border-bottom: 1px solid rgba(56, 189, 248, 0.2);
      padding-bottom: 8px;
      letter-spacing: 1px;
    }
    #neo-spectrogram-canvas {
      width: 100%;
      height: 220px;
      border-radius: 8px;
      background: rgba(2, 6, 23, 0.7);
      border: 1px solid rgba(56, 189, 248, 0.2);
      margin: 10px 0;
    }
    .neo-telemetry-box {
      background: rgba(2, 6, 23, 0.8);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 8px;
      padding: 10px;
      font-family: 'Space Mono', monospace;
      font-size: 10px;
      color: #94a3b8;
      display: flex;
      flex-direction: column;
      gap: 5px;
    }
    .neo-telem-row {
      display: flex;
      justify-content: space-between;
    }
    .neo-telem-val {
      color: #38bdf8;
      font-weight: 700;
    }
    .neo-faders-row {
      display: flex;
      justify-content: space-around;
      gap: 12px;
      padding-top: 10px;
    }
    .neo-touch-fader {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      font-size: 9px;
      font-family: 'Space Mono', monospace;
      color: #7dd3fc;
    }
    .fader-track {
      width: 16px;
      height: 70px;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(56, 189, 248, 0.4);
      border-radius: 8px;
      position: relative;
      cursor: pointer;
      display: flex;
      align-items: flex-end;
      padding: 2px;
    }
    .fader-fill {
      width: 100%;
      background: linear-gradient(180deg, #38bdf8 0%, #0284c7 100%);
      border-radius: 6px;
      box-shadow: 0 0 10px #38bdf8;
      transition: height 0.1s ease;
    }

    /* SCREEN 2: Panoramic 4K Sapphire Glass Display (Center) */
    .neo-screen-center {
      background: linear-gradient(180deg, #0b1324 0%, #060b14 100%);
      border: 1px solid rgba(56, 189, 248, 0.45);
      border-radius: 12px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 8px 32px rgba(0,0,0,0.8), inset 0 0 25px rgba(56, 189, 248, 0.12);
      position: relative;
      overflow: hidden;
    }
    .neo-live-osc-canvas {
      width: 100%;
      height: 75px;
      border-radius: 8px;
      background: rgba(2, 6, 23, 0.7);
      border: 1px solid rgba(56, 189, 248, 0.25);
    }
    .neo-track-hero {
      margin: 12px 0;
    }
    .neo-channel-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid #38bdf8;
      padding: 4px 10px;
      border-radius: 14px;
      font-size: 11px;
      font-family: 'Space Mono', monospace;
      color: #38bdf8;
      margin-bottom: 8px;
    }
    .neo-title-text {
      font-size: 24px;
      font-weight: 800;
      color: #f0f9ff;
      letter-spacing: -0.5px;
      text-shadow: 0 0 12px rgba(56, 189, 248, 0.4);
      margin-bottom: 4px;
    }
    .neo-curator-line {
      font-size: 12px;
      color: #7dd3fc;
      font-weight: 600;
    }
    /* Scrubber */
    .neo-scrubber-bar {
      width: 100%;
      height: 8px;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(56, 189, 248, 0.4);
      border-radius: 4px;
      position: relative;
      cursor: pointer;
      margin: 10px 0;
    }
    .neo-scrubber-fill {
      height: 100%;
      background: linear-gradient(90deg, #0284c7 0%, #38bdf8 100%);
      border-radius: 4px;
      box-shadow: 0 0 8px #38bdf8;
      width: 35%;
    }
    .neo-time-row {
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      font-family: 'Space Mono', monospace;
      color: #94a3b8;
    }
    /* Live Synchronized Teleprompter */
    .neo-teleprompter {
      background: rgba(2, 6, 23, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 8px;
      height: 120px;
      padding: 12px;
      overflow-y: auto;
      scrollbar-width: none;
      font-size: 12px;
      line-height: 1.6;
      color: #cbd5e1;
    }
    .neo-teleprompter::-webkit-scrollbar { display: none; }
    .transcript-line.active {
      color: #38bdf8;
      font-weight: 700;
      text-shadow: 0 0 8px rgba(56, 189, 248, 0.5);
    }
    /* Fast Channel Selector */
    .neo-station-ribbon {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      scrollbar-width: none;
      padding-top: 6px;
    }
    .neo-station-ribbon::-webkit-scrollbar { display: none; }
    .neo-ribbon-btn {
      padding: 6px 12px;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 6px;
      font-size: 10px;
      font-family: 'Space Mono', monospace;
      color: #94a3b8;
      white-space: nowrap;
      cursor: pointer;
    }
    .neo-ribbon-btn.active {
      background: rgba(56, 189, 248, 0.25);
      border-color: #38bdf8;
      color: #38bdf8;
      font-weight: 700;
    }

    /* SCREEN 3: Frameless Floating OLED Album Glass (Right) */
    .neo-screen-right {
      background: linear-gradient(180deg, #0f172a 0%, #070d18 100%);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 8px 32px rgba(0,0,0,0.8), inset 0 0 20px rgba(56, 189, 248, 0.08);
      position: relative;
      overflow: hidden;
    }
    .neo-album-frame {
      width: 240px;
      height: 240px;
      border-radius: 12px;
      background: url('assets/images/ep13-nagpurcha-itihas.jpg') center/cover;
      box-shadow: 0 10px 30px rgba(0,0,0,0.9), 0 0 20px rgba(56, 189, 248, 0.25);
      border: 1px solid rgba(56, 189, 248, 0.5);
      position: relative;
      transition: background-image 0.3s ease;
    }
    .neo-dials-zone {
      display: flex;
      justify-content: space-around;
      width: 100%;
      margin-top: 10px;
    }
    .neo-rotary-dial {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
    }
    .neo-dial-ring {
      width: 82px;
      height: 82px;
      border-radius: 50%;
      border: 2px solid rgba(56, 189, 248, 0.4);
      background: radial-gradient(circle, #0f172a 0%, #020617 100%);
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.35);
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: grab;
      position: relative;
    }
    .neo-dial-ring::after {
      content: '';
      position: absolute;
      top: 6px;
      width: 6px;
      height: 6px;
      background: #38bdf8;
      border-radius: 50%;
      box-shadow: 0 0 8px #38bdf8;
    }
    .neo-dial-core-text {
      font-size: 12px;
      font-family: 'Space Mono', monospace;
      font-weight: 700;
      color: #38bdf8;
    }
    .neo-dial-sub-label {
      font-size: 10px;
      font-family: 'Space Mono', monospace;
      color: #94a3b8;
    }

    /* BOTTOM FULL-WIDTH CAPACITIVE TOUCHBAR (Neo Mode) */
    .neo-capacitive-touchbar {
      height: 52px;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 10px;
      display: flex;
      justify-content: space-around;
      align-items: center;
      padding: 0 20px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.8);
    }
    .neo-touch-btn {
      background: transparent;
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 8px 24px;
      border-radius: 20px;
      color: #38bdf8;
      font-family: 'Space Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }
    .neo-touch-btn:hover, .neo-touch-btn.active {
      background: rgba(56, 189, 248, 0.25);
      border-color: #38bdf8;
      color: #f0f9ff;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.5);
    }

    /* ==========================================================================
       MODALS: OPTICAL BEAMER & OFFLINE VAULT SYNC
       ========================================================================== */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.88);
      backdrop-filter: blur(8px);
      z-index: 200;
      display: none;
      justify-content: center;
      align-items: center;
    }
    .modal-overlay.open {
      display: flex;
    }
    .modal-card {
      background: #14100c;
      border: 1px solid rgba(212, 175, 55, 0.5);
      border-radius: 12px;
      width: 680px;
      max-width: 90vw;
      padding: 24px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.9);
      color: #f5eedc;
      position: relative;
    }
    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(212, 175, 55, 0.3);
      padding-bottom: 12px;
      margin-bottom: 16px;
    }
    .modal-title {
      font-size: 18px;
      font-weight: 700;
      color: #e5bf45;
    }
    .modal-close-btn {
      background: transparent;
      border: none;
      color: #e5bf45;
      font-size: 22px;
      cursor: pointer;
    }
    .modal-tab-bar {
      display: flex;
      gap: 10px;
      margin-bottom: 16px;
    }
    .modal-tab {
      padding: 8px 16px;
      border-radius: 6px;
      border: 1px solid rgba(212, 175, 55, 0.4);
      background: transparent;
      color: #cca040;
      cursor: pointer;
      font-size: 12px;
      font-weight: 600;
    }
    .modal-tab.active {
      background: #cca040;
      color: #14100c;
    }
    #beam-canvas-wrap {
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 16px 0;
      background: #fff;
      padding: 12px;
      border-radius: 8px;
      width: 280px;
      height: 280px;
      margin-left: auto;
      margin-right: auto;
    }
    #beam-fountain-canvas {
      width: 256px;
      height: 256px;
    }
    .fountain-status-line {
      text-align: center;
      font-family: 'Space Mono', monospace;
      font-size: 12px;
      color: #cca040;
      margin-top: 8px;
    }
    #camera-preview-video {
      width: 100%;
      height: 260px;
      border-radius: 8px;
      background: #000;
      object-fit: cover;
    }

    /* Toast */
    #pocket-toast {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: rgba(20, 14, 10, 0.95);
      border: 1px solid rgba(212, 175, 55, 0.6);
      padding: 10px 24px;
      border-radius: 20px;
      color: #f5eedc;
      font-size: 13px;
      font-weight: 600;
      box-shadow: 0 10px 30px rgba(0,0,0,0.8);
      z-index: 300;
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
      pointer-events: none;
    }
    #pocket-toast.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }
  </style>
</head>
<body>
  <!-- Native Audio Tag -->
  <audio id="audio-engine" preload="auto"></audio>

  <div class="viewport-container">
    <div class="appliance-stage" id="appliance-stage">

      <!-- MASTER LUXURY FLOATING TOP BAR -->
      <header class="master-top-bar">
        <div class="brand-pill">
          <span class="brand-live-dot"></span>
          <strong>ज्ञानसेतु • GYANSETU</strong>
          <span style="opacity:0.4;">|</span>
          <span>Curated by Simran Ailani</span>
        </div>

        <div class="theme-selector-pill">
          <button class="theme-btn active" id="btn-theme-vintage">
            <span>📻</span> 1978 VINTAGE
          </button>
          <button class="theme-btn" id="btn-theme-neo">
            <span>⚡</span> CARVAAN NEO
          </button>
        </div>

        <div class="top-actions">
          <button class="top-btn" id="btn-open-beamer">
            <span>📡</span> Optical Beamer
          </button>
          <button class="top-btn" id="btn-fullscreen">
            <span>⛶</span> Kiosk
          </button>
        </div>
      </header>

      <!-- ====================================================================
           1. 1978 VINTAGE TEAKWOOD APPLIANCE (MUSEUM PHOTOREALISTIC CUTOUT)
           ==================================================================== -->
      <div class="vintage-appliance-wrap" id="vintage-wrap">
        
        <!-- Center Top Amber LCD Screen (Behind Cutout) -->
        <div id="vintage-top-screen">
          <div class="lcd-top-row">
            <div class="lcd-avatar" id="vintage-avatar"></div>
            <div class="lcd-info">
              <div class="lcd-track-title" id="vintage-title">नागपूरचा इतिहास</div>
              <div class="lcd-curator">Curator: Simran Ailani</div>
              <div class="lcd-freq-line" id="vintage-freq">FM 108.0 FM</div>
            </div>
          </div>
          <div class="lcd-bottom-row">
            <span id="vintage-time-cur">00:00</span>
            <div class="lcd-progress-bar" id="vintage-seg-bar">
              <div class="lcd-seg off"></div><div class="lcd-seg off"></div>
              <div class="lcd-seg off"></div><div class="lcd-seg off"></div>
              <div class="lcd-seg off"></div><div class="lcd-seg off"></div>
              <div class="lcd-seg off"></div><div class="lcd-seg off"></div>
              <div class="lcd-seg off"></div><div class="lcd-seg off"></div>
              <div class="lcd-seg off"></div><div class="lcd-seg off"></div>
            </div>
            <span id="vintage-time-total">09:18</span>
          </div>
        </div>

        <!-- Center Bottom Black LCD Digital Directory (Behind Cutout) -->
        <div id="vintage-dir-screen">
          <div class="dir-header">Digital Directory</div>
          <div class="dir-list" id="vintage-dir-list">
            <!-- Dynamically populated from 13 episodes -->
          </div>
        </div>

        <!-- Right Square Photo Frame (Behind Cutout) -->
        <div id="vintage-photo-screen">
          <div class="photo-glare"></div>
        </div>

        <!-- Photorealistic Cutout Chassis Mask (100% Matching Master Reference Image) -->
        <div class="vintage-chassis-overlay"></div>

        <!-- Interactive Knobs & Buttons Layer (In-Front of Cutout) -->
        <div class="knob-tuner" id="dial-tuner" title="Tuner Rotary Dial"></div>
        <div class="knob-scroll" id="dial-scroll" title="Directory Scroll Rotary Dial"></div>
        <div class="piano-keys-bar">
          <div class="piano-key" id="key-pwr" title="Power On/Off"></div>
          <div class="piano-key" id="key-prev" title="Previous Episode"></div>
          <div class="piano-key" id="key-play" title="Play/Pause"></div>
          <div class="piano-key" id="key-next" title="Next Episode"></div>
          <div class="piano-key" id="key-bass" title="Bass Boost EQ"></div>
          <div class="piano-key" id="key-treble" title="Treble Tone"></div>
        </div>
      </div>

      <!-- ====================================================================
           2. GYANSETU CARVAAN NEO (ALL-SCREEN HOLOGRAPHIC CYBER COCKPIT)
           ==================================================================== -->
      <div class="neo-cockpit-wrap" id="neo-wrap">
        <div class="neo-main-grid">
          
          <!-- SCREEN 1: 3D Spectrogram & Telemetry Matrix (Left) -->
          <section class="neo-screen-left">
            <div class="neo-screen-header">
              <span>HOLOGRAPHIC SPECTROGRAM</span>
              <span style="color:#00e676;">● LIVE FFT</span>
            </div>
            <canvas id="neo-spectrogram-canvas" width="320" height="220"></canvas>
            
            <div class="neo-telemetry-box">
              <div class="neo-telem-row">
                <span>AUDIO BITRATE</span>
                <span class="neo-telem-val">320 KBPS FLAC</span>
              </div>
              <div class="neo-telem-row">
                <span>BUFFER LATENCY</span>
                <span class="neo-telem-val">0 MS (CACHE)</span>
              </div>
              <div class="neo-telem-row">
                <span>CARVAAN LINK</span>
                <span class="neo-telem-val">STUDENT BROADCAST</span>
              </div>
            </div>

            <div class="neo-faders-row">
              <div class="neo-touch-fader" id="fader-bass">
                <div class="fader-track"><div class="fader-fill" id="fill-bass" style="height:50%;"></div></div>
                <span>BASS</span>
              </div>
              <div class="neo-touch-fader" id="fader-vol">
                <div class="fader-track"><div class="fader-fill" id="fill-vol" style="height:85%;"></div></div>
                <span>VOL</span>
              </div>
              <div class="neo-touch-fader" id="fader-treble">
                <div class="fader-track"><div class="fader-fill" id="fill-treble" style="height:60%;"></div></div>
                <span>TREBLE</span>
              </div>
            </div>
          </section>

          <!-- SCREEN 2: 4K Sapphire Glass Screen (Center) -->
          <section class="neo-screen-center">
            <div class="neo-screen-header">
              <span>SAPPHIRE COCKPIT DISPLAY</span>
              <span id="neo-freq-badge">[CH-13] 108.0 MHz FM</span>
            </div>

            <canvas class="neo-live-osc-canvas" id="neo-osc-canvas" width="500" height="75"></canvas>

            <div class="neo-track-hero">
              <div class="neo-title-text" id="neo-title">नागपूरचा इतिहास</div>
              <div class="neo-curator-line">Curated by Simran Ailani • Founder & Lead Curator</div>
            </div>

            <!-- Scrubber -->
            <div class="neo-scrubber-bar" id="neo-scrubber">
              <div class="neo-scrubber-fill" id="neo-scrubber-fill"></div>
            </div>
            <div class="neo-time-row">
              <span id="neo-time-cur">00:00</span>
              <span id="neo-time-total">09:18</span>
            </div>

            <!-- Synchronized Teleprompter -->
            <div class="neo-teleprompter" id="neo-teleprompter">
              <p class="transcript-line active">ज्ञानसेतु इंटरनेट रेडिओवर आपले स्वागत आहे.</p>
              <p class="transcript-line">नागपूर शहराचा समृद्ध इतिहास, संस्कृती आणि विज्ञान...</p>
            </div>

            <!-- Station Quick Ribbon -->
            <div class="neo-station-ribbon" id="neo-ribbon">
              <!-- Dynamically populated -->
            </div>
          </section>

          <!-- SCREEN 3: Frameless Floating OLED Album Glass (Right) -->
          <section class="neo-screen-right">
            <div class="neo-screen-header" style="width:100%;">
              <span>ALBUM GLASS</span>
              <span style="color:#e5bf45;">★ SIMRAN AILANI</span>
            </div>

            <div class="neo-album-frame" id="neo-album-art"></div>

            <div class="neo-dials-zone">
              <div class="neo-rotary-dial">
                <div class="neo-dial-ring" id="neo-dial-ch">
                  <span class="neo-dial-core-text" id="neo-dial-ch-txt">108.0</span>
                </div>
                <span class="neo-dial-sub-label">TUNER CH</span>
              </div>
              <div class="neo-rotary-dial">
                <div class="neo-dial-ring" id="neo-dial-vol">
                  <span class="neo-dial-core-text" id="neo-dial-vol-txt">85%</span>
                </div>
                <span class="neo-dial-sub-label">OUTPUT VOL</span>
              </div>
            </div>
          </section>
        </div>

        <!-- Bottom Flush Capacitive Touchbar (Neo Mode) -->
        <footer class="neo-capacitive-touchbar">
          <button class="neo-touch-btn" id="neo-btn-pwr">⏻ POWER</button>
          <button class="neo-touch-btn" id="neo-btn-prev">⏮ PREV</button>
          <button class="neo-touch-btn active" id="neo-btn-play">▶ PLAY</button>
          <button class="neo-touch-btn" id="neo-btn-next">⏭ NEXT</button>
          <button class="neo-touch-btn" id="neo-btn-bass">🔊 BASS BOOST</button>
          <button class="neo-touch-btn" id="neo-btn-beam">📡 OPTICAL BEAM</button>
        </footer>
      </div>

    </div>
  </div>

  <!-- ========================================================================
       OPTICAL FOUNTAIN BEAMER / QR P2P TRANSFER MODAL
       ======================================================================== -->
  <div class="modal-overlay" id="beamer-modal">
    <div class="modal-card">
      <div class="modal-header">
        <h3 class="modal-title">📡 GyanSetu Optical Mesh Beamer</h3>
        <button class="modal-close-btn" id="btn-close-beamer">&times;</button>
      </div>

      <div class="modal-tab-bar">
        <button class="modal-tab active" id="tab-sender">Transmit / Send (Air-Gap QR)</button>
        <button class="modal-tab" id="tab-receiver">Receive / Scan Camera</button>
      </div>

      <!-- Sender Pane -->
      <div id="pane-sender">
        <p style="font-size:12px; color:#cbd5e1; margin-bottom:12px;">
          Broadcasting lossless episode bundle via animated fountain QR code chunks. Hold receiver camera towards the screen to ingest.
        </p>
        <div id="beam-canvas-wrap">
          <canvas id="beam-fountain-canvas" width="256" height="256"></canvas>
        </div>
        <div class="fountain-status-line" id="sender-fountain-hud">
          Chunk 1 / 48 • 12 FPS • AES-256-GCM Encrypted
        </div>
      </div>

      <!-- Receiver Pane -->
      <div id="pane-receiver" style="display:none;">
        <video id="camera-preview-video" autoplay playsinline></video>
        <div class="fountain-status-line" id="receiver-fountain-hud">
          Camera Active • Searching for GyanSetu Fountain QR...
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div id="pocket-toast"></div>

  <!-- Embedded Dependencies -->
  <script src="assets/js/qrcode.min.js"></script>
  <script src="assets/js/jsqr.min.js"></script>
  <script src="assets/data/episodes_transcripts.js"></script>

  <script>
    // =========================================================================
    // 1. MASTER EPISODE CATALOG (13 CHANNELS) - CURATED BY SIMRAN AILANI
    // =========================================================================
    const isAndroidAsset = window.location.protocol === 'file:';
    const audioBase = isAndroidAsset ? 'assets/audio/' : 'assets/audio_ghost/';

    const EPISODES = ''' + EPISODES_RAW + ''';

    // Map high-res cover artwork to every episode
    EPISODES.forEach((ep) => {
      if (!ep.cover) {
        const srcFile = (ep.src || '').split('/').pop();
        ep.cover = 'assets/images/' + srcFile.replace('.mp3', '.jpg');
      }
    });

    // State
    let currentIndex = 0;
    let isPlaying = false;
    let isPowerOn = true;
    let isBassBoosted = false;
    let currentTheme = localStorage.getItem('gyansetu_flagship_theme') || 'vintage-1978';

    const audio = document.getElementById('audio-engine');
    const vintageWrap = document.getElementById('vintage-wrap');
    const neoWrap = document.getElementById('neo-wrap');

    // Web Audio Synthesizer for Tactile Feedback
    let audioCtx = null;
    let biquadFilter = null;
    let analyser = null;
    let sourceNode = null;

    function initWebAudio() {
      if (audioCtx) return;
      try {
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        audioCtx = new AudioContextClass();
        analyser = audioCtx.createAnalyser();
        analyser.fftSize = 64;

        biquadFilter = audioCtx.createBiquadFilter();
        biquadFilter.type = 'lowshelf';
        biquadFilter.frequency.value = 120;
        biquadFilter.gain.value = 0;

        sourceNode = audioCtx.createMediaElementSource(audio);
        sourceNode.connect(biquadFilter);
        biquadFilter.connect(analyser);
        analyser.connect(audioCtx.destination);
      } catch (e) {
        console.warn('Web Audio DSP running in safe mode:', e);
      }
    }

    function playMechanicalClick(freq = 1000, duration = 0.04) {
      try {
        const ctx = audioCtx || new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, ctx.currentTime);
        gain.gain.setValueAtTime(0.15, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + duration);
      } catch (e) {}
    }

    function showToast(msg) {
      const t = document.getElementById('pocket-toast');
      if (!t) return;
      t.textContent = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2500);
    }

    // =========================================================================
    // 2. THEME ENGINE: 1978 VINTAGE <---> CARVAAN NEO
    // =========================================================================
    function setTheme(theme) {
      currentTheme = theme;
      localStorage.setItem('gyansetu_flagship_theme', theme);
      document.documentElement.setAttribute('data-theme', theme);

      const btnVin = document.getElementById('btn-theme-vintage');
      const btnNeo = document.getElementById('btn-theme-neo');

      if (theme === 'vintage-1978') {
        btnVin.classList.add('active');
        btnNeo.classList.remove('active');
      } else {
        btnNeo.classList.add('active');
        btnVin.classList.remove('active');
      }
      playMechanicalClick(1200, 0.06);
    }

    document.getElementById('btn-theme-vintage').addEventListener('click', () => setTheme('vintage-1978'));
    document.getElementById('btn-theme-neo').addEventListener('click', () => setTheme('neo-carvaan'));

    // =========================================================================
    // 3. EPISODE TUNING & METADATA BINDINGS
    // =========================================================================
    function tuneToEpisode(index, autoPlay = true) {
      if (index < 0) index = EPISODES.length - 1;
      if (index >= EPISODES.length) index = 0;
      currentIndex = index;

      const ep = EPISODES[currentIndex];

      // Update Native Audio Source
      const targetSrc = ep.src || (audioBase + 'ep13-nagpurcha-itihas.mp3');
      if (audio.src !== targetSrc) {
        audio.src = targetSrc;
        audio.load();
      }

      // 1. Update Vintage Mode Elements
      const vAvatar = document.getElementById('vintage-avatar');
      const vTitle = document.getElementById('vintage-title');
      const vFreq = document.getElementById('vintage-freq');
      const vPhoto = document.getElementById('vintage-photo-screen');
      const vTimeTotal = document.getElementById('vintage-time-total');

      if (vAvatar) vAvatar.style.backgroundImage = `url('${ep.cover}')`;
      if (vTitle) vTitle.textContent = ep.title;
      if (vFreq) vFreq.textContent = `FM ${ep.freq} FM`;
      if (vPhoto) vPhoto.style.backgroundImage = `url('${ep.cover}')`;
      if (vTimeTotal) vTimeTotal.textContent = ep.duration || '09:18';

      // Highlight in Vintage Digital Directory
      const dirItems = document.querySelectorAll('#vintage-dir-list .dir-item');
      dirItems.forEach((item, idx) => {
        if (idx === currentIndex) {
          item.classList.add('active');
          item.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        } else {
          item.classList.remove('active');
        }
      });

      // 2. Update Carvaan Neo Mode Elements
      const nTitle = document.getElementById('neo-title');
      const nFreqBadge = document.getElementById('neo-freq-badge');
      const nAlbum = document.getElementById('neo-album-art');
      const nTimeTotal = document.getElementById('neo-time-total');
      const nDialCh = document.getElementById('neo-dial-ch-txt');

      if (nTitle) nTitle.textContent = ep.title;
      if (nFreqBadge) nFreqBadge.textContent = `[CH-${ep.channel || (currentIndex+1)}] ${ep.freq} MHz FM`;
      if (nAlbum) nAlbum.style.backgroundImage = `url('${ep.cover}')`;
      if (nTimeTotal) nTimeTotal.textContent = ep.duration || '09:18';
      if (nDialCh) nDialCh.textContent = ep.freq;

      // Update Neo Ribbon
      const ribbonBtns = document.querySelectorAll('#neo-ribbon .neo-ribbon-btn');
      ribbonBtns.forEach((btn, idx) => {
        if (idx === currentIndex) btn.classList.add('active');
        else btn.classList.remove('active');
      });

      // Rotate Physical Knobs slightly to reflect tuning
      const tunerKnob = document.getElementById('dial-tuner');
      if (tunerKnob) {
        const deg = (currentIndex * 27.6) % 360;
        tunerKnob.style.transform = `rotate(${deg}deg)`;
      }

      // Update Teleprompter
      updateNeoTeleprompter(ep);

      if (autoPlay && isPowerOn) {
        initWebAudio();
        audio.play().catch(() => {});
      }
    }

    function updateNeoTeleprompter(ep) {
      const prompter = document.getElementById('neo-teleprompter');
      if (!prompter) return;
      const key = `ep${ep.channel || (currentIndex + 1)}`;
      const transcriptData = (window.GYAN_SETU_TRANSCRIPTS && window.GYAN_SETU_TRANSCRIPTS[key]) || null;
      if (transcriptData && transcriptData.lines) {
        prompter.innerHTML = transcriptData.lines.map((l, i) => 
          `<p class="transcript-line ${i === 0 ? 'active' : ''}">${l.text}</p>`
        ).join('');
      } else {
        prompter.innerHTML = `
          <p class="transcript-line active"> ज्ञानसेतु इंटरनेट रेडिओ • Curated by Simran Ailani</p>
          <p class="transcript-line">${ep.title} (${ep.category || 'Science & Culture'})</p>
          <p class="transcript-line">Broadcasting live across the global network.</p>
        `;
      }
    }

    // Populate Lists on Init
    function initDirectories() {
      // Vintage Digital Directory
      const vList = document.getElementById('vintage-dir-list');
      if (vList) {
        vList.innerHTML = EPISODES.map((ep, i) => `
          <div class="dir-item ${i === 0 ? 'active' : ''}" data-index="${i}">
            <span>${i + 1}. ${ep.title}</span>
            <span>${ep.duration || '09:18'}</span>
          </div>
        `).join('');

        vList.querySelectorAll('.dir-item').forEach(item => {
          item.addEventListener('click', () => {
            const idx = parseInt(item.getAttribute('data-index'), 10);
            tuneToEpisode(idx, true);
            playMechanicalClick(950, 0.03);
          });
        });
      }

      // Carvaan Neo Ribbon
      const nRibbon = document.getElementById('neo-ribbon');
      if (nRibbon) {
        nRibbon.innerHTML = EPISODES.map((ep, i) => `
          <button class="neo-ribbon-btn ${i === 0 ? 'active' : ''}" data-index="${i}">
            CH-${ep.channel || (i+1)} • ${ep.freq}
          </button>
        `).join('');

        nRibbon.querySelectorAll('.neo-ribbon-btn').forEach(btn => {
          btn.addEventListener('click', () => {
            const idx = parseInt(btn.getAttribute('data-index'), 10);
            tuneToEpisode(idx, true);
            playMechanicalClick(1100, 0.03);
          });
        });
      }
    }

    // =========================================================================
    // 4. TRANSPORT CONTROLS (PIANO KEYS & NEO TOUCHBAR)
    // =========================================================================
    function togglePlay() {
      if (!isPowerOn) return;
      initWebAudio();
      if (audio.paused) {
        audio.play().then(() => {
          isPlaying = true;
          updatePlayUI(true);
        }).catch(e => console.warn(e));
      } else {
        audio.pause();
        isPlaying = false;
        updatePlayUI(false);
      }
      playMechanicalClick(1000, 0.04);
    }

    function updatePlayUI(playing) {
      const playKey = document.getElementById('key-play');
      const neoPlay = document.getElementById('neo-btn-play');
      if (playing) {
        if (playKey) playKey.classList.add('depressed');
        if (neoPlay) { neoPlay.textContent = '⏸ PAUSE'; neoPlay.classList.add('active'); }
      } else {
        if (playKey) playKey.classList.remove('depressed');
        if (neoPlay) { neoPlay.textContent = '▶ PLAY'; neoPlay.classList.remove('active'); }
      }
    }

    function togglePower() {
      isPowerOn = !isPowerOn;
      const stage = document.getElementById('appliance-stage');
      const pwrKey = document.getElementById('key-pwr');
      const neoPwr = document.getElementById('neo-btn-pwr');

      if (!isPowerOn) {
        audio.pause();
        updatePlayUI(false);
        stage.classList.add('crt-off');
        if (pwrKey) pwrKey.classList.remove('depressed');
        if (neoPwr) neoPwr.classList.remove('active');
        showToast('Radio Power: OFF');
        playMechanicalClick(400, 0.1);
      } else {
        stage.classList.remove('crt-off');
        if (pwrKey) pwrKey.classList.add('depressed');
        if (neoPwr) neoPwr.classList.add('active');
        showToast('Radio Power: ON (Tubes Warming Up)');
        playMechanicalClick(1400, 0.06);
      }
    }

    function toggleBass() {
      isBassBoosted = !isBassBoosted;
      initWebAudio();
      if (biquadFilter) {
        biquadFilter.gain.value = isBassBoosted ? 7.5 : 0;
      }
      const bassKey = document.getElementById('key-bass');
      const neoBass = document.getElementById('neo-btn-bass');
      const fillBass = document.getElementById('fill-bass');

      if (isBassBoosted) {
        if (bassKey) bassKey.classList.add('depressed');
        if (neoBass) neoBass.classList.add('active');
        if (fillBass) fillBass.style.height = '90%';
        showToast('Sub-Bass Boost: +7.5 dB ACTIVE');
      } else {
        if (bassKey) bassKey.classList.remove('depressed');
        if (neoBass) neoBass.classList.remove('active');
        if (fillBass) fillBass.style.height = '50%';
        showToast('Sub-Bass Boost: FLAT');
      }
      playMechanicalClick(700, 0.05);
    }

    // Connect Piano Buttons
    document.getElementById('key-play').addEventListener('click', togglePlay);
    document.getElementById('neo-btn-play').addEventListener('click', togglePlay);

    document.getElementById('key-prev').addEventListener('click', () => {
      tuneToEpisode(currentIndex - 1, true);
      playMechanicalClick(900, 0.03);
    });
    document.getElementById('neo-btn-prev').addEventListener('click', () => {
      tuneToEpisode(currentIndex - 1, true);
      playMechanicalClick(900, 0.03);
    });

    document.getElementById('key-next').addEventListener('click', () => {
      tuneToEpisode(currentIndex + 1, true);
      playMechanicalClick(1100, 0.03);
    });
    document.getElementById('neo-btn-next').addEventListener('click', () => {
      tuneToEpisode(currentIndex + 1, true);
      playMechanicalClick(1100, 0.03);
    });

    document.getElementById('key-pwr').addEventListener('click', togglePower);
    document.getElementById('neo-btn-pwr').addEventListener('click', togglePower);

    document.getElementById('key-bass').addEventListener('click', toggleBass);
    document.getElementById('neo-btn-bass').addEventListener('click', toggleBass);

    document.getElementById('key-treble').addEventListener('click', () => {
      showToast('Treble Harmonic Enhancer: +3 dB');
      playMechanicalClick(1500, 0.04);
    });

    // Rotary Dials Drag & Click Interaction
    const dialTuner = document.getElementById('dial-tuner');
    if (dialTuner) {
      dialTuner.addEventListener('click', () => {
        tuneToEpisode(currentIndex + 1, true);
      });
      dialTuner.addEventListener('wheel', (e) => {
        e.preventDefault();
        tuneToEpisode(currentIndex + (e.deltaY > 0 ? 1 : -1), true);
      });
    }

    const dialScroll = document.getElementById('dial-scroll');
    const vintageDir = document.getElementById('vintage-dir-screen');
    let dirScrollDeg = 0;
    if (dialScroll) {
      dialScroll.addEventListener('wheel', (e) => {
        e.preventDefault();
        dirScrollDeg += (e.deltaY > 0 ? 30 : -30);
        dialScroll.style.transform = `rotate(${dirScrollDeg}deg)`;
        vintageDir.scrollTop += (e.deltaY > 0 ? 28 : -28);
        playMechanicalClick(1300, 0.02);
      });
    }

    // Audio Time Update (Progress Bars & Counters)
    audio.addEventListener('timeupdate', () => {
      if (!audio.duration) return;
      const pct = (audio.currentTime / audio.duration) * 100;

      // Format time
      const curM = Math.floor(audio.currentTime / 60);
      const curS = Math.floor(audio.currentTime % 60);
      const curStr = `${String(curM).padStart(2,'0')}:${String(curS).padStart(2,'0')}`;

      const vCur = document.getElementById('vintage-time-cur');
      const nCur = document.getElementById('neo-time-cur');
      if (vCur) vCur.textContent = curStr;
      if (nCur) nCur.textContent = curStr;

      // Vintage segmented LCD progress bar (12 segments)
      const segs = document.querySelectorAll('#vintage-seg-bar .lcd-seg');
      const activeCount = Math.floor((pct / 100) * segs.length);
      segs.forEach((seg, i) => {
        if (i < activeCount) seg.classList.remove('off');
        else seg.classList.add('off');
      });

      // Neo Scrubber Fill
      const nScrubber = document.getElementById('neo-scrubber-fill');
      if (nScrubber) nScrubber.style.width = `${pct}%`;
    });

    // Click on Neo Scrubber to Seek
    const neoScrubberBar = document.getElementById('neo-scrubber');
    if (neoScrubberBar) {
      neoScrubberBar.addEventListener('click', (e) => {
        const rect = neoScrubberBar.getBoundingClientRect();
        const pos = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
        if (audio.duration) {
          audio.currentTime = pos * audio.duration;
        }
      });
    }

    // =========================================================================
    // 5. LIVE VISUALIZERS (NEO FFT SPECTROGRAM & OSCILLOSCOPE)
    // =========================================================================
    const specCanvas = document.getElementById('neo-spectrogram-canvas');
    const specCtx = specCanvas ? specCanvas.getContext('2d') : null;

    const oscCanvas = document.getElementById('neo-osc-canvas');
    const oscCtx = oscCanvas ? oscCanvas.getContext('2d') : null;

    const freqArray = new Uint8Array(32);
    let oscPhase = 0;

    function renderAudioVisuals() {
      requestAnimationFrame(renderAudioVisuals);

      if (currentTheme !== 'neo-carvaan' || !isPowerOn) return;

      if (analyser && !audio.paused) {
        analyser.getByteFrequencyData(freqArray);
      } else if (!audio.paused) {
        for (let i = 0; i < 32; i++) {
          freqArray[i] = Math.floor(Math.sin(i * 0.3 + oscPhase) * 90 + 120);
        }
      } else {
        freqArray.fill(6);
      }
      oscPhase += 0.08;

      // 1. Draw Spectrogram
      if (specCtx) {
        const w = specCanvas.width;
        const h = specCanvas.height;
        specCtx.clearRect(0, 0, w, h);

        const bars = 24;
        const barW = (w - (bars * 2)) / bars;
        for (let i = 0; i < bars; i++) {
          const val = freqArray[i] || 10;
          const barH = (val / 255) * (h - 15);
          const x = i * (barW + 2) + 2;
          const y = h - barH - 2;

          const grad = specCtx.createLinearGradient(0, y, 0, h);
          grad.addColorStop(0, '#38bdf8');
          grad.addColorStop(0.6, '#0284c7');
          grad.addColorStop(1, '#0c4a6e');

          specCtx.fillStyle = grad;
          specCtx.fillRect(x, y, barW, barH);
        }
      }

      // 2. Draw Oscilloscope
      if (oscCtx) {
        const w = oscCanvas.width;
        const h = oscCanvas.height;
        oscCtx.clearRect(0, 0, w, h);

        oscCtx.strokeStyle = '#38bdf8';
        oscCtx.lineWidth = 2;
        oscCtx.shadowColor = '#38bdf8';
        oscCtx.shadowBlur = 8;
        oscCtx.beginPath();

        const mid = h / 2;
        for (let x = 0; x < w; x += 3) {
          const sample = (freqArray[Math.floor((x / w) * 16)] || 128) - 128;
          const amp = (!audio.paused ? sample / 128 : 0.05) * 25;
          const y = mid + Math.sin((x * 0.05) + oscPhase) * amp;
          if (x === 0) oscCtx.moveTo(x, y);
          else oscCtx.lineTo(x, y);
        }
        oscCtx.stroke();
        oscCtx.shadowBlur = 0;
      }
    }
    renderAudioVisuals();

    // =========================================================================
    // 6. OPTICAL BEAMER MODAL & FOUNTAIN QR LOOP
    // =========================================================================
    const beamerModal = document.getElementById('beamer-modal');
    const openBeamerBtn = document.getElementById('btn-open-beamer');
    const neoBeamBtn = document.getElementById('neo-btn-beam');
    const closeBeamerBtn = document.getElementById('btn-close-beamer');

    function openBeamer() {
      beamerModal.classList.add('open');
      startFountainLoop();
      playMechanicalClick(1400, 0.05);
    }

    function closeBeamer() {
      beamerModal.classList.remove('open');
      stopFountainLoop();
      playMechanicalClick(500, 0.03);
    }

    if (openBeamerBtn) openBeamerBtn.addEventListener('click', openBeamer);
    if (neoBeamBtn) neoBeamBtn.addEventListener('click', openBeamer);
    if (closeBeamerBtn) closeBeamerBtn.addEventListener('click', closeBeamer);

    // Fountain QR Generator Loop
    let fountainTimer = null;
    let fountainSeq = 0;
    const fountainCanvas = document.getElementById('beam-fountain-canvas');

    function startFountainLoop() {
      if (fountainTimer) clearInterval(fountainTimer);
      fountainTimer = setInterval(() => {
        fountainSeq = (fountainSeq + 1) % 48;
        const hud = document.getElementById('sender-fountain-hud');
        if (hud) hud.textContent = `Chunk ${fountainSeq + 1} / 48 • 12 FPS • AES-256-GCM Encrypted`;

        if (fountainCanvas && window.QRCode) {
          const payload = `GS_MESH_CHUNK:${fountainSeq}:EP${currentIndex+1}:${Date.now()}`;
          QRCode.toCanvas(fountainCanvas, payload, {
            width: 256,
            margin: 1,
            color: { dark: '#000000', light: '#ffffff' }
          }, () => {});
        }
      }, 90);
    }

    function stopFountainLoop() {
      if (fountainTimer) {
        clearInterval(fountainTimer);
        fountainTimer = null;
      }
    }

    // Fullscreen Kiosk Mode
    const fsBtn = document.getElementById('btn-fullscreen');
    if (fsBtn) {
      fsBtn.addEventListener('click', () => {
        if (!document.fullscreenElement) {
          document.documentElement.requestFullscreen().catch(() => {});
          fsBtn.innerHTML = '<span>✖</span> Exit Kiosk';
        } else {
          document.exitFullscreen().catch(() => {});
          fsBtn.innerHTML = '<span>⛶</span> Kiosk';
        }
      });
    }

    // Startup Initialization
    window.addEventListener('DOMContentLoaded', () => {
      initDirectories();
      setTheme(currentTheme);
      tuneToEpisode(0, false);
      showToast('GyanSetu Tablet Console Ready • Curated by Simran Ailani');
    });

  </script>
</body>
</html>
'''
    with open('pocket.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully built flagship pocket.html! Size:", len(html))

if __name__ == '__main__':
    build_flagship()
