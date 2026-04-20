# Design System Strategy: The Kinetic Editorial

## 1. Overview & Creative North Star: "Dynamic Clarity"
This design system is not a set of static rules; it is a framework for **Dynamic Clarity**. While many systems prioritize "safety" through generic grids, we prioritize **"The Energy of Execution."** 

Our Creative North Star is the **Kinetic Editorial**. We treat the screen like a high-end digital broadsheet—combining the authoritative weight of premium typography with the fluid, layered depth of modern glassmorphism. We break the "template" look through intentional asymmetry, tight vertical rhythm, and a rejection of traditional structural lines (borders) in favor of tonal depth.

---

## 2. Color & Surface Architecture
We move beyond flat hex codes to a system of **Tonal Layering**. Color is used to define "zones of action" and "priority of thought."

### The Palette
*   **Primary (ACT Mint):** `primary_container` (#00C4B4). Used for high-energy moments and primary conversion.
*   **Tertiary (Spark Yellow):** `tertiary_container` (#CCAD00). Used as a high-contrast disruptor for badges and micro-interactions.
*   **Neutrals:** Using `surface` (#F7F9FF) for the canvas and `on_surface` (#0F1D2A) for high-readability text.

### The Rules of Engagement
*   **The "No-Line" Rule:** 1px solid borders are strictly prohibited for sectioning. Structural boundaries must be defined solely through background shifts. For example, a `surface_container_low` section sitting against a `surface` background.
*   **Surface Hierarchy & Nesting:** Treat the UI as a series of physical layers. 
    *   *Level 0:* `surface` (The base floor)
    *   *Level 1:* `surface_container_low` (Subtle sectioning)
    *   *Level 2:* `surface_container_lowest` (Pure white cards to "pop" off the page)
*   **The "Glass & Gradient" Rule:** To provide visual "soul," avoid flat Mint buttons. Use a subtle linear gradient from `primary` (#006A61) to `primary_container` (#00C4B4) to create a sense of curvature and premium finish. For floating navigation or overlays, use `surface` with 80% opacity and a 20px backdrop-blur.

---

## 3. Typography: Editorial Authority
We use **Pretendard (Inter)** not as a system font, but as a branding tool. Our typography scale is aggressive and intentional.

*   **Display (The Statement):** Use `display-lg` (3.5rem) with -0.02em letter-spacing. This is for high-impact hero sections that demand immediate attention.
*   **Headline (The Narrative):** `headline-lg` (2rem, Bold). Headlines should feel tight and energetic (1.4lh).
*   **Body (The Detail):** `body-lg` (1rem, Regular). We prioritize legibility with a 1.6lh line height to create breathing room amidst the high-energy headlines.
*   **Label (The Utility):** `label-md` (0.75rem, SemiBold). All-caps with increased letter-spacing (+0.05em) for category badges and small metadata.

---

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are a crutch. We use **Tonal Layering** to convey hierarchy.

*   **The Layering Principle:** Depth is achieved by "stacking." A card using `surface_container_lowest` (White) placed on a `surface_container_low` (Light Gray/Blue) background creates a natural, soft lift without a single pixel of shadow.
*   **Ambient Shadows:** When a component must float (e.g., a Modal or Floating Action Button), use a shadow tinted with the `on_surface` color at 4% opacity. 
    *   *Value:* `0px 20px 40px rgba(15, 29, 42, 0.04)`
*   **The "Ghost Border" Fallback:** If a container lacks contrast against its background, use a "Ghost Border"—the `outline_variant` token set to 15% opacity. Never use a 100% opaque border.

---

## 5. Components: Style & Execution

### Buttons (The Energy Drivers)
*   **Primary:** Background: `primary_container` (#00C4B4). Shape: `md` (0.75rem). Text: `on_primary` (White, SemiBold). 
    *   *Director’s Note:* Add a subtle inner-glow (1px white overlay at 10% opacity) on the top edge to simulate a premium 3D surface.
*   **Secondary:** Background: `surface_container_low`. Text: `on_secondary_container`. 
*   **Tertiary/Ghost:** No background. Text: `primary`. Use for low-emphasis actions.

### Cards & Content Groups
*   **Rules:** No dividers. Use `xl` (1.5rem) padding and `lg` (1rem) corner radius. 
*   **Separation:** Use vertical white space from the 8px grid (specifically 48px or 64px) to separate content blocks, rather than horizontal lines.

### Input Fields
*   **Resting:** `surface_container_lowest` background. No border. Subtle `outline_variant` at 10% opacity.
*   **Active:** 2px stroke using `primary_container`. 
*   **Feedback:** Error states use `error` (#BA1A1A) text but keep the background `error_container` (#FFDAD6) at 20% opacity.

### Navigation & Chips
*   **Selection Chips:** Use `tertiary_fixed` (#FFE167) for selected states to inject "Spark Yellow" energy into the utility-driven parts of the app.

---

## 6. Do’s and Don’ts

### Do
*   **Do** use "Candid iPhone Style" photography. Crops should feel off-center and authentic, never staged.
*   **Do** use asymmetry. Align a headline to the left and a CTA to the right to create "Visual Kineticism."
*   **Do** respect the 8px grid religiously. Trust the white space; it is a design element, not "empty" space.

### Don’t
*   **Don't** use 1px dividers to separate list items. Use 16px of vertical space and a subtle background shift on hover.
*   **Don't** use pure black (#000000). Always use `on_surface` (#0F1D2A) for text to maintain the premium slate-toned depth.
*   **Don't** use heavy "drop shadows." If the user can see the shadow, it's too dark. It should be felt, not seen.

---

**Director's Closing Thought:**
A design system is a living organism. When in doubt, choose **clarity over decoration**. If an element doesn't help the user execute their task with more energy, remove it. Use the Mint to guide, the Yellow to alert, and the white space to let the user breathe.