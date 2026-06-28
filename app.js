const username = "MimictoMastery";
const container = document.getElementById("projects-container");

async function loadProjects() {
    try {
        const response = await fetch(`https://api.github.com/users/${username}/repos`);
        const repos = await response.json();

        // Sort by most recently updated
        repos.sort((a, b) => new Date(b.updated_at) - new Date(a.updated_at));

        repos.forEach(repo => {
            const card = document.createElement("div");
            card.classList.add("repo-card");

            card.innerHTML = `
                <h3>${repo.name}</h3>
                <p>${repo.description ? repo.description : "No description available."}</p>
                <a href="${repo.html_url}" target="_blank">View Repo</a>
            `;

            container.appendChild(card);
        });

    } catch (error) {
        console.error("Error loading GitHub repos:", error);
        container.innerHTML = "<p>Could not load projects.</p>";
    }
}

loadProjects();