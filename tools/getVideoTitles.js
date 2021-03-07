//grab all video titles and links from Youtube

results = ''

videos = document.querySelectorAll("h3[class='style-scope ytd-grid-video-renderer']")

videos.forEach(video=>{
    let link = video.querySelector("a")
    let title = link.title
    let href = link.href
    results+=`${title}\t${href}\n`
    })

results