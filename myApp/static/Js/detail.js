const modal = document.querySelector(".modal-container");

const openModal = () =>{
   modal.classList.add("show-modal");
}
const closeModal = () => {
    modal.classList.remove("show-modal");
}
const focusedSearchBar = (id,spanId) => {
  const focusedInput = document.getElementById(id);
  const focusedPlaceholder = document.getElementById(spanId);
  focusedInput.classList.add("focused-text");
  focusedPlaceholder.style.color = "#0000CD"
  focusedPlaceholder.classList.add("focused-placeholder");
}
const focusedOutSearchBar = (id,spanId) => {
    const focusedInput = document.getElementById(id);
    const focusedPlaceholder = document.getElementById(spanId);
   if(focusedInput.value.length == 0) {
    
    focusedPlaceholder.classList.remove("focused-placeholder");  
          
   }
   focusedPlaceholder.style.color = "#a0a0a0"
    focusedInput.classList.remove("focused-text");
}
const openMobileSearch = () => {
    const mobileSearch = document.querySelector(".mobile-search-container");
   
    mobileSearch.classList.add("search-mobile-opened")
    document.querySelector(".search-mobile").focus();
}
const closeMobileSearch = () => {
    const mobileSearchContainer = document.querySelector(".mobile-search-container");
    mobileSearchContainer.classList.remove("search-mobile-opened");
    document.querySelector(".search-mobile").value = "";
   
}
