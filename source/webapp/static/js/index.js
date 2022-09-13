    async function buttonClick(event){
        let target = event.target
        let url = target.dataset.articlesLink;
        console.log(url)
        let response = await fetch(url);
        let articles_json = await response.json()
        console.log(articles_json)
        console.log(articles_json.test)
        console.log(articles_json.test2)
    }

     function getArticles(){
        let button = document.getElementById("button");
        button.addEventListener("click", buttonClick)
    }

    window.addEventListener("load", getArticles)