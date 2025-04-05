//hamburger-toggle open-close effect
const navBtn = document.getElementById("navbtn");
navBtn.addEventListener("click", () => {
  navBtn.classList.toggle("active");
});

//off-screen active
const offScreenMenu = document.querySelector(".off-screen-menu");

navBtn.addEventListener("click", () => {
  if (!offScreenMenu.classList.contains("active")) {
    offScreenMenu.classList.add("active");
    // Scroll'u kapat
    document.body.style.overflow = "hidden";
  } else {
    offScreenMenu.classList.remove("active");
    // Scroll'u tekrar aç
    document.body.style.overflow = "auto";
  }
});

const mediaQuery = window.matchMedia("(min-width: 864px)");

function kontrolEt(mediaQuery) {
  if (mediaQuery.matches) {
    // Scroll'u tekrar aç
    document.body.style.overflow = "auto";
  } else {
    // Scroll'u kapat
    if (offScreenMenu.classList.contains("active")) {
      document.body.style.overflow = "hidden";
    }
  }
}

// Sayfa yüklenince kontrol et
kontrolEt(mediaQuery);

// Boyut değişimini dinle
mediaQuery.addEventListener("change", kontrolEt);
