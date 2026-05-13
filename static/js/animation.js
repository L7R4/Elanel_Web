var barra_formulario;
var formulario;
window.barra_formulario = ScrollReveal();
barra_formulario.reveal('.barra', {
    duration: 1000,
    origin: 'left',
    distance: '100%',
    easing: 'ease-in-out',
    opacity: 0
});

window.formulario = ScrollReveal();
formulario.reveal(".formulario form",{
    duration: 1000,
    delay: 1000,
    origin:"right",
    distance: "20%",
    easing: "ease-in-out"
})


// Observer for WhatsApp button
document.addEventListener("DOMContentLoaded", function() {
    const whatsappBtn = document.getElementById('whatsapp_contact');
    const categoriaSection = document.querySelector('.categoria');

    if (whatsappBtn && categoriaSection) {
        const observer = new IntersectionObserver((entries) => {
            // We want it to appear when the user reaches '.categoria' and stay visible while scrolling down past it.
            // A simple way is to check if the section is intersecting, or if we scrolled past it.
            // Actually, we can just observe it and toggle the class if we scroll past its top.
            entries.forEach(entry => {
                if (entry.isIntersecting || entry.boundingClientRect.top < 0) {
                    whatsappBtn.classList.add('show');
                } else {
                    whatsappBtn.classList.remove('show');
                }
            });
        }, {
            root: null,
            threshold: 0,
            rootMargin: "0px 0px -100px 0px" // Trigger slightly before it fully comes into view
        });

        observer.observe(categoriaSection);
    }
});
