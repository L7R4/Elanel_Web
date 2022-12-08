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

