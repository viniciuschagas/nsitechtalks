function carregar_video(id_da_palestra, id_do_div_onde_renderizar) {
    $(document).ready(function() {
        $.post(
            '/retornar_video_embed',
            {'id_da_palestra': id_da_palestra},
            function(resposta) {
                $('#'+id_do_div_onde_renderizar).html(resposta[0].embed);
            }
        );
    });
}

function carregar_slide(id_da_palestra, id_do_div_onde_renderizar, id_do_div_da_url) {
    $(document).ready(function() {
        $.post(
            '/retornar_slide_embed_e_url',
            {'id_da_palestra': id_da_palestra},
            function(resposta) {
                $('#'+id_do_div_onde_renderizar).html(resposta[0].embed);
                $('#'+id_do_div_da_url).html(
                    '<a href="'+resposta[0].url+'">Link da apresentaçao no Slideshare</a>');
            }
        );
    });
}