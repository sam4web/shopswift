/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{css,js}', '*.html'],
  theme: {
    extend: {
      colors: {
        primary: '#0069E0',
        'primary-dark': '#021431',
        'graish-blue': '#394E6A',
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
