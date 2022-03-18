var gallery;

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

function add_details(details) {
  let details_title = document.getElementById("details-title-black");
  details_title.innerText = details.name;
  details_title = document.getElementById("details-title-white");
  details_title.innerText = details.name;

  const keys = Object.keys(details.photos)
    .map((k) => parseInt(k))
    .sort();
  const details_section = document.getElementById("details");

  const detail_section = document.createElement("div");
  detail_section.classList.add("detail");
  detail_section.classList.add("m-p-g__thumbs");
  detail_section.setAttribute("data-google-image-layout", "");
  detail_section.setAttribute("data-width", "300");
  details_section.appendChild(detail_section);

  const full_screen_section = document.createElement("div");
  full_screen_section.classList.add("m-p-g__fullscreen");
  details_section.appendChild(full_screen_section);

  for (let key of keys) {
    const detail = details.photos[key];
    const photo = document.createElement("img");
    photo.classList.add("detail_photo");
    photo.classList.add("m-p-g__thumbs-img");
    photo.setAttribute("src", detail.photo);
    photo.setAttribute("data-full", detail.photo);
    detail_section.appendChild(photo);

    // if (detail.caption) {
    //     const caption = document.createElement("p");
    //     caption.classList.add("detail_caption");
    //     caption.innerHTML = detail.caption;
    //     detail_section.appendChild(caption);
    // }
  }

  const elem = document.querySelector(".m-p-g");
  gallery = new MaterialPhotoGallery(elem);
}

function clear_details() {
  document.getElementById("details").innerHTML = "";
}

function get_detail(url) {
  fetch(url, { method: "GET" })
    .then((response) => response.json())
    .then((details) => {
      clear_details();
      add_details(details);
    });
}

function showNextInGallery() {
  const imgs = document.getElementsByClassName("img-in-gallery");
  _toggleClasses(Object.values(imgs));
}
