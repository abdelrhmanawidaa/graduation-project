var imgsElement = Array.from(document.querySelectorAll(".item img"))
var boxContainer = document.getElementById("boxContainer")
var boxInner = document.getElementById("boxInner")
var closeElement = document.getElementById("close")
var nextElement = document.getElementById("next")
var prevElement = document.getElementById("prev")
var currentIndex =0
for(var i=0;i<imgsElement.length;i++){
    imgsElement[i].addEventListener("click" ,function(event){
        boxContainer.style.display="flex";
        var imgSrc= event.target.getAttribute('src')
        boxInner.style.background= "url("+imgSrc+")"
        currentIndex= imgsElement.indexOf(event.target)


    })
}

nextElement.addEventListener("click",nextSlide)
function nextSlide(){
    currentIndex++
    if(currentIndex == imgsElement.length){
        currentIndex=0
    }
    var imgSrc= imgsElement[currentIndex].getAttribute("src")
    boxInner.style.background= "url("+imgSrc+")"

    
}
prevElement.addEventListener("click",prevSlide)
function prevSlide(){
    currentIndex--
    if(currentIndex <0){
        currentIndex=imgsElement.length-1
    }
    var imgSrc= imgsElement[currentIndex].getAttribute("src")
    boxInner.style.background= "url("+imgSrc+")"

}