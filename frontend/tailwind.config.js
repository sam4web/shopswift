/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{css,js}', '*.html'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: '#0069E0',
        'primary-dark': '#021431',
        'secondary-dark': '#181920',
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
