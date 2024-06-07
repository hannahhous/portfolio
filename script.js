document.addEventListener('DOMContentLoaded', function () {
  var menuButton = document.getElementById('menuButton');
  var sideMenu = document.getElementById('sideMenu');

  menuButton.addEventListener('click', function () {
    sideMenu.classList.toggle('sideMenuShow');
  });
});
