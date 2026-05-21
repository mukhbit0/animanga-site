/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        brand: {
          light: '#fdfcfe',
          dark: '#0f0f12',
          accent: '#ff0055',
          violet: '#7c3aed',
          pink: '#db2777',
        }
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out',
        'scale-up': 'scaleUp 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        scaleUp: {
          '0%': { transform: 'scale(1)' },
          '100%': { transform: 'scale(1.02)' },
        }
      }
    },
  },
  plugins: [],
}