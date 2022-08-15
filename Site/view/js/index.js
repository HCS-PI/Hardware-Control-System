video = document.getElementById("carLightVideo");
video.pause();
videoPlayed = false;

videoPosition = bannerVideo.getBoundingClientRect().top; // Menor que
videoHeight = bannerVideo.getBoundingClientRect().height; // Maior que
// window.scrollY
reveals = document.querySelectorAll(".reveal");

windowSize = document.body.scrollHeight;

function playVideo(){
    video.play();
}

function reveal() {
    if((((window.scrollY + window.innerHeight) <= videoPosition || window.scrollY > (videoPosition+videoHeight)) && (videoPlayed))){
        console.log('Fora do escopo');
        video.load();
        video.pause();
        videoPlayed = false;
    }

    for (i = 0; i < reveals.length; i++) {
        windowHeight = window.innerHeight;
        elementTop = reveals[i].getBoundingClientRect().top;
        elementVisible = 150;
  
        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add("active");
        } else {
            reveals[i].classList.remove("active");
        }
        
        if(!videoPlayed){
            let x = reveals[i].className.split(' ');
            for(i = 0; i < x.length; i++){
                if(x[i] == 'playVideo'){
                    console.log('Passou')

                    setTimeout(playVideo, 2000)
                    videoPlayed = true;
                }
            }
        }
        
        // else{
            // videoPlayed = false;
            // console.log('Não passa!')
        // }
    }
}

window.addEventListener("scroll", reveal);