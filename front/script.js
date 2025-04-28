async function puxar_api() {
    await axios.get("http://localhost:8000/api/v1/brawler").then((response) => {
        const brawlers = response.data;
        const container = document.getElementById("brawler-container")
        brawlers.forEach(element => {
            const brawlerDiv = document.createElement("div");
                brawlerDiv.classList.add("brawler");
                brawlerDiv.innerHTML = `
                    <h2>${element.nome}</h2>
                    <p>Ataque: ${element.ataque}</p>
                    <p>Super: ${element.ataque_super}</p>
                    <p>Saúde: ${element.saude}</p>
                    <p>Raridade: ${element.raridade}</p>
                    <img src="${element.foto}"></img>
                `;
                container.appendChild(brawlerDiv)
        })
    })
}
puxar_api()