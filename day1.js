
const readFile = function(event) {
    const input = event.target;

    const reader = new FileReader();
    reader.onload = function(){
        let text = reader.result;
        let textarr = text.split("\n");
        let res = document.getElementById('output');
        let resPair = document.getElementById('pair');
        let pair = [];
        
        for(let i=0; i < textarr.length; i++){
            let current = parseInt(textarr[i]);
            let temparr = textarr.slice(i+1);

            let matches = temparr.filter(elem => parseInt(elem) + current == 2020);
            if(!(matches.length == 0 || matches === undefined)){
                res.innerText = current * parseInt(matches[0]);
                resPair.innerText = textarr[i] + ", " + matches[0];
                break;
            }

        }
    };

    reader.readAsText(input.files[0]);

}