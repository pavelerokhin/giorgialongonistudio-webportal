function showNextInGallery() {
  const imgs = document.getElementsByClassName("img-in-gallery");
  _toggleClasses(Object.values(imgs));
}

function showPrevioustInGallery() {
  const imgs = document.getElementsByClassName("img-in-gallery");
  _toggleClasses(Object.values(imgs).reverse());
}

function _toggleClasses(imgs) {
  let passCurrentToNext = false;
  imgs.forEach((i) => {
    if (passCurrentToNext) {
      i.classList.remove("hidden");
      i.classList.add("current");
      passCurrentToNext = false;
      return;
    }
    if (i.classList.contains("current")) {
      i.classList.remove("current");
      i.classList.add("hidden");
      passCurrentToNext = true;
    }
  });
  if (passCurrentToNext) {
    imgs[0].classList.remove("hidden");
    imgs[0].classList.add("current");
  }
}

const blinkUrls = [
  "media/contacts_gallery/1.jpg",
  "media/contacts_gallery/3.jpg",
  "media/contacts_gallery/4.jpg",
  "media/contacts_gallery/5.jpg",
  "media/contacts_gallery/6.jpg",
  "media/contacts_gallery/7.jpg",
  "media/contacts_gallery/8.jpg",
];
const mainBlink = new Blink({
  containerId: "blink-photos-main",
  imgUrls: blinkUrls,
  changeEvent: "timer",
  style: {
    height: "1000px",
  },
  timer: 3000,
});
const contactsBlink = new Blink({
  containerId: "blink-photos-contacts",
  imgUrls: blinkUrls,
  changeEvent: "timer",
  style: {
    height: "1200px",
  },
  timer: 5000,
});

/* Scroll to anchor for Firefox */
function pgshow() {
  var elId = window.location.hash;
  if (elId.length > 1) {
    el = document.getElementById(elId.substr(1));
    if (el) {
      el.scrollIntoView(true);
    }
  }
}
// pageshow fires after load and on Back/Forward
window.addEventListener("pageshow", pgshow);

window.onload = () => {
  let wrapper = document.querySelector(".wrapper");
  wrapper.classList.remove("hidden");
  setTimeout(() => {
    document.querySelector("#cover").remove();
  }, 1500);

  // const contactsGalleryInterval = setInterval(showNextInGallery, 3000);
  mainBlink.init();
  contactsBlink.init();
};
