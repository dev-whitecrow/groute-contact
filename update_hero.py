import re

with open('acts29_gen3.html', 'r', encoding='utf-8') as f:
    html = f.read()

hero_start = html.find('<!-- 1. Hero Section -->')
mentors_start = html.find('<!-- 2. Mentors -->')

hero_content = html[hero_start:mentors_start]

# We need to replace the entire hero section with the new scroll-sticky logic.
new_hero = """<!-- 1. Hero Section -->
        <section class="h-[180vh] md:h-[220vh] relative pt-32 pb-32">
            <!-- Sticky Text -->
            <div class="sticky top-32 max-w-[800px] mx-auto px-8 w-full z-20 pointer-events-none">
                <div class="max-w-[500px] space-y-10 pointer-events-auto">
                    <div class="space-y-6">
                        <span class="inline-block glass-pill text-tertiary-container px-6 py-2.5 text-sm font-bold tracking-widest uppercase shadow-sm">ACTS 29</span>
                        <h1 class="text-[4rem] lg:text-[4.5rem] leading-[1.05] font-black tracking-tight text-on-surface drop-shadow-sm">
                            첫 시도를<br />
                            <span class="gradient-text">안전하게</span>
                        </h1>
                        <p class="text-xl leading-relaxed text-secondary font-semibold max-w-[380px]">
                            새로운 도전,<br />
                            안전하게 시도해보는 커뮤니티
                        </p>
                    </div>

                    <div class="relative inline-block w-full md:w-auto group">
                        <div class="absolute inset-2 bg-[#00c4b4] rounded-[3rem] blur-[24px] opacity-40 group-hover:opacity-70 group-hover:blur-[32px] transition-all duration-500"></div>
                        <button onclick="handleCTAClick(event)"
                            class="relative z-10 w-full glass px-12 py-6 font-extrabold text-2xl text-on-surface hover:-translate-y-1 transition-all flex justify-center items-center gap-4 bg-white/30 backdrop-blur-md border border-white/50 shadow-xl">
                            커뮤니티 합류하기
                            <span class="material-symbols-outlined text-[1.8rem]">rocket_launch</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Sticky Image coming from below -->
            <div class="sticky bottom-16 md:bottom-24 lg:top-[45vh] max-w-[800px] mx-auto px-8 w-full z-10 pt-[50vh] md:pt-[70vh]">
                <div class="w-full aspect-video bg-surface-container-lowest rounded-[3rem] shadow-[0_32px_64px_-16px_rgba(0,0,0,0.2)] overflow-hidden border-[8px] border-white relative group">
                    <img src="hero_finale.jpg" class="w-full h-full object-cover filter saturate-[0.8] contrast-[1.05]" alt="ACTS29 2기 피날레">
                    <div class="absolute inset-0 bg-primary-container/10 mix-blend-soft-light transition-opacity hover:opacity-0 duration-700"></div>
                </div>
            </div>
        </section>

        """

html = html[:hero_start] + new_hero + html[mentors_start:]

with open('acts29_gen3.html', 'w', encoding='utf-8') as f:
    f.write(html)

