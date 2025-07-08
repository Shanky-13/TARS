$(document).ready(function () {

    eel.init()()

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });

    // Siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
    });

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    // mic button click event

    $("#MicBtn").click(function () {
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()
    });


    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // to play assistant 
    function PlayAssistant(message) {

        if (message != "") {

            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }

    }

    // toggle function to hide and display mic and send button 
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    // key up event handler on text box
    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)

    });

    // send button event handler
    $("#SendBtn").click(function () {

        let message = $("#chatbox").val()
        PlayAssistant(message)

    });


    $("#chatbox").keypress(function (e) {
        let key = e.which || e.keyCode;
    
        // Check if Enter is pressed
        if (key === 13) {
            // If Shift is also held, insert a newline
            if (e.shiftKey) {
                // Insert newline at cursor position
                let textarea = $(this);
                let currentVal = textarea.val();
                let caretPos = this.selectionStart;
                let newVal = currentVal.substring(0, caretPos) + "\n" + currentVal.substring(caretPos);
                textarea.val(newVal);
    
                // Move the cursor to the correct position
                this.selectionStart = this.selectionEnd = caretPos + 1;
    
                e.preventDefault(); // prevent default newline behavior
            } else {
                // Otherwise, treat Enter as send
                let message = $("#chatbox").val();
                PlayAssistant(message);
                e.preventDefault(); // prevent form submission if inside <form>
            }
        }
    });
    




});