// GyanSetu - Master Dataset
// Student-Led Global Knowledge Platform & Internet Radio Station

const GYAN_SETU_SHOW = {
  name: "GyanSetu",
  subtitle: "Internet Radio Station & Global Knowledge Hub",
  tagline: "Demystifying Complex Ideas • Igniting Curiosity Across the World",
  founders: [
    {
      name: "Simran Ailani",
      role: "Founder and Lead Host",
      initials: "SA",
      bio: "Passionate student communicator dedicated to breaking down intricate, daunting concepts into engaging, intuitive discussions for learners everywhere."
    }
  ],
  mission: "Spreading unrestricted knowledge to the farthest corners of the world by making complex topics accessible, engaging, and delightfully clear.",
  logo: "assets/images/logo.png",
  totalEpisodes: 13,
  totalRuntime: "78 mins",
  broadcastMode: "24/7 Global Stream & On-Demand Library"
};

const GYAN_SETU_EPISODES = [
  {
    id: "ep-13",
    number: 13,
    title: "नागपूरचा इतिहास",
    category: "History of Ideas",
    date: "October 28, 2026",
    duration: "9m 18s",
    durationSec: 558,
    description: "या भागात जाणून घेऊया नागपूरचा इतिहास, भोसले राजांचा काळ आणि महालातील जुन्या वास्तूंमागच्या रंजक गोष्टी! Explore the rich history of Nagpur, the era of the Bhonsle dynasty, and the fascinating stories behind the historic monuments of Mahal.",
    image: "assets/images/ep13-nagpurcha-itihas.jpg",
    audioSrc: "assets/audio/ep13-nagpurcha-itihas.mp3",
    audioSrcEnglish: "assets/audio/ep13-nagpur-english-master.mp3",
    onlineAudioSrc: "https://anchor.fm/s/10129a7a0/podcast/play/128311004/https%3A%2F%2Fd3ctxlq1ktw2nl.cloudfront.net%2Fstaging%2F2026-9-28%2Faec3f0d6-9b3e-368a-f716-b068daa38dc6.mp3",
    hosts: ["Simran Ailani"]
  },
  {
    id: "ep-12",
    number: 12,
    title: "Oops, I Created Life: In Hindsight, Victor…",
    category: "Ethics & Ideas",
    date: "October 26, 2026",
    duration: "5m 21s",
    durationSec: 321,
    description: "What happens when curiosity crosses the line into obsession? Through Mary Shelley's Frankenstein, we explore the dark side of ambition, the ethics of creation, and the consequences of playing God. After all, just because we can create a monster, does that mean we should?",
    image: "assets/images/ep8-oops-i-created-life.jpg",
    audioSrc: "assets/audio/ep8-oops-i-created-life.mp3",
    hosts: ["Simran Ailani"]
  },
  {
    id: "ep-11",
    number: 11,
    title: "What colour is the sky?",
    category: "Everyday Phenomena",
    date: "October 26, 2026",
    duration: "4m 31s",
    durationSec: 271,
    description: "What colour is the sky? Discover the fascinating science of sunlight, air molecules, and Rayleigh scattering—and see how something we take for granted every day hides a beautiful scientific mystery.",
    image: "assets/images/ep9-what-colour-is-the-sky.jpg",
    audioSrc: "assets/audio/ep9-what-colour-is-the-sky.mp3",
    hosts: ["Simran Ailani"]
  },
  {
    id: "ep-10",
    number: 10,
    title: "Napoleon wasn't poisoned.....or was he?",
    category: "History of Ideas",
    date: "October 21, 2026",
    duration: "4m 43s",
    durationSec: 283,
    description: "Was Napoleon poisoned, or did he die of natural causes? Uncover the arsenic mystery behind one of history's most debated deaths in an intriguing deep dive into forensic chemistry and historical investigation.",
    image: "assets/images/ep10-napoleon-wasnt-poisoned.jpg",
    audioSrc: "assets/audio/ep10-napoleon-wasnt-poisoned.mp3",
    hosts: ["Simran Ailani"]
  },
  {
    id: "ep-9",
    number: 9,
    title: "Are we more than our Molecules?",
    category: "Mind & Neuroscience",
    date: "October 09, 2026",
    duration: "7m 10s",
    durationSec: 430,
    description: "What happens when matter begins to feel? Explore the chemistry behind attraction, dopamine, oxytocin, and human connection as we uncover the science of love—and question whether understanding its chemistry can ever explain its meaning.",
    image: "assets/images/ep11-are-we-more-than-our-molecules.jpg",
    audioSrc: "assets/audio/ep11-are-we-more-than-our-molecules.mp3",
    hosts: ["Simran Ailani"]
  },
  {
    id: "ep-8",
    number: 8,
    title: "There's always that one character",
    category: "Literature & Storytelling",
    date: "October 07, 2026",
    duration: "4m 57s",
    durationSec: 297,
    description: "Let's dive into the minds of authors whose characters make a fantasy truly fantastic! An insightful exploration into character design, archetypes, and the psychology that makes fictional figures feel remarkably alive.",
    image: "assets/images/ep12-theres-always-that-one-character.jpg",
    audioSrc: "assets/audio/ep12-theres-always-that-one-character.mp3",
    hosts: ["Simran Ailani"]
  },
  {
    id: "ep-1",
    number: 7,
    title: "Can Chemistry explain Consciousness?",
    category: "Mind & Neuroscience",
    date: "October 06, 2026",
    duration: "4m 29s",
    durationSec: 269,
    description: "Can atomic bonds and neurotransmitters explain what makes us think, feel, and experience the world? Dive into the profound frontier where biochemistry intersects with the mystery of human consciousness, exploring how matter gives rise to mind.",
    image: "assets/images/ep1-can-chemistry-explain-consciousness.jpg",
    audioSrc: "assets/audio/ep1-can-chemistry-explain-consciousness.mp3",
    hosts: ["Simran Ailani"]
  },
  {
    id: "ep-2",
    number: 6,
    title: "The secrets of Sadabahar",
    category: "Nature & Medicine",
    date: "August 04, 2026",
    duration: "3m 58s",
    durationSec: 238,
    description: "What if an unassuming common flower held a secret that revolutionized modern medicine? Uncover the astonishing true story of how a failed diabetes study unmasked vincristine—a groundbreaking life-saving chemotherapy drug—and why nature's deepest marvels often hide in plain sight.",
    image: "assets/images/ep2-the-secrets-of-sadabahar.jpg",
    audioSrc: "assets/audio/ep2-the-secrets-of-sadabahar.mp3",
    hosts: ["Simran Ailani"]
  },
  {
    id: "ep-3",
    number: 5,
    title: "The dream that gave us Benzene",
    category: "History of Ideas",
    date: "July 26, 2026",
    duration: "5m 04s",
    durationSec: 304,
    description: "What connects a legendary dream of an ancient snake seizing its own tail with one of humanity's most pivotal scientific breakthroughs? Discover the story behind August Kekulé's visionary epiphany and why the symmetrical benzene ring reshaped our entire understanding of molecular architecture.",
    image: "assets/images/ep3-the-dream-that-gave-us-benzene.jpg",
    audioSrc: "assets/audio/ep3-the-dream-that-gave-us-benzene.mp3",
    hosts: ["Simran Ailani"]
  },
  {
    id: "ep-4",
    number: 4,
    title: "How do drugs know where to go in the body?",
    category: "Everyday Phenomena",
    date: "July 30, 2025",
    duration: "6m 23s",
    durationSec: 383,
    description: "Ever wondered how a tiny swallowed pill knows exactly where you are aching? Does it have a biological GPS? Unravel the elegant choreography of circulatory diffusion, receptors, and lock-and-key targeting mechanisms that allow modern treatments to pinpoint pain without taking a single wrong turn.",
    image: "assets/images/ep4-how-do-drugs-know-where-to-go-in-th.jpg",
    audioSrc: "assets/audio/ep4-how-do-drugs-know-where-to-go-in-th.mp3",
    hosts: ["Simran Ailani"]
  },
  {
    id: "ep-5",
    number: 3,
    title: "Why bananas are slightly radioactive?",
    category: "Everyday Phenomena",
    date: "July 29, 2025",
    duration: "5m 37s",
    durationSec: 337,
    description: "Is your morning fruit bowl technically emitting radiation? Break down the fascinating physics of Potassium-40, background environmental radiation, and human biology in a fun, intuitive journey to see whether your banana smoothie is a radioactive marvel or simply nature at work.",
    image: "assets/images/ep5-why-bananas-are-slightly-radioactiv.jpg",
    audioSrc: "assets/audio/ep5-why-bananas-are-slightly-radioactiv.mp3",
    hosts: ["Simran Ailani"]
  },
  {
    id: "ep-6",
    number: 2,
    title: "AI in Chemistry: When machines meet molecules",
    category: "Future & Technology",
    date: "July 28, 2025",
    duration: "6m 08s",
    durationSec: 368,
    description: "What happens when neural networks and machine intelligence step inside the laboratory? Simran is joined by her AI co-host Neo to explore how generative algorithms and computational models are predicting molecular structures in seconds and accelerating breakthroughs that once took decades.",
    image: "assets/images/ep6-ai-in-chemistry-when-machines-meet-.jpg",
    audioSrc: "assets/audio/ep6-ai-in-chemistry-when-machines-meet-.mp3",
    hosts: ["Simran Ailani", "Neo (AI Co-Host)"]
  },
  {
    id: "ep-7",
    number: 1,
    title: "Carbenes",
    category: "Deep Concepts",
    date: "April 07, 2025",
    duration: "10m 21s",
    durationSec: 621,
    description: "Simran Ailani and Lawanya Deshmukh venture into the fleeting world of carbenes—ultra-reactive chemical species with lifetimes measured in microseconds. Explore how these temporary molecular dynamos drive breakthrough green syntheses, pharmaceutical innovations, and next-generation materials.",
    image: "assets/images/ep7-carbenes.jpg",
    audioSrc: "assets/audio/ep7-carbenes.mp3",
    hosts: ["Simran Ailani", "Lawanya Deshmukh"]
  }
];
