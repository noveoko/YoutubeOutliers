let items = document.querySelectorAll("tr[class='item']")

results = ''
​
items.forEach(item =>{
let subs = item.querySelector("td[class='text followerNum with-num']").querySelector("span").textContent.trim();
let yt = item.querySelector("a")
let title = yt.textContent.trim();
let link = yt.href
results+=`${title};${link};${subs}\n`
})
