
const blocked = ['my most','death',"world's",'life as a','scammer','killer','destroyed','amazing','reacting to','react to','win','$','insane','how to','how does','why does','what does','believe in','snl']

function hideVideos(blocked){
  let content = document.getElementById("contents");
  let videos = content.querySelectorAll("#content");
  videos.forEach(video=>{
    let video_title = video.querySelector("#video-title").textContent.toLowerCase();
    let delete_me = false
    blocked.forEach(word=>{
      if(video_title.includes(word)){
        delete_me = true
      }
    })
  if(delete_me==true){
  //remove video
    video.remove();
    console.log(`removed video ${video_title}`);
  }
  })
}

hideVideos(blocked)
