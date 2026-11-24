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
  function getEffectiveLangCode(lang, ep) {
    if (lang === 'orig') {
      return (ep && ep.id === 'ep-13') ? 'MR' : 'EN';
    }
    return lang.toUpperCase();
  }

  function renderLinguaPopoverOptions() {
    if (!dockLinguaOptionsList) return;
    const ep = GYAN_SETU_EPISODES[currentEpisodeIndex];
    if (!ep) return;
    dockLinguaOptionsList.innerHTML = '';

    const isEp13 = (ep.id === 'ep-13');
    // STANDARDIZED MULTILINGUAL TRACKS (Online Website Exclusive)
    // Ep 13: Original Marathi (Simran Ailani), English Master Dub, Hindi Master Dub
    // Ep 1-12: Original English (Simran Ailani), Hindi Master Dub
    let options = [];
    if (isEp13) {
      options = [
        { code: 'orig', label: '🇮🇳 Original Marathi', sub: 'Simran Ailani (Studio Master • Default)', badge: 'ORIGINAL' },
        { code: 'en', label: '🇬🇧 English Master', sub: 'Neerja Voice (Studio Dub)', badge: 'STUDIO DUB' },
        { code: 'hi', label: '🇮🇳 Hindi Master', sub: 'Swara Voice (Studio Dub)', badge: 'STUDIO DUB' }
      ];
    } else {
      options = [
        { code: 'orig', label: '🇬🇧 Original English', sub: 'Simran Ailani (Studio Master • Default)', badge: 'ORIGINAL' },
        { code: 'hi', label: '🇮🇳 Hindi Master', sub: 'Swara Voice (Neural Translation)', badge: 'TRANSLATION' }
      ];
    }

    options.forEach(opt => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = `btn-lingua-option ${currentTrackLanguage === opt.code ? 'active' : ''}`;
      btn.innerHTML = `
        <div>
          <div style="font-weight:600; font-size:0.8rem; display:flex; align-items:center; gap:6px;">${opt.label}</div>
          <div style="font-size:0.64rem; color:rgba(255,255,255,0.55); margin-top:2px;">${opt.sub}</div>
        </div>
        <span class="lingua-opt-badge">${opt.badge}</span>
      `;
      
      const selectOption = (e) => {
        if (e) {
          e.preventDefault();
          e.stopPropagation();
        }
        setTrackLanguage(opt.code);
        if (dockLinguaPopover) {
          dockLinguaPopover.classList.add('hidden');
        }
        if (dockLinguaBtn) {
          dockLinguaBtn.setAttribute('aria-expanded', 'false');
        }
      };

      btn.addEventListener('click', selectOption);
      btn.addEventListener('touchend', selectOption, { passive: false });
      dockLinguaOptionsList.appendChild(btn);
    });

    if (dockLinguaLabel) {
      dockLinguaLabel.textContent = getEffectiveLangCode(currentTrackLanguage, ep);
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
      dockLinguaLabel.textContent = getEffectiveLangCode(currentTrackLanguage, ep);
    }
    renderLinguaPopoverOptions();

    const toastMsgs = {
      orig: `🎙️ Playing Original Composition (${ep.hosts[0]} • Default)`,
      en: `🇬🇧 Switched to English Master Translation (Neerja Voice)`,
      hi: `🇮🇳 Switched to Hindi Master Translation (Swara Voice)`
    };
    showToast(toastMsgs[lang] || 'Language updated');
  }

  // Lingua Micro-Switcher Event Listeners (Universal Desktop & Mobile Touch Safe)
  if (dockLinguaBtn && dockLinguaPopover) {
    const toggleLinguaPopover = (e) => {
      if (e) {
        e.preventDefault();
        e.stopPropagation();
      }
      const isHidden = dockLinguaPopover.classList.contains('hidden');
      if (isHidden) {
        renderLinguaPopoverOptions();
        dockLinguaPopover.classList.remove('hidden');
        dockLinguaBtn.setAttribute('aria-expanded', 'true');
      } else {
        dockLinguaPopover.classList.add('hidden');
        dockLinguaBtn.setAttribute('aria-expanded', 'false');
      }
    };

    dockLinguaBtn.addEventListener('click', toggleLinguaPopover);
    dockLinguaBtn.addEventListener('touchend', toggleLinguaPopover, { passive: false });

    // Dedicated Header Close Button for Mobile
    const linguaCloseBtn = document.getElementById('btn-lingua-close');
    if (linguaCloseBtn) {
      const closeHandler = (e) => {
        if (e) {
          e.preventDefault();
          e.stopPropagation();
        }
        dockLinguaPopover.classList.add('hidden');
        dockLinguaBtn.setAttribute('aria-expanded', 'false');
      };
      linguaCloseBtn.addEventListener('click', closeHandler);
      linguaCloseBtn.addEventListener('touchend', closeHandler, { passive: false });
    }

    // Dismiss when tapping outside popover or button
    const outsideDismissHandler = (e) => {
      if (!dockLinguaPopover.contains(e.target) && !dockLinguaBtn.contains(e.target)) {
        dockLinguaPopover.classList.add('hidden');
        dockLinguaBtn.setAttribute('aria-expanded', 'false');
      }
    };
    document.addEventListener('click', outsideDismissHandler);
    document.addEventListener('touchend', outsideDismissHandler);
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

  function handleProgressSeek(clientX) {
    const rect = progressContainer.getBoundingClientRect();
    const seekX = Math.max(0, Math.min(clientX - rect.left, rect.width));
    if (audio.duration) {
      audio.currentTime = (seekX / rect.width) * audio.duration;
      progressFill.style.width = `${(seekX / rect.width) * 100}%`;
    }
  }

  progressContainer.addEventListener('click', (e) => {
    handleProgressSeek(e.clientX);
  });

  let isScrubbing = false;
  progressContainer.addEventListener('touchstart', (e) => {
    isScrubbing = true;
    if (e.touches && e.touches[0]) handleProgressSeek(e.touches[0].clientX);
  }, { passive: true });

  progressContainer.addEventListener('touchmove', (e) => {
    if (isScrubbing && e.touches && e.touches[0]) handleProgressSeek(e.touches[0].clientX);
  }, { passive: true });

  progressContainer.addEventListener('touchend', () => {
    isScrubbing = false;
  }, { passive: true });

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
    const formattedSpeed = (newSpeed === 1 || newSpeed === 2) ? `${newSpeed}×` : `${newSpeed}×`;
    speedToggleBtn.textContent = formattedSpeed;
    speedToggleBtn.setAttribute('aria-label', `Playback speed: ${newSpeed}x`);
    showToast(`⏩ Playback Speed: ${newSpeed}×`);
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
      document.querySelectorAll('.btn-data-saver-switch').forEach(btn => {
        btn.classList.add('active');
        btn.setAttribute('aria-checked', 'true');
      });
      document.querySelectorAll('.ds-state-tag').forEach(lbl => {
        lbl.textContent = 'ON';
      });
      if (dockGhostBtn) {
        dockGhostBtn.classList.add('active');
        dockGhostBtn.setAttribute('aria-checked', 'true');
      }
      if (dockGhostLabel) dockGhostLabel.textContent = 'ON';
    } else {
      document.body.classList.remove('ghost-mode-active');
      document.querySelectorAll('.btn-data-saver-switch').forEach(btn => {
        btn.classList.remove('active');
        btn.setAttribute('aria-checked', 'false');
      });
      document.querySelectorAll('.ds-state-tag').forEach(lbl => {
        lbl.textContent = 'OFF';
      });
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
    document.querySelectorAll('.btn-data-saver-switch').forEach(btn => {
      btn.addEventListener('click', () => {
        setGhostMode(!isGhostMode, false);
      });
    });

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
  // 12. CURIOSITY MAILBAG, MULTIMODAL THOUGHT DECK & CLASSROOM INQUIRY BRIEF
  // =========================================================================
  const liveStudioModal = document.getElementById('live-studio-modal');
  const closeLiveStudioBtn = document.getElementById('close-live-studio-btn');
  const navLiveStudioBtn = document.getElementById('nav-live-studio-btn');
  const studioTabBtns = document.querySelectorAll('.studio-tab-btn[data-tab]');
  const studioTabPanes = document.querySelectorAll('.studio-tab-pane');

  // Open & Close Mailbag / Studio Modal
  function openLiveStudioModal(initialTab = 'ask') {
    if (liveStudioModal) {
      liveStudioModal.classList.add('is-active');
      switchStudioTab(initialTab);
      renderMailbagInbox();
      renderCuratorQueue();
    }
  }

  function closeLiveStudioModal() {
    if (liveStudioModal) {
      liveStudioModal.classList.remove('is-active');
    }
  }

  const mobileLiveStudioBtn = document.getElementById('mobile-live-studio-btn');
  if (mobileLiveStudioBtn) {
    mobileLiveStudioBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openLiveStudioModal('ask');
    });
  }

  if (navLiveStudioBtn) {
    navLiveStudioBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openLiveStudioModal('ask');
    });
  }

  document.querySelectorAll('.studio-open-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openLiveStudioModal('ask');
    });
  });

  if (radioModeBtn) {
    radioModeBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openLiveStudioModal('ask');
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
      renderMailbagInbox();
      renderCuratorQueue();
    }
  }

  studioTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      switchStudioTab(btn.dataset.tab);
    });
  });

  // --- CURIOSITY MAILBAG ENGINE ("Ask Simran") ---
  const mailbagQuestionForm = document.getElementById('mailbag-question-form');
  const mailbagReceiptBox = document.getElementById('mailbag-receipt-box');
  const mailbagReceiptIdTag = document.getElementById('mailbag-receipt-id-tag');
  const btnResetMailbagForm = document.getElementById('btn-reset-mailbag-form');

  const DEFAULT_MAILBAG_QUESTIONS = [
    {
      id: "GS-ASK-4102",
      author: "Priya Sharma",
      location: "Kendriya Vidyalaya, Pune",
      topic: "Everyday Phenomena & Physics",
      episodeRef: "Ep 11: What colour is the sky?",
      question: "Why do sunsets turn deep vibrant orange and red instead of violet, even though violet light has an even shorter wavelength than blue light and should scatter more?",
      date: "October 30, 2026",
      status: "Starred for Upcoming Episode",
      starred: true
    },
    {
      id: "GS-ASK-3891",
      author: "Kwame Mensah",
      location: "University of Nairobi, Kenya",
      topic: "Chemistry & Solid-State Science",
      episodeRef: "Ep 1: Can Chemistry Explain Consciousness?",
      question: "Could solid-state ceramic electrolytes survive extreme Sahel desert temperatures without thermal runaway, allowing decentralized solar storage in rural off-grid villages?",
      date: "October 29, 2026",
      status: "Under Editorial Review",
      starred: false
    },
    {
      id: "GS-ASK-5520",
      author: "Ananya Iyer",
      location: "St. Xavier's, Mumbai",
      topic: "History of Ideas & Forgotten Science",
      episodeRef: "Ep 10: Napoleon wasn't poisoned.....or was he?",
      question: "If Scheele's Green wallpaper produced toxic arsine gas through fungal methylation, could the British captors on Saint Helena have accidentally caused Napoleon's symptoms without deliberate poisoning?",
      date: "October 28, 2026",
      status: "Starred for Upcoming Episode",
      starred: true
    }
  ];

  function getMailbagQuestions() {
    try {
      const stored = localStorage.getItem('gyansetu_mailbag_questions');
      if (stored) {
        const parsed = JSON.parse(stored);
        if (Array.isArray(parsed) && parsed.length > 0) return parsed;
      }
    } catch (e) {}
    return DEFAULT_MAILBAG_QUESTIONS;
  }

  function saveMailbagQuestions(questions) {
    try {
      localStorage.setItem('gyansetu_mailbag_questions', JSON.stringify(questions));
    } catch (e) {}
  }

  if (mailbagQuestionForm) {
    mailbagQuestionForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = (document.getElementById('ask-name')?.value || '').trim();
      const location = (document.getElementById('ask-location')?.value || '').trim();
      const topic = document.getElementById('ask-topic')?.value || 'Everyday Phenomena & Physics';
      const episodeRef = document.getElementById('ask-episode-ref')?.value || 'General Question';
      const questionText = (document.getElementById('ask-question-text')?.value || '').trim();

      if (!questionText) return;

      const trackingId = `GS-ASK-${Math.floor(1000 + Math.random() * 9000)}`;
      const newQuestion = {
        id: trackingId,
        author: name || 'Curious Learner',
        location: location || 'Global Classroom',
        topic: topic,
        episodeRef: episodeRef,
        question: questionText,
        date: 'October 31, 2026',
        status: 'Under Editorial Review',
        starred: false
      };

      const questions = getMailbagQuestions();
      questions.unshift(newQuestion);
      saveMailbagQuestions(questions);

      if (mailbagReceiptIdTag) mailbagReceiptIdTag.textContent = trackingId;
      mailbagQuestionForm.classList.add('hidden');
      if (mailbagReceiptBox) mailbagReceiptBox.classList.remove('hidden');

      showToast(`📬 Question Sent to Simran! Tracking ID: ${trackingId}`);
      renderMailbagInbox();
    });
  }

  if (btnResetMailbagForm) {
    btnResetMailbagForm.addEventListener('click', () => {
      if (mailbagQuestionForm) {
        mailbagQuestionForm.reset();
        mailbagQuestionForm.classList.remove('hidden');
      }
      if (mailbagReceiptBox) mailbagReceiptBox.classList.add('hidden');
    });
  }

  function renderMailbagInbox() {
    const listEl = document.getElementById('mailbag-inbox-list');
    if (!listEl) return;
    listEl.innerHTML = '';

    const questions = getMailbagQuestions();
    questions.forEach((q, idx) => {
      const item = document.createElement('div');
      item.className = 'mailbag-inbox-item';
      item.innerHTML = `
        <div class="mailbag-item-meta">
          <div>
            <span class="mailbag-item-author">💬 ${q.author} &bull; ${q.location}</span>
            <span style="font-size:0.68rem; color:rgba(255,255,255,0.4); margin-left:8px;">${q.id} &bull; ${q.date}</span>
          </div>
          <span class="mailbag-item-topic-badge">${q.topic}</span>
        </div>
        <div class="mailbag-item-text">"${q.question}"</div>
        <div style="font-size:0.72rem; color:rgba(255,255,255,0.5);">Target Episode: <strong>${q.episodeRef}</strong> &bull; Status: <span style="color:#38bdf8;">${q.status}</span></div>
        <div class="mailbag-item-actions">
          <button type="button" class="btn-star-question ${q.starred ? 'starred' : ''}" data-idx="${idx}">
            <span>${q.starred ? '★ Starred for On-Air Segment' : '☆ Star Question for Episode'}</span>
          </button>
        </div>
      `;

      const starBtn = item.querySelector('.btn-star-question');
      if (starBtn) {
        starBtn.addEventListener('click', () => {
          q.starred = !q.starred;
          q.status = q.starred ? 'Starred for Upcoming Episode' : 'Under Editorial Review';
          saveMailbagQuestions(questions);
          renderMailbagInbox();
          showToast(q.starred ? `⭐ Starred question from ${q.author} for Simran's next episode!` : 'Question unstarred');
        });
      }

      listEl.appendChild(item);
    });
  }

  // --- MULTIMODAL VISUAL THOUGHT DECK ENGINE ---
  const thoughtDeckModal = document.getElementById('thought-deck-modal');
  const closeThoughtDeckBtn = document.getElementById('close-thought-deck-btn');
  const btnHeroThoughtDeck = document.getElementById('btn-hero-thought-deck');
  const thoughtDeckPlayBtn = document.getElementById('thought-deck-play-btn');
  const thoughtDeckToBriefBtn = document.getElementById('thought-deck-to-brief-btn');

  let activeThoughtDeckEpisode = null;

  const THOUGHT_DECK_CONTENT = {
    "ep-11": {
      diagramLabel: "Rayleigh Scattering & Atmospheric Geometry",
      svg: `<svg viewBox="0 0 540 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <radialGradient id="sunGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#fbbf24" stop-opacity="1"/>
            <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.2"/>
          </radialGradient>
          <linearGradient id="atmoGrad" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#0284c7" stop-opacity="0.3"/>
            <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.05"/>
          </linearGradient>
        </defs>
        <!-- Sun -->
        <circle cx="50" cy="90" r="32" fill="url(#sunGlow)"/>
        <text x="50" y="94" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">White Sun</text>
        <!-- Incoming Multi-wavelength rays -->
        <line x1="86" y1="90" x2="220" y2="90" stroke="#f8fafc" stroke-width="3" stroke-dasharray="6,3"/>
        <text x="145" y="80" font-size="9" fill="#94a3b8" text-anchor="middle">Unscattered Sunlight (λ=400-700nm)</text>
        <!-- Atmosphere Boundary -->
        <rect x="220" y="20" width="220" height="140" rx="14" fill="url(#atmoGrad)" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <text x="330" y="38" font-size="10" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Earth Atmosphere (N₂ / O₂ Molecules ~0.3nm)</text>
        <!-- Microscopic Air Molecule Target -->
        <circle cx="280" cy="90" r="8" fill="#38bdf8"/>
        <!-- Blue Scattering (Short λ scattered everywhere) -->
        <path d="M280,90 L240,45" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
        <path d="M280,90 L320,45" stroke="#38bdf8" stroke-width="2.5"/>
        <path d="M280,90 L250,135" stroke="#38bdf8" stroke-width="2.5"/>
        <path d="M280,90 L310,135" stroke="#38bdf8" stroke-width="2.5"/>
        <text x="280" y="152" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Blue &amp; Violet Light Scattered in All Directions (∝ 1/λ⁴)</text>
        <!-- Transmitted Red/Orange (Long λ passes straight) -->
        <line x1="288" y1="90" x2="480" y2="90" stroke="#f97316" stroke-width="3.5"/>
        <polygon points="480,90 470,85 470,95" fill="#f97316"/>
        <text x="430" y="80" font-size="9" font-weight="bold" fill="#fb923c">Red / Amber Passes Through</text>
        <!-- Observer Eye -->
        <circle cx="500" cy="90" r="16" fill="#1e293b" stroke="#f1f5f9" stroke-width="2"/>
        <circle cx="500" cy="90" r="6" fill="#38bdf8"/>
        <text x="500" y="125" font-size="9" fill="#e2e8f0" text-anchor="middle">Sunset Observer</text>
      </svg>`,
      cards: [
        {
          num: "CONCEPT 01",
          title: "The Inverse 4th Power Law",
          desc: "Lord Rayleigh proved that scattering efficiency is inversely proportional to wavelength to the 4th power (1/λ⁴). Blue light (400nm) scatters almost 10 times more efficiently than red light (700nm)."
        },
        {
          num: "CONCEPT 02",
          title: "The Human Vision Paradox",
          desc: "Sunlight contains violet light which scatters even more than blue, but human cone receptors are peak-sensitive to blue/green wavelengths, causing our brains to perceive the sky as sky-blue."
        },
        {
          num: "CONCEPT 03",
          title: "Twilight Optical Geometry",
          desc: "At sunset, sunlight must traverse through 10× greater atmospheric depth. Almost all high-frequency blue rays are scattered away, leaving only direct low-frequency orange and red waves."
        }
      ],
      anchorTitle: "Frugal Observation & Cosmic Counterpart",
      anchorText: "On Mars, where thin atmosphere contains coarse suspended iron-oxide dust, Mie scattering dominates: daytime skies look butterscotch-brown, and sunsets turn mesmerizing cobalt blue!"
    },
    "ep-1": {
      diagramLabel: "Electrochemical Synapse & Action Potential",
      svg: `<svg viewBox="0 0 540 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
        <!-- Presynaptic Bulb -->
        <path d="M40,30 C120,30 160,50 170,90 C160,130 120,150 40,150" fill="rgba(56,189,248,0.12)" stroke="#38bdf8" stroke-width="2"/>
        <text x="90" y="48" font-size="10" font-weight="bold" fill="#7dd3fc">Axon Terminal</text>
        <!-- Synaptic Vesicles with Neurotransmitters -->
        <circle cx="80" cy="80" r="9" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <circle cx="110" cy="95" r="9" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <circle cx="135" cy="75" r="9" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <!-- Synaptic Cleft (20nm gap) -->
        <line x1="180" y1="40" x2="180" y2="140" stroke="rgba(255,255,255,0.2)" stroke-width="1" stroke-dasharray="2,2"/>
        <text x="180" y="26" font-size="9" fill="#94a3b8" text-anchor="middle">Synaptic Cleft (20nm)</text>
        <!-- Diffusing Molecules -->
        <circle cx="188" cy="70" r="3" fill="#f59e0b"/>
        <circle cx="192" cy="90" r="3" fill="#f59e0b"/>
        <circle cx="186" cy="110" r="3" fill="#f59e0b"/>
        <!-- Postsynaptic Membrane & Receptors -->
        <path d="M210,40 C220,70 220,110 210,140 L340,140 C350,110 350,70 340,40 Z" fill="rgba(249,124,34,0.12)" stroke="#f97316" stroke-width="2"/>
        <text x="270" y="55" font-size="10" font-weight="bold" fill="#fdba74" text-anchor="middle">Postsynaptic Dendrite</text>
        <rect x="206" y="65" width="8" height="14" rx="2" fill="#f59e0b"/>
        <rect x="206" y="100" width="8" height="14" rx="2" fill="#f59e0b"/>
        <!-- Action Potential Wave -->
        <path d="M370,90 Q400,30 420,90 T470,90 T520,90" fill="none" stroke="#10b981" stroke-width="3"/>
        <text x="440" y="48" font-size="10" font-weight="bold" fill="#34d399">Action Potential (-70mV &rarr; +40mV)</text>
        <text x="440" y="125" font-size="9" fill="#94a3b8">Na⁺ / K⁺ Ion Translocation</text>
      </svg>`,
      cards: [
        {
          num: "CONCEPT 01",
          title: "The Ion Gradient Battery",
          desc: "Every thinking neuron is an electrochemical battery maintained by ATP-driven sodium-potassium pumps (3 Na⁺ out for 2 K⁺ in), creating a resting -70 millivolt polarity."
        },
        {
          num: "CONCEPT 02",
          title: "Neurochemical Modulation",
          desc: "Feelings of curiosity and drive are mediated by neurotransmitter kinetics (dopamine, serotonin) altering protein channel conformations across synaptic junctions in milliseconds."
        },
        {
          num: "CONCEPT 03",
          title: "The Hard Problem Boundary",
          desc: "While physical chemistry maps neural circuits and signal propagation completely, explaining how subjective qualia (the internal feeling of curiosity) arises remains an open frontier."
        }
      ],
      anchorTitle: "Everyday Clinical Link",
      anchorText: "General anesthetics shut down conscious perception not by destroying chemical bonds, but by physically altering lipid membrane fluidity and halting synchronized neuronal firing!"
    },
    "ep-10": {
      diagramLabel: "The 1836 Marsh Arsenic Mirror Test",
      svg: `<svg viewBox="0 0 540 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
        <!-- Generator Flask -->
        <path d="M60,140 L100,140 L90,90 L90,60 L70,60 L70,90 Z" fill="rgba(56,189,248,0.15)" stroke="#38bdf8" stroke-width="2"/>
        <text x="80" y="115" font-size="9" fill="#7dd3fc" text-anchor="middle">Zn + H₂SO₄</text>
        <text x="80" y="160" font-size="9" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Reaction Flask</text>
        <!-- Delivery Tube -->
        <path d="M80,60 L80,45 L240,45 L240,80 L290,80" fill="none" stroke="#38bdf8" stroke-width="3"/>
        <text x="160" y="38" font-size="9" fill="#94a3b8">Volatile Arsine Gas (AsH₃)</text>
        <!-- Heat Source (Bunsen Burner) -->
        <path d="M330,130 L350,130 L345,95 L335,95 Z" fill="#475569" stroke="#64748b"/>
        <path d="M336,95 Q340,70 345,95 Z" fill="#ef4444"/>
        <text x="340" y="152" font-size="9" fill="#cbd5e1" text-anchor="middle">Thermal Pyrolysis</text>
        <!-- Reduction Tube & Arsenic Metallic Mirror -->
        <rect x="290" y="74" width="160" height="12" rx="4" fill="rgba(255,255,255,0.1)" stroke="#94a3b8" stroke-width="1.5"/>
        <rect x="375" y="75" width="28" height="10" rx="2" fill="#1e293b" stroke="#e2e8f0" stroke-width="2"/>
        <text x="389" y="65" font-size="10" font-weight="bold" fill="#f8fafc" text-anchor="middle">Black Arsenic Mirror (As)</text>
        <text x="389" y="112" font-size="9" fill="#38bdf8" text-anchor="middle">Sublimed Metallic Ring</text>
      </svg>`,
      cards: [
        {
          num: "CONCEPT 01",
          title: "Birth of Modern Forensic Toxicology",
          desc: "Before James Marsh invented his test in 1836, arsenic was known as 'inheritance powder' because it left no definitive chemical trace. Marsh converted arsenic trioxide into volatile arsine gas."
        },
        {
          num: "CONCEPT 02",
          title: "Scheele's Green Wallpaper",
          desc: "Napoleon's Longwood residence was decorated with vibrant copper-arsenite wallpaper. In St. Helena's humid climate, Penicillium mold metabolized the dye into toxic gaseous trimethylarsine."
        },
        {
          num: "CONCEPT 03",
          title: "Contextual Environmental Baseline",
          desc: "While 1961 neutron activation analysis revealed arsenic in Napoleon's hair, 19th-century control specimens also showed elevated arsenic from tonics, wine, and coal dust."
        }
      ],
      anchorTitle: "Scientific Investigation Takeaway",
      anchorText: "Forensic truth requires understanding historical baselines. What looks like targeted assassination today was often ubiquitous environmental background exposure 200 years ago."
    },
    "ep-12": {
      diagramLabel: "Galvanism & The Bioethical Boundary",
      svg: `<svg viewBox="0 0 540 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
        <!-- Voltaic Pile / Galvanic Battery -->
        <rect x="60" y="50" width="40" height="80" rx="4" fill="rgba(245,158,11,0.15)" stroke="#f59e0b" stroke-width="2"/>
        <line x1="60" y1="70" x2="100" y2="70" stroke="#f59e0b" stroke-width="2"/>
        <line x1="60" y1="90" x2="100" y2="90" stroke="#f59e0b" stroke-width="2"/>
        <line x1="60" y1="110" x2="100" y2="110" stroke="#f59e0b" stroke-width="2"/>
        <text x="80" y="150" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">Voltaic Pile (1800)</text>
        <!-- Spark Arc Wires -->
        <path d="M80,50 L80,30 L220,30 L220,70" fill="none" stroke="#f59e0b" stroke-width="2"/>
        <path d="M100,110 L140,110 L140,70 L200,70" fill="none" stroke="#94a3b8" stroke-width="2"/>
        <!-- Electric Spark -->
        <polygon points="210,65 215,70 208,72 216,78 206,75 210,65" fill="#38bdf8"/>
        <!-- Bioethical Line of Responsibility -->
        <line x1="270" y1="20" x2="270" y2="160" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
        <text x="270" y="172" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">The Moral Responsibility Boundary</text>
        <!-- Ethical Dilemma Balance -->
        <circle cx="410" cy="80" r="34" fill="rgba(56,189,248,0.1)" stroke="#38bdf8" stroke-width="2"/>
        <text x="410" y="75" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Curiosity vs</text>
        <text x="410" y="92" font-size="10" font-weight="bold" fill="#f97316" text-anchor="middle">Custodianship</text>
      </svg>`,
      cards: [
        {
          num: "CONCEPT 01",
          title: "Galvanism in the Romantic Era",
          desc: "Luigi Galvani and Giovanni Aldini demonstrated that static electric sparks caused dead muscular tissue to contract, suggesting electricity was the vital driving fluid of animal life."
        },
        {
          num: "CONCEPT 02",
          title: "The Myth of Prometheus",
          desc: "Shelley subtitled her novel 'The Modern Prometheus.' Victor's failing was not daring to discover the secret of life, but refusing moral responsibility and empathy toward the being he created."
        },
        {
          num: "CONCEPT 03",
          title: "Modern Synthetic Biology",
          desc: "Today's discussions around CRISPR gene editing, synthetic embryos, and autonomous intelligence systems mirror Shelley's warning: innovation without stewardship leads to crisis."
        }
      ],
      anchorTitle: "Modern Ethical Philosophy",
      anchorText: "The Precautionary Principle: Just because scientific capability allows humanity to engineer something does not relieve creators of the duty to protect and nurture its consequences."
    },
    "ep-13": {
      diagramLabel: "Geography & Stone Hydrology of Historical Nagpur",
      svg: `<svg viewBox="0 0 540 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
        <!-- Zero Mile Monument -->
        <rect x="70" y="80" width="30" height="60" rx="3" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
        <polygon points="70,80 85,45 100,80" fill="#f97316"/>
        <text x="85" y="155" font-size="9" font-weight="bold" fill="#fdba74" text-anchor="middle">Zero Mile Stone</text>
        <text x="85" y="168" font-size="8" fill="#94a3b8" text-anchor="middle">Center of India (1907)</text>
        <!-- Nag River Basin Line -->
        <path d="M120,110 Q200,140 280,100 T440,110" fill="none" stroke="#0284c7" stroke-width="3"/>
        <text x="250" y="135" font-size="9" font-weight="bold" fill="#38bdf8">Nag River Natural Basin</text>
        <!-- Mahal Basalt Fortification & Cooling Corridor -->
        <rect x="360" y="50" width="120" height="70" rx="8" fill="rgba(249,124,34,0.15)" stroke="#ea580c" stroke-width="2"/>
        <text x="420" y="75" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Mahal Fort &amp; Stepwells</text>
        <text x="420" y="92" font-size="8" fill="#fdba74" text-anchor="middle">Deccan Basalt Masonry</text>
        <text x="420" y="106" font-size="8" fill="#94a3b8" text-anchor="middle">Passive Geothermal Cooling</text>
      </svg>`,
      cards: [
        {
          num: "CONCEPT 01",
          title: "Geographical Keystone of India",
          desc: "Nagpur was chosen as the geographical center of undivided British India for the Great Trigonometrical Survey of 1907, with all national distances calibrated from the Zero Mile Stone."
        },
        {
          num: "CONCEPT 02",
          title: "Deogarh Gond Foundations",
          desc: "Founded in 1702 by Gond Raja Bakht Buland Shah and later expanded into a thriving administrative capital under Raghuji Bhonsle I of the Maratha Empire."
        },
        {
          num: "CONCEPT 03",
          title: "Frugal Stone Hydrology",
          desc: "Traditional builders used high-thermal-mass basalt lava rock and interconnected lake reservoirs (Futala, Ambazari) to maintain cool living environments during 45°C summers."
        }
      ],
      anchorTitle: "Modern Architectural Lesson",
      anchorText: "Ancient Vidarbha stepwells and natural ventilation shafts in Mahal prove that passive thermal cooling and decentralized rainwater harvesting beat energy-intensive mechanical air conditioning!"
    }
  };

  function openThoughtDeck(ep) {
    if (!ep || !thoughtDeckModal) return;
    activeThoughtDeckEpisode = ep;

    const epTag = document.getElementById('thought-deck-ep-tag');
    const titleEl = document.getElementById('thought-deck-title');
    const subtitleEl = document.getElementById('thought-deck-subtitle');
    const diagramLabelEl = document.getElementById('thought-diagram-label');
    const canvasWrapEl = document.getElementById('thought-diagram-canvas-wrap');
    const cardsContainer = document.getElementById('thought-cards-container');
    const anchorContainer = document.getElementById('thought-anchor-container');

    if (epTag) epTag.textContent = `EPISODE #${ep.number || ''} • ${ep.category}`;
    if (titleEl) titleEl.textContent = ep.title;
    if (subtitleEl) subtitleEl.textContent = `Multimodal Conceptual Blueprint & Scientific Mental Models • Curated by Simran Ailani`;

    const deckData = THOUGHT_DECK_CONTENT[ep.id] || {
      diagramLabel: `${ep.title} • Structural Overview`,
      svg: `<svg viewBox="0 0 540 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
        <circle cx="270" cy="90" r="45" fill="rgba(56,189,248,0.15)" stroke="#38bdf8" stroke-width="2"/>
        <text x="270" y="86" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">GyanSetu Concept</text>
        <text x="270" y="104" font-size="9" fill="#7dd3fc" text-anchor="middle">${ep.category}</text>
        <path d="M120,90 Q180,40 225,90" fill="none" stroke="#f59e0b" stroke-width="2"/>
        <path d="M315,90 Q360,140 420,90" fill="none" stroke="#10b981" stroke-width="2"/>
        <text x="170" y="60" font-size="9" fill="#94a3b8">Inquiry Genesis</text>
        <text x="370" y="130" font-size="9" fill="#94a3b8">Scientific Resonance</text>
      </svg>`,
      cards: [
        {
          num: "CONCEPT 01",
          title: "Fundamental Hypothesis",
          desc: ep.description.slice(0, 140) + '...'
        },
        {
          num: "CONCEPT 02",
          title: "Conversational Clarity",
          desc: "Simran Ailani breaks down daunting terminology into intuitive everyday metaphors designed for listeners of all educational backgrounds."
        },
        {
          num: "CONCEPT 03",
          title: "Universal Access",
          desc: "Optimized for offline storage in rural schools and bandwidth-free streaming across 2G mobile networks worldwide."
        }
      ],
      anchorTitle: "Everyday Connection",
      anchorText: "Every episode connects abstract knowledge to tangible real-world phenomena observable in daily life."
    };

    if (diagramLabelEl) diagramLabelEl.textContent = deckData.diagramLabel;
    if (canvasWrapEl) canvasWrapEl.innerHTML = deckData.svg;

    if (cardsContainer) {
      cardsContainer.innerHTML = deckData.cards.map(c => `
        <div class="thought-card">
          <div class="thought-card-num">${c.num}</div>
          <div class="thought-card-title">${c.title}</div>
          <div class="thought-card-desc">${c.desc}</div>
        </div>
      `).join('');
    }

    if (anchorContainer) {
      anchorContainer.innerHTML = `
        <div class="thought-anchor-title">${deckData.anchorTitle}</div>
        <div class="thought-anchor-text">${deckData.anchorText}</div>
      `;
    }

    thoughtDeckModal.classList.add('is-active');
  }

  function closeThoughtDeck() {
    if (thoughtDeckModal) thoughtDeckModal.classList.remove('is-active');
  }

  if (closeThoughtDeckBtn) closeThoughtDeckBtn.addEventListener('click', closeThoughtDeck);
  if (thoughtDeckModal) {
    thoughtDeckModal.addEventListener('click', (e) => {
      if (e.target === thoughtDeckModal) closeThoughtDeck();
    });
  }

  if (btnHeroThoughtDeck) {
    btnHeroThoughtDeck.addEventListener('click', () => {
      const ep = GYAN_SETU_EPISODES[currentEpisodeIndex] || GYAN_SETU_EPISODES[0];
      openThoughtDeck(ep);
    });
  }

  if (thoughtDeckPlayBtn) {
    thoughtDeckPlayBtn.addEventListener('click', () => {
      closeThoughtDeck();
      if (activeThoughtDeckEpisode) {
        const idx = GYAN_SETU_EPISODES.findIndex(e => e.id === activeThoughtDeckEpisode.id);
        if (idx !== -1) loadEpisode(idx, true);
      }
    });
  }

  if (thoughtDeckToBriefBtn) {
    thoughtDeckToBriefBtn.addEventListener('click', () => {
      closeThoughtDeck();
      if (activeThoughtDeckEpisode) openClassroomBrief(activeThoughtDeckEpisode);
    });
  }

  // --- 1-PAGE PRINTABLE CLASSROOM INQUIRY BRIEF ENGINE ---
  const classroomBriefModal = document.getElementById('classroom-brief-modal');
  const closeClassroomBriefBtn = document.getElementById('close-classroom-brief-btn');
  const btnPrintBrief = document.getElementById('btn-print-brief');
  const btnHeroClassroomBrief = document.getElementById('btn-hero-classroom-brief');

  const CLASSROOM_BRIEFS = {
    "ep-11": {
      bigIdea: "Sunlight is composed of all colors of the visible spectrum. Because microscopic air molecules (nitrogen and oxygen) are much smaller than light wavelengths, they scatter short blue and violet wavelengths across the entire sky (Rayleigh scattering), while longer red wavelengths pass straight through.",
      sparks: [
        "If Earth had no atmosphere whatsoever, what color would the sky appear during midday, and how would stars look?",
        "Why don't we see the sky as violet, even though violet light has an even shorter wavelength than blue and scatters the most?",
        "During a dust storm or heavy fog, why does the sky turn gray or white instead of remaining blue?"
      ],
      vocab: [
        { term: "Rayleigh Scattering", def: "The scattering of light by particles much smaller than the wavelength of the radiation, proportional to 1/λ⁴." },
        { term: "Visible Spectrum", def: "The portion of electromagnetic radiation (400nm to 700nm) that can be detected by human eye cone cells." },
        { term: "Optical Path Length", def: "The distance light travels through a medium, which multiplies tenfold when the sun is near the horizon." }
      ],
      experiment: "Fill a clear glass with water and stir in 2 drops of milk. Shine a white flashlight through the glass: viewed from the side, the scattered water glows faint sky-blue; viewed directly through the end, the transmitted beam glows sunset-orange!"
    },
    "ep-1": {
      bigIdea: "Every human thought, emotion, and sensation corresponds to electrochemical impulses jumping across trillions of synaptic clefts. Yet science still faces the 'Hard Problem': how physical ion channels create subjective conscious experience.",
      sparks: [
        "If an artificial computer could simulate every single molecule and neuron of a human brain, would that computer genuinely feel joy and sadness?",
        "Why can simple physical changes (like lack of sleep or low blood glucose) drastically change our emotional patience and personality?",
        "Can physical chemistry explain both 'how' the brain detects light and 'why' the subjective experience of redness feels the way it does?"
      ],
      vocab: [
        { term: "Action Potential", def: "A temporary electrical voltage reversal across a neuron membrane (-70mV to +40mV) that propagates nerve signals." },
        { term: "Synaptic Cleft", def: "The microscopic 20-nanometer gap between communicating neurons across which chemical neurotransmitters diffuse." },
        { term: "The Hard Problem", def: "The philosophical question of why and how physical physical brain processes produce subjective conscious experience." }
      ],
      experiment: "Two-Point Touch Test: Gently touch two pencil tips 1 cm apart to your fingertip (you clearly feel two distinct points). Touch the same 1 cm tips to your upper arm or back (your brain perceives it as a single point), proving varying sensory receptor density!"
    },
    "ep-10": {
      bigIdea: "Forensic toxicology relies on detecting trace chemical signatures in biological tissues. While arsenic was discovered in Napoleon's hair, 19th-century everyday items—from wallpaper dyed with copper arsenite to tonics—routinely contained high arsenic levels.",
      sparks: [
        "How can modern forensic scientists distinguish between intentional poisoning versus everyday environmental exposure from two centuries ago?",
        "If an entire historic town drank from lead pipes and wore arsenic-dyed clothing, what baseline should researchers use to prove homicide?",
        "Why is quantitative chemical evidence sometimes interpreted differently by two reputable scientific teams?"
      ],
      vocab: [
        { term: "Forensic Toxicology", def: "The application of analytical chemistry and pharmacology to legal, medical, and historical investigations." },
        { term: "Scheele's Green", def: "A copper-arsenite pigment widely used in 19th-century wallpapers that emitted toxic arsine gas in damp conditions." },
        { term: "Neutron Activation", def: "A high-precision nuclear technique measuring trace elements by bombarding hair or tissue samples with neutrons." }
      ],
      experiment: "Examine common household food and cleaning products for hazard labels (corrosive, flammable). Discuss how table salt (NaCl) is completely safe to eat, yet made of explosive sodium metal and poisonous chlorine gas!"
    },
    "ep-12": {
      bigIdea: "Mary Shelley was inspired by 1818 bioelectric experiments showing electricity stimulated muscle contractions. The story is a timeless reminder that scientific ingenuity requires deep ethical responsibility and compassion for what we create.",
      sparks: [
        "Should inventors and scientists be held morally responsible for how society uses their discoveries centuries after they are gone?",
        "Where should society draw the line between using biotechnology to cure diseases versus artificially creating new life forms?",
        "Why was Victor Frankenstein horrified by his creation the moment it opened its eyes, despite years of obsessive work?"
      ],
      vocab: [
        { term: "Galvanism", def: "The contraction of biological muscles stimulated by electric current, discovered by Luigi Galvani." },
        { term: "Bioethics", def: "The discipline dealing with ethical, social, and moral implications of biological and medical research." },
        { term: "Precautionary Principle", def: "The rule that if an innovation carries suspected risks of irreversible harm, the burden of proof falls on the innovator." }
      ],
      experiment: "Feel the electrical rhythm in your own body: check your pulse at your wrist (triggered by the sinoatrial pacemaker node in your heart). Notice how lightning in the sky and heartbeat in your chest use the exact same electron physics!"
    },
    "ep-13": {
      bigIdea: "Nagpur's strategic location as the geographical crossroads of India shaped its urban evolution—from the early 18th-century Gond kingdom of Deogarh through the Maratha Bhonsle era, featuring heat-resilient basalt architecture and lake hydrology.",
      sparks: [
        "How does the physical geology of a landscape (such as river basins and basalt quarries) determine where ancient rulers built capitals?",
        "What can modern architects learn from historic stone stepwells that remained naturally cool during 45°C summers without electricity?",
        "Why was the Zero Mile Stone placed specifically in Nagpur during the Great Trigonometrical Survey of India?"
      ],
      vocab: [
        { term: "Trigonometrical Survey", def: "A nationwide geodetic survey measuring exact distances across the subcontinent using triangulation geometry." },
        { term: "Basalt Masonry", def: "Durable stone construction using ancient Deccan volcanic rock with high thermal inertia." },
        { term: "Hydrological Stepwell", def: "Engineered underground water reservoirs designed to capture seasonal monsoons and prevent winter drought." }
      ],
      experiment: "Place a cup of dry dark stone and a cup of water in midday sunlight for 20 minutes. Touch both: the stone heats quickly while water warms slowly. Notice how ancient architects used water bodies and heavy stone to regulate building temperatures!"
    }
  };

  function openClassroomBrief(ep) {
    if (!ep || !classroomBriefModal) return;

    const epNumEl = document.getElementById('brief-sheet-ep-num');
    const titleEl = document.getElementById('brief-sheet-title');
    const catEl = document.getElementById('brief-sheet-category');
    const durEl = document.getElementById('brief-sheet-duration');
    const bigIdeaEl = document.getElementById('brief-sheet-big-idea');
    const sparksEl = document.getElementById('brief-sheet-sparks');
    const vocabEl = document.getElementById('brief-sheet-vocab');
    const expEl = document.getElementById('brief-sheet-experiment');

    if (epNumEl) epNumEl.textContent = `EPISODE #${ep.number || ''}`;
    if (titleEl) titleEl.textContent = ep.title;
    if (catEl) catEl.textContent = ep.category;
    if (durEl) durEl.textContent = ep.duration;

    const briefData = CLASSROOM_BRIEFS[ep.id] || {
      bigIdea: ep.description,
      sparks: [
        `What fundamental questions does "${ep.title}" raise about our understanding of the universe?`,
        "How does the historical context of this discovery change how we view science today?",
        "If you could ask Simran Ailani one question about this topic on the Curiosity Mailbag, what would it be?"
      ],
      vocab: [
        { term: "Scientific Method", def: "Systematic observation, measurement, experiment, and the formulation and testing of hypotheses." },
        { term: "Pedagogy", def: "The method and practice of teaching, especially as an academic subject or theoretical concept." },
        { term: "Knowledge Equity", def: "Ensuring open, barrier-free access to high-quality learning materials for students in every region." }
      ],
      experiment: "Listen to the episode with a friend and spend 5 minutes discussing which concept surprised you the most. Formulate your own inquiry question to send to Simran!"
    };

    if (bigIdeaEl) bigIdeaEl.textContent = briefData.bigIdea;

    if (sparksEl) {
      sparksEl.innerHTML = briefData.sparks.map(s => `<li>${s}</li>`).join('');
    }

    if (vocabEl) {
      vocabEl.innerHTML = briefData.vocab.map(v => `
        <div class="sheet-vocab-item">
          <div class="vocab-term">${v.term}</div>
          <div class="vocab-def">${v.def}</div>
        </div>
      `).join('');
    }

    if (expEl) expEl.textContent = briefData.experiment;

    classroomBriefModal.classList.add('is-active');
  }

  function closeClassroomBrief() {
    if (classroomBriefModal) classroomBriefModal.classList.remove('is-active');
  }

  if (closeClassroomBriefBtn) closeClassroomBriefBtn.addEventListener('click', closeClassroomBrief);
  if (classroomBriefModal) {
    classroomBriefModal.addEventListener('click', (e) => {
      if (e.target === classroomBriefModal) closeClassroomBrief();
    });
  }

  if (btnPrintBrief) {
    btnPrintBrief.addEventListener('click', () => {
      window.print();
    });
  }

  if (btnHeroClassroomBrief) {
    btnHeroClassroomBrief.addEventListener('click', () => {
      const ep = GYAN_SETU_EPISODES[currentEpisodeIndex] || GYAN_SETU_EPISODES[0];
      openClassroomBrief(ep);
    });
  }

  // Hook into notes modal "Classroom Brief (PDF)" button
  const modalOpenBriefBtn = document.getElementById('modal-open-brief-btn');
  if (modalOpenBriefBtn) {
    modalOpenBriefBtn.addEventListener('click', () => {
      if (notesModal) notesModal.classList.remove('is-active');
      const ep = GYAN_SETU_EPISODES[currentEpisodeIndex] || GYAN_SETU_EPISODES[0];
      openClassroomBrief(ep);
    });
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
      document.querySelectorAll('#nav-host-name-tag, #mob-nav-host-name-tag').forEach(el => {
        el.textContent = `Host: ${profile.name}`;
      });
      if (curatorLoggedInLabel) curatorLoggedInLabel.textContent = `Lead Host Session Active: ${profile.name}`;
      
      // Render host exclusive components
      renderMailbagInbox();
      renderCuratorQueue();
    } else {
      document.body.classList.remove('is-host');
      
      // If user had curator tab open, switch back to ask tab
      const curatorTabPane = document.getElementById('tab-content-curator');
      if (curatorTabPane && curatorTabPane.classList.contains('active')) {
        curatorTabPane.classList.remove('active');
        const askPane = document.getElementById('tab-content-ask');
        if (askPane) askPane.classList.add('active');
        studioTabBtns.forEach(btn => {
          if (btn.getAttribute('data-tab') === 'ask') btn.classList.add('active');
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

    // Host Portal buttons click (open login directly)
    document.querySelectorAll('.btn-host-portal-nav').forEach(btn => {
      btn.addEventListener('click', () => {
        if (gatewayModal) {
          if (gatewayViewChoose) gatewayViewChoose.classList.remove('active');
          if (gatewayViewLogin) gatewayViewLogin.classList.add('active');
          gatewayModal.classList.add('is-active');
          if (hostEmailInput) hostEmailInput.focus();
        }
      });
    });

    // Host Logout Handlers
    function handleLogout() {
      sessionStorage.setItem('gyansetu_user_role', 'listener');
      sessionStorage.removeItem('gyansetu_host_email');
      updateRoleUI();
      showToast('👋 Host session logged out. Reverted to Listener mode.');
    }

    document.querySelectorAll('.btn-host-logout').forEach(btn => {
      btn.addEventListener('click', handleLogout);
    });
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

  // Initialize Retro Radio Device Edition Selector (Android Phone vs Tab Console)
  initDeviceEditionSelector();

  // Initialize Android Native Bottom Navigation Bar active highlights
  function initAndroidBottomNav() {
    const bottomNavItems = document.querySelectorAll('.android-bottom-nav .bottom-nav-item');
    if (!bottomNavItems.length) return;

    bottomNavItems.forEach(item => {
      item.addEventListener('click', (e) => {
        const href = item.getAttribute('href');
        if (href && href.startsWith('#')) {
          const targetEl = document.querySelector(href);
          if (targetEl) {
            e.preventDefault();
            targetEl.scrollIntoView({ behavior: 'smooth' });
          }
        }
        bottomNavItems.forEach(i => i.classList.remove('active'));
        item.classList.add('active');
      });
    });

    // Auto-update based on scroll position
    window.addEventListener('scroll', () => {
      const scrollPos = window.scrollY + 200;
      const broadcastSection = document.getElementById('broadcast');
      const episodesSection = document.getElementById('episodes');
      const appSection = document.getElementById('app');

      const bnavHome = document.getElementById('bnav-home');
      const bnavEpisodes = document.getElementById('bnav-episodes');
      const bnavVault = document.getElementById('bnav-vault');

      if (appSection && scrollPos >= appSection.offsetTop - 100) {
        bottomNavItems.forEach(i => i.classList.remove('active'));
        if (bnavVault) bnavVault.classList.add('active');
      } else if (episodesSection && scrollPos >= episodesSection.offsetTop - 100) {
        bottomNavItems.forEach(i => i.classList.remove('active'));
        if (bnavEpisodes) bnavEpisodes.classList.add('active');
      } else if (broadcastSection) {
        bottomNavItems.forEach(i => i.classList.remove('active'));
        if (bnavHome) bnavHome.classList.add('active');
      }
    }, { passive: true });
  }

  initAndroidBottomNav();

  // Register Global Progressive Web App (PWA) Offline Service Worker
  if ('serviceWorker' in navigator && window.location.protocol.startsWith('http')) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js').then((reg) => {
        console.log('[GyanSetu PWA] Service Worker registered successfully with scope:', reg.scope);
      }).catch((err) => {
        console.warn('[GyanSetu PWA] Service Worker registration failed:', err);
      });
    });
  }
});

// ==========================================================
// RETRO RADIO DEVICE EDITION SELECTOR (ANDROID PHONE vs TAB CONSOLE)
// ==========================================================
function initDeviceEditionSelector() {
  const btnAndroid = document.getElementById('btn-device-android');
  const btnTablet = document.getElementById('btn-device-tablet');
  const btnReloadToggle = document.getElementById('btn-switch-and-reload');
  const reloadText = document.getElementById('reload-action-btn-text');
  const indicatorTag = document.getElementById('edition-indicator-tag');
  const titleEl = document.getElementById('app-download-name');
  const tagEl = document.getElementById('app-download-tag');
  const containerAndroid = document.getElementById('edition-android-container');
  const containerTablet = document.getElementById('edition-tablet-container');
  const overlay = document.getElementById('edition-reloading-overlay');

  if (!btnAndroid || !btnTablet) return;

  // 1. Determine active device edition (Default is strictly Android Smartphone)
  const urlParams = new URLSearchParams(window.location.search);
  const urlDevice = urlParams.get('device');
  const currentDevice = (urlDevice === 'tablet') ? 'tablet' : 'android';

  // 2. Render state
  function renderEditionState(device) {
    if (device === 'tablet') {
      btnAndroid.classList.remove('active');
      btnTablet.classList.add('active');
      if (indicatorTag) {
        indicatorTag.innerHTML = '📟 Tablet Console Active';
        indicatorTag.style.borderColor = 'rgba(80, 155, 147, 0.6)';
        indicatorTag.style.color = '#5eead4';
        indicatorTag.style.background = 'rgba(80, 155, 147, 0.2)';
      }
      if (titleEl) titleEl.textContent = 'GyanSetu Tablet Radio Console';
      if (tagEl) tagEl.textContent = 'Tab Edition • Dual Analog VU Meters, Dark Mesh & 160px Knurled Tuner';
      if (containerAndroid) containerAndroid.style.display = 'none';
      if (containerTablet) containerTablet.style.display = 'grid';
      if (reloadText) reloadText.textContent = 'Switch to Android Phone & Reload Options';
    } else {
      btnAndroid.classList.add('active');
      btnTablet.classList.remove('active');
      if (indicatorTag) {
        indicatorTag.innerHTML = '📱 Android Smartphone Active (Default)';
        indicatorTag.style.borderColor = 'rgba(249, 124, 34, 0.4)';
        indicatorTag.style.color = '#ffa048';
        indicatorTag.style.background = 'rgba(249, 124, 34, 0.15)';
      }
      if (titleEl) titleEl.textContent = 'GyanSetu Pocket Radio';
      if (tagEl) tagEl.textContent = 'Android Smartphone Edition • Handheld Transistor Radio • Pocket Offline Suite';
      if (containerAndroid) containerAndroid.style.display = 'grid';
      if (containerTablet) containerTablet.style.display = 'none';
      if (reloadText) reloadText.textContent = 'Switch to Tablet (Tab) Edition & Reload Options';
    }
  }

  // 3. Trigger reload to switch target
  function switchAndReload(targetDevice) {
    try {
      localStorage.setItem('gyansetu_device_edition', targetDevice);
    } catch (e) {}

    if (overlay) overlay.classList.add('is-active');
    if (btnReloadToggle) btnReloadToggle.classList.add('reloading');
    renderEditionState(targetDevice);

    setTimeout(() => {
      try {
        const currentPath = window.location.pathname || '/index.html';
        window.location.href = currentPath + '?device=' + targetDevice + '#app';
      } catch (e) {
        window.location.search = '?device=' + targetDevice;
      }
    }, 280);
  }

  btnAndroid.addEventListener('click', (e) => {
    e.preventDefault();
    if (currentDevice !== 'android') {
      switchAndReload('android');
    }
  });

  btnTablet.addEventListener('click', (e) => {
    e.preventDefault();
    if (currentDevice !== 'tablet') {
      switchAndReload('tablet');
    }
  });

  if (btnReloadToggle) {
    btnReloadToggle.addEventListener('click', (e) => {
      e.preventDefault();
      const target = currentDevice === 'tablet' ? 'android' : 'tablet';
      switchAndReload(target);
    });
  }

  // Initial render on page load
  renderEditionState(currentDevice);
}

