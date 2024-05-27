// script.js

document.addEventListener('DOMContentLoaded', function() {
  const menuButton = document.getElementById('menuButton');
  const sideMenu = document.getElementById('sideMenu');

  menuButton.addEventListener('click', function() {
    sideMenu.classList.toggle('sideMenuShow');
  });
});
