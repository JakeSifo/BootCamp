function h1_on_click_handler(){
    var date_time = new Date();
    console.log('Called on ' + date_time);
    alert ('See browser console for the event details' );
 }

function update_by_id(){
    let msg = 'OK' ;
    document.getElementById('itext').innerHTML = msg;
}