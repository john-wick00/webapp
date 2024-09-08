document.addEventListener("DOMContentLoaded", function () {
    const waifusContainer = document.getElementById("waifus-container");
    let currentPage = 1;  // Declare with `let` instead of `const` for updating

    function loadWaifus(page) {
        fetch(`/load_waifus?user_id=${userId}&page=${page}`)
            .then(response => response.json())
            .then(data => {
                console.log("Waifus data:", data);  // Log fetched data
                if (data.waifus && data.waifus.length > 0) {
                    data.waifus.forEach(waifu => {
                        const waifuElement = document.createElement('div');
                        waifuElement.classList.add('waifu');

                        const img = document.createElement('img');
                        img.src = waifu.img_url;
                        img.alt = waifu.name;
                        waifuElement.appendChild(img);

                        waifusContainer.appendChild(waifuElement);
                    });
                } else {
                    console.log("No waifus found.");
                }
            })
            .catch(error => console.error("Error loading waifus:", error));
    }

    loadWaifus(currentPage);
});
