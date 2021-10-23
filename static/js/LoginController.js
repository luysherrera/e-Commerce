$(document).ready(function() {
    var registrarse = document.getElementById("register");
    var login = document.getElementById("btnlogin");
    var sigin = document.getElementById('sigin');
    var login = document.getElementById('login');
    var delUser = document.getElementById('btn-delUser');
    sigin.style.display = "none"
    console.log("controller login");
    $('.message').click(function(){
        $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
        $('#idMensajeError').hide();
    });

    registrarse.onclick = function(e){
        e.preventDefault();
        document.getElementById('text').innerHTML = "REGISTRARSE";
        login.style.display = "none";
        sigin.style.display = ""
    }

    btnlogin.onclick= function(e){
        e.preventDefault();
        document.getElementById('text').innerHTML = "INICIAR SESION";
        login.style.display = "";
        sigin.style.display = "none"
    }

    delUser.onclick = function(e){
        e.preventDefault();
        delUser.on('click', function(){
            swal({
                  title: 'Quieres salir del sistema?',
                 text: "La sesión actual se cerrará y saldrá del sistema.",
                  type: 'warning',
                  showCancelButton: true,
                  confirmButtonText: 'SI, CERRAR',
                  closeOnConfirm: false
            },
            function(isConfirm) {
                  if (isConfirm) {
                    // window.location='/logout'; 
                  }
            });
        });
    }

    $('.btnlogin').on('click', function(){
    	swal({
            title:"", 
            text:"Loading...",
            icon: "https://www.boasnotas.com/img/loading2.gif",
            buttons: false,      
            closeOnClickOutside: false,
            timer: 3000,
            //icon: "success"
        });
    });

   
});