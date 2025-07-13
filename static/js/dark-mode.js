const toggleBtn = document.getElementById('darkmode-switch');
const themeIcon = document.getElementById('theme-icon');


// lightmode
function setLightMode() {
  document.body.classList.remove('darkmode');
  document.body.classList.add('lightmode');
  themeIcon.src = '/static/images/dark_mode.svg';
  localStorage.setItem('darkMode', 'light');
}
// darkmode
function setDarkMode() {
  document.body.classList.remove('lightmode');
  document.body.classList.add('darkmode');
  themeIcon.src = '/static/images/light_mode.svg';
  localStorage.setItem('darkMode', 'dark');
}

// On page load, apply the saved mode or default to darkmode
const darkMode = localStorage.getItem('darkMode');
if (darkMode === 'light') {
  setLightMode();
} else {
  setDarkMode();
}

// Toggle on button click
toggleBtn.addEventListener('click', () => {
console.log("Dark mode toggle clicked");

  if (document.body.classList.contains('darkmode')) {
    setLightMode();
  } else {
    setDarkMode();
  }
});


/* This code was adapted for my needs from the following sources:

- MDN Web - Web Storage API, classList, addEventListener
    https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API
    https://developer.mozilla.org/en-US/docs/Web/API/Element/classList
    https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener

- W3Schools - JavaScript localStorage, classList
    https://www.w3schools.com/jsref/prop_win_localstorage.asp
    https://www.w3schools.com/howto/howto_js_toggle_class.asp

- Stack Overflow - Darkmode toggle
    https://stackoverflow.com/questions/75005912/switch-to-dark-mode-button

- Icons - Google Fonts
    https://fonts.google.com/icons

*/