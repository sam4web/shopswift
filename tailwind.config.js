/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./template/**/*.html', './static/**/*.{css,js}'],
  theme: {
    extend: {},
  },
  plugins: [],
};

// npx tailwindcss -i ./static/css/main.css -o ./static/css/main.min.css --watch
