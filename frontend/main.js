window.addEventListener('DOMContentLoaded', (event) => {
    getVisitCount();
});


const functionApi = 'https://visitorshttptriggerfunction.azurewebsites.net/api/VisitorTrigger'; 

const getVisitCount = () => {
    let count = 30;
    fetch(functionApi)
    .then(response => {
        return response.json()
    })
    .then(response => {
        console.log("Website called function API.");
        count = response.count;
        document.getElementById('counter').innerText = count;
    }).catch(function(error) {
        console.log(error);
      });
    return count;
}