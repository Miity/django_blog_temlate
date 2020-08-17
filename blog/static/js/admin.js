
$(function() {

    $("#post-edit").click(function(e){
        e.preventDefault();

        var postTitle = $("#post-title").hide().text();
        $("#post-title-edit").show().val(postTitle);

        var postContent = $("#post-content").hide().html();
        $("#post-content-edit").show().html(postContent);
        var ckeditor_conf = JSON.parse($("#post-content-edit").attr('data-config'));
        delete ckeditor_conf.height;
        delete ckeditor_conf.width;
        CKEDITOR.replace('post-content-edit', ckeditor_conf);
    });

//    $("#post-title").on("dblclick", function(){
//        alert("dblclick on");
//    });
//    console.log( "ready!" );
});