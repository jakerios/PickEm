function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId})
    }).then((_res) => {
        window.location.href = "/";
    })
}


$(document).ready(function (e) {
    var $selects = $('select');
    $selects.change(function () {
        var value = $(this).val();
        if (value == "") {
            return false;
        }
        $selects.not(this).each(function () {
            $('option', this).each(function () {
                var sel = $(this).val();
                if (sel == value) {
                    $(this).prop('disabled', true);
                }
            });
        });
    }).change();
});

