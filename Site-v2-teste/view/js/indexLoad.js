isVideo = false;

try{
    video = document.getElementById("carLightVideo");
    video.pause();
    videoPlayed = false;
    isVideo = true
}catch(err){
    console.log('')
    videoPlayed = false;
}

function playVideo(){
    if(isVideo){
        video.play();
    }
}

function reveal() {
    var reveals = document.querySelectorAll(".reveal");
  
    for (i = 0; i < reveals.length; i++) {
        windowHeight = window.innerHeight;
        elementTop = reveals[i].getBoundingClientRect().top;
        elementVisible = 150;
  
        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add("active");
        } else {
            reveals[i].classList.remove("active");
        }
        
        if(!videoPlayed && isVideo){
            let x = reveals[i].className.split(' ');
            for(i = 0; i < x.length; i++){
                if(x[i] == 'playVideo'){
                    console.log('Passou')

                    setTimeout(playVideo, 2000)
                    videoPlayed = true;
                }
            }
        }
    }
}

window.addEventListener("scroll", reveal);