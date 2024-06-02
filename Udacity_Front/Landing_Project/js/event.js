/**
 *
 * Manipulating the DOM exercise.
 * Exercise programmatically builds navigation,
 * scrolls to anchors from navigation,
 * and highlights section in viewport upon scrolling.
 *
 * Dependencies: None
 *
 * JS Version: ES2015/ES6
 *
 * JS Standard: ESlint
 *
*/
(function (){
  console.log("test");
})();


(number = function (num=3){
  console.log("test" + num);
})();
/**
 * Comments should be present at the beginning of each procedure and class.
 * Great to have comments before crucial code sections within the procedure.
*/

// Define global variable
const section = document.querySelectorAll('section'); // href, observer
const menuList = document.getElementById('navbar__list'); // inserthtml


// Insert <li> tag to make menu bar

section.forEach(el => {
  const menuElement = `<li class="menu__link" data-link="${el.id}">${el.dataset.nav}</li>`
  menuList.insertAdjacentHTML('beforeend',menuElement)
});


// Add scroll Animation
function scrollSmooth (e) {
  const parent = e.target.hasAttribute("data-link")
  ? e.target
  : None
  const elementToScrollTo = document.getElementById(parent.dataset.link)
  elementToScrollTo.scrollIntoView({behavior:"smooth"});
}

menuList.addEventListener('click',scrollSmooth,false);


// Use intersectionobserver to make menu bar Active

const options = {
  root : null,
  rootMargin : '0px',
  threshold : 0.6
};

const callback = (entries, observer) => {
  entries.forEach(entry => {
     const menu_element = document.querySelector(
       `.menu__link[data-link='${entry.target.id}']`
     )
     const section = document.getElementById(entry.target.id)

     if (entry.isIntersecting) {
       menu_element.classList.add('active')
       section.classList.add('active')
     } else {
       if (menu_element.classList.contains('active')) {
         menu_element.classList.remove('active')
       }

       if (section.classList.contains('active')) {
         section.classList.remove('active')
       }
     }
  })
};

const observer = new IntersectionObserver(callback, options);
section.forEach(el => {
  observer.observe(document.getElementById(el.id))
});

//Adding scroll to top
const moveTop 	= document.getElementById("top");

moveTop.addEventListener('click', function () {
	document.body.scrollTo({
		top: 0,
		behavior: "smooth",
	});
})
