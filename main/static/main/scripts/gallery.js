window.onload = () => {
  let wrapper = document.querySelector("#projects-container");
  wrapper.classList.remove("hidden");
  setTimeout(() => {
    document.querySelector("#cover").remove();
  }, 500);

  let details = document.querySelector("#details-container");
  let project = document.querySelector("project");
  // const myTimeout = setInterval(showNextInGallery, 3000);

  // GO UP
  // document.getElementById("back").addEventListener("click", ridirectToHome);
};
