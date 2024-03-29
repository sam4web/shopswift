/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./template/**/*.html', './static/**/*.{css,js}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: '#0069E0',
        'secondary-dark': '#021431',
        'primary-dark': '#181920',
        'body-dark': '#272935',
        gray: { DEFAULT: '#394E6A', dark: '#414558' },
        light: '#F0F6FF',
      },
    },
    fontFamily: {
      heading: ['Nunito', 'sans-serif'],
      display: ['Poppins', 'sans-serif'],
    },
  },
  plugins: [],
};
