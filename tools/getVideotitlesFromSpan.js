titles = document.querySelectorAll("span[id='video-title']")

results = '';
titles.forEach(title=>{
results+=`${title.textContent.trim()}\n`
})

results
