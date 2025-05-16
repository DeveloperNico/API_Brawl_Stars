// Função para puxar todos os brawlers
async function puxar_api() {
    try {
        const response = await axios.get("http://localhost:8000/api/v1/brawler/");
        const brawlers = response.data;
        const container = document.getElementById("brawler-container");
        container.innerHTML = "";
        brawlers.forEach(element => {
            const brawlerDiv = document.createElement("div");
            brawlerDiv.classList.add("brawler");
            brawlerDiv.innerHTML = `
                <h2>${element.nome}</h2>
                <p>Ataque: ${element.ataque}</p>
                <p>Super: ${element.ataque_super}</p>
                <p>Saúde: ${element.saude}</p>
                <p>Raridade: ${element.raridade}</p>
                <img src="${element.foto}" alt="${element.nome}">
                <div class=containerButton>
                    <button class=button onclick="deleteBrawler(${element.id})">Excluir</button>
                    <button class=button onclick="editBrawler(${element.id})">Editar</button>
                </div>
            `;
            container.appendChild(brawlerDiv);
        });
    } catch (error) {
        console.error("Erro ao buscar brawlers", error);
    }
}

// Função para criar um novo brawler
async function createBrawler() {
    const nome = prompt("Nome do Brawler:");
    const ataque = prompt("Ataque:");
    const ataque_super = prompt("Ataque Super:");
    const saude = parseInt(prompt("Saúde:"));
    const raridade = prompt("Raridade:");
    const foto = prompt("URL da Foto:");

    const newBrawler = {
        nome,
        ataque,
        ataque_super,
        saude,
        raridade,
        foto
    };

    try {
        await axios.post("http://localhost:8000/api/v1/brawler/", newBrawler);
        puxar_api();  // Atualiza a lista após adicionar
    } catch (error) {
        console.error("Erro ao criar brawler", error);
    }
}

// Função para excluir um brawler
async function deleteBrawler(id) {
    try {
        await axios.delete(`http://localhost:8000/api/v1/brawler/${id}`);
        puxar_api();  // Atualiza a lista após excluir
    } catch (error) {
        console.error("Erro ao excluir brawler", error);
    }
}

// Função para editar um brawler
async function editBrawler(id) {
    const nome = prompt("Novo nome do Brawler:");
    const ataque = prompt("Novo ataque:");
    const ataque_super = prompt("Novo ataque super:");
    const saude = parseInt(prompt("Nova saúde:"));
    const raridade = prompt("Nova raridade:");
    const foto = prompt("Nova URL da foto:");

    const updatedBrawler = {
        nome,
        ataque,
        ataque_super,
        saude,
        raridade,
        foto
    };

    try {
        await axios.put(`http://localhost:8000/api/v1/brawler/${id}`, updatedBrawler);
        puxar_api();
    } catch (error) {
        console.error("Erro ao editar brawler", error);
    }
}

// Chama a função de carregar os brawlers ao carregar a página
window.onload = puxar_api;
