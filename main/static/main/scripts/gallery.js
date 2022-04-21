"use strict";

var isMobileOrSmallScreen = false;

window.onload = () => {
  let wrapper = document.querySelector("#projects-container");
  wrapper.classList.remove("hidden");
  setTimeout(() => {
    document.querySelector("#cover").remove();
  }, 500);

  mobileDeviceDetailsClose();
  window.addEventListener("resize", mobileDeviceDetailsClose);
};

function mobileDeviceDetailsClose() {
  const detailsContainer = document.getElementById("details-container");

  isMobileOrSmallScreen = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
    navigator.userAgent
  );
  if (isMobileOrSmallScreen) {
    detailsContainer.addEventListener("click", (e) => {
      if (e.target.id == "details-container") {
        detailsContainer.classList.add("hidden");
      }
    });
  }
}

function _detail_caption(caption) {
  let caption_element = document.querySelector("#detail-description");
  if (!caption) {
    return;
  }
  caption_element.innerText = caption;
}

function _detail_mpg() {
  const detailsContainer = document.getElementById("details-container");
  detailsContainer.classList.remove("hidden");

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
}

function _detail_mpg_populate(photos) {
  const detail_section = document.querySelector(".detail.m-p-g__thumbs");

  const keys = Object.keys(photos)
    .map((k) => parseInt(k))
    .sort();

  for (let key of keys) {
    const detail = photos[key];
    const photo = document.createElement("img");
    photo.classList.add("detail_photo");
    photo.classList.add("m-p-g__thumbs-img");
    photo.setAttribute("src", detail.photo);
    photo.setAttribute("data-full", detail.photo);
    detail_section.appendChild(photo);
  }
}

function _detail_titles(name) {
  document.getElementById("details-title-black").innerText = name;
  document.getElementById("details-title-white").innerText = name;
}

function add_details(details) {
  _detail_titles(details.name);
  _detail_caption(details.caption);
  _detail_mpg();
  _detail_mpg_populate(details.photos);
  const elem = document.querySelector(".m-p-g");
  new MaterialPhotoGallery(elem);
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
