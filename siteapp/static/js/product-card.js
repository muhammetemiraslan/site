const addToCart = document.querySelectorAll(".add-to-cart");

addToCart.forEach((button) => {
  button.addEventListener("click", function () {
    button.classList.add("add-to-cart-active");
    button.classList.add("add-to-cart-no-hover");
    button.textContent = "Sepete eklendi!";
  });
});

//SEPETE EKLENDİ YAZISI İÇİN

document.getElementById("addToCart").addEventListener("click", function() {
  document.getElementById("form-cart").submit();
});
