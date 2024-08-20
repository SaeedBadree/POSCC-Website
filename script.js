function myFunction() {
    var x = document.getElementById("top-menu-bar");
    if (x.className === "menu-bar") {
      x.className += " responsive";
    } else {
      x.className = "menu-bar";
    }
  }