// // const dropDown = document.querySelector(".drop");
// // const dropDownol = document.querySelector(".drop ol");
// // dropDown.addEventListener("mouseover", () => {
  
// //     dropDownol.style.display = "block";
// // });
// // dropDown.addEventListener("mouseout", () => {
// //   dropDownol.style.display = "none";
// // });

// document.querySelector('.dropbtn').addEventListener('click', function(){
//     document.querySelector('.dropdown-content').classList.toggle('show');
// });

// window.onclick = function(event) {
//     if(!event.target.matches('.dropbtn')) {
//         var dropdowns = document.getElementsByClassName
//         ("dropdown-content");
//         for (var i = 0; i < dropdowns.length; i++ ){
//             var openDropdown = dropdowns[i];
//             if(openDropdown.classList.contains('show')){
//                 openDropdown.classList.remove()
//             }
//         }
//     }
// }

const backdrop = document.querySelector(".backdrop")
const menu = document.querySelector(".menu")
const ham = document.getElementById("ham")
ham.addEventListener("click", () => {
    backdrop.style.display = "block"
    menu.style.display = "block"
})
backdrop.addEventListener("click", () => {
    backdrop.style.display = "none"
    menu.style.display = "none"
})