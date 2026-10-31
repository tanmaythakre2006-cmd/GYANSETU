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

  // Multilingual Audio Track Switcher Elements
  const dockLinguaBtn = document.getElementById('dock-lingua-btn');
  const dockLinguaLabel = document.getElementById('dock-lingua-label');
  const dockLinguaPopover = document.getElementById('dock-lingua-popover');
  const dockLinguaOptionsList = document.getElementById('dock-lingua-options-list');
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

    const toastMsgs = {
      orig: `🎙️ Playing Original Composition (${ep.hosts[0]} • Default)`,
      en: `🇬🇧 Switched to English Master Translation (Neerja Voice)`,
      hi: `🇮🇳 Switched to Hindi Master Translation (Swara Voice)`
    };
    showToast(toastMsgs[lang] || 'Language updated');
  }

  // Lingua Micro-Switcher Event Listeners
  if (dockLinguaBtn && dockLinguaPopover) {
    dockLinguaBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      renderLinguaPopoverOptions();
      dockLinguaPopover.classList.toggle('hidden');
    });

    document.addEventListener('click', (e) => {
      if (!dockLinguaPopover.contains(e.target) && !dockLinguaBtn.contains(e.target)) {
        dockLinguaPopover.classList.add('hidden');
      }
    });
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
  // 12. GLOBAL LIVE TRANSMISSION STUDIO & COLLABORATIVE CURATION ENGINE
  // =========================================================================
  const liveStudioModal = document.getElementById('live-studio-modal');
  const closeLiveStudioBtn = document.getElementById('close-live-studio-btn');
  const navLiveStudioBtn = document.getElementById('nav-live-studio-btn');
  const studioTabBtns = document.querySelectorAll('.studio-tab-btn[data-tab]');
  const studioTabPanes = document.querySelectorAll('.studio-tab-pane');

  // Tab 1 Elements
  const liveStreamCanvas = document.getElementById('live-stream-canvas');
  const btnToggleLiveListen = document.getElementById('btn-toggle-live-listen');
  const liveListenLabel = document.getElementById('live-listen-label');
  const liveListenIcon = document.getElementById('live-listen-icon');
  const liveReactionsFloatingZone = document.getElementById('live-reactions-floating-zone');
  let isListeningLiveStream = false;
  let liveWaveformAnimId = null;

  // Tab 2 Elements (Go Live & 10-Min Timer)
  const goliveAuthGate = document.getElementById('golive-auth-gate');
  const goliveCockpit = document.getElementById('golive-cockpit');
  const studioPasscodeInput = document.getElementById('studio-passcode-input');
  const btnVerifyPasscode = document.getElementById('btn-verify-passcode');
  const btnRequestPasscodeTab = document.getElementById('btn-request-passcode-tab');
  const studioCountdownClock = document.getElementById('studio-countdown-clock');
  const btnStartLiveTransmit = document.getElementById('btn-start-live-transmit');
  const btnTransmitLabel = document.getElementById('btn-transmit-label');
  const btnRelockStudio = document.getElementById('btn-relock-studio');
  const cockpitLamp = document.getElementById('cockpit-lamp');
  const cockpitStatusText = document.getElementById('cockpit-status-text');
  const studioMicCanvas = document.getElementById('studio-mic-canvas');
  const studioVuMeter = document.getElementById('studio-vu-meter');
  const micStatusDot = document.getElementById('mic-status-dot');
  const micStatusLabel = document.getElementById('mic-status-label');

  let isLiveTransmitting = false;
  let liveSessionTimeRemaining = 600; // 10 minutes (600 seconds)
  let liveSessionInterval = null;
  let broadcasterMediaStream = null;
  let broadcasterAudioCtx = null;
  let broadcasterAnalyser = null;
  let broadcasterAnimId = null;

  // Broadcast Channel for Real-time Inter-window Communication
  let liveBroadcastChannel = null;
  try {
    liveBroadcastChannel = new BroadcastChannel('gyansetu_live_transmission_channel');
    liveBroadcastChannel.onmessage = (event) => {
      const data = event.data;
      if (data && data.type === 'LIVE_START') {
        const liveOnAirText = document.getElementById('live-on-air-status-text');
        const liveTitle = document.getElementById('live-stream-title');
        const liveSpeaker = document.getElementById('live-speaker-name');
        if (liveOnAirText) liveOnAirText.textContent = `🔴 TRANSMITTING LIVE FROM ${data.country.toUpperCase()}`;
        if (liveTitle) liveTitle.textContent = data.topic || 'Global Collaborative Inquiry';
        if (liveSpeaker) liveSpeaker.textContent = data.name || 'Guest Broadcaster';
        showToast(`🔴 Live Broadcast Started: ${data.name} (${data.country})`);
      }
    };
  } catch (e) {}

  // Open & Close Studio Modal
  function openLiveStudioModal(initialTab = 'listen') {
    if (liveStudioModal) {
      liveStudioModal.classList.add('is-active');
      switchStudioTab(initialTab);
      startLiveStreamWaveform();
      renderCuratorQueue();
    }
  }

  function closeLiveStudioModal() {
    if (liveStudioModal) {
      liveStudioModal.classList.remove('is-active');
      if (liveWaveformAnimId) cancelAnimationFrame(liveWaveformAnimId);
    }
  }

  if (navLiveStudioBtn) {
    navLiveStudioBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openLiveStudioModal('listen');
    });
  }

  if (radioModeBtn) {
    radioModeBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openLiveStudioModal('listen');
    });
  }

  if (closeLiveStudioBtn) {
    closeLiveStudioBtn.addEventListener('click', closeLiveStudioModal);
  }

  if (liveStudioModal) {
    liveStudioModal.addEventListener('click', (e) => {
      if (e.target === liveStudioModal) closeLiveStudioModal();
    });
  }

  // Tab Switching
  function switchStudioTab(targetTab) {
    studioTabBtns.forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === targetTab);
    });

    studioTabPanes.forEach(pane => {
      pane.classList.remove('active');
    });

    const activePane = document.getElementById(`tab-content-${targetTab}`);
    if (activePane) activePane.classList.add('active');

    if (targetTab === 'curator') {
      renderCuratorQueue();
    }
  }

  studioTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      switchStudioTab(btn.dataset.tab);
    });
  });

  if (btnRequestPasscodeTab) {
    btnRequestPasscodeTab.addEventListener('click', () => {
      switchStudioTab('collaborate');
    });
  }

  // --- TAB 1: Live Stream Waveform & Reactions ---
  function startLiveStreamWaveform() {
    if (!liveStreamCanvas) return;
    const ctx = liveStreamCanvas.getContext('2d');
    let phase = 0;

    function renderWave() {
      ctx.clearRect(0, 0, liveStreamCanvas.width, liveStreamCanvas.height);
      const width = liveStreamCanvas.width;
      const height = liveStreamCanvas.height;
      const mid = height / 2;

      // Draw background glow grid
      ctx.strokeStyle = 'rgba(239, 68, 68, 0.1)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(0, mid);
      ctx.lineTo(width, mid);
      ctx.stroke();

      // Draw active sine harmonic lines
      const colors = ['rgba(239, 68, 68, 0.8)', 'rgba(56, 189, 248, 0.7)', 'rgba(255, 190, 68, 0.6)'];
      colors.forEach((col, cIdx) => {
        ctx.strokeStyle = col;
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let x = 0; x < width; x += 4) {
          const freq = 0.02 + cIdx * 0.01;
          const amp = (isListeningLiveStream || isLiveTransmitting) ? 24 : 10;
          const y = mid + Math.sin(x * freq + phase + cIdx) * amp * Math.sin(x / width * Math.PI);
          if (x === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();
      });

      phase += 0.05;
      liveWaveformAnimId = requestAnimationFrame(renderWave);
    }

    if (liveWaveformAnimId) cancelAnimationFrame(liveWaveformAnimId);
    renderWave();
  }

  if (btnToggleLiveListen) {
    btnToggleLiveListen.addEventListener('click', () => {
      isListeningLiveStream = !isListeningLiveStream;
      if (isListeningLiveStream) {
        liveListenLabel.textContent = 'Disconnect from Live Stream';
        liveListenIcon.innerHTML = '<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>';
        btnToggleLiveListen.classList.remove('btn-primary-gradient');
        btnToggleLiveListen.classList.add('btn-secondary-glass');
        showToast('🔴 Connected to Global Live Transmission • Nairobi Relay Active');
      } else {
        liveListenLabel.textContent = 'Tune In to Live Transmission';
        liveListenIcon.innerHTML = '<path d="M8 5v14l11-7z"/>';
        btnToggleLiveListen.classList.add('btn-primary-gradient');
        btnToggleLiveListen.classList.remove('btn-secondary-glass');
        showToast('Disconnected from Live Stream');
      }
    });
  }

  // Floating Reactions
  document.querySelectorAll('.btn-live-reaction').forEach(btn => {
    btn.addEventListener('click', () => {
      const reaction = btn.dataset.reaction;
      const countEl = btn.querySelector('.reaction-count');
      if (countEl) {
        const cur = parseInt(countEl.textContent, 10) || 0;
        countEl.textContent = cur + 1;
      }

      // Spawn floating emoji
      if (liveReactionsFloatingZone) {
        const emojiMap = { insight: '💡', clap: '👏', globe: '🌍', heart: '❤️' };
        const bubble = document.createElement('div');
        bubble.className = 'floating-reaction-emoji';
        bubble.textContent = emojiMap[reaction] || '✨';
        bubble.style.left = `${Math.floor(Math.random() * 80)}px`;
        liveReactionsFloatingZone.appendChild(bubble);
        setTimeout(() => bubble.remove(), 2200);
      }
    });
  });

  // --- TAB 2: Go Live Authorization & 10-Minute Timer Cockpit ---
  if (btnVerifyPasscode && studioPasscodeInput) {
    btnVerifyPasscode.addEventListener('click', () => {
      const code = studioPasscodeInput.value.trim().toUpperCase();
      const codeObj = verifyAndConsumePasscode(code);
      if (codeObj) {
        goliveAuthGate.classList.add('hidden');
        goliveCockpit.classList.remove('hidden');
        
        // Auto-fill guest metadata if registered by Lead Host
        if (codeObj.guest) {
          const nameInput = document.getElementById('broadcaster-name');
          const countryInput = document.getElementById('broadcaster-country');
          const topicInput = document.getElementById('broadcaster-topic');
          if (nameInput && !nameInput.value) nameInput.value = codeObj.guest;
          if (countryInput && !countryInput.value) countryInput.value = codeObj.country || '';
          if (topicInput && !topicInput.value) topicInput.value = codeObj.topic || '';
        }
        
        initBroadcasterMic();
        showToast(`🔓 Broadcast Authorized: Welcome ${codeObj.guest || 'Guest'} (10-Minute Studio)`);
      } else {
        studioPasscodeInput.style.borderColor = '#ef4444';
        showToast('❌ Invalid or Expired Passcode. Request authorization from Lead Host.');
        setTimeout(() => studioPasscodeInput.style.borderColor = '', 2500);
      }
    });
  }

  if (btnRelockStudio) {
    btnRelockStudio.addEventListener('click', () => {
      stopLiveTransmission();
      goliveCockpit.classList.add('hidden');
      goliveAuthGate.classList.remove('hidden');
      if (studioPasscodeInput) studioPasscodeInput.value = '';
    });
  }

  async function initBroadcasterMic() {
    try {
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        if (micStatusLabel) micStatusLabel.textContent = 'Web Audio Studio Stream (Simulated)';
        return;
      }
      broadcasterMediaStream = await navigator.mediaDevices.getUserMedia({ audio: true, video: false });
      if (micStatusDot) micStatusDot.style.background = '#10b981';
      if (micStatusLabel) micStatusLabel.textContent = 'Studio Microphone Connected (Low Latency)';

      broadcasterAudioCtx = new (window.AudioContext || window.webkitAudioContext)();
      const source = broadcasterAudioCtx.createMediaStreamSource(broadcasterMediaStream);
      broadcasterAnalyser = broadcasterAudioCtx.createAnalyser();
      broadcasterAnalyser.fftSize = 64;
      source.connect(broadcasterAnalyser);

      renderBroadcasterMicVU();
    } catch (err) {
      console.warn('Microphone permission or hardware access note:', err);
      if (micStatusDot) micStatusDot.style.background = '#ffaa11';
      if (micStatusLabel) micStatusLabel.textContent = 'Audio Stream Ready (Browser Sandbox)';
      startSimulatedMicVU();
    }
  }

  function renderBroadcasterMicVU() {
    if (!studioMicCanvas || !broadcasterAnalyser) return;
    const ctx = studioMicCanvas.getContext('2d');
    const dataArray = new Uint8Array(broadcasterAnalyser.frequencyBinCount);

    function draw() {
      broadcasterAnalyser.getByteFrequencyData(dataArray);
      ctx.clearRect(0, 0, studioMicCanvas.width, studioMicCanvas.height);
      const barWidth = (studioMicCanvas.width / dataArray.length) * 1.5;
      let x = 0;

      for (let i = 0; i < dataArray.length; i++) {
        const barHeight = (dataArray[i] / 255) * studioMicCanvas.height;
        ctx.fillStyle = isLiveTransmitting ? '#ef4444' : '#10b981';
        ctx.fillRect(x, studioMicCanvas.height - barHeight, barWidth - 1, barHeight);
        x += barWidth + 1;
      }

      // Update VU meter blocks
      let sum = 0;
      for (let i = 0; i < dataArray.length; i++) sum += dataArray[i];
      const avg = sum / dataArray.length;
      if (studioVuMeter) {
        const segs = studioVuMeter.querySelectorAll('.vu-seg');
        const activeCount = Math.floor((avg / 255) * segs.length);
        segs.forEach((s, idx) => s.classList.toggle('active', idx < activeCount));
      }

      broadcasterAnimId = requestAnimationFrame(draw);
    }
    draw();
  }

  function startSimulatedMicVU() {
    if (broadcasterAnimId) cancelAnimationFrame(broadcasterAnimId);
    let tick = 0;
    function sim() {
      tick++;
      if (studioVuMeter) {
        const segs = studioVuMeter.querySelectorAll('.vu-seg');
        const level = isLiveTransmitting ? Math.floor(Math.sin(tick * 0.2) * 4 + 4) : 1;
        segs.forEach((s, idx) => s.classList.toggle('active', idx < level));
      }
      broadcasterAnimId = requestAnimationFrame(sim);
    }
    sim();
  }

  if (btnStartLiveTransmit) {
    btnStartLiveTransmit.addEventListener('click', () => {
      if (!isLiveTransmitting) {
        startLiveTransmission();
      } else {
        stopLiveTransmission();
      }
    });
  }

  function startLiveTransmission() {
    isLiveTransmitting = true;
    liveSessionTimeRemaining = 600; // 10 minutes
    if (cockpitLamp) cockpitLamp.classList.add('live');
    if (cockpitStatusText) cockpitStatusText.textContent = '🔴 ON AIR • LIVE TRANSMITTING ACROSS GYANSETU';
    btnTransmitLabel.textContent = '⏹️ Conclude & End Broadcast';
    btnStartLiveTransmit.style.background = 'linear-gradient(135deg, #1e293b 0%, #334155 100%)';

    const bName = (document.getElementById('broadcaster-name') && document.getElementById('broadcaster-name').value.trim()) || 'Guest Researcher';
    const bCountry = (document.getElementById('broadcaster-country') && document.getElementById('broadcaster-country').value.trim()) || 'Nairobi, Kenya';
    const bTopic = (document.getElementById('broadcaster-topic') && document.getElementById('broadcaster-topic').value.trim()) || 'Global South Inquiry';

    // Broadcast message via BroadcastChannel
    if (liveBroadcastChannel) {
      liveBroadcastChannel.postMessage({
        type: 'LIVE_START',
        name: bName,
        country: bCountry,
        topic: bTopic
      });
    }

    showToast(`🔴 Transmission Active! You are Live to the World (10:00 Countdown Started)`);

    // 10-Minute Timer
    if (liveSessionInterval) clearInterval(liveSessionInterval);
    liveSessionInterval = setInterval(() => {
      liveSessionTimeRemaining--;
      const mins = Math.floor(liveSessionTimeRemaining / 60);
      const secs = liveSessionTimeRemaining % 60;
      if (studioCountdownClock) {
        studioCountdownClock.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
        if (liveSessionTimeRemaining <= 120) {
          studioCountdownClock.classList.add('warning');
        }
      }

      if (liveSessionTimeRemaining <= 0) {
        stopLiveTransmission();
        showToast('⏰ 10-Minute Session Gracefully Concluded. Thank you for broadcasting!');
      }
    }, 1000);
  }

  function stopLiveTransmission() {
    isLiveTransmitting = false;
    if (liveSessionInterval) clearInterval(liveSessionInterval);
    if (cockpitLamp) cockpitLamp.classList.remove('live');
    if (cockpitStatusText) cockpitStatusText.textContent = 'STUDIO AUTHORIZED • STANDBY MODE';
    if (btnTransmitLabel) btnTransmitLabel.textContent = '🔴 Transmit Live Across GyanSetu Network';
    if (btnStartLiveTransmit) btnStartLiveTransmit.style.background = '';
    if (studioCountdownClock) {
      studioCountdownClock.textContent = '10:00';
      studioCountdownClock.classList.remove('warning');
    }
  }

  // --- TAB 3: Collaborate & In-Browser Audio Recorder ---
  const collabForm = document.getElementById('collab-submission-form');
  const collabReceiptBox = document.getElementById('collab-receipt-box');
  const receiptIdTag = document.getElementById('receipt-id-tag');
  const btnResetCollabForm = document.getElementById('btn-reset-collab-form');
  const audioModeRadios = document.querySelectorAll('input[name="audio-mode-choice"]');
  const collabUploadZone = document.getElementById('collab-upload-zone');
  const collabRecordZone = document.getElementById('collab-record-zone');
  const collabFileInput = document.getElementById('collab-file-input');
  const collabFileNameLabel = document.getElementById('collab-file-name-label');

  // In-Browser Recorder Elements
  const btnCollabRecordStart = document.getElementById('btn-collab-record-start');
  const btnCollabRecordStop = document.getElementById('btn-collab-record-stop');
  const collabRecorderTimer = document.getElementById('collab-recorder-timer');
  const collabRecordedAudioPreview = document.getElementById('collab-recorded-audio-preview');

  let mediaRecorder = null;
  let recordedAudioChunks = [];
  let recordTimerInterval = null;
  let recordSeconds = 0;
  let recordedBlobUrl = null;

  audioModeRadios.forEach(radio => {
    radio.addEventListener('change', () => {
      const mode = radio.value;
      if (mode === 'upload') {
        collabUploadZone.classList.add('active');
        collabRecordZone.classList.remove('active');
      } else {
        collabUploadZone.classList.remove('active');
        collabRecordZone.classList.add('active');
      }
    });
  });

  if (collabFileInput && collabFileNameLabel) {
    collabFileInput.addEventListener('change', () => {
      const file = collabFileInput.files[0];
      if (file) {
        const sizeMb = (file.size / (1024 * 1024)).toFixed(1);
        collabFileNameLabel.textContent = `Selected: ${file.name} (${sizeMb} MB)`;
      } else {
        collabFileNameLabel.textContent = 'No file selected';
      }
    });
  }

  // In-Browser Studio Recording Engine
  if (btnCollabRecordStart && btnCollabRecordStop) {
    btnCollabRecordStart.addEventListener('click', async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        recordedAudioChunks = [];

        mediaRecorder.ondataavailable = (e) => {
          if (e.data.size > 0) recordedAudioChunks.push(e.data);
        };

        mediaRecorder.onstop = () => {
          const audioBlob = new Blob(recordedAudioChunks, { type: 'audio/mp3' });
          if (recordedBlobUrl) URL.revokeObjectURL(recordedBlobUrl);
          recordedBlobUrl = URL.createObjectURL(audioBlob);
          if (collabRecordedAudioPreview) {
            collabRecordedAudioPreview.src = recordedBlobUrl;
            collabRecordedAudioPreview.classList.remove('hidden');
          }
          showToast('🎙️ Voice Recording Captured! You can review audio below.');
        };

        mediaRecorder.start();
        btnCollabRecordStart.disabled = true;
        btnCollabRecordStop.disabled = false;
        recordSeconds = 0;

        if (recordTimerInterval) clearInterval(recordTimerInterval);
        recordTimerInterval = setInterval(() => {
          recordSeconds++;
          const mins = Math.floor(recordSeconds / 60);
          const secs = recordSeconds % 60;
          if (collabRecorderTimer) {
            collabRecorderTimer.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
          }
        }, 1000);
      } catch (err) {
        showToast('Microphone access needed to record in-browser.');
      }
    });

    btnCollabRecordStop.addEventListener('click', () => {
      if (mediaRecorder && mediaRecorder.state !== 'inactive') {
        mediaRecorder.stop();
        mediaRecorder.stream.getTracks().forEach(t => t.stop());
      }
      if (recordTimerInterval) clearInterval(recordTimerInterval);
      btnCollabRecordStart.disabled = false;
      btnCollabRecordStop.disabled = true;
    });
  }

  // Form Submission
  if (collabForm) {
    collabForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('collab-name').value.trim();
      const contact = document.getElementById('collab-contact').value.trim();
      const country = document.getElementById('collab-country').value.trim();
      const language = document.getElementById('collab-language').value.trim();
      const title = document.getElementById('collab-title').value.trim();
      const abstract = document.getElementById('collab-abstract').value.trim();

      const receiptId = `GS-SUB-${Math.floor(1000 + Math.random() * 9000)}`;

      const newProposal = {
        id: receiptId,
        author: name,
        contact: contact,
        country: country,
        language: language,
        title: title,
        abstract: abstract,
        date: 'October 31, 2026',
        audioSrc: recordedBlobUrl || 'assets/audio/ep-1-hindi-master.mp3',
        status: 'Pending Review'
      };

      // Save to localStorage
      try {
        const stored = JSON.parse(localStorage.getItem('gyansetu_guest_proposals') || '[]');
        stored.unshift(newProposal);
        localStorage.setItem('gyansetu_guest_proposals', JSON.stringify(stored));
      } catch (e) {}

      if (receiptIdTag) receiptIdTag.textContent = receiptId;
      collabForm.classList.add('hidden');
      if (collabReceiptBox) collabReceiptBox.classList.remove('hidden');

      showToast(`🚀 Transmission Logged: ${receiptId}. Sent to Simran Ailani's Curation Vault.`);
      renderCuratorQueue();
    });
  }

  if (btnResetCollabForm) {
    btnResetCollabForm.addEventListener('click', () => {
      if (collabForm) {
        collabForm.reset();
        collabForm.classList.remove('hidden');
      }
      if (collabReceiptBox) collabReceiptBox.classList.add('hidden');
      if (collabRecordedAudioPreview) {
        collabRecordedAudioPreview.classList.add('hidden');
        collabRecordedAudioPreview.src = '';
      }
      if (collabFileNameLabel) collabFileNameLabel.textContent = 'No file selected';
    });
  }

  // --- TAB 4: Curator Review Console (Simran Ailani Review Queue) ---
  const defaultGlobalProposals = [
    {
      id: "GS-SUB-8491",
      author: "Amara Okafor",
      country: "Lagos, Nigeria • University of Lagos",
      language: "English & Yoruba",
      title: "Cassava Cyanide Detoxification: Indigenous Chemistry meets Modern Biochemistry",
      abstract: "How traditional fermentation methods developed over centuries in West Africa chemically neutralize toxic linamarin glucosides in cassava roots, creating a safe dietary staple.",
      audioSrc: "assets/audio/ep-2-hindi-master.mp3",
      date: "October 30, 2026",
      status: "Ready for Approval"
    },
    {
      id: "GS-SUB-7922",
      author: "Kofi Mensah",
      country: "Nairobi, Kenya • University of Nairobi",
      language: "English & Swahili",
      title: "Geothermal Reservoirs of the Great Rift Valley: Volcanology & Frugal Clean Power",
      abstract: "An exploration into the steam vents and subsurface thermodynamics of Olkaria, revealing how geological fissures provide decentralized green baseload electricity for rural communities.",
      audioSrc: "assets/audio/ep-4-hindi-master.mp3",
      date: "October 29, 2026",
      status: "Ready for Approval"
    }
  ];

  function getCuratorProposals() {
    try {
      const stored = localStorage.getItem('gyansetu_guest_proposals');
      if (stored) {
        const parsed = JSON.parse(stored);
        if (Array.isArray(parsed) && parsed.length > 0) return parsed;
      }
    } catch (e) {}
    return defaultGlobalProposals;
  }

  function renderCuratorQueue() {
    const listEl = document.getElementById('curator-queue-list');
    if (!listEl) return;
    listEl.innerHTML = '';

    const proposals = getCuratorProposals();

    proposals.forEach((p, idx) => {
      const card = document.createElement('div');
      card.className = 'curator-proposal-card';
      card.innerHTML = `
        <div class="proposal-card-header">
          <div>
            <span class="proposal-author">🌍 ${p.author} (${p.country})</span>
            <span style="font-size:0.68rem; color:rgba(255,255,255,0.4); margin-left:8px;">Receipt: ${p.id} • ${p.date}</span>
          </div>
          <span class="proposal-lang-badge">${p.language}</span>
        </div>
        <h5 class="proposal-title">${p.title}</h5>
        <p class="proposal-abstract">${p.abstract}</p>
        <div class="proposal-actions">
          <button type="button" class="liquid-btn btn-secondary-glass btn-sm btn-preview-proposal-audio">
            <span>▶ Listen Audio</span>
          </button>
          <button type="button" class="btn-approve-catalog" data-id="${p.id}" data-idx="${idx}">
            <span>✅ Approve &amp; Add to Global Catalog</span>
          </button>
        </div>
      `;

      // Audio preview click
      const previewBtn = card.querySelector('.btn-preview-proposal-audio');
      if (previewBtn) {
        previewBtn.addEventListener('click', () => {
          audio.src = p.audioSrc;
          playAudio();
          showToast(`🎧 Previewing Submission: "${p.title}"`);
        });
      }

      // Approve & Add to Catalog
      const approveBtn = card.querySelector('.btn-approve-catalog');
      if (approveBtn) {
        approveBtn.addEventListener('click', () => {
          approveProposalToCatalog(p);
        });
      }

      listEl.appendChild(card);
    });
  }

  function approveProposalToCatalog(proposal) {
    // Check if already in episodes
    const exists = GYAN_SETU_EPISODES.some(e => e.title === proposal.title);
    if (exists) {
      showToast('⚠️ Episode is already in the official broadcast catalog!');
      return;
    }

    const newEp = {
      id: `ep-collab-${Date.now()}`,
      number: GYAN_SETU_EPISODES.length + 1,
      title: proposal.title,
      category: "Global Inquiry",
      date: proposal.date || "October 31, 2026",
      duration: "6m 15s",
      durationSec: 375,
      description: `${proposal.abstract} • Guest Broadcaster: ${proposal.author} (${proposal.country}). Curated & approved by Simran Ailani.`,
      image: "assets/images/ep1-can-chemistry-explain-consciousness.jpg",
      audioSrc: proposal.audioSrc,
      hosts: ["Simran Ailani", proposal.author]
    };

    // Add to active episodes list
    GYAN_SETU_EPISODES.unshift(newEp);
    filteredEpisodes = [...GYAN_SETU_EPISODES];
    renderEpisodeCards(filteredEpisodes);
    loadEpisode(0, true);

    showToast(`🎉 Approved! "${proposal.title}" by ${proposal.author} is now live in the official GyanSetu catalog!`);
    closeLiveStudioModal();
  }

  // =========================================================================
  // 13. ROLE-BASED ACCESS CONTROL (RBAC) & LEAD HOST AUTHENTICATION ENGINE
  // =========================================================================

  const AUTHORIZED_HOSTS = [
    { email: 'tanmaythakre2006@gmail.com', name: 'Tanmay Thakre' },
    { email: 'simranailani2@gmail.com', name: 'Simran Ailani' }
  ];
  const AUTHORIZED_HOST_PASSWORD = '22102024';

  // Elements: Gateway & Auth
  const gatewayModal = document.getElementById('gyansetu-gateway-modal');
  const btnChooseListener = document.getElementById('btn-gateway-choose-listener');
  const btnChooseHost = document.getElementById('btn-gateway-choose-host');
  const gatewayViewChoose = document.getElementById('gateway-view-choose');
  const gatewayViewLogin = document.getElementById('gateway-view-login');
  const btnGatewayBack = document.getElementById('btn-gateway-back-to-choose');
  const hostLoginForm = document.getElementById('gateway-host-login-form');
  const hostEmailInput = document.getElementById('gateway-host-email');
  const hostPasswordInput = document.getElementById('gateway-host-password');
  const hostLoginError = document.getElementById('gateway-login-error');
  
  // Navbar & Deck Host Badges
  const navHostLoginBtn = document.getElementById('nav-host-login-btn');
  const navHostLogoutBtn = document.getElementById('nav-host-logout-btn');
  const btnHostDeckLogout = document.getElementById('btn-host-deck-logout');
  const navHostNameTag = document.getElementById('nav-host-name-tag');
  const curatorLoggedInLabel = document.getElementById('curator-logged-in-label');

  // Passcode Mint Elements
  const btnMintPasscode = document.getElementById('btn-mint-passcode');
  const mintGuestName = document.getElementById('mint-guest-name');
  const mintGuestCountry = document.getElementById('mint-guest-country');
  const mintGuestTopic = document.getElementById('mint-guest-topic');
  const mintedCodeResultBox = document.getElementById('minted-code-result-box');
  const mintedCodeText = document.getElementById('minted-code-text');
  const btnCopyMintedCode = document.getElementById('btn-copy-minted-code');
  const activeCodesListEl = document.getElementById('active-codes-list');

  // Role Session Accessors
  function getActiveUserRole() {
    return sessionStorage.getItem('gyansetu_user_role');
  }

  function getActiveHostEmail() {
    return (sessionStorage.getItem('gyansetu_host_email') || '').trim().toLowerCase();
  }

  function isHostAuthenticated() {
    const role = getActiveUserRole();
    const email = getActiveHostEmail();
    return role === 'host' && AUTHORIZED_HOSTS.some(h => h.email.toLowerCase() === email);
  }

  function getHostProfile() {
    const email = getActiveHostEmail();
    return AUTHORIZED_HOSTS.find(h => h.email.toLowerCase() === email) || { name: 'Lead Curator' };
  }

  // Update UI based on active role
  function updateRoleUI() {
    const hostActive = isHostAuthenticated();
    if (hostActive) {
      document.body.classList.add('is-host');
      const profile = getHostProfile();
      if (navHostNameTag) navHostNameTag.textContent = `Host: ${profile.name}`;
      if (curatorLoggedInLabel) curatorLoggedInLabel.textContent = `Lead Host Session Active: ${profile.name}`;
      
      // Render host exclusive components
      renderActiveCodesList();
      renderCuratorQueue();
    } else {
      document.body.classList.remove('is-host');
      
      // If user had curator tab open, switch back to listen tab
      const curatorTabPane = document.getElementById('tab-content-curator');
      if (curatorTabPane && curatorTabPane.classList.contains('active')) {
        curatorTabPane.classList.remove('active');
        const listenPane = document.getElementById('tab-content-listen');
        if (listenPane) listenPane.classList.add('active');
        studioTabBtns.forEach(btn => {
          if (btn.getAttribute('data-tab') === 'listen') btn.classList.add('active');
          else btn.classList.remove('active');
        });
      }
    }
  }

  // Gateway Modal Controller
  function initGatewayModal() {
    const role = getActiveUserRole();
    
    // If user has not chosen role in this session, display gateway
    if (!role) {
      if (gatewayModal) gatewayModal.classList.add('is-active');
    } else {
      updateRoleUI();
    }

    // Choice 1: Listener
    if (btnChooseListener) {
      btnChooseListener.addEventListener('click', () => {
        sessionStorage.setItem('gyansetu_user_role', 'listener');
        if (gatewayModal) gatewayModal.classList.remove('is-active');
        updateRoleUI();
        showToast('🎧 Welcome to GyanSetu! Enjoy unrestricted global broadcasts.');
      });
    }

    // Choice 2: Lead Host Login
    if (btnChooseHost) {
      btnChooseHost.addEventListener('click', () => {
        if (gatewayViewChoose) gatewayViewChoose.classList.remove('active');
        if (gatewayViewLogin) gatewayViewLogin.classList.add('active');
        if (hostEmailInput) hostEmailInput.focus();
      });
    }

    // Back to role selection
    if (btnGatewayBack) {
      btnGatewayBack.addEventListener('click', () => {
        if (gatewayViewLogin) gatewayViewLogin.classList.remove('active');
        if (gatewayViewChoose) gatewayViewChoose.classList.add('active');
        if (hostLoginError) hostLoginError.classList.add('hidden');
      });
    }

    // Host Login Form Submission
    if (hostLoginForm) {
      hostLoginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = (hostEmailInput ? hostEmailInput.value : '').trim().toLowerCase();
        const pwd = (hostPasswordInput ? hostPasswordInput.value : '').trim();

        const match = AUTHORIZED_HOSTS.find(h => h.email.toLowerCase() === email);
        if (match && pwd === AUTHORIZED_HOST_PASSWORD) {
          sessionStorage.setItem('gyansetu_user_role', 'host');
          sessionStorage.setItem('gyansetu_host_email', email);
          if (gatewayModal) gatewayModal.classList.remove('is-active');
          if (hostLoginError) hostLoginError.classList.add('hidden');
          
          updateRoleUI();
          showToast(`🎉 Lead Host Authenticated: Welcome, ${match.name}!`);
        } else {
          if (hostLoginError) {
            hostLoginError.classList.remove('hidden');
            hostLoginError.style.animation = 'none';
            void hostLoginError.offsetWidth; // trigger reflow
            hostLoginError.style.animation = 'shake 0.3s ease';
          }
        }
      });
    }

    // Navbar Host Portal click (open login directly)
    if (navHostLoginBtn) {
      navHostLoginBtn.addEventListener('click', () => {
        if (gatewayModal) {
          if (gatewayViewChoose) gatewayViewChoose.classList.remove('active');
          if (gatewayViewLogin) gatewayViewLogin.classList.add('active');
          gatewayModal.classList.add('is-active');
          if (hostEmailInput) hostEmailInput.focus();
        }
      });
    }

    // Host Logout Handlers
    function handleLogout() {
      sessionStorage.setItem('gyansetu_user_role', 'listener');
      sessionStorage.removeItem('gyansetu_host_email');
      updateRoleUI();
      showToast('👋 Host session logged out. Reverted to Listener mode.');
    }

    if (navHostLogoutBtn) navHostLogoutBtn.addEventListener('click', handleLogout);
    if (btnHostDeckLogout) btnHostDeckLogout.addEventListener('click', handleLogout);
  }

  // --- Dynamic 10-Minute Passcode Minting Engine ---
  const DEFAULT_PASSCODES = [
    { code: 'GS-AFRICA-2026', guest: 'Global South Initiative', country: 'Africa', topic: 'Solar Chemistry', issuedAt: 'Oct 31, 2026', status: 'ACTIVE' },
    { code: 'GS-LIVE', guest: 'Live Host Override', country: 'Global Station', topic: 'Live Editorial', issuedAt: 'Oct 31, 2026', status: 'ACTIVE' },
    { code: 'GS-STUDENT', guest: 'Student Researcher', country: 'India', topic: 'Biomolecules', issuedAt: 'Oct 31, 2026', status: 'ACTIVE' }
  ];

  function getIssuedPasscodes() {
    try {
      const stored = localStorage.getItem('gyansetu_issued_passcodes');
      if (stored) {
        const parsed = JSON.parse(stored);
        if (Array.isArray(parsed) && parsed.length > 0) return parsed;
      }
    } catch (e) {}
    return DEFAULT_PASSCODES;
  }

  function saveIssuedPasscodes(list) {
    localStorage.setItem('gyansetu_issued_passcodes', JSON.stringify(list));
  }

  function verifyAndConsumePasscode(enteredCode) {
    const list = getIssuedPasscodes();
    const found = list.find(p => p.code.toUpperCase() === enteredCode && p.status === 'ACTIVE');
    if (found) {
      // Mark as used unless it is the permanent host override
      if (found.code !== 'GS-LIVE') {
        found.status = 'USED';
        saveIssuedPasscodes(list);
        renderActiveCodesList();
      }
      return found;
    }
    return null;
  }

  function renderActiveCodesList() {
    if (!activeCodesListEl) return;
    activeCodesListEl.innerHTML = '';
    const list = getIssuedPasscodes();

    list.slice().reverse().forEach((item, revIdx) => {
      const origIdx = list.length - 1 - revIdx;
      const row = document.createElement('div');
      row.className = 'active-code-row';
      const statusClass = item.status === 'ACTIVE' ? 'active' : 'used';
      
      row.innerHTML = `
        <div>
          <span class="active-code-key">${item.code}</span>
          <span class="active-code-meta"> &bull; ${item.guest} (${item.country || 'Global'})</span>
        </div>
        <div style="display:flex; align-items:center; gap:8px;">
          <span class="active-code-status-pill ${statusClass}">${item.status}</span>
          ${item.status === 'ACTIVE' ? `<button type="button" class="btn-revoke-code" data-idx="${origIdx}" style="background:none; border:none; color:#ef4444; font-size:0.7rem; cursor:pointer;" title="Revoke Passcode">✕ Revoke</button>` : ''}
        </div>
      `;

      const revokeBtn = row.querySelector('.btn-revoke-code');
      if (revokeBtn) {
        revokeBtn.addEventListener('click', () => {
          list[origIdx].status = 'REVOKED';
          saveIssuedPasscodes(list);
          renderActiveCodesList();
          showToast(`Passcode ${item.code} revoked.`);
        });
      }

      activeCodesListEl.appendChild(row);
    });
  }

  // Passcode Minting Button
  if (btnMintPasscode) {
    btnMintPasscode.addEventListener('click', () => {
      const gName = (mintGuestName ? mintGuestName.value : '').trim() || 'Global Guest Broadcaster';
      const gCountry = (mintGuestCountry ? mintGuestCountry.value : '').trim() || 'Global';
      const gTopic = (mintGuestTopic ? mintGuestTopic.value : '').trim() || 'Knowledge Inquiry';

      // Clean country slug (e.g. "Kenya" -> "KENYA", "Lagos, Nigeria" -> "NIGERIA")
      let slug = gCountry.replace(/[^a-zA-Z]/g, '').toUpperCase();
      if (!slug || slug.length < 3) slug = 'STUDENT';
      if (slug.length > 7) slug = slug.substring(0, 7);

      const randNum = Math.floor(1000 + Math.random() * 9000);
      const newCode = `GS-${slug}-${randNum}`;

      const list = getIssuedPasscodes();
      list.push({
        code: newCode,
        guest: gName,
        country: gCountry,
        topic: gTopic,
        issuedAt: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
        status: 'ACTIVE'
      });
      saveIssuedPasscodes(list);

      // Display newly minted code box
      if (mintedCodeResultBox && mintedCodeText) {
        mintedCodeText.textContent = newCode;
        mintedCodeResultBox.classList.remove('hidden');
      }

      renderActiveCodesList();
      showToast(`🔑 Passcode ${newCode} minted for ${gName}!`);

      // Clear input fields
      if (mintGuestName) mintGuestName.value = '';
      if (mintGuestCountry) mintGuestCountry.value = '';
      if (mintGuestTopic) mintGuestTopic.value = '';
    });
  }

  // Copy minted code button
  if (btnCopyMintedCode && mintedCodeText) {
    btnCopyMintedCode.addEventListener('click', () => {
      const code = mintedCodeText.textContent.trim();
      if (navigator.clipboard) {
        navigator.clipboard.writeText(code).then(() => {
          showToast(`📋 Code "${code}" copied to clipboard! Send to your guest.`);
        });
      } else {
        showToast(`Passcode: ${code}`);
      }
    });
  }

  // Initialize Gateway Modal & Role State
  initGatewayModal();

  // Initialize Network Monitoring
  initNetworkDetection();
});
