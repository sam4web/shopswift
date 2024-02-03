const toggleBtn = document.querySelector('#toggle-btn');
let darkToggleOn = JSON.parse(localStorage.getItem('isDarkTheme'));

if (darkToggleOn) {
  document.body.classList.add('dark');
}

toggleBtn.addEventListener('click', () => {
  darkToggleOn = !darkToggleOn;
  localStorage.setItem('isDarkTheme', darkToggleOn);
  document.body.classList.toggle('dark');
});
