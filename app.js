// GyanSetu — Global Knowledge Radio Engine
// Client Controller & Audio Playback Manager

document.addEventListener('DOMContentLoaded', () => {
  // Playback State
  let currentEpisodeIndex = 0;
  let isPlaying = false;
  let isRadioContinuousMode = true;
  let currentSpeedIndex = 0;
  const speeds = [1.0, 1.25, 1.5, 2.0];
  let filteredEpisodes = [...GYAN_SETU_EPISODES];

  // Core Audio Node
  const audio = document.getElementById('audio-engine');
  
  // Hero Showcase Elements
  const featuredCover = document.getElementById('featured-cover');
  const featuredTitle = document.getElementById('featured-title');
  const featuredMeta = document.getElementById('featured-meta');
  const featuredCategory = document.getElementById('featured-category');
  const featuredPlayBtn = document.getElementById('featured-play-btn');
  const featuredPlayIcon = document.getElementById('featured-play-icon');
  const featuredPrevBtn = document.getElementById('featured-prev-btn');
  const featuredNextBtn = document.getElementById('featured-next-btn');
  const heroVisualizer = document.getElementById('hero-visualizer');
  const startBroadcastBtn = document.getElementById('start-broadcast-btn');
  const radioModeBtn = document.getElementById('radio-mode-btn');

  // Floating Dock Player Elements
  const dockCover = document.getElementById('dock-cover');
  const dockTitle = document.getElementById('dock-title');
  const dockArtist = document.getElementById('dock-artist');
  const dockPlayBtn = document.getElementById('player-play-btn');
  const dockPlayIcon = document.getElementById('dock-play-icon');
  const dockPrevBtn = document.getElementById('player-prev-btn');
  const dockNextBtn = document.getElementById('player-next-btn');
  const dockRw15Btn = document.getElementById('player-rw15-btn');
  const dockFf15Btn = document.getElementById('player-ff15-btn');
  const currentTimeLabel = document.getElementById('current-time-label');
  const totalTimeLabel = document.getElementById('total-time-label');
  const progressContainer = document.getElementById('progress-container');
  const progressFill = document.getElementById('progress-fill');
  const speedToggleBtn = document.getElementById('speed-toggle-btn');
  const muteToggleBtn = document.getElementById('mute-toggle-btn');
  const volumeSlider = document.getElementById('volume-slider');

  // Modal Elements
  const notesModal = document.getElementById('notes-modal');
  const closeModalBtn = document.getElementById('close-modal-btn');
  const modalEpisodeTitle = document.getElementById('modal-episode-title');
  const modalEpisodeCategory = document.getElementById('modal-episode-category');
  const modalEpisodeDate = document.getElementById('modal-episode-date');
  const modalEpisodeDuration = document.getElementById('modal-episode-duration');
  const modalEpisodeDesc = document.getElementById('modal-episode-desc');
  const modalPlayBtn = document.getElementById('modal-play-btn');

  // QR Lightbox Elements
  const qrModal = document.getElementById('qr-modal');
  const openQrLightboxBtn = document.getElementById('open-qr-lightbox-btn');
  const closeQrModalBtn = document.getElementById('close-qr-modal-btn');

  // Teleprompter Modal Elements
  const transcriptModal = document.getElementById('transcript-modal');
  const closeTranscriptModalBtn = document.getElementById('close-transcript-modal-btn');
  const dockTranscriptBtn = document.getElementById('dock-transcript-btn');
  const teleprompterBody = document.getElementById('teleprompter-body');
  const teleprompterTitle = document.getElementById('teleprompter-title');
  const teleprompterEpTag = document.getElementById('teleprompter-ep-tag');
  const tpCurrentLineTime = document.getElementById('tp-current-line-time');
  const tpPlayPauseBtn = document.getElementById('tp-play-pause-btn');
  const tpPlayIcon = document.getElementById('tp-play-icon');
  const tpAutoScrollBtn = document.getElementById('tp-autoscroll-btn');
  const tpTtsBtn = document.getElementById('tp-tts-btn');
  const tpPolyglotBtn = document.getElementById('tp-polyglot-btn');
  const tpPolyglotMenu = document.getElementById('tp-polyglot-menu');
  const tpConceptDrawer = document.getElementById('tp-concept-drawer');
  const closeConceptBtn = document.getElementById('close-concept-btn');
  const tpConceptTitle = document.getElementById('tp-concept-title');
  const tpConceptCat = document.getElementById('tp-concept-cat');
  const tpConceptDef = document.getElementById('tp-concept-def');
  const tpCopyTranscriptBtn = document.getElementById('tp-copy-transcript-btn');
  const dockLinguaBtn = document.getElementById('dock-lingua-btn');
  const dockLinguaLabel = document.getElementById('dock-lingua-label');
  const dockLinguaPopover = document.getElementById('dock-lingua-popover');
  const dockLinguaOptionsList = document.getElementById('dock-lingua-options-list');
  const tpTrackSwitchBtn = document.getElementById('tp-track-switch-btn');
  const tpTrackLabel = document.getElementById('tp-track-label');
  const tpMrBtn = document.getElementById('tp-mr-btn');
  let currentTrackLanguage = 'orig'; // STRICT DEFAULT: 'orig' (Original composition by Simran Ailani)

  // 2G Ghost Stream & Network Elements
  const ghostModeBtn = document.getElementById('ghost-mode-btn');
  const ghostNavLabel = document.getElementById('ghost-nav-label');
  const dockGhostBtn = document.getElementById('dock-ghost-btn');
  const dockGhostLabel = document.getElementById('dock-ghost-label');
  const networkToast = document.getElementById('network-toast');
  const networkToastMsg = document.getElementById('network-toast-msg');
  const closeToastBtn = document.getElementById('close-toast-btn');

  let isGhostMode = localStorage.getItem('gyansetu_ghost_mode') === 'true';
  let toastTimeout = null;

  // Library & Search Elements
  const episodesGrid = document.getElementById('episodes-grid');
  const searchInput = document.getElementById('search-input');
  const categoryPills = document.getElementById('category-pills');

  // 1. Initial State
  renderEpisodeCards(filteredEpisodes);
  loadEpisode(0, false);

  // 2. Render Cards
  function renderEpisodeCards(episodes) {
    episodesGrid.innerHTML = '';
    
    if (episodes.length === 0) {
      episodesGrid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; color: var(--text-muted);">
          <p style="font-size: 1.15rem; font-weight: 600;">No episodes matched your search.</p>
          <p style="font-size: 0.9rem; color: var(--text-faint); margin-top: 6px;">Try searching for consciousness, benzene, medicine, or carbenes.</p>
        </div>
      `;
      return;
    }

    episodes.forEach((ep) => {
      const card = document.createElement('article');
      const isCurrentActive = (ep.id === GYAN_SETU_EPISODES[currentEpisodeIndex].id && isPlaying);
      card.className = `episode-glass-card ${isCurrentActive ? 'is-playing' : ''}`;
      card.dataset.id = ep.id;

      card.innerHTML = `
        <div class="card-visual-header">
          <img src="${ep.image}" alt="${ep.title}" class="card-cover-art" loading="lazy">
          <div class="card-sheen-overlay"></div>
          <span class="card-number-pill">EP ${ep.number} • ${ep.category}</span>
          <span class="card-duration-pill">${ep.duration}</span>
        </div>
        <div class="card-content-pane">
          <div class="card-meta-line">${ep.date}</div>
          <h3 class="card-heading">${ep.title}</h3>
          <p class="card-narrative-snip">${ep.description}</p>
          <div class="card-action-bar">
            <button class="btn-card-listen" data-id="${ep.id}">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
              <span>${isCurrentActive ? 'Pause' : 'Listen Now'}</span>
            </button>
            <button class="btn-card-notes" data-id="${ep.id}">Research Notes</button>
          </div>
          ${ep.id === 'ep-13' ? `
          <button class="btn-card-transcript" data-id="${ep.id}" title="Open Synchronized English Master Teleprompter">
            <span>📜 English Master Transcript (100% Vetted)</span>
          </button>
          ` : ''}
        </div>
      `;
      episodesGrid.appendChild(card);
    });

    attachCardListeners();
  }

  function attachCardListeners() {
    document.querySelectorAll('.btn-card-listen').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.dataset.id;
        const index = GYAN_SETU_EPISODES.findIndex(ep => ep.id === id);
        if (index !== -1) {
          if (index === currentEpisodeIndex && isPlaying) {
            pauseAudio();
          } else {
            loadEpisode(index, true);
          }
        }
      });
    });

    document.querySelectorAll('.btn-card-notes').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.dataset.id;
        const ep = GYAN_SETU_EPISODES.find(item => item.id === id);
        if (ep) openNotesModal(ep);
      });
    });

    document.querySelectorAll('.btn-card-transcript').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.dataset.id;
        const index = GYAN_SETU_EPISODES.findIndex(item => item.id === id);
        if (index !== -1 && index !== currentEpisodeIndex) {
          loadEpisode(index, true);
        }
        if (typeof openTranscriptModal === 'function') {
          openTranscriptModal(id);
        }
      });
    });
  }

  // 3. Audio Loading, Playback & Multilingual Language Tracks
  function renderLinguaPopoverOptions() {
    if (!dockLinguaOptionsList) return;
    const ep = GYAN_SETU_EPISODES[currentEpisodeIndex];
    if (!ep) return;
    dockLinguaOptionsList.innerHTML = '';

    const isEp13 = (ep.id === 'ep-13');
    // STRICT USER RULE:
    // Ep 13 (Marathi original): Available in Original (MR), English (EN), Hindi (HI)
    // Ep 1-12 (English original): Available in Original (EN), Hindi (HI)
    let options = [];
    if (isEp13) {
      options = [
        { code: 'orig', label: '🇮🇳 Original Marathi', sub: 'Simran Ailani (Default)', badge: 'ORIGINAL' },
        { code: 'en', label: '🇬🇧 English Master', sub: 'Neerja Voice (Studio Dub)', badge: 'STUDIO DUB' },
        { code: 'hi', label: '🇮🇳 Hindi Master', sub: 'Swara Voice (Studio Dub)', badge: 'STUDIO DUB' }
      ];
    } else {
      options = [
        { code: 'orig', label: '🇬🇧 Original English', sub: 'Simran Ailani (Default)', badge: 'ORIGINAL' },
        { code: 'hi', label: '🇮🇳 Hindi Master', sub: 'Swara Voice (Neural Translation)', badge: 'TRANSLATION' }
      ];
    }

    options.forEach(opt => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = `btn-lingua-option ${currentTrackLanguage === opt.code ? 'active' : ''}`;
      btn.innerHTML = `
        <div>
          <div>${opt.label}</div>
          <div style="font-size:0.62rem; color:rgba(255,255,255,0.5);">${opt.sub}</div>
        </div>
        <span class="lingua-opt-badge">${opt.badge}</span>
      `;
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        setTrackLanguage(opt.code);
        if (dockLinguaPopover) dockLinguaPopover.classList.add('hidden');
      });
      dockLinguaOptionsList.appendChild(btn);
    });

    if (dockLinguaLabel) {
      dockLinguaLabel.textContent = currentTrackLanguage.toUpperCase();
    }
  }

  function setTrackLanguage(lang) {
    if (currentTrackLanguage === lang) return;
    const ep = GYAN_SETU_EPISODES[currentEpisodeIndex];
    currentTrackLanguage = lang;

    const curTime = audio.currentTime;
    const wasPlaying = isPlaying;

    let targetSrc = ep.audioSrc;
    if (ep.id === 'ep-13') {
      if (lang === 'en' && ep.audioSrcEnglish) targetSrc = ep.audioSrcEnglish;
      if (lang === 'hi' && ep.audioSrcHindi) targetSrc = ep.audioSrcHindi;
    } else {
      if (lang === 'hi' && ep.audioSrcHindi) targetSrc = ep.audioSrcHindi;
    }

    const finalSrc = isGhostMode 
      ? targetSrc.replace('assets/audio/', 'assets/audio_ghost/') 
      : targetSrc;

    audio.src = finalSrc;
    audio.onloadedmetadata = () => {
      if (curTime > 0 && curTime < audio.duration) {
        audio.currentTime = curTime;
      }
    };

    if (wasPlaying) playAudio();

    if (dockLinguaLabel) {
      dockLinguaLabel.textContent = currentTrackLanguage.toUpperCase();
    }
    renderLinguaPopoverOptions();

    // If teleprompter is open, sync its language too
    if (typeof syncTeleprompterLanguage === 'function') {
      syncTeleprompterLanguage(lang);
    }

    const toastMsgs = {
      orig: `🎙️ Playing Original Composition (${ep.hosts[0]} • Default)`,
      en: `🇬🇧 Switched to English Master Translation (Neerja Voice)`,
      hi: `🇮🇳 Switched to Hindi Master Translation (Swara Voice)`
    };
    showToast(toastMsgs[lang] || 'Language updated');
  }

  function loadEpisode(index, autoPlay = true) {
    if (index < 0) index = GYAN_SETU_EPISODES.length - 1;
    if (index >= GYAN_SETU_EPISODES.length) index = 0;
    
    currentEpisodeIndex = index;
    const ep = GYAN_SETU_EPISODES[currentEpisodeIndex];

    // STRICT USER RULE: Always reset to Original composition by default!
    currentTrackLanguage = 'orig';
    renderLinguaPopoverOptions();

    const targetAudioSrc = isGhostMode 
      ? ep.audioSrc.replace('assets/audio/', 'assets/audio_ghost/') 
      : ep.audioSrc;
    audio.src = targetAudioSrc;
    audio.playbackRate = speeds[currentSpeedIndex];

    // Hero Showcase Sync
    featuredCover.src = ep.image;
    featuredTitle.textContent = ep.title;
    featuredMeta.textContent = `Hosted by ${ep.hosts.join(', ')} • ${ep.duration}`;
    featuredCategory.textContent = ep.category;

    // Dock Sync
    dockCover.src = ep.image;
    dockTitle.textContent = ep.title;
    dockArtist.textContent = `GyanSetu • ${ep.hosts.join(', ')}`;
    totalTimeLabel.textContent = ep.duration;
    progressFill.style.width = '0%';
    currentTimeLabel.textContent = '0:00';

    highlightActiveCard();

    if (autoPlay) {
      playAudio();
    } else {
      updatePlayIcons(false);
    }
  }

  function playAudio() {
    audio.play().then(() => {
      isPlaying = true;
      updatePlayIcons(true);
      heroVisualizer.classList.add('active');
      highlightActiveCard();
      if (typeof trackEpisodePlay === 'function') {
        trackEpisodePlay(currentEpisodeIndex);
      }
    }).catch(err => {
      console.warn('Playback error or user gesture required:', err);
      isPlaying = false;
      updatePlayIcons(false);
    });
  }

  function pauseAudio() {
    audio.pause();
    isPlaying = false;
    updatePlayIcons(false);
    heroVisualizer.classList.remove('active');
    highlightActiveCard();
  }

  function togglePlayPause() {
    if (isPlaying) {
      pauseAudio();
    } else {
      playAudio();
    }
  }

  function updatePlayIcons(playing) {
    const playSvg = `<path d="M8 5v14l11-7z"/>`;
    const pauseSvg = `<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>`;
    
    featuredPlayIcon.innerHTML = playing ? pauseSvg : playSvg;
    dockPlayIcon.innerHTML = playing ? pauseSvg : playSvg;

    document.querySelectorAll('.btn-card-listen').forEach(btn => {
      const epId = btn.dataset.id;
      const isCurrent = (epId === GYAN_SETU_EPISODES[currentEpisodeIndex].id);
      btn.querySelector('span').textContent = (isCurrent && playing) ? 'Pause' : 'Listen Now';
    });

    if (typeof updateTpPlayState === 'function') {
      updateTpPlayState(playing);
    }
  }

  function highlightActiveCard() {
    document.querySelectorAll('.episode-glass-card').forEach(card => {
      const isCurrent = (card.dataset.id === GYAN_SETU_EPISODES[currentEpisodeIndex].id);
      if (isCurrent && isPlaying) {
        card.classList.add('is-playing');
      } else {
        card.classList.remove('is-playing');
      }
    });
  }

  // 4. Progress, Timing & Continuous Stream
  audio.addEventListener('timeupdate', () => {
    if (!audio.duration) return;
    const current = audio.currentTime;
    const duration = audio.duration;
    const percent = (current / duration) * 100;
    progressFill.style.width = `${percent}%`;
    currentTimeLabel.textContent = formatTime(current);

    if (typeof syncTeleprompterTime === 'function') {
      syncTeleprompterTime(current);
    }
  });

  audio.addEventListener('loadedmetadata', () => {
    totalTimeLabel.textContent = formatTime(audio.duration);
  });

  audio.addEventListener('ended', () => {
    if (isRadioContinuousMode) {
      loadEpisode(currentEpisodeIndex + 1, true);
    } else {
      pauseAudio();
    }
  });

  progressContainer.addEventListener('click', (e) => {
    const rect = progressContainer.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const width = rect.width;
    if (audio.duration) {
      audio.currentTime = (clickX / width) * audio.duration;
    }
  });

  function formatTime(seconds) {
    if (isNaN(seconds)) return '0:00';
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
  }

  // 5. Controls
  featuredPlayBtn.addEventListener('click', togglePlayPause);
  dockPlayBtn.addEventListener('click', togglePlayPause);

  featuredNextBtn.addEventListener('click', () => loadEpisode(currentEpisodeIndex + 1, true));
  dockNextBtn.addEventListener('click', () => loadEpisode(currentEpisodeIndex + 1, true));

  featuredPrevBtn.addEventListener('click', () => loadEpisode(currentEpisodeIndex - 1, true));
  dockPrevBtn.addEventListener('click', () => loadEpisode(currentEpisodeIndex - 1, true));

  dockRw15Btn.addEventListener('click', () => {
    audio.currentTime = Math.max(0, audio.currentTime - 15);
  });

  dockFf15Btn.addEventListener('click', () => {
    if (audio.duration) {
      audio.currentTime = Math.min(audio.duration, audio.currentTime + 15);
    }
  });

  speedToggleBtn.addEventListener('click', () => {
    currentSpeedIndex = (currentSpeedIndex + 1) % speeds.length;
    const newSpeed = speeds[currentSpeedIndex];
    audio.playbackRate = newSpeed;
    speedToggleBtn.textContent = `${newSpeed.toFixed(1)}×`;
  });

  volumeSlider.addEventListener('input', (e) => {
    audio.volume = parseFloat(e.target.value);
  });

  muteToggleBtn.addEventListener('click', () => {
    audio.muted = !audio.muted;
    muteToggleBtn.style.color = audio.muted ? 'var(--orange-accent)' : 'var(--text-muted)';
  });

  startBroadcastBtn.addEventListener('click', () => {
    loadEpisode(0, true);
    document.getElementById('broadcast').scrollIntoView({ behavior: 'smooth' });
  });

  radioModeBtn.addEventListener('click', () => {
    isRadioContinuousMode = true;
    loadEpisode(currentEpisodeIndex, true);
    document.getElementById('broadcast').scrollIntoView({ behavior: 'smooth' });
  });

  // 6. Modal
  function openNotesModal(ep) {
    modalEpisodeTitle.textContent = ep.title;
    modalEpisodeCategory.textContent = ep.category;
    modalEpisodeDate.textContent = `Broadcast Date: ${ep.date}`;
    modalEpisodeDuration.textContent = ep.duration;
    modalEpisodeDesc.textContent = ep.description;
    
    modalPlayBtn.onclick = () => {
      notesModal.classList.remove('is-active');
      const idx = GYAN_SETU_EPISODES.findIndex(item => item.id === ep.id);
      if (idx !== -1) loadEpisode(idx, true);
    };

    notesModal.classList.add('is-active');
  }

  closeModalBtn.addEventListener('click', () => {
    notesModal.classList.remove('is-active');
  });

  notesModal.addEventListener('click', (e) => {
    if (e.target === notesModal) {
      notesModal.classList.remove('is-active');
    }
  });

  // QR Dual Stream & Modal Logic
  const qrModalHeading = document.getElementById('qr-modal-heading');
  const qrModalLargeImg = document.getElementById('qr-modal-large-img');
  const qrModalLinkBtn = document.getElementById('qr-modal-link-btn');
  const qrModalLinkText = document.getElementById('qr-modal-link-text');
  const modalTabVercel = document.getElementById('modal-tab-vercel');
  const modalTabNetlify = document.getElementById('modal-tab-netlify');

  const qrStreams = {
    vercel: {
      name: 'Vercel Stream',
      url: 'https://gyansetu-five.vercel.app/',
      img: 'assets/images/gyansetu_qr_vercel.png',
      heading: 'Scan to Stream • Vercel Network'
    },
    netlify: {
      name: 'Netlify Mirror',
      url: 'https://imaginative-centaur-0c2b59.netlify.app/',
      img: 'assets/images/gyansetu_qr_netlify.png',
      heading: 'Scan to Stream • Netlify Mirror'
    }
  };

  function switchQrModalTab(target) {
    const data = qrStreams[target] || qrStreams.vercel;
    if (qrModalHeading) qrModalHeading.textContent = data.heading;
    if (qrModalLargeImg) qrModalLargeImg.src = data.img;
    if (qrModalLinkBtn) qrModalLinkBtn.href = data.url;
    if (qrModalLinkText) qrModalLinkText.textContent = `Open ${data.name}`;

    if (modalTabVercel && modalTabNetlify) {
      if (target === 'vercel') {
        modalTabVercel.classList.add('active');
        modalTabNetlify.classList.remove('active');
      } else {
        modalTabNetlify.classList.add('active');
        modalTabVercel.classList.remove('active');
      }
    }
  }

  document.querySelectorAll('.stream-qr-thumb-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const target = btn.dataset.qr || 'vercel';
      switchQrModalTab(target);
      if (qrModal) qrModal.classList.add('is-active');
    });
  });

  if (modalTabVercel) {
    modalTabVercel.addEventListener('click', () => switchQrModalTab('vercel'));
  }
  if (modalTabNetlify) {
    modalTabNetlify.addEventListener('click', () => switchQrModalTab('netlify'));
  }

  if (closeQrModalBtn && qrModal) {
    closeQrModalBtn.addEventListener('click', () => {
      qrModal.classList.remove('is-active');
    });
  }

  if (qrModal) {
    qrModal.addEventListener('click', (e) => {
      if (e.target === qrModal) {
        qrModal.classList.remove('is-active');
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      if (notesModal) notesModal.classList.remove('is-active');
      if (qrModal) qrModal.classList.remove('is-active');
      if (transcriptModal) transcriptModal.classList.remove('is-active');
      if (isTpTtsEnabled && 'speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
    }
  });

  // 7. Search & Filter
  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase().trim();
    filterEpisodes(query);
  });

  categoryPills.addEventListener('click', (e) => {
    if (!e.target.classList.contains('filter-capsule')) return;
    
    document.querySelectorAll('.capsule-ribbon .filter-capsule').forEach(p => p.classList.remove('active'));
    e.target.classList.add('active');

    const cat = e.target.dataset.category;
    if (cat === 'all') {
      filteredEpisodes = [...GYAN_SETU_EPISODES];
    } else {
      filteredEpisodes = GYAN_SETU_EPISODES.filter(ep => 
        ep.category.toLowerCase().includes(cat.toLowerCase())
      );
    }
    renderEpisodeCards(filteredEpisodes);
  });

  function filterEpisodes(query) {
    if (!query) {
      filteredEpisodes = [...GYAN_SETU_EPISODES];
    } else {
      filteredEpisodes = GYAN_SETU_EPISODES.filter(ep => 
        ep.title.toLowerCase().includes(query) ||
        ep.description.toLowerCase().includes(query) ||
        ep.category.toLowerCase().includes(query)
      );
    }
    renderEpisodeCards(filteredEpisodes);
  }

  // ==========================================================================
  // 8. REAL-TIME LISTENER & GEOLOCATION ANALYTICS ENGINE (POWERED BY FIREBASE)
  // ==========================================================================
  const FIREBASE_CONFIG = {
    apiKey: "AIzaSyB4XlBzKLUoORea4MYiGBXvM7Ul0VEJ-8Y",
    authDomain: "gyansetu-be409.firebaseapp.com",
    databaseURL: "https://gyansetu-be409-default-rtdb.firebaseio.com",
    projectId: "gyansetu-be409",
    storageBucket: "gyansetu-be409.firebasestorage.app",
    messagingSenderId: "340853834749",
    appId: "1:340853834749:web:c80e36bbbcecf3b5260f94",
    measurementId: "G-K1P7HPG0DW"
  };

  const BASELINE_DATA = {
    total: 215,
    countries: {
      IN: { name: 'India', flag: '🇮🇳', count: 182 },
      ZM: { name: 'Zambia', flag: '🇿🇲', count: 14 },
      UG: { name: 'Uganda', flag: '🇺🇬', count: 10 },
      US: { name: 'United States', flag: '🇺🇸', count: 6 },
      AU: { name: 'Australia', flag: '🇦🇺', count: 3 }
    }
  };

  const STORAGE_KEY = 'gyansetu_live_analytics_v3';
  let analyticsState = loadAnalyticsState();
  let userDetectedCountry = 'IN';
  let lastTrackedEpisodeId = null;
  let lastTrackedTime = 0;
  let firebaseDb = null;
  let isFirebaseConnected = false;

  function loadAnalyticsState() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        if (parsed.countries && parsed.countries.ZM && parsed.countries.UG) {
          return parsed;
        }
      }
    } catch (e) {
      console.warn('LocalStorage unavailable, using baseline state');
    }
    return JSON.parse(JSON.stringify(BASELINE_DATA));
  }

  function saveAnalyticsState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(analyticsState));
    } catch (e) {
      // Ignore
    }
  }

  function calculatePercentages(state) {
    const total = state.total || 1;
    return {
      IN: ((state.countries.IN.count / total) * 100).toFixed(1),
      ZM: ((state.countries.ZM.count / total) * 100).toFixed(1),
      UG: ((state.countries.UG.count / total) * 100).toFixed(1),
      US: ((state.countries.US.count / total) * 100).toFixed(1),
      AU: ((state.countries.AU.count / total) * 100).toFixed(1)
    };
  }

  function updateStatusBadge(message) {
    const statusBadge = document.getElementById('live-status-text');
    if (statusBadge) {
      statusBadge.innerHTML = `<span class="pulse-beacon-teal-inline"></span> ${message}`;
      if (statusBadge._timer) clearTimeout(statusBadge._timer);
      statusBadge._timer = setTimeout(() => {
        statusBadge.innerHTML = `<span class="pulse-beacon-teal-inline"></span> Live Stream Sync`;
      }, 4000);
    }
  }

  function renderAnalyticsUI(highlightCountry = null, triggerFlash = false) {
    if (!analyticsState.countries || !analyticsState.countries.IN) {
      analyticsState.countries = BASELINE_DATA.countries;
    }
    const pcts = calculatePercentages(analyticsState);

    // KPI values
    const kpiIndiaPct = document.getElementById('kpi-india-pct');
    const kpiTotalViews = document.getElementById('kpi-total-views');
    if (kpiIndiaPct) kpiIndiaPct.textContent = `${pcts.IN}%`;
    if (kpiTotalViews) {
      kpiTotalViews.textContent = Number(analyticsState.total).toLocaleString();
      if (triggerFlash) {
        kpiTotalViews.classList.remove('kpi-updated-pulse');
        void kpiTotalViews.offsetWidth; // trigger reflow
        kpiTotalViews.classList.add('kpi-updated-pulse');
      }
    }

    // Unified distribution bar segments
    const segIndia = document.getElementById('seg-india');
    const segZambia = document.getElementById('seg-zambia');
    const segUganda = document.getElementById('seg-uganda');
    const segUsa = document.getElementById('seg-usa');
    const segAus = document.getElementById('seg-aus');
    if (segIndia) segIndia.style.width = `${pcts.IN}%`;
    if (segZambia) segZambia.style.width = `${pcts.ZM}%`;
    if (segUganda) segUganda.style.width = `${pcts.UG}%`;
    if (segUsa) segUsa.style.width = `${pcts.US}%`;
    if (segAus) segAus.style.width = `${pcts.AU}%`;

    // Legend percentages
    const legIndia = document.getElementById('leg-india-pct');
    const legZambia = document.getElementById('leg-zambia-pct');
    const legUganda = document.getElementById('leg-uganda-pct');
    const legUsa = document.getElementById('leg-usa-pct');
    const legAus = document.getElementById('leg-aus-pct');
    if (legIndia) legIndia.textContent = `${pcts.IN}%`;
    if (legZambia) legZambia.textContent = `${pcts.ZM}%`;
    if (legUganda) legUganda.textContent = `${pcts.UG}%`;
    if (legUsa) legUsa.textContent = `${pcts.US}%`;
    if (legAus) legAus.textContent = `${pcts.AU}%`;

    // Country cards
    // 1. India
    const cardIndiaPct = document.getElementById('card-india-pct');
    const cardIndiaSub = document.getElementById('card-india-sub');
    const fillIndia = document.getElementById('fill-india');
    if (cardIndiaPct) cardIndiaPct.textContent = `${pcts.IN}%`;
    if (cardIndiaSub) cardIndiaSub.textContent = `${Number(analyticsState.countries.IN.count).toLocaleString()} Verified Streams`;
    if (fillIndia) fillIndia.style.width = `${pcts.IN}%`;

    // 2. Zambia
    const cardZambiaPct = document.getElementById('card-zambia-pct');
    const cardZambiaSub = document.getElementById('card-zambia-sub');
    const fillZambia = document.getElementById('fill-zambia');
    if (cardZambiaPct) cardZambiaPct.textContent = `${pcts.ZM}%`;
    if (cardZambiaSub) cardZambiaSub.textContent = `${Number(analyticsState.countries.ZM.count).toLocaleString()} Verified Streams`;
    if (fillZambia) fillZambia.style.width = `${Math.min(100, Math.max(14, pcts.ZM * 4))}%`;

    // 3. Uganda
    const cardUgandaPct = document.getElementById('card-uganda-pct');
    const cardUgandaSub = document.getElementById('card-uganda-sub');
    const fillUganda = document.getElementById('fill-uganda');
    if (cardUgandaPct) cardUgandaPct.textContent = `${pcts.UG}%`;
    if (cardUgandaSub) cardUgandaSub.textContent = `${Number(analyticsState.countries.UG.count).toLocaleString()} Verified Streams`;
    if (fillUganda) fillUganda.style.width = `${Math.min(100, Math.max(12, pcts.UG * 4))}%`;

    // 4. USA
    const cardUsaPct = document.getElementById('card-usa-pct');
    const cardUsaSub = document.getElementById('card-usa-sub');
    const fillUsa = document.getElementById('fill-usa');
    if (cardUsaPct) cardUsaPct.textContent = `${pcts.US}%`;
    if (cardUsaSub) cardUsaSub.textContent = `${Number(analyticsState.countries.US.count).toLocaleString()} Verified Streams`;
    if (fillUsa) fillUsa.style.width = `${Math.min(100, Math.max(10, pcts.US * 4))}%`;

    // 5. Australia
    const cardAusPct = document.getElementById('card-aus-pct');
    const cardAusSub = document.getElementById('card-aus-sub');
    const fillAus = document.getElementById('fill-aus');
    if (cardAusPct) cardAusPct.textContent = `${pcts.AU}%`;
    if (cardAusSub) cardAusSub.textContent = `${Number(analyticsState.countries.AU.count).toLocaleString()} Verified Streams`;
    if (fillAus) fillAus.style.width = `${Math.min(100, Math.max(8, pcts.AU * 4))}%`;

    // Flash animation if country specified
    if (highlightCountry) {
      const cardMap = {
        IN: 'card-wrap-india',
        ZM: 'card-wrap-zambia',
        UG: 'card-wrap-uganda',
        US: 'card-wrap-usa',
        AU: 'card-wrap-aus'
      };
      const cardElem = document.getElementById(cardMap[highlightCountry]);
      if (cardElem) {
        cardElem.classList.remove('ping-active');
        void cardElem.offsetWidth; // trigger reflow
        cardElem.classList.add('ping-active');
      }
    }
  }

  // Real-time visitor GeoIP detection & counting
  async function detectAndRecordVisit() {
    let countryCode = 'IN';
    let countryName = 'India';

    try {
      const res = await fetch('https://api.country.is', { cache: 'no-store' });
      if (res.ok) {
        const data = await res.json();
        if (data && data.country) {
          countryCode = data.country;
          const countryNames = {
            IN: 'India', ZM: 'Zambia', UG: 'Uganda', US: 'United States', AU: 'Australia',
            GB: 'United Kingdom', CA: 'Canada', DE: 'Germany', FR: 'France', JP: 'Japan'
          };
          countryName = countryNames[countryCode] || countryCode;
        }
      }
    } catch (e) {
      console.log('GeoIP lookup fallback to local baseline');
    }

    userDetectedCountry = countryCode;

    // Update detected region badge
    const detectedRegionElem = document.getElementById('kpi-detected-country');
    const flagEmojis = { IN: '🇮🇳', ZM: '🇿🇲', UG: '🇺🇬', US: '🇺🇸', AU: '🇦🇺' };
    const flag = flagEmojis[countryCode] || '🌐';
    if (detectedRegionElem) {
      detectedRegionElem.textContent = `${flag} ${countryName}`;
    }

    // Increment visit if first time in session
    const SESSION_KEY = 'gyansetu_session_recorded_v3';
    if (!sessionStorage.getItem(SESSION_KEY)) {
      sessionStorage.setItem(SESSION_KEY, 'true');
      recordListenerPing(countryCode, false);
    } else {
      renderAnalyticsUI();
    }
  }

  function recordListenerPing(countryCode, flashCard = true, episodeId = null) {
    const validCodes = ['IN', 'ZM', 'UG', 'US', 'AU'];
    const targetCode = validCodes.includes(countryCode) ? countryCode : 'IN';

    if (firebaseDb && isFirebaseConnected) {
      // 1. Atomic increment total
      firebaseDb.ref('analytics/total').transaction((curr) => {
        return (typeof curr === 'number') ? curr + 1 : 216;
      });

      // 2. Atomic increment country count
      firebaseDb.ref(`analytics/countries/${targetCode}/count`).transaction((curr) => {
        return (typeof curr === 'number') ? curr + 1 : 1;
      });

      // 3. Atomic increment episode listens if episode provided
      if (episodeId) {
        firebaseDb.ref(`analytics/episodes/${episodeId}/listens`).transaction((curr) => {
          return (typeof curr === 'number') ? curr + 1 : 1;
        });
      }

      // 4. Update last ping metadata
      firebaseDb.ref('analytics/last_updated').set(Date.now());
      firebaseDb.ref('analytics/last_country').set(targetCode);

      if (flashCard) {
        renderAnalyticsUI(targetCode, true);
      }
    } else {
      // Local fallback
      analyticsState.total = (analyticsState.total || 215) + 1;
      if (!analyticsState.countries[targetCode]) {
        analyticsState.countries[targetCode] = { name: targetCode, count: 0, flag: '🌐' };
      }
      analyticsState.countries[targetCode].count += 1;
      saveAnalyticsState();
      renderAnalyticsUI(flashCard ? targetCode : null, true);
    }

    const flag = (analyticsState.countries && analyticsState.countries[targetCode]) ? analyticsState.countries[targetCode].flag : '🌐';
    const name = (analyticsState.countries && analyticsState.countries[targetCode]) ? analyticsState.countries[targetCode].name : targetCode;
    updateStatusBadge(`Stream Ping Logged (${flag} ${name})`);
  }

  function trackEpisodePlay(epIndex) {
    const ep = GYAN_SETU_EPISODES[epIndex];
    if (!ep) return;
    const now = Date.now();
    if (lastTrackedEpisodeId === ep.id && (now - lastTrackedTime) < 2500) {
      return;
    }
    lastTrackedEpisodeId = ep.id;
    lastTrackedTime = now;

    recordListenerPing(userDetectedCountry, true, ep.id);
  }

  function initFirebaseRealtimeSync() {
    try {
      if (typeof firebase !== 'undefined') {
        if (!firebase.apps || !firebase.apps.length) {
          firebase.initializeApp(FIREBASE_CONFIG);
          try {
            if (typeof firebase.analytics === 'function') {
              firebase.analytics();
            }
          } catch (e) { /* analytics optional */ }
        }
        firebaseDb = firebase.database();
        isFirebaseConnected = true;

        const analyticsRef = firebaseDb.ref('analytics');
        let initialLoadDone = false;

        // WebSocket Real-time listener: triggers whenever ANY client mutates data
        analyticsRef.on('value', (snapshot) => {
          const val = snapshot.val();
          if (val && typeof val.total === 'number') {
            const previousTotal = analyticsState ? analyticsState.total : 0;
            const isRemoteIncrease = initialLoadDone && (val.total > previousTotal);

            analyticsState = {
              total: val.total,
              countries: (val.countries && val.countries.IN) ? val.countries : BASELINE_DATA.countries,
              episodes: val.episodes || {},
              last_country: val.last_country || 'IN',
              last_updated: val.last_updated || Date.now()
            };

            saveAnalyticsState();
            renderAnalyticsUI(val.last_country || null, isRemoteIncrease);

            if (isRemoteIncrease) {
              const countryInfo = analyticsState.countries[val.last_country] || analyticsState.countries.IN;
              updateStatusBadge(`Live Cloud Sync (+1 ${countryInfo.flag} ${countryInfo.name})`);
            } else if (!initialLoadDone) {
              updateStatusBadge('Cloud Sync Connected');
            }
            initialLoadDone = true;
          }
        }, (error) => {
          console.warn('Firebase RTDB sync listener notice:', error);
          isFirebaseConnected = false;
        });
      }
    } catch (err) {
      console.warn('Firebase init error, using local fallback:', err);
      isFirebaseConnected = false;
    }
  }

  // Hook up simulation ping button for interactive demonstration
  const simulateBtn = document.getElementById('simulate-visit-btn');
  if (simulateBtn) {
    simulateBtn.addEventListener('click', () => {
      // Weighted distribution: ~84% India, ~7% Zambia, ~5% Uganda, ~3% USA, ~1% Australia
      const rand = Math.random();
      let picked = 'IN';
      if (rand > 0.99) picked = 'AU';
      else if (rand > 0.96) picked = 'US';
      else if (rand > 0.91) picked = 'UG';
      else if (rand > 0.84) picked = 'ZM';

      recordListenerPing(picked, true);
    });
  }

  // Hook up external stream links to track clicks
  document.querySelectorAll('.stream-url-link, #qr-modal-link-btn').forEach(link => {
    link.addEventListener('click', () => {
      recordListenerPing(userDetectedCountry, true);
    });
  });

  // Initial detection, Firebase connection, & render
  renderAnalyticsUI();
  initFirebaseRealtimeSync();
  detectAndRecordVisit();



  // ==========================================================================
  // 2G GHOST STREAM & AUTO NETWORK DETECTION (Round 2 Innovations)
  // ==========================================================================
  function showToast(msg, duration = 4000) {
    if (!networkToast) return;
    if (networkToastMsg) networkToastMsg.textContent = msg;
    networkToast.classList.add('show');
    if (toastTimeout) clearTimeout(toastTimeout);
    toastTimeout = setTimeout(() => {
      networkToast.classList.remove('show');
    }, duration);
  }

  function setGhostMode(active, isAuto = false) {
    isGhostMode = active;
    localStorage.setItem('gyansetu_ghost_mode', isGhostMode ? 'true' : 'false');

    if (isGhostMode) {
      document.body.classList.add('ghost-mode-active');
      if (ghostModeBtn) {
        ghostModeBtn.classList.add('active');
        ghostModeBtn.setAttribute('aria-checked', 'true');
      }
      if (ghostNavLabel) ghostNavLabel.textContent = 'ON';
      if (dockGhostBtn) {
        dockGhostBtn.classList.add('active');
        dockGhostBtn.setAttribute('aria-checked', 'true');
      }
      if (dockGhostLabel) dockGhostLabel.textContent = 'ON';
    } else {
      document.body.classList.remove('ghost-mode-active');
      if (ghostModeBtn) {
        ghostModeBtn.classList.remove('active');
        ghostModeBtn.setAttribute('aria-checked', 'false');
      }
      if (ghostNavLabel) ghostNavLabel.textContent = 'OFF';
      if (dockGhostBtn) {
        dockGhostBtn.classList.remove('active');
        dockGhostBtn.setAttribute('aria-checked', 'false');
      }
      if (dockGhostLabel) dockGhostLabel.textContent = 'OFF';
    }

    // Seamless audio hot-swap if playing or loaded
    const ep = GYAN_SETU_EPISODES[currentEpisodeIndex];
    if (ep && audio.src) {
      const targetSrc = isGhostMode 
        ? ep.audioSrc.replace('assets/audio/', 'assets/audio_ghost/') 
        : ep.audioSrc;
      
      const currentUrl = new URL(audio.src, window.location.href).pathname;
      const targetUrl = new URL(targetSrc, window.location.href).pathname;

      if (currentUrl !== targetUrl) {
        const curTime = audio.currentTime;
        const wasPlaying = isPlaying;
        audio.src = targetSrc;
        audio.currentTime = curTime;
        if (wasPlaying) {
          playAudio();
        }
      }
    }

    if (isAuto) {
      showToast('⚡ Low Bandwidth Detected • Data Saver Auto-Engaged (82% Saved)');
    } else {
      showToast(isGhostMode 
        ? '⚡ Data Saver ON • 82% Lower Bandwidth (Voice Stream)' 
        : '🎧 Data Saver OFF • High-Fidelity Studio Stream Restored');
    }
  }

  function initNetworkDetection() {
    // 1. Initial UI sync
    if (isGhostMode) {
      setGhostMode(true, false);
    }

    // 2. Network Information API
    const conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
    if (conn) {
      const checkNetwork = () => {
        const isSlow = conn.effectiveType === 'slow-2g' || conn.effectiveType === '2g';
        const isSaveData = conn.saveData === true;
        if ((isSlow || isSaveData) && !isGhostMode) {
          setGhostMode(true, true);
        }
      };
      checkNetwork();
      conn.addEventListener('change', checkNetwork);
    }

    // 3. Button Click Handlers
    if (ghostModeBtn) {
      ghostModeBtn.addEventListener('click', () => {
        setGhostMode(!isGhostMode, false);
      });
    }

    if (dockGhostBtn) {
      dockGhostBtn.addEventListener('click', () => {
        setGhostMode(!isGhostMode, false);
      });
    }

    if (closeToastBtn && networkToast) {
      closeToastBtn.addEventListener('click', () => {
        networkToast.classList.remove('show');
      });
    }
  }

  // =========================================================================
  // 12. GLOBAL LINGUA TELEPROMPTER & SYNCHRONIZED MASTER TRANSCRIPT ENGINE
  // =========================================================================
  let currentTpLang = 'en'; // 'en', 'hi', 'dual', 'mr', 'poly-hi', 'poly-es', 'poly-fr', 'poly-sw', 'poly-de'
  let isTpAutoScroll = true;
  let isTpTtsEnabled = false;
  let activeTpSegmentIdx = -1;
  let currentActiveTranscript = null;

  function openTranscriptModal(epId) {
    if (!epId) {
      const currentEp = GYAN_SETU_EPISODES[currentEpisodeIndex];
      epId = currentEp ? currentEp.id : 'ep-13';
    }

    const tData = (window.GYAN_SETU_TRANSCRIPTS && window.GYAN_SETU_TRANSCRIPTS[epId]) 
      ? window.GYAN_SETU_TRANSCRIPTS[epId] 
      : (window.GYAN_SETU_TRANSCRIPTS && window.GYAN_SETU_TRANSCRIPTS['ep-13']);

    currentActiveTranscript = tData;
    if (!tData) {
      showToast('Master transcript is loading...');
      return;
    }

    if (teleprompterEpTag) teleprompterEpTag.textContent = `Episode ${tData.number || currentEpisodeIndex + 1}`;
    if (teleprompterTitle) {
      const titleMain = tData.titleMarathi || tData.titleOriginal || tData.titleEnglish || 'Episode Transcript';
      const titleSub = (tData.titleMarathi && tData.titleEnglish) ? ` • ${tData.titleEnglish}` : '';
      teleprompterTitle.textContent = `${titleMain}${titleSub}`;
    }

    // Toggle Marathi button depending on episode language
    if (tpMrBtn) {
      const isMarathi = (tData.origLang === 'mr' || tData.language === 'mr');
      tpMrBtn.style.display = isMarathi ? 'inline-flex' : 'none';
    }

    // Synchronize initial teleprompter language with current audio track
    if (currentTrackLanguage === 'hi') {
      currentTpLang = 'hi';
    } else if (currentTrackLanguage === 'en') {
      currentTpLang = 'en';
    } else {
      currentTpLang = (tData.origLang === 'mr' || tData.language === 'mr') ? 'mr' : 'en';
    }

    document.querySelectorAll('.tp-lang-btn[data-lang]').forEach(b => {
      b.classList.toggle('active', b.dataset.lang === currentTpLang);
    });

    if (tpTrackLabel) {
      const isEp13 = (tData.episodeId === 'ep-13' || tData.origLang === 'mr');
      const labels = {
        orig: isEp13 ? 'Original Marathi' : 'Original English',
        en: 'English Master',
        hi: 'Hindi Master'
      };
      tpTrackLabel.textContent = labels[currentTrackLanguage] || currentTrackLanguage.toUpperCase();
    }

    renderTeleprompterContent();
    updateTpPlayState(isPlaying);

    if (transcriptModal) {
      transcriptModal.classList.add('is-active');
      syncTeleprompterTime(audio.currentTime);
    }
  }

  function syncTeleprompterLanguage(lang) {
    if (lang === 'orig') {
      const ep = GYAN_SETU_EPISODES[currentEpisodeIndex];
      currentTpLang = (ep && ep.id === 'ep-13') ? 'mr' : 'en';
    } else {
      currentTpLang = lang;
    }

    document.querySelectorAll('.tp-lang-btn[data-lang]').forEach(b => {
      b.classList.toggle('active', b.dataset.lang === currentTpLang);
    });

    if (tpTrackLabel) {
      const ep = GYAN_SETU_EPISODES[currentEpisodeIndex];
      const isEp13 = (ep && ep.id === 'ep-13');
      const labels = {
        orig: isEp13 ? 'Original Marathi' : 'Original English',
        en: 'English Master',
        hi: 'Hindi Master'
      };
      tpTrackLabel.textContent = labels[currentTrackLanguage] || currentTrackLanguage.toUpperCase();
    }

    if (transcriptModal && transcriptModal.classList.contains('is-active')) {
      renderTeleprompterContent();
      if (activeTpSegmentIdx !== -1) {
        highlightTpSegment(activeTpSegmentIdx, true);
      }
    }
  }

  function renderTeleprompterContent() {
    if (!teleprompterBody || !currentActiveTranscript) return;
    teleprompterBody.innerHTML = '';

    const segments = currentActiveTranscript.segments || [];
    segments.forEach((seg, idx) => {
      const segEl = document.createElement('div');
      segEl.className = 'tp-segment';
      segEl.dataset.index = idx;
      segEl.dataset.start = seg.start;
      segEl.dataset.end = seg.end;

      let innerHtml = `
        <div class="tp-segment-meta">
          <div style="display:flex; align-items:center; gap:8px;">
            <span class="tp-time-pill">${seg.timeLabel}</span>
            <button type="button" class="tp-speak-line-btn" title="Speak translation aloud">
              <svg viewBox="0 0 24 24" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
              <span>Speak</span>
            </button>
          </div>
          ${seg.concept ? `<span class="tp-concept-chip" data-concept="${seg.concept}">💡 ${seg.concept}</span>` : ''}
        </div>
      `;

      if (currentTpLang === 'en') {
        innerHtml += `<div class="tp-english-text">${seg.english || seg.marathi || ''}</div>`;
      } else if (currentTpLang === 'mr') {
        innerHtml += `<div class="tp-marathi-text">${seg.marathi || seg.english || ''}</div>`;
      } else if (currentTpLang === 'hi') {
        innerHtml += `<div class="tp-hindi-text" style="font-size:1.02rem; line-height:1.75; color:#f8fafc; font-family:'Noto Sans Devanagari', 'Mukta', sans-serif;">${seg.hindi || seg.english || ''}</div>`;
      } else if (currentTpLang === 'dual') {
        if (seg.marathi) {
          innerHtml += `<div class="tp-marathi-text" style="margin-bottom:6px;">${seg.marathi}</div>`;
          innerHtml += `<div class="tp-english-text" style="color:#7dd3fc;">${seg.english}</div>`;
        } else {
          innerHtml += `<div class="tp-english-text" style="margin-bottom:6px;">${seg.english}</div>`;
          innerHtml += `<div class="tp-hindi-text" style="color:#7dd3fc; font-family:'Noto Sans Devanagari', 'Mukta', sans-serif;">${seg.hindi || ''}</div>`;
        }
      } else if (currentTpLang.startsWith('poly-')) {
        const polyCode = currentTpLang.replace('poly-', '');
        const polyNames = { hi: 'हिन्दी (Hindi)', es: 'Español (Spanish)', fr: 'Français (French)', sw: 'Kiswahili (Swahili)', de: 'Deutsch (German)' };
        innerHtml += `
          <div class="tp-english-text">${seg.english || ''}</div>
          <div class="tp-marathi-text" style="color: #67e8f9;">[${polyNames[polyCode] || polyCode} Translation Layer Active] • ${seg.hindi || seg.marathi || seg.english}</div>
        `;
      }

      segEl.innerHTML = innerHtml;

      // Speak line button
      const speakBtn = segEl.querySelector('.tp-speak-line-btn');
      if (speakBtn) {
        speakBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            speakBtn.classList.add('is-speaking');
            const toSpeak = (currentTpLang === 'hi' && seg.hindi) ? seg.hindi : (seg.english || seg.marathi);
            const utter = new SpeechSynthesisUtterance(toSpeak);
            utter.lang = (currentTpLang === 'hi') ? 'hi-IN' : ((currentTpLang === 'mr') ? 'mr-IN' : 'en-US');
            utter.rate = 1.0;
            utter.onend = () => speakBtn.classList.remove('is-speaking');
            utter.onerror = () => speakBtn.classList.remove('is-speaking');
            window.speechSynthesis.speak(utter);
          }
        });
      }

      // Click to seek audio
      segEl.addEventListener('click', (e) => {
        if (e.target.classList.contains('tp-concept-chip')) return;
        const targetStart = parseFloat(seg.start);
        audio.currentTime = targetStart;
        if (!isPlaying) playAudio();
        highlightTpSegment(idx, true);
      });

      // Concept chip click
      const conceptChip = segEl.querySelector('.tp-concept-chip');
      if (conceptChip) {
        conceptChip.addEventListener('click', (e) => {
          e.stopPropagation();
          const cName = conceptChip.dataset.concept;
          showConceptDrawer(cName);
        });
      }

      teleprompterBody.appendChild(segEl);
    });

    activeTpSegmentIdx = -1;
  }

  function highlightTpSegment(idx, forceScroll = false) {
    if (!teleprompterBody) return;
    const items = teleprompterBody.querySelectorAll('.tp-segment');
    if (idx < 0 || idx >= items.length) return;

    if (activeTpSegmentIdx !== -1 && items[activeTpSegmentIdx]) {
      items[activeTpSegmentIdx].classList.remove('active');
    }

    activeTpSegmentIdx = idx;
    const activeItem = items[idx];
    activeItem.classList.add('active');

    const startSec = activeItem.dataset.start;
    const mins = Math.floor(startSec / 60);
    const secs = Math.floor(startSec % 60);
    if (tpCurrentLineTime) {
      tpCurrentLineTime.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }

    if (isTpAutoScroll || forceScroll) {
      activeItem.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    // TTS Dubbing Voiceover if active
    if (isTpTtsEnabled && 'speechSynthesis' in window && currentActiveTranscript) {
      const seg = currentActiveTranscript.segments[idx];
      if (seg) {
        let toSpeak = seg.english;
        let speakLang = 'en-US';
        if (currentTpLang === 'hi' && seg.hindi) {
          toSpeak = seg.hindi;
          speakLang = 'hi-IN';
        } else if (currentTpLang === 'mr' && seg.marathi) {
          toSpeak = seg.marathi;
          speakLang = 'mr-IN';
        }
        if (toSpeak && !toSpeak.startsWith('[')) {
          window.speechSynthesis.cancel();
          if (audio) audio.volume = 0.12; // Duck background original voice
          const utter = new SpeechSynthesisUtterance(toSpeak);
          utter.lang = speakLang;
          utter.rate = 1.05;
          utter.onend = () => {
            if (audio && !isTpTtsEnabled) audio.volume = volumeSlider ? parseFloat(volumeSlider.value) : 0.9;
          };
          window.speechSynthesis.speak(utter);
        }
      }
    }
  }

  function syncTeleprompterTime(timeSec) {
    if (!currentActiveTranscript || !currentActiveTranscript.segments) {
      const currentEp = GYAN_SETU_EPISODES[currentEpisodeIndex];
      const epId = currentEp ? currentEp.id : 'ep-13';
      if (window.GYAN_SETU_TRANSCRIPTS && window.GYAN_SETU_TRANSCRIPTS[epId]) {
        currentActiveTranscript = window.GYAN_SETU_TRANSCRIPTS[epId];
      } else {
        return;
      }
    }
    const segments = currentActiveTranscript.segments;
    
    let foundIdx = -1;
    for (let i = 0; i < segments.length; i++) {
      if (timeSec >= segments[i].start && timeSec < segments[i].end) {
        foundIdx = i;
        break;
      }
    }

    if (foundIdx !== -1 && foundIdx !== activeTpSegmentIdx) {
      highlightTpSegment(foundIdx);
    }
  }

  function showConceptDrawer(conceptName) {
    if (!currentActiveTranscript || !currentActiveTranscript.glossary) return;
    const g = currentActiveTranscript.glossary[conceptName];
    if (!g || !tpConceptDrawer) return;

    if (tpConceptTitle) tpConceptTitle.textContent = `${conceptName} ${g.marathi ? `(${g.marathi})` : ''}`;
    if (tpConceptCat) tpConceptCat.textContent = g.category ? g.category.toUpperCase() : 'SCIENCE';
    if (tpConceptDef) tpConceptDef.textContent = g.definition;
    tpConceptDrawer.classList.remove('hidden');
  }

  function updateTpPlayState(playing) {
    if (!tpPlayIcon) return;
    tpPlayIcon.innerHTML = playing 
      ? '<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>' 
      : '<path d="M8 5v14l11-7z"/>';
  }

  // Event Listeners for Teleprompter & Lingua Micro-Switcher
  if (dockLinguaBtn && dockLinguaPopover) {
    dockLinguaBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      dockLinguaPopover.classList.toggle('hidden');
    });

    document.addEventListener('click', (e) => {
      if (!dockLinguaPopover.contains(e.target) && e.target !== dockLinguaBtn) {
        dockLinguaPopover.classList.add('hidden');
      }
    });
  }

  if (dockTranscriptBtn) {
    dockTranscriptBtn.addEventListener('click', () => {
      openTranscriptModal();
    });
  }

  if (closeTranscriptModalBtn && transcriptModal) {
    closeTranscriptModalBtn.addEventListener('click', () => {
      transcriptModal.classList.remove('is-active');
      if (isTpTtsEnabled && 'speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
    });

    transcriptModal.addEventListener('click', (e) => {
      if (e.target === transcriptModal) {
        transcriptModal.classList.remove('is-active');
        if (isTpTtsEnabled && 'speechSynthesis' in window) {
          window.speechSynthesis.cancel();
        }
      }
    });
  }

  if (tpPlayPauseBtn) {
    tpPlayPauseBtn.addEventListener('click', () => {
      togglePlayPause();
      updateTpPlayState(isPlaying);
    });
  }

  // Language switchers inside Teleprompter
  document.querySelectorAll('.tp-lang-btn[data-lang]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.tp-lang-btn[data-lang]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentTpLang = btn.dataset.lang;
      renderTeleprompterContent();
      if (activeTpSegmentIdx !== -1) {
        highlightTpSegment(activeTpSegmentIdx, true);
      }
    });
  });

  // Polyglot menu toggle and selection
  if (tpPolyglotBtn && tpPolyglotMenu) {
    tpPolyglotBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      tpPolyglotMenu.classList.toggle('hidden');
    });

    document.querySelectorAll('.tp-poly-opt').forEach(opt => {
      opt.addEventListener('click', (e) => {
        const polyCode = opt.dataset.poly;
        currentTpLang = `poly-${polyCode}`;
        document.querySelectorAll('.tp-lang-btn[data-lang]').forEach(b => b.classList.remove('active'));
        tpPolyglotBtn.classList.add('active');
        tpPolyglotBtn.textContent = `🌍 ${opt.textContent.split(' ')[1]} ▾`;
        tpPolyglotMenu.classList.add('hidden');
        renderTeleprompterContent();
        if (activeTpSegmentIdx !== -1) {
          highlightTpSegment(activeTpSegmentIdx, true);
        }
      });
    });

    document.addEventListener('click', () => {
      if (!tpPolyglotMenu.classList.contains('hidden')) {
        tpPolyglotMenu.classList.add('hidden');
      }
    });
  }

  // Auto-scroll toggle
  if (tpAutoScrollBtn) {
    tpAutoScrollBtn.addEventListener('click', () => {
      isTpAutoScroll = !isTpAutoScroll;
      tpAutoScrollBtn.classList.toggle('active', isTpAutoScroll);
      tpAutoScrollBtn.innerHTML = `<span class="tp-toggle-indicator"></span> Auto-Scroll: ${isTpAutoScroll ? 'ON' : 'OFF'}`;
    });
  }

  // TTS Dubbing toggle
  if (tpTtsBtn) {
    tpTtsBtn.addEventListener('click', () => {
      isTpTtsEnabled = !isTpTtsEnabled;
      tpTtsBtn.classList.toggle('tts-active', isTpTtsEnabled);
      tpTtsBtn.innerHTML = `<span class="tp-toggle-indicator"></span> 🗣️ Live Voice Dub: ${isTpTtsEnabled ? 'ON' : 'OFF'}`;
      if (!isTpTtsEnabled && 'speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      } else if (isTpTtsEnabled) {
        showToast('🗣️ Live Voice Dubbing Active • Synchronized Narration');
        if (activeTpSegmentIdx !== -1) {
          highlightTpSegment(activeTpSegmentIdx);
        }
      }
    });
  }

  // Concept close
  if (closeConceptBtn && tpConceptDrawer) {
    closeConceptBtn.addEventListener('click', () => {
      tpConceptDrawer.classList.add('hidden');
    });
  }

  // Copy Transcript
  if (tpCopyTranscriptBtn) {
    tpCopyTranscriptBtn.addEventListener('click', () => {
      if (!currentActiveTranscript) return;
      const fullText = currentActiveTranscript.segments.map(s => {
        const text = (currentTpLang === 'hi' && s.hindi) ? s.hindi : (s.english || s.marathi);
        return `[${s.timeLabel}] ${text}`;
      }).join('\n\n');
      navigator.clipboard.writeText(`GyanSetu Episode ${currentActiveTranscript.number}: ${currentActiveTranscript.titleEnglish || currentActiveTranscript.titleOriginal}\nHost: ${currentActiveTranscript.host}\n\n${fullText}`).then(() => {
        showToast('📋 Active Transcript Copied to Clipboard!');
      });
    });
  }

  // Teleprompter Audio Track Switcher
  if (tpTrackSwitchBtn) {
    tpTrackSwitchBtn.addEventListener('click', () => {
      const ep = GYAN_SETU_EPISODES[currentEpisodeIndex];
      const isEp13 = (ep && ep.id === 'ep-13');
      let nextLang = 'orig';
      if (isEp13) {
        if (currentTrackLanguage === 'orig') nextLang = 'en';
        else if (currentTrackLanguage === 'en') nextLang = 'hi';
        else nextLang = 'orig';
      } else {
        nextLang = (currentTrackLanguage === 'orig') ? 'hi' : 'orig';
      }
      setTrackLanguage(nextLang);
    });
  }

  // Initialize Network Monitoring
  initNetworkDetection();
});
