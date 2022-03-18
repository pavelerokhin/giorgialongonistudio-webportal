// // Next/previous controls
// function plusSlides(n, galleryObjectId) {
//     currentSlide += n;
//     showSlides(galleryObjectId);
// }

// function gotoSlide(n, galleryObjectId) {
//     currentSlide = n;
//     showSlides(galleryObjectId);
// }

// function loadSlides(projectId, slidesNumber, captions, galleryObjectId) {
//     let galleryObject = document.getElementById(galleryObjectId);
//     let htmlBlock = "";

//     for (let i = 1; i < slidesNumber + 1; i++) {
//         htmlBlock +=
//             `<div class="mySlides fade data-id="${i}">
//                 <div class="numbertext">${i} / ${slidesNumber}</div>
//                 <img src="./etc/${projectId}/${i}.jpg">
//                 <div class="text">${captions[i]}</div>
//             </div>`
//     }
//     htmlBlock += (
//         `<a class="prev" onclick="plusSlides(-1, '${galleryObjectId}')">&#10094;</a>
//          <a class="next" onclick="plusSlides(1, '${galleryObjectId}')">&#10095;</a><br>
//          <div style="text-align:center"></div>`
//     )
//     for (let i = 1; i < slidesNumber + 1; i++) {
//         htmlBlock +=
//             `<span class="dot" onclick="gotoSlide(${i}, '${galleryObjectId}')"></span>`;
//     }
//     htmlBlock += `</div>`;
//     galleryObject.querySelector('.slideshow-container').innerHTML = htmlBlock;
// }
// å
// function showSlides(galleryObjectId) {
//     let i;
//     const galleryObject = document.getElementById(galleryObjectId);
//     const slides = galleryObject.getElementsByClassName("mySlides");
//     const dots = galleryObject.getElementsByClassName("dot");

//     if (currentSlide > slides.length) { currentSlide = 1 }
//     if (currentSlide < 1) { currentSlide = slides.length }

//     for (i = 0; i < slides.length; i++) {
//         slides[i].style.display = "none";
//     }
//     for (i = 0; i < dots.length; i++) {
//         dots[i].className = dots[i].className.replace(" active", "");
//     }

//     slides[currentSlide - 1].style.display = "block";
//     dots[currentSlide - 1].className += " active";
// }

// function clearSlides(galleryObjectId) {
//     let galleryObject = document.getElementById(galleryObjectId);
//     galleryObject.querySelector('.slideshow-container').innerHTML = "";
// }