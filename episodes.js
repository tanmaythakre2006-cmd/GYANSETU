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
    },
    {
      name: "Tanmay Rambhau Thakre",
      role: "Technical Architect, Digital Production, and Co-Founder",
      initials: "TT",
      bio: "Visionary student builder leading platform architecture, audio systems, and digital transmission to deliver open knowledge to all corners of the earth."
    }
  ],
  mission: "Spreading unrestricted knowledge to the farthest corners of the world by making complex topics accessible, engaging, and delightfully clear.",
  logo: "assets/images/logo.png",
  totalEpisodes: 7,
  totalRuntime: "42 mins",
  broadcastMode: "24/7 Global Stream & On-Demand Library"
};

const GYAN_SETU_EPISODES = [
  {
    id: "ep-1",
    number: 1,
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
    number: 2,
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
    number: 3,
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
    number: 5,
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
    number: 6,
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
    number: 7,
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
