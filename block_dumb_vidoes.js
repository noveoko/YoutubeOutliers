
const blocked = ['reacting to','react to','win','$','insane','how to']

function hideVideos(blocked){
  let content = document.getElementById("contents");
  let videos = content.querySelectorAll("#content");
  videos.forEach(video=>{
    let delete_me = false
    blocked.forEach(word=>{
      if(video.querySelector("#video-title").textContent.toLowerCase().includes(word)){
        delete_me = true
      }
    })
  if(delete_me==true){
  //remove video
    video.remove();
    console.log("removed video x");
  }
  })
}
