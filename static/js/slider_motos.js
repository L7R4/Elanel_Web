const images = document.querySelectorAll(".list > li");
const btn_prev = document.querySelector(".btn-prev")
const btn_next = document.querySelector(".btn-next")

let slider = document.querySelector(".list");
var item = document.querySelectorAll(".list > li");




// images.forEach(function(image,i){
//   image.addEventListener("click",function(){
//     if(image.classList.contains("next")){
//       image.classList.remove("next");
//       images.forEach(e =>{
//         if(e.classList.contains("prev")){
//           e.classList.replace("prev", "next")
//         }
//       });
//       images.forEach(e =>{
//         if(e.classList.contains("act")){
//           e.classList.replace("act","prev");
//         }
        
//       });
//     }
      
//     if(image.classList.contains("prev")){
//       image.classList.remove("prev");
//       images.forEach(e =>{
//         if(e.classList.contains("next")){
//           e.classList.replace("next", "prev")
//         }
//       });
//       images.forEach(e =>{
//         if(e.classList.contains("act")){
//           e.classList.replace("act","next");
//         }
        
//       });
      
//     }
// })
// });