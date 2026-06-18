document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".locales button");
    const all_elements = document.querySelectorAll(".mapa, .ubicacion__direccion, .ubicacion__text_container");

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            // Remove active button class
            buttons.forEach(btn => btn.classList.remove("active_ubication"));
            // Add active button class
            button.classList.add("active_ubication");

            // Deactivate all map and address display elements
            all_elements.forEach(el => el.classList.remove("active_provincia"));

            // Get target suffix based on button id
            const targetId = button.id;

            // Activate elements for selected branch
            const dirEl = document.getElementById(`ubicacion__direccion_${targetId}`);
            const mapEl = document.getElementById(`mapa_${targetId}`);
            const textEl = document.querySelector(`.ubicacion__text_container.${targetId}`);

            if (dirEl) dirEl.classList.add("active_provincia");
            if (mapEl) mapEl.classList.add("active_provincia");
            if (textEl) textEl.classList.add("active_provincia");
        });
    });
});
