document.querySelectorAll(".add-to-cart").forEach((button) => {
  button.addEventListener("click", function() {
    const originalText = button.textContent;
    button.classList.add("add-to-cart-active", "add-to-cart-no-hover");
    button.textContent = "✓ Sepete Eklendi!";
    
    // 2 saniye sonra eski haline dönsün
    setTimeout(() => {
      button.textContent = originalText;
      button.classList.remove("add-to-cart-active", "add-to-cart-no-hover");
    }, 2000);
  });
});

//SEPETE EKLENDİ YAZISI İÇİN

document.getElementById("addToCart").addEventListener("click", function() {
  document.getElementById("form-cart").submit();
});
